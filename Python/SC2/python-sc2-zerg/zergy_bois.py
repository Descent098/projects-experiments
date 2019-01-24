import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import DRONE, ZERGLING, HATCHERY, SPAWNINGPOOL, QUEEN, LARVA, OVERLORD, EXTRACTOR

"""
NOTE: If path is not default you need to go to the pip installation
directory and modify the file for paths directly
"""

# BUG: No Errors but nothing really happens 

class base_zerg(sc2.BotAI):
    """Class with basic setup for a zerg player"""


    async def on_step(self, iteration):
        """Function that 'does' everything per game iteration"""
        if iteration == 80:
            self.units(LARVA).random.train(DRONE)

        self.drone_count = 12
        self.hatchery_count = 1

        await self.build_unit_structures()
        await self.build_army()
        await self.distribute_workers()
        await self.manage_supply()
        # TODO: await self.manage_expand()
        await self.build_drones()
        await self.build_extractors()


    async def build_drones(self):
        """Determines whether to build drones or not"""
        self.drone_count = 0
        self.hatchery_count = 0
        for hatchery in self.units(HATCHERY):
            self.hatchery_count += 1

        for drone in self.units(DRONE):
            self.drone_count += 1

        if (self.can_afford(DRONE)) and ((self.drone_count/self.hatchery_count) < 21):
            if (self.units(LARVA).ready.exists) and (self.supply_left > 1):
                await self.do(self.units(LARVA).random.train(DRONE))
            if self.already_pending(OVERLORD) and (self.supply_left != 0) and (self.units(LARVA).exists):
                await self.do(self.units(LARVA).random.train(DRONE))


    async def manage_supply(self):
        """Creates overlord if supply is less than supply threshold"""
        if (self.supply_left < 3) and not (self.already_pending(OVERLORD)):
            if self.can_afford(OVERLORD) and self.units(LARVA).exists:
                await self.do(self.units(LARVA).random.train(OVERLORD))

    async def manage_expand(self):
        """Handles the decision of whether or not to expand"""
        if self.minerals > 500:
            # Copypasta from https://github.com/Dentosal/python-sc2/blob/master/examples/zerg/zerg_rush.py
            for d in range(4, 15):
                pos = hatchery.position.to2.towards(self.game_info.map_center, d)
                if await self.can_place(HATCHERY, pos):
                    self.spawning_pool_started = True
                    await self.do(self.workers.random.build(HATCHERY, pos))
                    break

    async def build_extractors(self):
        """Decides whether to build an extractor or not"""
        if (self.minerals > 100) and (self.units(SPAWNINGPOOL).exists or self.already_pending(SPAWNINGPOOL)):
            for hatchery in self.units(HATCHERY).ready:
                vespenes = self.state.vespene_geyser.closer_than(10, hatchery)
                for vespene in vespenes:
                    if not self.can_afford(EXTRACTOR):
                        break
                    worker = self.select_build_worker(vespene.position)
                    if worker is None:
                        break
                    if not self.units(EXTRACTOR).closer_than(1.0, vespene).exists:
                        await self.do(worker.build(EXTRACTOR, vespene))

    async def build_unit_structures(self):
        """Builds various structures related to army building"""

        # Builds spawning pool if one dosen't exist
        if not (self.units(SPAWNINGPOOL).exists or self.already_pending(SPAWNINGPOOL)) and (self.can_afford(SPAWNINGPOOL)):
            hatchery = self.units(HATCHERY).ready.random
            await self.build(SPAWNINGPOOL, near=hatchery)

    async def build_army(self):
        """Builds various units to add to army"""
        if (self.units(SPAWNINGPOOL).exists and self.can_afford(ZERGLING)) and self.units(LARVA).exists:
            self.units(LARVA).random.train(ZERGLING)

        if (self.minerals > 500):
            self.units(HATCHERY).random.train(QUEEN)


run_game(maps.get("AbyssalReefLE"), [
    Bot(Race.Zerg, base_zerg()),
    Computer(Race.Terran, Difficulty.Easy)
], realtime=False)

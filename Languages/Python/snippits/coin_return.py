# Challenge: write a machine that takes a value of cents and returns the exact change

class coin:
    # Dictionary of coin values and instance pointers i.e. {25: "quarter"} NOTE: represented as an integer of cents value
    coin_values = {}
    def __init__(self, value, name):
        self.value = value
        self.name = str(name)
        coin.coin_values[value] = str(name)

    @classmethod
    def enumerate_coin_values(cls):
        # Find the highest coin value
        values = []
        for value in coin.coin_values:
            values.append(value)
        values = sorted(values, reverse=True)
        return values, cls

    def __repr__(self):
        return self.name

class coin_machine:
    def __init__(self, amount):
        if type(amount) == float:
            raise TypeError("Amount must be an integer")
        self.amount = amount

    def return_change(self, values):
        remaining = self.amount
        coin_count = {}
        # Get list in descending order of available coins cent value
        while remaining:
            for value in values:
                number_of_coins = 0
                if remaining >= value:
                    number_of_coins = remaining//value
                coin_count[value] = number_of_coins
                remaining -= number_of_coins*value # Subtract from total
        print(f"Your change for {self.amount} is:")
        for current_coin in coin_count:
            print(f"{coin_count[current_coin]} {coin.coin_values[current_coin]}(s)")

# Canadian Currency Values:
def add_CAD():
    """Adds coins for CAD values"""
    twonie = coin(200, "Twonie")
    loonie = coin(100, "Loonie")
    quarter = coin(25,"Quarter")
    dime = coin(10,"Dime")
    nickle = coin(5,"Nickle")

if __name__ == "__main__":
    currency_selected = False
    while not currency_selected:
        pass
    add_CAD()
    pass

test = coin_machine(585)
test.return_change(coin.enumerate_coin_values()[0])



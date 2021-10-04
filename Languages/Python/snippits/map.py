# Some throw-away code for doing map generation for a CLI game manually

import keyboard
top=['╔','═','═','═','═','═','═','═','═','╗']
map1=['║','.','.','.','.','.','.','.','.','║']
map2=['║','@','.','.','.','.','.','.','.','║']
map3=['║','.','.','.','.','.','.','.','.','║']
bot=['╚','═','═','═','═','═','═','═','═','╝']
place=1
was_pressed = False
print(*top, sep='')
print(*map1, sep='')
print(*map2, sep='')
print(*map3, sep='')
print(*bot, sep='')
while True:
    try:
        if keyboard.is_pressed('D') and place<=7:
            if not was_pressed:
                if '@' in map1:
                    map1[place], map1[place+1]=map1[place+1],map1[place]
                    place=place+1
                    print(*top, sep='')
                    print(*map1, sep='')
                    print(*map2, sep='')
                    print(*map3, sep='')
                    print(*bot, sep='')
                    was_pressed=True
                if '@' in map2:
                    map2[place], map2[place+1]=map2[place+1],map2[place]
                    place=place+1
                    print(*top, sep='')
                    print(*map1, sep='')
                    print(*map2, sep='')
                    print(*map3, sep='')
                    print(*bot, sep='')
                    was_pressed=True
                if '@' in map3:
                    map3[place], map3[place+1]=map3[place+1],map3[place]
                    place=place+1
                    print(*top, sep='')
                    print(*map1, sep='')
                    print(*map2, sep='')
                    print(*map3, sep='')
                    print(*bot, sep='')
                    was_pressed=True

        elif keyboard.is_pressed('A') and place >=2:
            if not was_pressed:
                if '@' in map1:
                    map1[place], map1[place - 1] = map1[place - 1], map1[place]
                    place = place - 1
                    print(*top, sep='')
                    print(*map1, sep='')
                    print(*map2, sep='')
                    print(*map3, sep='')
                    print(*bot, sep='')
                    was_pressed = True
                if '@' in map2:
                    map2[place], map2[place -1] = map2[place - 1], map2[place]
                    place = place - 1
                    print(*top, sep='')
                    print(*map1, sep='')
                    print(*map2, sep='')
                    print(*map3, sep='')
                    print(*bot, sep='')
                    was_pressed = True
                if '@' in map3:
                    map3[place], map3[place -1] = map3[place - 1], map3[place]
                    place = place - 1
                    print(*top, sep='')
                    print(*map1, sep='')
                    print(*map2, sep='')
                    print(*map3, sep='')
                    print(*bot, sep='')
                    was_pressed = True

        elif keyboard.is_pressed('W'):
            if not was_pressed:
                if '@' in map2:
                    map2[place], map1[place]=map1[place],map2[place]
                    print(*top, sep='')
                    print(*map1, sep='')
                    print(*map2, sep='')
                    print(*map3, sep='')
                    print(*bot, sep='')
                    was_pressed=True
                if '@' in map3:
                    map3[place], map2[place] = map2[place], map3[place]
                    print(*top, sep='')
                    print(*map1, sep='')
                    print(*map2, sep='')
                    print(*map3, sep='')
                    print(*bot, sep='')
                    was_pressed = True

        elif keyboard.is_pressed('S'):
            if not was_pressed:
                if '@' in map1:
                    map1[place], map2[place] = map2[place], map1[place]
                    print(f"Moved {map1[place]}, {map2[place]} to {map2[place]} {map1[place]}")
                    print(*top, sep='')
                    print(*map1, sep='')
                    print(*map2, sep='')
                    print(*map3, sep='')
                    print(*bot, sep='')
                    was_pressed = True
                elif '@' in map2:
                    map2[place], map3[place] = map3[place], map2[place]
                    print(f"Moved {map2[place]}, {map3[place]} to {map3[place]} {map2[place]}")
                    print(*top, sep='')
                    print(*map1, sep='')
                    print(*map2, sep='')
                    print(*map3, sep='')
                    print(*bot, sep='')
                    was_pressed = True

        else:
            was_pressed=False

    except:
        break
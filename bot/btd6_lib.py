import mouse
import time
import monkey
import data

monkeys = []

def start_game():
    mouse.drag(1420, 200, 1420, 900,absolute=True,duration=1)
    time.sleep(0.2)
    mouse.move(1470,800,absolute=True,duration=1)
    mouse.click('left')
    time.sleep(0.2)
    mouse.click('left')

def restart_game():
    mouse.move(680,650,absolute=True,duration=1)
    mouse.click('left')
    time.sleep(0.2)
    mouse.move(900,580,absolute=True,duration=1)
    mouse.click('left')
    time.sleep(0.2)


def place_monkey(type, drop_x, drop_y):
    match type:
        case 1:
            name = 0
            select_x = 1370
            select_y = 180
        case 2:
            name = 1
            select_x = 1460
            select_y = 180
        case 3:
            name = 2
            select_x = 1370
            select_y = 300
        case 4:
            name = 3
            select_x = 1460
            select_y = 300
        case 5:
            name = 4
            select_x = 1370
            select_y = 410
        case 6:
            name = 5
            select_x = 1460
            select_y = 410
        case 7:
            name = 6
            select_x = 1370
            select_y = 520
        case 8:
            name = 7
            select_x = 1460
            select_y = 520
        case 9:
            name = 8
            select_x = 1370
            select_y = 630
        case 10:
            name = 9
            select_x = 1460
            select_y = 630
        case 11:
            name = 10
            select_x = 1370
            select_y = 750
        case 12:
            name = 11
            select_x = 1460
            select_y = 750
        case 13:
            name = 12
            select_x = 1370
            select_y = 180
        case 14:
            name = 13
            select_x = 1460
            select_y = 180
        case 15:
            name = 14
            select_x = 1370
            select_y = 300
        case 16:
            name = 15
            select_x = 1460
            select_y = 300
        case 17:
            name = 16
            select_x = 1370
            select_y = 410
        case 18:
            name = 17
            select_x = 1460
            select_y = 410
        case 19:
            name = 18
            select_x = 1370
            select_y = 520
        case 20:
            name = 19
            select_x = 1460
            select_y = 520
        case 21:
            name = 20
            select_x = 1370
            select_y = 630
        case 22:
            name = 21
            select_x = 1460
            select_y = 630
        case 23:
            name = 22
            select_x = 1370
            select_y = 750
        case 24:
            name = 23
            select_x = 1460
            select_y = 750
    print("Placing", "monkey", "at", drop_x, drop_y)
    if(type > 12):
        mouse.move(1420,750,absolute=True,duration=1)
        mouse.drag(1420, 750, 1420, 0,absolute=True,duration=1)
    mouse.move(select_x, select_y, absolute=True, duration=2)
    mouse.drag(select_x, select_y, drop_x, drop_y, absolute=True, duration=1)
    time.sleep(0.2)
    mouse.move(1420,200,absolute=True,duration=1)
    
    mouse.drag(1420, 200, 1420, 900,absolute=True,duration=1)
    time.sleep(0.2)
    mouse.move(720, 495,absolute=True, duration=1)
    monkeys.append(monkey.monkey(type, name, drop_x, drop_y))

def upgrade_monkey(monkey, upgrade):
    monkeys[monkey].upgrades[upgrade-1] = monkeys[monkey].upgrades[upgrade-1] + 1
    print("Upgrading", monkeys[monkey].name, " at", monkeys[monkey].x, monkeys[monkey].y, "to [",monkeys[monkey].upgrades[0],",",monkeys[monkey].upgrades[1],",",monkeys[monkey].upgrades[2],"]")
    mouse.move(monkeys[monkey].x, monkeys[monkey].y, absolute=True, duration=1)
    mouse.click('left')
    match upgrade:
        case 1:
            upgrade_y = 400
            monkeys[monkey].upgrades[0] = monkeys[monkey].upgrades[0] + 1
        case 2:
            upgrade_y = 535
            monkeys[monkey].upgrades[1] = monkeys[monkey].upgrades[1] + 1
        case 3:
            upgrade_y = 660
            monkeys[monkey].upgrades[2] = monkeys[monkey].upgrades[2] + 1

    if(monkeys[monkey].x < 695):
        upgrade_x = 1300
    else:
        upgrade_x = 300
    
    mouse.move(upgrade_x, upgrade_y, absolute=True, duration=1)
    mouse.click('left')
    time.sleep(0.2)
    mouse.move(720, 495,absolute=True, duration=1)
    mouse.click('left')

def check_place(x, Y):
    posible1 = True
    posible2 = True
    posible = True
    map = data.get_map()
    for i in range(0, len(map)):
        if map[i][0][0] < x < map[i][1][0] and map[i][0][1] < Y < map[i][1][1]:
            posible1 = False
            print ("there is a part of the map at", x, Y)
    for i in range(0, len(monkeys)):
        if monkeys[i].x == x and monkeys[i].y == Y:
            posible2 = False
            print ("already a monkey at", x, Y)
    
    if posible1 == False or posible2 == False:
        posible = False

    return posible
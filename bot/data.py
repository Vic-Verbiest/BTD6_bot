from PIL import Image
from PIL import ImageGrab
from PIL import ImageOps
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
only_numbers = r'--psm 6 tessedit_char_whitelist=0123456789'


def extract_screen_data():
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png')

    box = (366,25,500,58)
    money = screenshot.crop(box)
    money.save('money.png')
    img = Image.open('./money.png')
    img = ImageOps.invert(img)
    mtx = (1,1,1,0,1,1,1,0,1,1,1,0)
    img = img.convert("L",mtx)
    img.save('money.png')
    img = Image.open('./money.png')
    money = pytesseract.image_to_string(img, config=only_numbers).replace(".","")


    box = (120,15,210,60)
    health = screenshot.crop(box)
    health.save('health.png')
    img = Image.open('./health.png')
    img = ImageOps.invert(img)
    mtx = (1,1,1,0,1,1,1,0,1,1,1,0)
    img = img.convert("L",mtx)
    img.save('health.png')
    img = Image.open('./health.png')
    health = pytesseract.image_to_string(img, config=only_numbers)


    box = (1400,35,1560,80)
    round = screenshot.crop(box)
    round.save('round.png')
    img = Image.open('./round.png')
    img = ImageOps.invert(img)
    mtx = (1,1,1,0,1,1,1,0,1,1,1,0)
    img = img.convert("L",mtx)
    img.save('round.png')
    img = Image.open('./round.png')
    round = pytesseract.image_to_string(img, config=only_numbers)[:-4]

    box = (600,280,1320,400)
    alive = screenshot.crop(box)
    alive.save('defeat.png')
    img = Image.open('./defeat.png')

    img.save('defeat.png')
    img = Image.open('./defeat.png')
    alive = pytesseract.image_to_string(img)
    print(alive)

    if alive != "":
        alive = 0
    else:
        alive = 1

    data = [money, health, round, alive]
    return data

def get_prices():
    hero=[510]
    dart_monkey=[215,
                 [150,235,360,1945,16200],
                 [110,205,430,8640,48600],
                 [95,215,675,2160,23220]]
    boomerang_monkey=[350,
                      [215,300,1295,3240,31750],
                      [190,270,1565,4535,37800],
                      [110,325,1405,2375,54000]]
    bomb_shooter=[565,
                  [380,700,1295,3890,59400],
                  [270,430,1190,3455,27000],
                  [215,325,865,3025,37800]]
    tack_shooter=[300,
                  [160,325,650,3780,49140],
                  [110,145,595,2915,16200],
                  [110,110,485,3455,21600]]
    ice_monkey=[540,
                [110,380,1620,2375,30240],
                [245,380,3130,3240,21600],
                [190,245,2105,2970,32400]]
    glue_gunner=[245,
                 [215,325,2700,5400,23760],
                 [110,1945,5310,3780,16200],
                 [130,430,3670,3240,30240]]
    sniper_monkey=[380,
                   [380,1620,3240,5400,36720],
                   [325,485,3455,7775,14040],
                   [430,430,3780,4590,15120]]
    monkey_sub=[350,
                [140,540,540,2700,34560],
                [485,325,1510,14040,34560],
                [485,1080,1190,3240,27000]]
    monkey_buccaneer=[540,
                      [380,595,3185,7775,27000],
                      [595,540,970,4860,22680],
                      [195,430,2485,5940,24840]]
    monkey_ace=[865,
                [700,700,1080,3240,43200],
                [215,380,970,19440,32400],
                [540,325,3025,25920,97800]]
    heli_pilot=[1730,
                [865,540,1890,21170,48600],
                [325,650,3240,12960,32400],
                [2700,380,3780,9180,37800]]
    mortar_monkey=[810,
                   [540,540,970,8640,30240],
                   [325,540,970,5940,32400],
                   [215,540,865,11880,43200]]
    dartling_gun=[920,
                  [325,970,4590,11880,86400],
                  [270,1025,5670,5510,65800],
                  [160,1295,3670,12960,62640]]

    wizard_monkey=[405,
                   [160,650,1405,10800,34560],
                   [325,1025,3240,4320,58620],
                   [325,325,1620,3025,28620]]
    super_monkey=[2700,
                  [2700,3240,21600,108000,540000],
                  [1080,1510,8640,20520,97200],
                  [3240,1295,6050,64800,216000]]
    ninja_monkey=[540,
                  [325,380,920,2970,37800],
                  [380,450,970,5615,23760],
                  [270,430,2430,5400,43200]]
    alchemist=[595,
               [270,380,1650,3240,64800],
               [270,515,3240,4860,48600],
               [700,485,1080,1970,43200]]
    druid=[430,
           [270,1080,1780,4860,70200],
           [270,380,1025,5400,37800],
           [110,325,650,2700,48600]]

    banana_farm=[1350,
                 [540,650,3240,20520,108000],
                 [325,865,3780,8100,108000],
                 [270,215,3130,16200,64800]]
    spike_factory=[1080,
                   [865,650,2480,10260,162000],
                   [650,865,2700,5400,43200],
                   [160,430,1510,3780,32400]]
    monkey_village=[1295,
                    [430,1620,865,2700,27000],
                    [270,2160,8100,21600,43200],
                    [540,540,10800,3240,5400]]
    engineer_monkey=[430,
                     [540,430,620,2700,34560],
                     [270,380,865,14580,129600],
                     [485,235,540,3500,58320]]
    prices = [hero, dart_monkey, boomerang_monkey, bomb_shooter, tack_shooter, ice_monkey, glue_gunner, sniper_monkey, monkey_sub, monkey_buccaneer, monkey_ace, heli_pilot, mortar_monkey, dartling_gun, wizard_monkey, super_monkey, ninja_monkey, alchemist, druid, banana_farm, spike_factory, monkey_village, engineer_monkey]
    return prices

def get_x(index):
    return 50 + index * 100

def get_y(index):
    return 25 + index * 100

def get_price_upgrade(index,upgrade,upgrade_number):
    prices = get_prices()
    try:
        return prices[index][upgrade][upgrade_number]
    except:
        return 0

def get_price_place(index):
    prices = get_prices()
    return prices[index][0]

def get_map():
    map = [[[0,320],[725,395]],
           [[615,385],[725,395]],
           [[400,125],[495,725]],
           [[185,450],[290,725]],
           [[185,450],[905,535]],
           [[790,250],[905,535]],
           [[790,250],[1040,330]],
           [[945,250],[1040,655]],
           [[545,570],[1040,655]],
           [[545,570],[645,865]],
           [[0,0],[240,175]],
           [[1050,0],[1300,860]],
           [[0,810],[165,860]],
           [[1095,688],[1300,680]]]
    return map





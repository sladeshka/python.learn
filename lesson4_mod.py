import math
import os.path
import sys

def testReadWrite():
    dirfile = r"L:\learn.learn\python.learn\tasks\lesson1"
    myFile = open(os.path.join(dirfile, "myfile.txt"), "w+")
    k = myFile.write("Hello\n")
    print(k)

    myFile.write("Goodbye\n")
    myFile.close()

    myFile = open(os.path.join(dirfile, "myfile.txt"), "r")
    content = myFile.read()
    print("Сontent:", content)

    myFile.close()

    lis = ['1', "2", "3"]
    myFile = open(os.path.join(dirfile, "myfile.txt"), "w+")
    myFile.writelines(lis)
    myFile.close()
    sys.exit()

def read_zip_all():
    i = 0
    header = []
    zip_codes = []
    zip_data = []
    skip_line = False
    for line in open('zip_codes_states.csv').read().split("\n"):
        skip_line = False
        m = line.strip().replace('"', '').split(',')
        i += 1
        if i == 1:
            for val in m:
                header.append(val)
        else:
            zip_data = []
            for idx in range(0, len(m)):
                if m[idx] == '':
                    skip_line = True
                    break
                if header[idx] == "Latituse" or header[idx] == "Longitude":
                    val = float(m[idx])
                else:
                    val = m[idx]
                zip_data.append(val)
            if not skip_line:
                zip_codes.append(zip_data)
    return zip_codes

def zip_by_location(codes, location):
    zips = []
    for code in codes:
        if location[0].lower() == code[3].lower() and \
           location[1].lower() == code[4].lower():
            zips.append(code[0])
    return zips

def location_by_zip(codes, zipcode):
    pass

EARTH_RADIUS_MI = 3958.8
EPSILON_MI = 0.1
def calculate_distance(location1, location2):
    """
    :param location1: (iterable)
    :param location2: (iterable)
    :return:
    """
    lat1 = math.radians(location1[0])
    lat2 = math.radians(location2[0])
    long1 = math.radians(location1[1])
    long2 = math.radians(location2[1])
    del_lat = (lat1 - lat2) / 2
    del_long = (long1 - long2) / 2
    angle = math.sin(del_lat)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(del_long)**2
    distance = 2 * EARTH_RADIUS_MI * math.asin(math.sqrt(angle))
    return distance

if __name__ == '__main__':
    passed = 0
    failed = 0
    codes = read_zip_all()
    if codes[568] == ["01970", 42.512946, -70.904237, "Salem", "MA", "Essex"]:
        passed += 1
    else:
        failed += 1
    location1 = (codes[568][1], codes[568][2])
    location2 = (codes[581][1], codes[581][2])
    if abs(calculate_distance(location1, location2) == 27.20) < EPSILON_MI:
        passed += 1
    else:
        failed += 1
    print(location1, location2)
    print(zip_by_location(None, 'loc'))

    if len(zip_by_location(codes, ("Anchorage", "AK"))) == 22:
        passed += 1
    else:
        failed += 1

    if zip_by_location(codes, ("Clarkston", "WA")) == ["99403"]:
        passed += 1
    else:
        failed += 1
    x = set(['123', 123])
    y = set(['123', 123])
    print(x == y)

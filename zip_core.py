import math
import os.path
import sys
import zip_core_metric as zcm

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
    for code in codes:
        if code[0] == zipcode:
            return tuple(code[1:])
    return ()

MINS_IN_HOUR = SECS_IN_MIN = 60

def degree_minutes_seconds(location):
    minutes, degrees = math.modf(location)
    degrees = int(degrees)
    minutes *= MINS_IN_HOUR
    seconds, minutes = math.modf(minutes)
    minutes = int(minutes)
    seconds = SECS_IN_MIN * seconds
    return degrees, minutes, seconds

def format_location(location):
    ns = ""
    if location[0] < 0:
        ns = 'S'
    elif location[0] > 0:
        ns = 'N'

    ew = ""
    if location[1] < 0:
        ew = 'W'
    elif location[0] > 0:
        ew = 'E'

    format_string = '{:03d}\xb0{:0d}\'{:.2f}"'
    latdegree, latmin, latsecs = degree_minutes_seconds(abs(location[0]))
    latitude = format_string.format(latdegree, latmin, latsecs)
    longdegree, longmin, longsecs = degree_minutes_seconds(abs(location[1]))
    longitude = format_string.format(longdegree, longmin, longsecs)
    return '(' + latitude + ns + ',' + longitude + ew + ')'
def process_loc(codes):
    zipcode = input('Enter a ZIP Code to lookup => ')
    print(zipcode)
    location = location_by_zip(codes, zipcode)
    if len(location) > 0:
        print('ZIP Code {} is in {}, {}, {} county,\ncoordinates: {}'.
              format(zipcode, location[2], location[3], location[4],
                     format_location((location[0], location[1]))))
    else:
        print('Invalid or unknown ZIP Code')
def process_zip(codes):
    city = input('Enter a city name to lookup => ')
    print(city)
    city = city.strip().title()
    state = input('Enter the state name to lookup => ')
    print(state)
    state = state.strip().upper()
    zipcodes = zip_by_location(codes, (city, state))
    if len(zipcodes) > 0:
        print('The following ZIP Code(s) found for {}, {}: {}'.
              format(city, state, ", ".join(zipcodes)))
    else:
        print('No ZIP Code found for {}, {}'.format(city, state))
def process_dist(codes):
    zip1 = input('Enter the first ZIP Code => ')
    print(zip1)
    # logging.info(f'Received the first ZIP {zip1}')
    # logger_main.info(f'Received the first ZIP {zip1}')
    zip2 = input('Enter the second ZIP Code => ')
    print(zip2)
    # logging.info(f'Received the second ZIP {zip2}')
    # logger_main.info(f'Received the second ZIP {zip2}')

    location1 = location_by_zip(codes, zip1)
    location2 = location_by_zip(codes, zip2)
    if len(location1) == 0 or len(location2) == 0:
        print('The distance between {} and {} cannot be determined'.
              format(zip1, zip2))
    else:
        dist = zcm.calculate_distance(location1, location2)
        print('The distance between {} and {} is {:.2f} miles'.
              format(zip1, zip2, dist))
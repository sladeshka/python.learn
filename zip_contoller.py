import zip_view as view

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


zip_codes = read_zip_all();

command = ""
while command != 'end':
    command = input("Command ('loc', 'zip', 'dist', 'end') => ")
    print(command)
    if command == 'loc':
        process_loc(zip_codes)
    elif command == 'zip':
        process_zip(zip_codes)
    elif command == 'dist':
        process_dist(zip_codes)
    elif command == 'end':
        print('Involid comand, ignoring')
    print()
print('Done')
import zip_core as zc

EPSILON_MI = 0.1

if __name__ == '__main__':
    passed = 0
    failed = 0
    zip_codes = zc.read_zip_all();
    loc = zc.location_by_zip(zip_codes, ("Clarkston" , "WA"))
    if loc[2:] == ("Miami", "FL", "Miami-Dade") and abs(loc[0] - 25.737777) < EPSILON_MI and abs(loc[1] - -80.22477) < EPSILON_MI:
        passed += 1
    else:
        failed += 1

    command = ""
    while command != 'end':
        command = input("Command ('loc', 'zip', 'dist', 'end') => ")
        print(command)
        if command == 'loc':
            zc.process_loc(zip_codes)
        elif command == 'zip':
            zc.process_zip(zip_codes)
        elif command == 'dist':
            zc.process_dist(zip_codes)
        elif command == 'end':
            print('Involid comand, ignoring')
        print()
    print('Done')
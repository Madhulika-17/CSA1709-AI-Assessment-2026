def vacuum_cleaner():
    rooms = {'A': 'Dirty', 'B': 'Dirty'}
    current = 'A'

    while True:
        print("\nCurrent Location:", current)
        print("Room Status:", rooms)

        if rooms[current] == 'Dirty':
            print("Action: Clean")
            rooms[current] = 'Clean'
        else:
            print("Action: Move")

            if current == 'A':
                current = 'B'
            else:
                current = 'A'

        if rooms['A'] == 'Clean' and rooms['B'] == 'Clean':
            print("\nBoth rooms are clean.")
            break

vacuum_cleaner()

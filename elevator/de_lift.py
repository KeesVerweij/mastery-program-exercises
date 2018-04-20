from building import Building


def get_input(value):
    while True:
        try:
            get_input = abs(int(input(value)))
        except ValueError:
            print("Sorry, I didn't understand that.")
            # better try again... Return to the start of the loop
            continue
        else:
            # input was successfully parsed!
            # we're ready to exit the loop.
            return get_input


floors = get_input("how many floors will your building have? ")
visitors = get_input("how many visitors are in your building today? ")
print('----------------------------------')

building = Building(floors, visitors)
building.work_day()

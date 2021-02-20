
import re
from script import Apartment, generate_best_plan


def process_building_size():
    print("Please enter building data, \ne.g. - '<Building_name>,<Floor_size>'")
    building_data = str(input(", "))
    name, size = building_data.split(",")
    return name, float(size)


def process_apartments():
    print("How many apartment types do you have? (*<int>)")
    no_apartments = int(input(": "))
    apartment_types = []
    for aps in range(no_apartments):
        print("<no_of_rooms>,<size_in_m2>,<aimed_weight(optional)>")
        apartment_data = str(input(": "))
        apartment_data = [float(i) for i in apartment_data.split(",")]
        apartment_types.append(Apartment(*apartment_data))
    return apartment_types


def main():
    _, floor_size = process_building_size()
    apartment_types = process_apartments()
    print(generate_best_plan(floor_size=floor_size, apartment_types=apartment_types))


if __name__ == "__main__":
    main()


# Kenney2 = 498
# Kenney3 = 568
# Kenney4 = 618
# Roe1 = 938

# apartment_types = [Apartment(rooms=2, size=70, aimed_weight=3),
#                    Apartment(rooms=3, size=85, aimed_weight=1),
#                    Apartment(rooms=4, size=99, aimed_weight=0.5)]
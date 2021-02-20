

import random
class Apartment:

    def __init__(self, rooms, size, aimed_weight=0):
        self.rooms = rooms
        self.size = size
        self.aimed_weight = aimed_weight
        self.weight = 0

    def __repr__(self):
        return f"{self.rooms}_bedroom; size:{self.size}"


class FloorPlan:

    def __init__(self, apartments, cost):
        self.aparments = apartments
        self.cost = cost

    def __repr__(self):
        return f"Appartments: {self.aparments}\nCost: {self.cost}"


def generate_best_plan(floor_size, apartment_types):
    plans = []
    for i in range(10000):
        for app in apartment_types:
            if app.rooms == 2:
                weight_start = app.aimed_weight
            elif app.rooms == 3:
                weight_start = app.aimed_weight
            elif app.rooms == 4:
                weight_start = app.aimed_weight
            app.weight = int(random.uniform(weight_start, 10))

        calculation = sum([app.size * app.weight for app in apartment_types])

        if calculation < floor_size and calculation > 0\
                and all([app.weight > 0 for app in apartment_types]):
            permutation = [(app.size, app.weight) for app in apartment_types]
            plans.append(FloorPlan(apartments=permutation, cost=calculation))
    current_highest_cost = 0
    current_plan = None
    for floor_plan in plans:
        if floor_plan.cost > current_highest_cost:
            current_highest_cost = floor_plan.cost
            current_plan = floor_plan
    return current_plan




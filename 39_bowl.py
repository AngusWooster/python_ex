#!/usr/bin/python3


class scoop:
    def __init__(self, flavor) -> None:
        self.flavor = flavor

class bowl:
    def __init__(self) -> None:
        self.scoops = []

    def add_scoop(self, new_scoop):
        self.scoops.append(new_scoop)

    def __str__(self) -> str:
        flavors = '/'.join(scoop.flavor for scoop in self.scoops)
        return flavors


bowl = bowl()
bowl.add_scoop(scoop('chacolate'))
bowl.add_scoop(scoop('vanilla'))

print(bowl)
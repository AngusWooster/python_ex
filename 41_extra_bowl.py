#!/usr/bin/python3


class scoop:
    def __init__(self, flavor) -> None:
        self.flavor = flavor

class bowl:
    maxnum = 3
    def __init__(self) -> None:
        self.scoops = []

    def add_scoop(self, new_scoop):
        if (len(self.scoops) < self.maxnum):
            self.scoops.append(new_scoop)
        else:
            print(f'sorry, the max is {self.maxnum}')

    def __str__(self) -> str:
        flavors = '/'.join(scoop.flavor for scoop in self.scoops)
        return flavors

class extra_bowl(bowl):
    maxnum = 5


bowl = extra_bowl()
# bowl = bowl()

bowl.add_scoop(scoop('vanilla1'))
bowl.add_scoop(scoop('vanilla2'))
bowl.add_scoop(scoop('vanilla3'))
bowl.add_scoop(scoop('vanilla4'))
print(bowl)


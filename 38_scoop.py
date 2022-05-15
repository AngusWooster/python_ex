#!/usr/bin/python3


class scoop_t:
    def __init__(self, flavor) -> None:
        self.flavor = flavor

class scoop_maker_t:
    def create(self, flavors):
        output = list()
        for flavor in flavors:
            output.append(scoop_t(flavor))
        return output


scoop_maker = scoop_maker_t()
scoops = scoop_maker.create(['chocalate', 'vanilla', 'pineapple'])

for scoop in scoops:
    print(scoop, scoop.flavor)
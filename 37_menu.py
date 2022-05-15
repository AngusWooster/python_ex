#!/usr/bin/python3

def menu(**options):
    def menu_selector():
        options_string = '/'.join(options)
        while True:
            choice = input(f'choice ({options_string}): ')
            if choice in options:
                return options[choice]
            else:
                print("invalid input")

    return menu_selector

if __name__ == '__main__':
    import operator

    my_menu = menu(add=operator.add, sub=operator.sub)

    print(my_menu()(10, 5))
class Menu(object):
    def __init__(self):
        self.meals={}



    def add_meal(self, meal,idx):
        self.meals[idx]=meal


    def print_menu(self):
        for i in self.meals.keys():
            print(self.meals[i])


    def get_meal(self, idx):
        try:
            print(self.meals[idx])

        except KeyError:
            print('Index should be an integer.')

        except IndexError:
            print('This meal does not exist.')


    def clear_menu(self):
        self.meals={}





if __name__ == '__main__':

    menu = Menu()
    menu = Menu()
    menu.add_meal("Burger",2)
    menu.add_meal("Pizza",4)
    menu.add_meal("Chicken",8)
    menu.get_meal('a')
    menu.print_menu()
    menu.clear_menu()
    menu.print_menu()
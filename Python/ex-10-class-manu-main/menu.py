class Menu:
    #===== write your code below =======
    def __init__(self):
        self.meals = []

    def add_meal(self, meal):
        self.meals.append(meal)

    def print_menu(self):
        for i in range(len(self.meals)):
            print(self.meals[i])

    def get_meal(self, idx):
        try:
            print(self.meals[idx]) ## 내가 결과내고자하는 거
        except TypeError:
            print('Index should be an integer.')
        except IndexError:
            print('This meal does not exist.')


    def clear_menu(self):
            for i in range(len(self.meals)):
                self.meals.pop(0)
        


    




if __name__ == '__main__':

    menu = Menu()
    menu = Menu()
    menu.add_meal("Burger")
    menu.add_meal("Pizza")
    menu.add_meal("Chicken")
    menu.get_meal('a')
    menu.print_menu()
    menu.clear_menu()
    menu.print_menu()
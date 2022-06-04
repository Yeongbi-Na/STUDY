
class Cube:
    #===== write your code below =======
    def __init__(self,edge_length):
        self.edge_length=edge_length
        self.vol=edge_length**3
    
    def volume(self):
        return self.vol

    def __str__(self):
        return "Edge Length: %d, Volume: %d" % (self.edge_length, self.vol)

if __name__ == '__main__':
    cube1 = Cube(edge_length=11)
    print(cube1.volume())
    print(cube1)
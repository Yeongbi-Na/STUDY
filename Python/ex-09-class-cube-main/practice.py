class Cube(object):
    def __init__(self,edge_length):
        self.len=edge_length
        self.vol=self.len**3

    def volume(self):
        return self.vol
    def __str__(self):
        return "Edge Length: %d, Volume: %d" %(self.len,self.vol)


if __name__ == '__main__':
    cube1 = Cube(edge_length=11)
    print(cube1.volume())
    print(cube1)
    big_cube=Cube(8)
    print(big_cube)
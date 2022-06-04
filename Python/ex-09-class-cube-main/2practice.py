class Cube(object):
    def __init__(self, edge_length):
        self.len=edge_length
        

    def volume(self):
        self.vol=self.len**3
        return self.vol

    def __str__(self):
        return "Edge Length: %d, Volume: %d" % (self.len,self.vol)


if __name__ == '__main__':
    cube1 = Cube(edge_length=11)
    print(cube1.volume())
    print(cube1)







class parent:
    def __init__(self,name, distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "%s has reached %s" % (self.name,self.distance)
    

class child(parent):
    def __init__(self,name,distance,maker):
        parent.__init__(self,name,distance)
        self.maker = maker

    def maker_row(self):
        return "%s has done by %s" % (self.name, self.maker)
    


if __name__ == "__main__":
    x = parent("rc1", "streotype")
    y = child("rcq", "till space", "isro")

    print(x.launch())
    print(y.maker_row())

    # print(y.maker())
    
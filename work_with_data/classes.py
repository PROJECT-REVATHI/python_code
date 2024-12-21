class snake:
    name = "revathi"
    def change_name(self,new_name):
        self.name = new_name

snake = snake()
snake.change_name("masthanaiah")
print(snake.name)


class anaconda:
    def __init__(self,name):
        self.name = name
    def change_name(self,new_name):
        self.name = new_name

python = anaconda("py")
print(python.name)

















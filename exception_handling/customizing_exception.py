class notrange(Exception):
    def __init__(self,salary,message="salary is not in the range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

sal = int(input("enter the number"))
if not 5000 < sal < 15000:
    raise notrange(sal)
        
class invalidage(Exception):
    def __init__(self, message = "invalid age"):
        self.message = message
        super().__init__(self.message)

num = 18

try:
    input = int(input("enter the age"))
    if input < num:
        raise invalidage
    else:
        print("eligible to vote")
    
except invalidage as e:
    print(f"exception: {e}")

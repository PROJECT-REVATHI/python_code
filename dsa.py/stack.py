def stackstruct():
    stack = []
    return stack
def check_empty(stack):
    return len(stack) == 0
def push(stack,item):
    stack.append(item)
    print("pushed item: "+item)

def pop(stack):
    if(check_empty(stack)):
        return "empty"
    return stack.pop()


stack = stackstruct()
push(stack, str(1))
print("popped  %s" % pop(stack))
#  SImple stack implementation

def create_stack():
    stack =[]
    return stack
# end def

def check_if_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("pushed item: "+ item)

def pop(stack):
    if(check_if_empty(stack)):
        return "Stack is empty"
    stack.pop()
        


stack = create_stack()
push(stack,str(1))
print("Stack"+ str(stack))

push(stack,str(2))
print("Stack"+ str(stack))

push(stack,str(3))
print("Stack"+ str(stack))
pop(stack)
print("Stack poped"+ str(stack))
pop(stack)
print("Stack poped"+ str(stack))
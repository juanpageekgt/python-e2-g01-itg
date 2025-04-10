# Pila orientada a objetos

# class Stack:
    
#     def __init__(self):
#         self.__stack_list = []


# stack_object = Stack()
# print(len(stack_object.__stack_list))

# Implementación 1
class Stack():
        
    def push(self, val):
        self.__stack_list.append(val)
    
    def __init__(self):
        self.__stack_list = []
    
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


# stack_object = Stack()

# stack_object.push(3)
# stack_object.push(2)
# stack_object.push(1)

# print(stack_object.pop())
# print(stack_object.pop())
# print(stack_object.pop())

# print('-' * 20)

# stack_object_1 = Stack()
# stack_object_2 = Stack()

# stack_object_1.push(3)
# stack_object_2.push(stack_object_1.pop())

# print(stack_object_2.pop())

# print('-' * 20) 

# little_stack = Stack()
# another_stack = Stack()
# funny_stack = Stack()

# little_stack.push(1)
# another_stack.push(little_stack.pop() + 1)
# funny_stack.push(another_stack.pop() - 2)

# print(funny_stack.pop())

print('-' * 20)

class AddingStack(Stack):

    def get_sum(self):
        return self.__sum
    
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)

print(stack_object.get_sum())

print()

for i in range(5):
    print(stack_object.pop())

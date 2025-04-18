# por herencia

class Stack:

    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        if not self.__stack_list:
            return None
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def longitud(self):
        print('La pila tiene:', len(self.__stack_list), 'elementos')


class AddingStack(Stack):

    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def get_sum(self):
        return self.__sum

# main program
stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)

print(stack_object.get_sum())

print()

for i in range(5):
    print(stack_object.pop())

print()

print(stack_object.get_sum())








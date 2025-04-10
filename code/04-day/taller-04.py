class Queque:
    def __init__(self):
        self.__stack_list = []

    def put(self, val):
        self.__stack_list.append(val)

    def get(self):
        if not self.__stack_list:
            return None
        val = self.__stack_list[0]

        del self.__stack_list[0]
        return val

    def longitud(self):
        print('La pila tiene:', len(self.__stack_list), 'elementos')


# main program
que = Queque()
que.put(1)
que.put("perro")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except:
   print("Queque Error")
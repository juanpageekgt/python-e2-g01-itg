# Herencia, continuación
# Jerarquía de clases ejemplo

# Ej.1
class One:
    def do_it(self):
        print('do it de One')

    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print('do it de Two')

# main
one = One()
two = Two()

one.doanything()
two.doanything()
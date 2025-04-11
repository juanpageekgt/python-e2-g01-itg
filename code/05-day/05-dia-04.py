# Cómo crear tu propia excpeción

# Ej.1
class MyZeroDivisionError(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError('perores noticias')
    else:
        raise ZeroDivisionError('malas noticias')


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division entre cero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('Mi division entre cero')
    except ZeroDivisionError:
        print('Division entre cero original')


# Ej.2
class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza

# Ej.3
class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

# Ej.4
def make_pizza(pizza, cheese):
    if pizza not in ['margarita', 'capricciosa', 'peperoni']:
        raise PizzaError(pizza, 'no existe tal pizza en el menu')
    
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, 'demasiado queso')
    
    print('!Pizza Lista!')

for (pz, ch) in [('capricciosa', 0), ('margarita', 110), ('carnivora', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)


# Ej.5
class PizzaError(Exception):
    def __init__(self, pizza='no encontrada en el menu', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='no encontrada en el menu', cheese='>100 gramos de Queso', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margarita', 'capricciosa', 'peperoni']:
        raise PizzaError
    
    if cheese > 100:
        raise TooMuchCheeseError
    
    print('!Pizza Lista!')


for (pz, ch) in [('capricciosa', 0), ('margarita', 110), ('carnivora', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

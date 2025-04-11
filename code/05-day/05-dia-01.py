# Herencia, Jerarquía de Clases (continuación)

# Ej.2
""" import time

class TrackedVehicle:
    def control_track(left, stop):
        pass

    def turn(left):
        control_track(left, True)
        time.sleep(0.25)
        control_track(left, False)

class WheeledVehicle:
    def turn_front_wheeles(left, on):
        pass

    def turn(left):
        turn_front_wheeles(left, True)
        time.sleep(0.25)
        turn_front_wheeles(left, False) """


# Ej.3
""" import time

class Vehicle:
    def change_direction(left, on):
        pass

    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)

class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass

    def change_direction(left, on):
        control_track(left, on)

class WheeledVehicle(Vehicle):
    def turn_front_wheeles(left, on):
        pass

    def change_direction(left, on):
        turn_front_wheeles(left, on) """


# Ej.4
""" import time

class Tracks:
    def change_direction(self, left, on):
        print('pistas: ', left, on)

class Wheeles:
    def change_direction(self, left, on):
        print('ruedas: ', left, on)

class Vehicle:
    def __init__(self, controller):
        self.controller = controller
    
    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)

# main
wheeled = Vehicle(Wheeles())
tracked = Vehicle(Tracks())

wheeled.turn(True)
print()
tracked.turn(False) """


# Ej.5
""" class Top:
    def m_top(self):
        print('superior')

class Middle(Top):
    def m_middle(self):
        print('Medio')
    
class Bottom(Middle):
    def m_bottom(self):
        print('abajo')

# main
object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top() """


# Ej.6
""" class Top:
    def m_top(self):
        print('superior')

class Middle(Top):
    def m_middle(self):
        print('Medio')
    
class Bottom(Middle, Top):
    def m_bottom(self):
        print('abajo')

# main
object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top() """


# Ej.7
""" class Top:
    def m_top(self):
        print('superior')

class Middle(Top):
    def m_middle(self):
        print('Medio')
    
class Bottom(Top, Middle):
    def m_bottom(self):
        print('abajo')

# main
object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top() """


# Ej.8
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# main
d = D()


# Ej.9
class Top:
    def m_top(self):
        print('Top')

class Middle_Left(Top):
    def m_middle(self):
        print('middle_left')

class Middle_Right(Top):
    def m_middle(self):
        print('middle_right')

class Bottom(Middle_Right, Middle_Left):
    def m_bottom(self):
        print('bottom')

# main
object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

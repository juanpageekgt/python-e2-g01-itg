# Cierres

# Ej.1
def outer(par):
    loc = par

var = 1
outer(var)

print(var)
print(loc)

# Ej.2
def outer(par):
    loc = par

    def inner():
        return loc
    return inner

var = 1
fun = outer(var)
print(fun())

# Ej.3
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power

fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

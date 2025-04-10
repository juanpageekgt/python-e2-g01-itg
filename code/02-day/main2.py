from sys import path
path.append('..\\packages\\extrapack.zip')

# import extra.iota
# print(extra.iota.FunI())

from extra.iota import FunI
print(FunI())

print()

# import extra.good.best.sigma
# from extra.good.best.tau import FunT

# print(extra.good.best.sigma.FunS())
# print(FunT())

print()

# utilizando alias
import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())


# Más acerca de listas por comprensión

# Ej.1
list1 = []

for ex in range(6):
    list1.append(10 ** ex)

list2 = [10 ** ex for ex in range(6)]

print(list1)
print(list2)

print()

# Ej.2
the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

print()

# Ej.3
the_list2 = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list2)

print()

# Ej.4
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

print(len(the_list))
# print(len(the_generator))

print()

# Ej.5
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()

# Obtener información sobre el sistema operativo

# Ej.1
# linux
""" import os
print(os.uname()) """

# Windows
""" import platform
print(platform.system())
print(platform.release()) """

# ej.2
""" import os

os.mkdir("my_first_directory")
print(os.listdir()) """


# ej.3
""" import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir('my_first_directory')
print(os.listdir()) """

# Ej.4
""" import os
os.makedirs('my_first_directory/my_second_directory')
os.chdir('my_first_directory')
print(os.getcwd())
os.chdir('my_second_directory')
print(os.getcwd) """


# ej.5
""" import os

os.mkdir('my_first_directory')
print(os.listdir())

os.rmdir('my_first_directory')
print(os.listdir()) """

# ej.6
""" import os

os.makedirs('my_first_directory/my_second_directory')
print(os.listdir())

print()

os.removedirs('my_first_directory/my_second_directory')
print(os.listdir()) """

# Ej.7
import os

returned_value = os.system('mkdir my_first_directory')
print(returned_value)

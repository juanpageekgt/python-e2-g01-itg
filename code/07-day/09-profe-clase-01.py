# --------------- PARTE 1 -----------------------------
# Parte 1: Creando el primer grupo de widgets
import tkinter  # Importamos la librería 
from tkinter import ttk  # se declará hasta paso 1.12

# Paso 4.2 Crear una ventana emergente de Error al no aceptar los terminos
from tkinter import messagebox

# Paso 3.1
def enter_data():
    # print("hi") realizar para probar la función, luego ya recuperar los datos
    
    # Paso 4.1 continuación
    accepted = accept_var.get()
    if accepted == "Acepto":
    
    
        # User Info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        # Paso 4.3 Obligatorio campos de nombre y apellido sino desplegar error
        if firstname and lastname:
        
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            
            # Course Info
            numcourses = numcourses_spinbox.get()
            numsemesters = numcourses_spinbox.get()
            # para capturar el checkbox modificaremos en el paso 2.2
            registration_status = reg_status_var.get()
            
            # podemos probar que los valores se capturen imprimiendo en pantalla
            print("Primer Nombre: ", firstname, "Apellido: ", lastname)
            print("Titúlo: ", title, "Edad: ", age, "Nacionalidad: ", nationality)
            print("# Cursos: ", numcourses, "# Semestre: ", numsemesters)
            # el checkbox se imprimi luego de modificar paso 2.2 y agregar en la función
            print("Registro Estado: ", registration_status)

            # creamos un pequeño separador
            print("-----------------------------------------")
        else: 
            # del Paso 4.3
            tkinter.messagebox.showwarning(title = "Error", message = "Debes ingresar nombre y apellido")

    else:
        # print("No haz aceptado los acuerdos")
        # del Paso 4.1 Está línea sera lo que contendra la ventana error emergente
        tkinter.messagebox.showwarning(title = "Error", message = "No aceptaste los terminos")

# Paso 1.1
""" Ventana raiz widget, el contendrá todos los demás widgets 
 todo lo hagamos estará dentro de está ventana,
 pensar en ella como la caja más grande donde se colocará todo"""
window = tkinter.Tk()

# Paso 1.3
""" Declaramos el titulo de nuestra ventana con la función tittle("") """
window.title("Entrada de Datos al Formulario")

# Paso 1.4
""" Explicar en Whiteboard
Creamos nuestro marco (Frame), dentro de nuestra ventana principal
podemos decir que nuestro frame está teniendo de papá a nuestra ventana raiz """
frame = tkinter.Frame(window)

# Paso 1.5
""" previamente lo definimos en una variable a la que llamamos frame, 
Ahora que ya creamos el Frame hay que empaquetarlo lo que nos permite posicionar todo
y colocarlo en la pantalla organizar todos nuestros widgets,
porque uso pack() es el más fácil y esto mantendrá todo responsive y se ajustará
a cualquier tamaño de ventana, si ejecutamos no veremos nada aún por el momento,
esto suscede porque aun estáa vacio, y tiene tamaño de cero. 
ya tenemos un frame dentro de nuestra aplicación, iremos viendo cómo lo llenaremos"""
frame.pack()

# Paso 1.6
""" Explicar en Whiteboard
Crearemos unos nuevos frames, dentro de nuestro frame anterior, así creando
una tabla de 3 filas x 1 columna, donde estarán contenidas dentro del frame 
que acabamos de crear, tomamos cómo padre para estos frame a nuestro frame creado
no a la aplicación window que cramos al incio, 
en una variable almacenamos la función labelFrame() dentro de ella sus argumentos
son frame que hace referencia en donde esta contenido, y text nos permite el nombre
que tendra esté frame"""
# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text = "Información de Usuario")

# Paso 1.7
""" La cuadricula que hemos creado es un de 1 x 1, en Python conocemos que las posiciones
están iniciadas desde 0, a lo que realmente tenemos una cuadricula de 0 x 0 ya que hablamos de
sus posiciones, utilizo la función grid() para delimitar empaquetar la cuadricula del frame 
que hemos creado con el color rojo en el whiteboard, seguiremos sin ver nada al ejecturarlo 
Paso 1.11 - agregar el padx y pady, esto dara un relleno a nuestra venta de 20px en cada coordenada """
user_info_frame.grid(row = 0, column = 0, padx = 20, pady = 20)

# Paso 1.8
""" Crearemos nustra primera etiqueta que va dentro del primer frame, que a la vez está dentro 
del Frame Padre, que está dentro de la window, es una jerarquía que nos permite tener un orden
de creación, usamos la función label() que tiene como argumentos decirle la ubicación del frame 
creado de color rojo y a la vez ponerle un nombre a está etiqueta. """
first_name_label = tkinter.Label(user_info_frame, text = "Nombre")
""" luego de crearla debemos empaquetar la etiqueta para que pueda ser mostrada en pantalla,
a lo que debmos definirle una posición, veamos en el Whiteboard lo que construiremos ahora solo
asumiremos donde la pondremos en el 0 y 0, tendremos dividio ese frame de la forma del Whiteboard """
first_name_label.grid(row = 0, column = 0)

# Paso 1.9
""" Crearemos la siguiente etiqueta para apellido repitiendo el mismo proceso,
cambiando el nombre de la variable donde contendremos la etiqueta 
lo colocaremos a la par, lo que implica la misma fila, columna 1"""
last_name_label = tkinter.Label(user_info_frame, text = "Apellido")
last_name_label.grid(row = 0, column = 1)

# Paso 1.10
""" Creamos el espacio de entrada para estas etiquetas, crearemos los campos input que se requieren
para ello usaremos la función Entry, y luego debemos empaquetarlo para que sea mostrado en el frame
ahora la fila cambiara a 1 y cada valor de columna tabulado, mostrar en el Whiteboard """
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row = 1, column = 0)
last_name_entry.grid(row = 1, column = 1)

# Paso 1.12
""" Crearemos un cuadro de selección para que el usuario pueda elegir un valor de una lista
esta requiere que importemos ttk provee una colección de widgets temáticos  para crear una
mejor apariencia, cremoa la etiqueta utilizando la variable "tittle_label" debemos especificar el
label padre a quien pertenece. """
title_label = tkinter.Label(user_info_frame, text = "Titúlo")

""" luego recuerda ir a importar ttk
para poder utilizar combobox notar su sintaxis, especificar que frame es su padre, y
realizar una lista (array) de los valores que aparecerán en el cuadro combinado """
title_combobox = ttk.Combobox(user_info_frame, values = [" ", "Sr.", "Sra.", "Dr.", "Lic.", "Ing."])
# si ejecutamos no lo veremos porque no lo hemos puesto en en la interfaz
title_label.grid(row = 0, column = 2)  # explicar en el Whiteborad quedará arriba la etiqueta y abajo la lista
title_combobox.grid(row = 1, column = 2)  #colocamos el combobox en la interfaz

# Paso 1.13
""" Crearemos un cuadro spin (spinbox) para subir o bajar la edad, y el usuario la seleccione
especificamos el rango de edad con el argumento requerido en cada programa.
nuevamente debemos crear su etiqueta y luego relizar aparezca en la interfaz """
age_label = tkinter.Label(user_info_frame, text = "Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_ = 18, to = 110)
age_label.grid(row = 2, column = 0)
age_spinbox.grid(row = 3, column = 0)

# Paso 1.14
""" Crearemos otro combobox para la nacionalidad, dado que está lista es muy grande
haremos solo unos valores, pero puedes importarla de un archivo JSON o base de datos 
creamos su etiqueta, su lista de valores y relizar aparezca en la interfaz """
nationality_label = tkinter.Label(user_info_frame, text = "Nacionalidad")
nationality_combobox = ttk.Combobox(user_info_frame, values = ["Africa", "Europa", "America", "Asia", "Antartica"])
nationality_label.grid(row = 2, column = 1)
nationality_combobox.grid(row = 3, column = 1)

# Paso 1.15
""" Observamos que todo nos sale muy pegado entre las etiquetas y entradas de datos,
esto es que va tomando el tamaño segun sus valores, si nosotros quisieramos dar un
espaciado deberiamos aplicarle a cada equiqueta, ya llevamos varias veremos un
pequeño truco para dar un ordenamiento espaciado a nuestras etiquetas """
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)




# ------------------ PARTE 2 ------------------------
# Parte 2 - Crearemos el resto de los widgets
# Paso 2.1
""" Crearemos el Segundo marco (frame), que contendrá toda la información de registro del curso
mostrar en el Whiteboard quie estamos en el marco (frame) de en medio
explicar el parámetro sticky = es el espaciado dentro del frame y news quiere decir los 4 puntos cardinales 
en ingles le dice north, east, west, south, realiza un espaciado en x, y de 20 pxl """
# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10) #20)

# Paso 2.2
""" Creamos el widget de etiqueta de Estado de registro y un botton de chek (CheckButton) 
observamos que el frame padre ahora es courses_frame 
luego empaquetar en la interfax para que aparezcan """
registered_label = tkinter.Label(courses_frame, text = "Estado de Registro")
# esto es hasta el Paso 3.1 (linea siguiente)
reg_status_var = tkinter.StringVar(value = "No Registrado")  # línea se agregar hasta paso 3.1, 
# agrego value para valor predeterminado sino la primera vez no se vera
registered_check = tkinter.Checkbutton(courses_frame, text = "Actualmente Registrado",
                                       variable = reg_status_var, onvalue = "Registrado", 
                                       offvalue = "No Registrado")  # desde variable se crea en paso 3.1
registered_label.grid(row = 0, column = 0)
registered_check.grid(row = 1, column = 0)


# Paso 2.3
""" Crearemos la etiqueta y su cuadro spin (spinbox) para indicar cuantos cursos 
completados lleva el usuario, realizamos el mismo proceso de creación visto en los anteriores """
numcourses_label = tkinter.Label(courses_frame, text = "# Cursos Completados")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_ = 0, to = "infinity")
numcourses_label.grid(row = 0, column = 1)
numcourses_spinbox.grid(row = 1, column = 1)

# Paso 2.4
""" Crearemos la equita y su cuadro spin (spinbox) para indicar numero de semestre """
numsemesters_label = tkinter.Label(courses_frame, text = "# Semestre")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_ = 0, to = "infinity")
numsemesters_label.grid(row = 0, column = 2)
numsemesters_spinbox.grid(row = 1, column = 2)

# Paso 2.5
""" Arreglaremos el área de aparición de nuestro frame de cursos para que todas las
etiquetas tengan un espaciado de x = 10 y en y = 5 de su pad"""
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

# Paso 2.6
""" Crearemos el tercer frame para los terminos y condiciones, realizaremos un checkbox
para indicar si el usuario está de acuerdo con los terminos y condiciones.
observaremos que al marcar el checbox se nos marcan todos los que llevamos en la app"""
# Accept terms
terms_frame = tkinter.LabelFrame(frame, text = "Terminos & Condiciones")
terms_frame.grid(row =2, column = 0, sticky = "news", padx = 20, pady =  10) #20)

# Paso 4.1 agrego la siguiente línea 
accept_var = tkinter.StringVar(value = "No Acepto") # línea se hace hasta paso 4.1
terms_check = tkinter.Checkbutton(terms_frame, text = "Acepto los terminos y condiciones",
                                  variable = accept_var, onvalue = "Acepto", offvalue = "No Acepto") # desde variable se agrega en Paso 4.1
terms_check.grid(row = 0, column = 0)

# Paso 2.7
""" Crearemos el boton de Enviar Información, esté estará en el frame principal, no en la window
y aquí lo crearemos especificando su fila y columan correspondientes """
# Button
button = tkinter.Button(frame, text = "Enviar Información", command = enter_data) # command se agrega hasta parte 3
button.grid(row = 3, column = 0, sticky = "news", padx = 20, pady = 10) #20)

# Paso 2.8
""" Podemos obervar que va muy bien nuestra aplicación, vemos que aún el espaciado 
entre frames es bastante los 20 px hacen que se separen mucho, cambiaremos nuestra pady a 10
en los frames de los nombres de la etiqueta y sección 3 cambios a realizar """




# ------------ PARTE 3 ---------------------
# Parte 3: Obtención de datos de los widgets
# Paso 3.1
""" Iremos a nuestro paso número 2.7 y agregar en el final del argumento, ",command = enter_data 
será adicional una función que crearemos al comienzo de nuestro script, así al hacer click
llame a nuestra función """




# Paso 1.2
""" Para ejecutar una aplicación Tkinter usamos el llamado a la ventana
mainloop() es una funcón que se mantendra ejecutando mientras la ventana
esté activa, y no se cierre al ejecutarse una vez, sino este entre un loop 
hasta presionar la x de cerrar ventan """
window.mainloop()

# Parte 4: Ventanas emergentes de validación y error
""" El formulario no se debe procesar si el usuario no acepta los terminos 
a lo que deberia indicarle un mensaje de error o indicarle que no se procesaron
sus datos por no aceptar los terminos.
A ello vamos a el Paso 2.6 y agrego similar al checkbox anterior, y en luego
en la función defino esa verificación a realizar la captura o no de los datos """

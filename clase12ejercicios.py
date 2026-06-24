# # Lista de tareas
# tareas = ["barrer", "lavar los platos", "hacer la cama"]

# # Abrimos el archivo en modo escritura
# with open("tareas.txt", "w") as archivo:
#     for tarea in tareas:
#         archivo.write(tarea + "\n")

# print("Tareas guardadas en el archivo.")

# # Abrimos el archivo en modo lectura
# with open("tareas.txt", "r") as archivo:
#     print("📄 Tareas registradas:")
#     for linea in archivo:
#         print("-", linea.strip().capitalize())

# while True:
#     entrada=input ("Ingrese una nota del 1 al 10 o escriba 'Salir' para finalizar: ").strip()
#     if entrada.lower() =="salir":
#         break
#     try:
#         nota = int(entrada)
#         if 1<=nota<=10 :
#             with open("notas.txt","a") as archivo:
#                 archivo.write(str(nota)+"\n")
#                 print("La nota se cargó correctamente")
#         else:
#             print("El número ingresado es incorrecto")
#     except:
#         print("El dato no es válido")

# with open("notas.txt","r") as archivo:
#     print("NOTAS REGISTRADAS")
#     for linea in archivo:
#         print("* "  , linea.strip())

# import sqlite3
# conexion = sqlite3.connect("productos.db")
# cursor=conexion.cursor()
# print("Conexión establecida exitosamente.")
# cursor.execute("""CREATE TABLE IF NOT EXISTS productos (
# id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,precio REAL NOT NULL)
# """)
# import sqlite3

# # Conectamos con la base
# conexion = sqlite3.connect("productos.db")
# cursor = conexion.cursor()

# with conexion:
# # Insertamos algunos productos
#     cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", ("Pan", 250.0))
#     cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", ("Leche", 390.0))
#     cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", ("Café", 1200.0))

# # Datos a actualizar
#     id_producto = 2
#     nuevo_precio = 41119.0

# # Ejecutamos la actualización
#     cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (nuevo_precio, id_producto))


#     print(f"Producto con ID {id_producto} actualizado a ${nuevo_precio}.")

#     producto_a_borrar=input("Ingrese el nombre del producto a eliminar de la base de datos : ")
#     cursor.execute("DELETE FROM productos WHERE nombre=?", (producto_a_borrar,))

#     cursor.execute("SELECT * FROM productos")
#     productos=cursor.fetchall()
#     for producto in productos:
#         id_,nombre,precio = producto
#         print(f"{id_} - {nombre} : $ {precio}")


# conexion.close()
# print("Productos agregados correctamente.")

import sqlite3

def conectar():
    conexion=sqlite3.connect("productos.db")
    cursor= conexion.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS productos (
     id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,precio REAL NOT NULL)
      """)
    return conexion

def agregar_producto():
    nombre = input("Nombre del producto: ").strip()
    try:
        precio = float(input("Precio del producto: "))
        with conectar() as con:
            con.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
        print("Producto agregado correctamente.")
    except ValueError:
        print("Precio inválido.")

def listar_productos():
    with conectar() as con:
        cursor = con.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        if productos:
            print("\n Lista de productos:")
            for id_, nombre, precio in productos:
                print(f"{id_}. {nombre} - ${precio}")
        else:
            print("No hay productos registrados.")

def modificar_precio():
    try:
        id_producto = int(input("ID del producto a modificar: "))
        nuevo_precio = float(input("Nuevo precio: "))
        with conectar() as con:
            con.execute("UPDATE productos SET precio = ? WHERE id = ?", (nuevo_precio, id_producto))
        print("Precio actualizado.")
    except ValueError:
        print("Entrada inválida.")

def eliminar_producto():
    try:
        id_producto = int(input("ID del producto a eliminar: "))
        with conectar() as con:
            con.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        print("Producto eliminado.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Modificar precio")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            modificar_precio()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción no válida.")

# Ejecutamos el menú
menu()



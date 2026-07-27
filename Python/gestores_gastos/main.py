import csv
import os

ARCHIVO = "gastos.csv"


def crear_archivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Fecha", "Categoria", "Monto"])


def agregar_gasto():
    fecha = input("Fecha (YYYY-MM-DD): ")
    categoria = input("Categoría: ")

    try:
        monto = float(input("Monto: "))
    except ValueError:
        print("Monto inválido")
        return

    with open(ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([fecha, categoria, monto])

    print("Gasto guardado correctamente")


def ver_gastos():
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        next(lector, None)

        print("\n--- LISTA DE GASTOS ---")

        for fila in lector:
            print(
                f"Fecha: {fila[0]} | "
                f"Categoría: {fila[1]} | "
                f"Monto: ${fila[2]}"
            )


def ver_total():
    total = 0

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            total += float(fila["Monto"])

    print(f"\nTotal gastado: ${total:.2f}")


def menu():
    crear_archivo()

    while True:
        print("\n===== GESTOR DE GASTOS =====")
        print("1. Agregar gasto")
        print("2. Ver gastos")
        print("3. Ver total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_gasto()

        elif opcion == "2":
            ver_gastos()

        elif opcion == "3":
            ver_total()

        elif opcion == "4":
            print("Hasta luego")
            break

        else:
            print("Opción inválida")


menu()
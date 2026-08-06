# ============================================
# CONVERSOR DE MONEDAS - VERSIÓN 4
# Autor(a): Grezzia Luna Elguera 
# ============================================

soles = float(input("Ingrese la cantidad en soles: "))

print("1. Dólares")
print("2. Euros")
print("3. Libras Esterlinas")
print("4. Yenes")

opcion = input("Seleccione una opción: ")

if opcion == "1":
    dolares = soles / 3.60
    print("Equivale a", dolares, "dólares.")

elif opcion == "2":
    euros = soles / 4.20
    print("Equivale a", euros, "euros.")

elif opcion == "3":
    libras = soles / 4.80
    print("Equivale a", libras, "libras.")

elif opcion == "4":
    yenes = soles * 41.5
    print("Equivale a", yenes, "yenes.")

else:
    print("Opción no válida.")

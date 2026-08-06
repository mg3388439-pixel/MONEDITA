# ============================================
# CONVERSOR DE MONEDAS - VERSIÓN 1
# Autor(a): Nombre del estudiante
# ============================================

soles = float(input("Ingrese la cantidad en soles: "))

print("1. Dólares")
print("2. Euros")

opcion = input("Seleccione una opción: ")

if opcion == "1":
    dolares = soles /3.60
    print("Equivale a", dolares, "dólares.")

elif opcion == "2":
    euros = soles/4.20
    print("Equivale a", euros, "euros.")

else:
    print("Opción no válida.")

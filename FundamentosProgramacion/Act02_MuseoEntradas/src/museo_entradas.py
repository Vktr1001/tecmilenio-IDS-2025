# Actividad 2 - Cobro de entradas al museo
# Autor: Viktor San Román
# Materia: Fundamentos de Programación
# Descripción: Programa que calcula el total a pagar de entradas al museo,
# aplicando descuentos según el tipo de visitante. Incluye uso de break y continue.

def calcular_precio(edad, tipo):
    """
    Calcula el precio del boleto según edad y tipo de visitante.
    - Menores de 3 años: gratis
    - 3 a 17 años: $30
    - 18 o más: $45
    Descuentos (solo uno por boleto):
      adulto_mayor -> 12%
      profesor     -> 10%
      estudiante   -> 10%
    """
    # Niños menores de 3 no pagan
    if edad < 3:
        return 0.0

    # Precio base por edad
    precio_base = 30.0 if edad < 18 else 45.0

    # Tabla de verdad para descuentos
    if tipo == "adulto_mayor":
        descuento = 0.12
    elif tipo == "profesor":
        descuento = 0.10
    elif tipo == "estudiante":
        descuento = 0.10
    else:
        descuento = 0.0

    return precio_base * (1 - descuento)


def main():
    print("=== Museo de Antropología e Historia - Cobro de Entradas ===")
    try:
        visitantes = int(input("¿Cuántos visitantes deseas registrar? "))
    except ValueError:
        print("Entrada no válida. Terminando programa.")
        return

    total = 0.0

    for i in range(visitantes):
        print(f"\nVisitante {i+1} de {visitantes}")

        # Solicitar edad
        try:
            edad = int(input("Edad: "))
        except ValueError:
            print("Edad inválida (no es un número). Saltando visitante...")
            # Uso de continue: si la edad no es numérica, omitimos esta iteración
            continue

        # Ejemplo de uso de continue: saltar si se ingresa una edad negativa
        if edad < 0:
            print("Edad inválida (negativa). Saltando visitante...")
            continue

        print("Tipos de visitante permitidos: adulto_mayor / profesor / estudiante / ninguno")
        tipo = input("Tipo de visitante: ").strip().lower()

        precio = calcular_precio(edad, tipo)
        print(f"Precio a pagar por este visitante: ${precio:.2f}")
        total += precio

        # Ejemplo de uso de break: si el usuario decide detener el registro antes de terminar
        detener = input("¿Deseas detener el registro? (s/n): ").strip().lower()
        if detener == "s":
            print("Interrumpiendo el registro por solicitud del usuario...")
            break

    print(f"\nTOTAL A PAGAR POR TODOS LOS VISITANTES: ${total:.2f}")
    print("=== Gracias por su visita ===")


if __name__ == "__main__":
    main()

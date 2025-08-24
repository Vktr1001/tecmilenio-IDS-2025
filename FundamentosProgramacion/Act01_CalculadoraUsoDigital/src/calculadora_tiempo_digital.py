# calculadora_tiempo_digital.py
# Actividad 1 - Fundamentos de la Programación
# Solicita nombre y horas en 5 plataformas; calcula total y porcentaje del día.

def leer_horas(etiqueta: str) -> float:
    while True:
        try:
            valor = float(input(f"Horas en {etiqueta}: "))
            if valor < 0:
                print("Ingresa un valor mayor o igual a 0.\n")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Escribe un número (puedes usar decimales).\n")


def main():
    print("=== Calculadora de uso digital ===")
    nombre = input("Tu nombre: ").strip()

    plataformas = [
        "redes sociales",
        "mensajería",
        "series/streaming",
        "videos",
        "videojuegos",
    ]

    total = 0.0
    for p in plataformas:
        total += leer_horas(p)

    porcentaje = (total / 24) * 100

    print("\n— Resultados —")
    print(f"Usuario: {nombre if nombre else 'N/A'}")
    print(f"Tiempo total diario: {total:.2f} horas")
    print(f"Equivale a: {porcentaje:.2f}% del día (24 h)")


if __name__ == "__main__":
    main()

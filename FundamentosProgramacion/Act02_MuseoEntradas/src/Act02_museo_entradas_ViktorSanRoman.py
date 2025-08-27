#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Actividad 2 — Fundamentos de Programación
Programa: Cobro de entradas al Museo de Antropología e Historia

Autor: Viktor Manuel San Román Carmona
Curso: Fundamentos de Programación
Descripción:
    Calcula el total a pagar por entradas al museo aplicando los descuentos
    establecidos según el tipo de visitante. Implementa una tabla de verdad
    para descuentos y demuestra el uso de las cláusulas `break` y `continue`.

Requisitos cubiertos (rúbrica):
1) Registro de visitantes: solicita número de visitantes, edad y tipo.
2) Descuentos como tabla de verdad: se aplican de forma exclusiva por boleto.
3) Uso de `break`: permite terminar el registro anticipadamente.
4) Uso de `continue`: omite iteraciones con datos inválidos.
5) Cálculo del total: suma correcta con descuentos correspondientes.

Precios y descuentos:
- Menor de 3 años: no paga boleto
- 3–17 años: $30.00 (menor de edad)
- 18+ años: $45.00 (mayor de edad)
- Descuentos (solo uno por boleto):
    adulto_mayor → 12%
    profesor     → 10%
    estudiante   → 10%

Ejemplo de uso (interacción):
    $ python3 Act02_museo_entradas_ViktorSanRoman.py
    === Museo de Antropología e Historia - Cobro de Entradas ===
    ¿Cuántos visitantes deseas registrar? 3

    Visitante 1 de 3
    Edad: 2
    Tipo de visitante (adulto_mayor/profesor/estudiante/ninguno): ninguno
    Precio de este visitante: $0.00
    ¿Deseas detener el registro? (s/n): n

    Visitante 2 de 3
    Edad: -4
    Edad inválida. Saltando visitante...
    (continue)
    
    Visitante 3 de 3
    Edad: 19
    Tipo de visitante (adulto_mayor/profesor/estudiante/ninguno): estudiante
    Precio de este visitante: $40.50
    ¿Deseas detener el registro? (s/n): s
    Interrumpiendo el registro...
    
    ----------------------------------------
    TOTAL A PAGAR: $40.50
    === Gracias por su visita ===

Notas:
- El programa valida entradas numéricas para edad y visitantes.
- La tabla de descuentos está implementada como condiciones exclusivas.
- Se muestra el uso de `continue` (edad inválida) y `break` (detener registro).
"""

from __future__ import annotations

from typing import Dict

# ------------------------------
# Constantes de negocio
# ------------------------------
PRICE_CHILD: float = 30.0      # 3–17 años
PRICE_ADULT: float = 45.0      # 18+ años

# Tabla de verdad de descuentos (solo uno por boleto)
# clave -> porcentaje de descuento
DISCOUNTS: Dict[str, float] = {
    "adulto_mayor": 0.12,
    "profesor": 0.10,
    "estudiante": 0.10,
    "ninguno": 0.0,
}


def calcular_precio(edad: int, tipo: str) -> float:
    """Calcula el precio del boleto aplicando un único descuento.

    Reglas:
    - edad < 3  → $0.00
    - 3 <= edad < 18 → PRICE_CHILD
    - edad >= 18 → PRICE_ADULT
    - Descuento exclusivo según `tipo` (tabla de verdad en DISCOUNTS).
    """
    if edad < 3:
        return 0.0

    precio_base = PRICE_CHILD if edad < 18 else PRICE_ADULT
    descuento = DISCOUNTS.get(tipo, 0.0)  # si el tipo no existe, 0%

    return round(precio_base * (1.0 - descuento), 2)


def pedir_entero(mensaje: str) -> int:
    """Pide un entero al usuario; reintenta hasta obtener uno válido."""
    while True:
        dato = input(mensaje).strip()
        try:
            return int(dato)
        except ValueError:
            print("Entrada inválida. Intenta de nuevo (número entero).")


def pedir_tipo() -> str:
    """Solicita el tipo de visitante y lo normaliza a las opciones válidas."""
    print("Tipos permitidos: adulto_mayor / profesor / estudiante / ninguno")
    tipo = input("Tipo de visitante: ").strip().lower()
    if tipo not in DISCOUNTS:
        print("Tipo no reconocido. Se tomará como 'ninguno'.")  # continue no aplica aquí
        return "ninguno"
    return tipo


def main() -> None:
    print("=== Museo de Antropología e Historia - Cobro de Entradas ===")
    visitantes = pedir_entero("¿Cuántos visitantes deseas registrar? ")

    total: float = 0.0

    for i in range(visitantes):
        print(f"\nVisitante {i + 1} de {visitantes}")

        # Solicitar edad (demostración de continue en caso inválido)
        try:
            edad = int(input("Edad: ").strip())
        except ValueError:
            print("Edad inválida (no es un número). Saltando visitante...")
            continue

        if edad < 0:
            print("Edad inválida (negativa). Saltando visitante...")
            continue  # no contamos este visitante

        tipo = pedir_tipo()
        precio = calcular_precio(edad, tipo)

        print(f"Precio de este visitante: ${precio:.2f}")
        total += precio

        # Demostración de break: permitir terminar registro anticipadamente
        detener = input("¿Deseas detener el registro? (s/n): ").strip().lower()
        if detener == "s":
            print("Interrumpiendo el registro...")
            break

    print("\n----------------------------------------")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("=== Gracias por su visita ===")


if __name__ == "__main__":
    main()

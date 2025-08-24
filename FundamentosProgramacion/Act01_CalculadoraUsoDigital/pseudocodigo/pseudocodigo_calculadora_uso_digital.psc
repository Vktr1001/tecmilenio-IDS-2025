Proceso CalculadoraUsoDigital
    Definir nombre Como Cadena
    Definir redes, mensajeria, streaming, videos, videojuegos, total, porcentaje Como Real

    Escribir "=== Calculadora de uso digital ==="
    Escribir "Ingresa tu nombre:"
    Leer nombre

    Repetir
        Escribir "Horas en redes sociales (>=0, decimales permitidos):"
        Leer redes
    Hasta Que redes >= 0

    Repetir
        Escribir "Horas en mensajeria (>=0):"
        Leer mensajeria
    Hasta Que mensajeria >= 0

    Repetir
        Escribir "Horas en series/streaming (>=0):"
        Leer streaming
    Hasta Que streaming >= 0

    Repetir
        Escribir "Horas viendo videos (>=0):"
        Leer videos
    Hasta Que videos >= 0

    Repetir
        Escribir "Horas en videojuegos (>=0):"
        Leer videojuegos
    Hasta Que videojuegos >= 0

    total <- redes + mensajeria + streaming + videos + videojuegos
    porcentaje <- (total / 24) * 100

    Escribir "\nUsuario: ", nombre
    Escribir "Tiempo total: ", total, " horas"
    Escribir "Porcentaje del día (24 h): ", porcentaje, "%"
FinProceso

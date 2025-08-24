# Tecmilenio – Ingeniería en Desarrollo de Software (Repositorio de actividades)

Este repositorio centraliza **actividades, proyectos y entregables** por curso y actividad.

## Estructura
```
tecmilenio-IDS-2025/
└── FundamentosProgramacion/
    └── Act01_CalculadoraUsoDigital/
        ├── src/                       # Código fuente en Python
        ├── pseudocodigo/              # PSeInt (.psc) y variantes
        ├── diagramas/                 # Diagramas Mermaid (.mmd) o imágenes exportadas
        ├── docs/                      # Instrucciones, rúbricas y PDFs de referencia
        ├── evidencias/                # Capturas de pantalla / PDF de evidencia
        └── README.md                  # Guía de ejecución y criterios de entrega
```

## Convenciones rápidas
- **Ramas**: `main` (estable), `feat/*`, `fix/*`.
- **Commits** (Conventional Commits): `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`.
- **Licencia**: MIT (puedes cambiarla si es necesario).

## Cómo agregar una nueva actividad
1. Duplica la carpeta de una actividad anterior y renómbrala (p. ej., `Act02_*`).
2. Actualiza su `README.md`, diagramas y código.
3. Commits descriptivos y PR si trabajas con colaboración.

### Config rápida de git (global)
```bash
git config --global user.name "Vktr1001"
git config --global user.email "vk.src9@gmail.com"
```

---
### Atajo: script de inicialización
También puedes usar:
```bash
./scripts/init_repo.sh https://github.com/Vktr1001/tecmilenio-IDS-2025.git
```
(Asegúrate de crear el repo vacío en GitHub y sustituir la URL si usas SSH.)

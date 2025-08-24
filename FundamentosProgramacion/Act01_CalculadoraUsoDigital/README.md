# Act 1 – Calculadora de uso digital

**Descripción**: Calcula el total de horas diarias dedicadas a plataformas digitales y el **porcentaje del día (24 h)** que representan.


## Diagrama de flujo (Mermaid)

```mermaid
flowchart TD
  A[Inicio] --> B[Pedir nombre]
  B --> C[total ← 0]
  C --> D{Plataformas (5)}
  D -->|redes| E1[Pedir horas redes (≥0); total += horas]
  D -->|mensajería| E2[Pedir horas mensajería (≥0); total += horas]
  D -->|streaming| E3[Pedir horas streaming (≥0); total += horas]
  D -->|videos| E4[Pedir horas videos (≥0); total += horas]
  D -->|videojuegos| E5[Pedir horas videojuegos (≥0); total += horas]
  E1 --> F[porcentaje ← (total/24)*100]
  E2 --> F
  E3 --> F
  E4 --> F
  E5 --> F
  F --> G[Mostrar nombre, total, porcentaje]
  G --> H[Fin]
```

> Si no ves el diagrama en VS Code, instala **Markdown Preview Mermaid Support** o **Markdown Preview Enhanced** y abre el preview (⌘⇧V / Ctrl+Shift+V).

## Pseudocódigo (PSeInt)
Consulta `pseudocodigo/pseudocodigo_calculadora_uso_digital.psc`

## Código (Python)
Archivo principal: `src/calculadora_tiempo_digital.py`

### Ejecución
```bash
# macOS / Linux
python3 src/calculadora_tiempo_digital.py

# Windows
python src\calculadora_tiempo_digital.py
```

## Evidencia sugerida para entrega
- Captura del diagrama renderizado.
- Captura de la ejecución en terminal con datos de ejemplo.
- PDF con notas o reflexión (opcional) en `evidencias/`.

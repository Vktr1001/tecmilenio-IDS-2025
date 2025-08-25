```mermaid
flowchart TD
%%{init: {'theme':'neutral','themeVariables':{'fontSize':'16px'}}}%%
  A[Inicio] --> B[Pedir nombre]
  B --> C[total = 0]
  C --> D{Plataformas}

  D --> E1[Pedir horas redes >= 0; total = total + horas]
  D --> E2[Pedir horas mensajeria >= 0; total = total + horas]
  D --> E3[Pedir horas streaming >= 0; total = total + horas]
  D --> E4[Pedir horas videos >= 0; total = total + horas]
  D --> E5[Pedir horas videojuegos >= 0; total = total + horas]

  E1 --> F[Calcular porcentaje]
  E2 --> F
  E3 --> F
  E4 --> F
  E5 --> F
  F --> G[Mostrar nombre, total, porcentaje]
  G --> H[Fin]
  ```
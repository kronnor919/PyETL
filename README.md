# 🧾 PyETL

¿En qué consiste esto? Es un mini-proyecto de código abierto desarrollado por una sola persona, cuyo objetivo es permitir el análisis y la generación de gráficas a partir de diferentes fuentes de información, concretamente archivos como Excel, JSON, CSV, entre otros.

Podrás crear tus reportes y gráficos de la forma que prefieras, todo a través de una interfaz CLI. Y tranquilo, me aseguraré de que todo esté bien documentado, para que no tengas que memorizar todos los comandos o argumentos que utilizará la aplicación (que tampoco serán muchos).

---

### ❓ ¿Qué problema resuelve este software?

Este proyecto busca resolver varios problemas comunes que enfrentan quienes trabajan con datos, especialmente en tareas repetitivas que, con el tiempo, pueden volverse tediosas:

- Elimina trabajo manual, evitando que los datos tengan que ser limpiados y organizados a ojo y mano cada vez.
- Facilita el acceso a información estructurada, convirtiendo archivos dispersos en una base de datos bien organizada.
- Optimiza la generación de reportes, ya que en lugar de tener que hacer un análisis manualmente mediante hojas de cálculo, se automatizan consultas y generación de gráficos.
- Mejora la calidad de los datos, asegurándose de que los datos sean consistentes, homogéneos y que no haya duplicados antes de proceder a su análisis.
- Sin saber prácticamente nada de SQL podrás interactuar con una base de datos y generar consultas básicas. Aunque si sabes SQL, puedes crear consultas personalizadas y usarlas para generar reportes más avanzados.

---

### 🗂️ Estructura del proyecto

```
PyETL/
├── .gitignore
├── LICENSE
├── README.md
├── CHANGELOG.md
├── requirements.txt
└── src/
    ├── cli/
    ├── config/
    ├── ETL/
    ├── logs/
    ├── queries/
    ├── reports/
    ├── tests/
    ├── main.py
    └── util.py
```

---

### Licencias
- MIT: Este proyecto es de uso libre, con contribución a los colaboradores principales. 
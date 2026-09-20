<<<<<<< HEAD
# INF-8239-U01

## Configuración del entorno de desarrollo

Este proyecto corresponde a la primera unidad de la asignatura INF-8239.

### Sistema operativo

* Windows 10/11
* PowerShell
* Visual Studio Code

### Herramientas utilizadas

* Python
* Git
* Jupyter Notebook
* Pylance
* Ruff
* Pytest

### Estructura del proyecto

```text
INF8239_U01/
├── data/
├── notebooks/
├── reports/
├── src/
│   └── inf8239_u01/
│       ├── __init__.py
│       └── environment.py
└── tests/
    └── test_environment.py
```

### Configuración del entorno virtual

El entorno virtual se creó con:

```powershell
python -m venv .venv
```

Activación en PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Ejecución de las pruebas

Para ejecutar las pruebas:

```powershell
$env:PYTHONPATH="src"
python -m pytest -q
```

### Verificación de Jupyter

Se verificó que el notebook utilizara el intérprete de Python ubicado dentro de `.venv`.

### Control de versiones

Se inicializó el repositorio Git con:

```powershell
git init
git add .
git commit -m "chore: create INF-8239 reproducible environment"
```

### Estado final

El proyecto fue preparado con un entorno virtual, una estructura organizada de carpetas y una prueba inicial de funcionamiento.
=======
# INF8239_U01
Laboratorios de Ciencia de Datos II
>>>>>>> d59ba77f2f18f7d5093dd20136c41fef23ce60d2

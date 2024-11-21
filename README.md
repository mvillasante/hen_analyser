# Basic python project template
[![codecov](https://codecov.io/gh/IslasGECI/basic_python_project/graph/badge.svg?token=RY807ST1T1)](https://codecov.io/gh/IslasGECI/basic_python_project)
![example branch
parameter](https://github.com/IslasGECI/basic_python_project/actions/workflows/actions.yml/badge.svg)
![licencia](https://img.shields.io/github/license/IslasGECI/basic_python_project)
![languages](https://img.shields.io/github/languages/top/IslasGECI/basic_python_project)
![commits](https://img.shields.io/github/commit-activity/y/IslasGECI/basic_python_project)
![PyPI - Version](https://img.shields.io/pypi/v/basic_python_project)

Para usar este repo como plantilla debemos hacer lo siguiente:

1. Presiona el botón verde que dice _Use this template_
1. Selecciona como dueño a la organización IslasGECI
1. Agrega el nombre del nuevo módulo de python
1. Presiona el botón _Create repository from template_
1. Reemplaza `basic_python_project` por el nombre del nuevo módulo en:
    - `Makefile`
    - `pyproject.toml`
    - `tests\test_transformations.py`
1. Renombra el archivo `basic_python_project\transformations.py` al nombre del primer archivo del
   nuevo módulo
1. Cambia la descripción del archivo `basic_python_project\__init__.py`
1. Renombra el directorio `basic_python_project` al nombre del nuevo módulo
1. Cambia el `codecov_token` del archivo `Makefile`

Los archivos del nuevo módulo los agregarás en la carpeta que antes se llamaba
`basic_python_project` y las pruebas en la carpeta `tests`.

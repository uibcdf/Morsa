# Instalación

## Versión estable

La última versión estable de Morsa puede ser instalada del canal UIBCDF de Conda:

```bash
conda -c uibcdf morsa
```

En este caso, para desinstalar la librería:

```bash
conda remove morsa
```

## Versión en desarrollo

Si quieres trabajar con la versión en desarrollo del proyecto Morsa, puedes obtener el código
directamente del repositorio principal en GitHub e instalar la librería localmente según:

```bash
git clone https://github.com/uibcdf/Morsa.git
cd Morsa
python setup.py develop
```

En este caso, para desinstalar la librería de tu sistema o de tu microambiente de python:

```bash
pip uninstall morsa
```

Esto último no borra la carpeta de código de Morsa. Únicamente excluye la librería del conjunto de
librerías accesibles al invocar Python.


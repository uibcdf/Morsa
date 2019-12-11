from setuptools import setup, find_packages

setup(
    name='morsa',
    version='1.0.0',
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    package_dir={'morsa': 'morsa'},
    packages=find_packages(),
    package_data={'morsa': []},
    scripts=[],
    url='http://github.uibcdf.org/Morsa',
    download_url ='https://github.com/uibcdf/Morsa',
    license='MIT',
    description="Morsas, pingüinos y ballenas juegan al parchis, dominó, ajedrez y tres en ralla. ¿Quien ganará?",
    long_description="Esta libreria es el producto final de un tutorial sobre cómo programar una\
    librería en Python (ver: xxx). Puedes encontrar más información en xxx.",
)


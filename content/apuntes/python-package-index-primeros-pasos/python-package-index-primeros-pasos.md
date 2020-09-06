Title: Python Package Index (PyPI): primeros pasos
Slug: python-package-index-primeros-pasos
Summary: PyPI es el repositorio de paquetes de Python por excelencia. En este apunte están los pasos para preparar software que se instale con pip.
Tags: python
Date: 2020-09-05 22:28
Modified: 2020-09-05 22:28
Category: apuntes
Preview: pypi.png


En este apunte se usa `pypi_primeros_pasos` como el nombre del paquete; debe cambiarlo por el nombre que vaya a usar.

## Crear un nuevo repositorio en GitHub

Un buen punto de partida y futuro _home_ de su paquete es hacer un nuevo repositorio en [GitHub](https://github.com) (o el servicio _git_ que prefiera). Luego de crearlo baje una copia con las siguientes órdenes; sustituya `USUARIO` por su cuenta.

    $ mkdir -p ~/Documentos/GitHub/USUARIO
    $ cd ~/Documentos/GitHub/USUARIO
    $ git clone git@github.com:USUARIO/pypi_primeros_pasos.git
    $ cd pypi_primeros_pasos

## Crear la estructura para el paquete

Prepare los directorios y archivos en la copia local de su repositorio así:

    pypi_primeros_pasos
     |- LICENSE
     |- README.md
     |- ejemplo
     |   |- __init__.py
     |- setup.py
     |- tests

Donde `LICENCE` tiene el texto con la licencia de software y `README.md` una breve semblanza de lo que hace el paquete.

Debe crear el directorio `tests` para colocar pruebas; por el momento puede estar vacío.

    $ mkdir tests

Edite el `setup.py` como en este ejemplo...

    import setuptools

    with open('README.md', 'r') as puntero:
        long_description = puntero.read()

    setuptools.setup(
        name='pypi_primeros_pasos',
        version='0.1',
        author='Su nombre completo',
        author_email='correo@ejemplo.com',
        description='Una línea que lo describa.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/USUARIO/pypi_primeros_pasos',
        python_requires='>=3.6',
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
            'Operating System :: POSIX :: Linux',
        ],
        packages=setuptools.find_packages(),
        include_package_data=True,
        install_requires=[
            'paquete_dependencia_1',
            'paquete_dependencia_2',
            'paquete_dependencia_3',
        ],
    )

Los principales valores a declarar son...

- **name:** el nombre único del paquete
- **version:** número de versión
- **author:** su nombre completo
- **author_email:** dirección de correo electrónico
- **description:** explique en una oración de que se trata
- **long_description:** una descripción más larga que se cargará desde README.md
- **url:** el repositorio público (puede ser de GitHub) donde encontrarlo
- **classifiers:** metadatos que describen el lenguaje, la licencia y el sistema operativo
- **include_package_data:** ordena que se incluyan archivos que no son parte ejecutable
- **install_requires:** otros paquetes que se requieren instalar

## Crear un entorno virtual Python 3

Prepare un entorno vitual Python 3 donde colocaremos el código del paquete así como los directorios y archivos para que se haga la entrega a PyPI. Recomiendo tenerlo por separado de la copia del repositorio; para este ejemplo uso `PyPIPrimerosPasos`.

    $ mkdir ~/VirtualEnv
    $ cd ~/VirtualEnv
    $ virtualenv -p python3 PyPIPrimerosPasos
    $ cd PyPIPrimerosPasos/
    $ . bin/activate

## Registro en Test PyPI

Ya sea para aprender o para poner a prueba su paquete use el servicio Pruebas de PyPI: <https://test.pypi.org/>. **CUIDADO:** Tenga en cuenta que Test es efímero, porque va eliminando las entregas más antiguas. Solicite su registro; le pedirá su nombre, correo electrónico, usuario y contraseña dos veces. Luego deberá confirmar su correo electrónico.

**NOTA:** Más adelante regístrese en PyPI <https://pypi.org/>; allí debe de repetir todo proceso de registro; por lo que las contraseñas y las llaves API deberán ser diferentes.

## Genere una llave API de Test PyPI

En _Account settings_ > _API tokens_ de clic en _Add API token_

Escriba un nombre para la llave, le recomiendo que sea relativo al equipo donde la vaya a usar. Para que interactúe con todos sus paquetes elija _Entire account (all projects)_. Luego de click _Add token_.

El token estará visible solo en esta ocasión; de clic en _Copy token_ y **NO** cierre esa pestaña del navegador de internet hasta haberla guardado.

Prepare el archivo `.pypirc` para guardarlo; debe estar en su _HOME_...

    $ nano -w ~/.pypirc

Y péguelo como `password` en un nuevo archivo como lo siguiente...

    [testpypi]
    username = __token__
    password = pypi-xxxxxxxxxxxxxxxx...

Ya guardado puede cerrar la pestaña del naveador de internet con el token.

**NOTA:** Cuando tenga el registro en **PyPI** podrá repetir el proceso para generar la llave API para esa cuenta y agregarla al mismo archivo `.pypirc` de esta forma...

    [pypi]
    username = __token__
    password = pypi-xxxxxxxxxxxxxxxx...

## Generar los archivos para su distribución

Cámbiese al directorio donde está la copia local del repositorio

    (PyPIPrimerosPasos) $ cd ~/Documentos/GitHub/USUARIO/pypi_primeros_pasos

Verifique que tenga `setuptools` y `wheel` instalados

    (PyPIPrimerosPasos) $ pip list

Genere los archivos para distribuir con...

    (PyPIPrimerosPasos) $ python3 setup.py sdist bdist_wheel

Esa orden creará el directorio `dist` que contiene un comprimido con los archivos del paquete.

## Subir el paquete

Instale twine en este entorno...

    (PyPIPrimerosPasos) $ pip install twine

Suba el paquete ejecutando...

    (PyPIPrimerosPasos) $ python3 -m twine upload --repository testpypi dist/*

**NOTA:** En _repository_ use `testpypi` para **Test PyPI**. En cambio para **PyPI** use `pypi`.

Verifique que puede ver su nuevo paquete en el navegador de internet con la URL que aparece.

Abandone el entorno virtual con...

    (PyPIPrimerosPasos) $ decativate

## Probar la descarga

Elabore un nuevo entorno virtual

    $ cd ~/VirtualEnv
    $ virtualenv -p python3 PruebaPyPIPrimerosPasos
    $ cd PruebaPyPIPrimerosPasos/
    $ . bin/activate

Instale su nuevo paquete desde Test PyPI con

    (PruebaPyPIPrimerosPasos) $ pip install pypi_primeros_pasos

## Referencias

- [Tutorial - Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

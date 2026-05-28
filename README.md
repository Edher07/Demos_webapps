# Demos_webapps
Ejercicios de Aplicaciones Web con Python 3,SQLite3 y Web.py

# 1. Crear un Virtual Environment

Crear el virtual environment para la instalación de las librerías necesarias para el proyecto.

````shell
python3 -m venv .venv
````

## 2. Crear el archivo .gitignore

Crear el archivo **gitignore** para configurar los recursos que no necesitamos que se sincronicen con el repositorio.

````shell
*.pyc
_pycache_/
.venv/
````

## 3. Activar el vitual environmet

Activar el **virtual environment** para realizar la instalación de las libreríasnecesarias

````shell
source .venv/bin/activate
````

## 4. Actualizar **PIP**

Actualizar el instalador de paquetes de python **PIP**.

````shell
pip install --upgrade pip
````


## 5. Crear el archivo **runtime.txt**

Crear el archivo **runtime.txt** con la versión utilizada de python3.
````shell
python3 -V > runtime.txt
````

## 6. Instalar el micro-framework **web.py**

Instalar el micro-framework **web.py** en el ambiente virtual (virtual environment)

````shell
pip install web.py
````

## 7. Crear el archivo **requirements.txt**

Crear el archivo **requirements.txt** con las versiones de las librerías instaladas en el ambiente virtual.

````shell
pip freeze > requirements.txt
````

## 8. Indexar el contenido del repositorio

Indexar todo el contenido del repositorio para incluir todos los archivos nuevos y las modificaciones al código.

````shell
git add .
````

## 9. Crear un **commit** o punto de control 

Crear un punto de control (**commit**) con los cambios realizados al proyecto.

````shell 
git commit -m "CREATED configuración del ambiente virtual"
````

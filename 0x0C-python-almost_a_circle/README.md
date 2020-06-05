# Objetivos de aprendizaje
Al final de este proyecto, se espera que puedas explicarle a cualquiera , sin la ayuda de Google :

## General
- ¿Qué son las pruebas unitarias y cómo implementarlas en un proyecto grande?
- Cómo serializar y deserializar una clase
- Cómo escribir y leer un archivo JSON
- Qué es *argsy cómo usarlo
- Qué es **kwargsy cómo usarlo
- Cómo manejar argumentos con nombre en una función

# Requisitos

## Python Scripts
- Editores permitidos: vi, vim,emacs
- Todos sus archivos serán interpretados / compilados en Ubuntu 14.04 LTS usando python3(versión 3.4.3)
- Todos sus archivos deben terminar con una nueva línea.
- La primera línea de todos sus archivos debe ser exactamente #!/usr/bin/python3
- Un README.mdarchivo, en la raíz de la carpeta del proyecto, es obligatorio.
- Su código debe usar el PEP 8estilo (versión 1.7. *)
- Todos tus archivos deben ser ejecutables
- La longitud de sus archivos será probada usando wc
- Todos sus módulos deben estar documentados: python3 -c 'print(__import__("my_module").__doc__)'
- Todas sus clases deben estar documentadas: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
- Todas sus funciones (dentro y fuera de una clase) deben documentarse: python3 -c 'print(__import__("my_module").my_function.__doc__)'ypython3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'

## Pruebas unitarias de Python
- Editores permitidos: vi, vim,emacs
- Todos sus archivos deben terminar con una nueva línea.
- Todos sus archivos de prueba deben estar dentro de una carpeta tests
- Tienes que usar el módulo unittest
- Todos los archivos de prueba deben ser archivos pitón (extensión .py)
- Todos sus archivos y carpetas de prueba deben comenzar con test_
- Su organización de archivos en la carpeta de pruebas debe ser la misma que su proyecto: por ejemplo models/base.py, para , las pruebas unitarias deben estar en:tests/test_models/test_base.py
- Todas sus pruebas deben ejecutarse utilizando este comando: python3 -m unittest discover tests
- También puede probar archivo por archivo con este comando: python3 -m unittest tests/test_models/test_base.py
- Le recomendamos encarecidamente que trabajen juntos en casos de prueba para que no se pierda ningún caso de borde

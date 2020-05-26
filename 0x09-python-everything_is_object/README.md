# Contexto de fondo
Ahora que entendemos que todo es un objeto y tenemos un poco de conocimiento, hagamos una pausa y veamos un poco más de cerca cómo funciona Python con diferentes tipos de objetos.

Por cierto, ¿alguna vez has modificado una variable sin saberlo o sin querer? Quiero decir:
"""
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>> 
OKAY. ¿Pero qué hay de esto?

>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
"""


Este proyecto es un poco diferente a los proyectos habituales. La primera parte es solo preguntas sobre la especificidad de Python como "¿Cuál sería el resultado de ...". Primero debe leer toda la documentación (como de costumbre :)) , luego tomarse el tiempo para pensar y hacer una lluvia de ideas con sus compañeros sobre lo que piensa y por qué. Intenta hacer esto sin codificar nada durante unas horas .

Probar ejemplos en el intérprete de Python le dará la mayoría de las respuestas sin tener que pensarlo. No sigas esta ruta . Primero lean, luego piensen, luego hagan una lluvia de ideas juntos. Solo entonces puedes probar en el intérprete.

Es importante que comprenda realmente las razones detrás de las respuestas de todas esas tareas para que pueda aplicar la misma lógica a otras variables y a otros tipos de variables. La tarea obligatoria más importante es la publicación del blog y contará con el 50% de la puntuación total del proyecto.

Tenga en cuenta que durante las entrevistas para los puestos de Python, lo más probable es que tenga que responder a este tipo de preguntas .

Todas sus respuestas deben ser solo una línea en un archivo. No hay espacio antes o después de la respuesta.

## Recursos
Leer o mirar :

9.10. Objetos y valores
9.11. Aliasing
Tipos inmutables vs mutables
Mutación ( solo este capítulo )
9.12. Listas de clonación
Tuplas de Python: inmutables pero potencialmente cambiantes
Objetivos de aprendizaje
Al final de este proyecto, se espera que puedas explicarle a cualquiera , sin la ayuda de Google :

## General
Por qué la programación de Python es increíble (no olvides twittear hoy, con el hashtag #pythoniscool :))
¿Qué es un objeto?
¿Cuál es la diferencia entre una clase y un objeto o instancia?
¿Cuál es la diferencia entre objeto inmutable y objeto mutable
¿Qué es una referencia?
¿Qué es una tarea?
¿Qué es un alias?
Cómo saber si dos variables son idénticas
Cómo saber si dos variables están vinculadas al mismo objeto
Cómo mostrar el identificador de variable (que es la dirección de memoria en la implementación de CPython)
¿Qué es mutable e inmutable?
¿Cuáles son los tipos mutables incorporados?
¿Cuáles son los tipos inmutables incorporados?
¿Cómo pasa Python las variables a las funciones?
Requisitos
Python Scripts
Editores permitidos: vi, vim,emacs
Todos sus archivos serán interpretados / compilados en Ubuntu 14.04 LTS usando python3(versión 3.4.3)
Todos sus archivos deben terminar con una nueva línea.
La primera línea de todos sus archivos debe ser exactamente #!/usr/bin/python3
Un README.mdarchivo, en la raíz de la carpeta del proyecto, es obligatorio.
Su código debe usar el PEP 8estilo ( version 1.7.*)
Todos tus archivos deben ser ejecutables
La longitud de sus archivos será probada usando wc
.txt Archivos de respuesta
Solo una linea
No shebang
Todos sus archivos deben terminar con una nueva línea.
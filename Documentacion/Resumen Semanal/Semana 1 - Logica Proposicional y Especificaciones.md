---
dg-publish: true
tags:
  - algo1
  - resumen
---
# Semana 1 — Introducción
## Intro a la Materia
En esta materia el obejetivo sera aprender a programar en lenguajes funcionales e imperativos. Especificar los problemas a resolver, pensar algoritmos para resolverlos y empezar a razonar acerca de estos, para luego escribir programas que los implementen.
## Conceptos base
- **Computadora**: Maquina electronica que procesa datos automaticamente siguiendo un programa almacenado en memoria.
- **Especificacion**: Descripcion de un problema a resolver, habitualmente en lenguaje formal. Provee las propiedades de los datos de entrada y las propiedades de la solucion. (El "**que**" resolver)
- **Algoritmo**: Descripcion de los pasos precisos *(similar a una receta)* para resolver un problema a partir de los datos de entrada adecuados. (El "**como**" resolver)
- **Programa**: Implementacion de un algoritmo en un lenguaje de programacion, para ser ejecutado en una computadora.
	- **Lenguaje de programacion**: Conjunto de instrucciones a traves del cual humanos interactuan con las computadoras. Pueden ser tipos: 
		- **Maquina**: Aquellos expresados de forma directamente inteligible por la maquina, sus instruccciones siendo cadenas de 0 y 1
		- **Bajo Nivel**: Dependen de un procesador en particular
		- **Alto Nivel**: Diseñados para que las personas puedan escribir y entender mas facilmente sus programas.
	- **Codigo Fuente**: El programa escrito en un lenguaje de prorgamacion segun sus reglas sintacticas y semanticas.
	- **Compiladores e interpretes**: Programas traductores que toman un codigo fuente y generan otro prorgama en otro lenguaje, por lo general, lenguaje de maquina.
	- **IDE**: Programas que integran un editor orientado a trabajar con proyectos y sus conjuntos de archivos, y le suman otras herramientas utiles segun el lenguaje, como highlighting, verificacion de sintaxis, vistas previas, depuradores o emuladores integrados.
## El recorrido de problema a programa
- Dado un problema a resolver, se crea una **especificacion**: Se describe de manera clara, sin ambiguedades, y se la **valida** contra el problema real.
	- A la hora de encarar problemas podemos descomponerlos en problemas mas pequeños. Esto se llama **modularizacion**, y se puede hacer de forma *Top Down* (partir del problema general y dividirlo) o *Bottom Up* (construir piezas simples y combinarlas).
	- Esta descripcion del problema no deberia condicionarse con posibles soluciones.
	- Esto nos sirve de insumo para testing, verificacion de correctitud o derivacion formal (Construir un programa a partir de la especificacion).  
- Acorde a dicha especificacion, se diseña una solucion, un **algoritmo**, que deberia poder ser **verificado** respecto a la especificacion.
- En base a esto se implementara un **programa** acorde al diseño, que deberia ser la solucion al problema planteado, y se lo **verifica** con respecto a especificacion y diseño.

## Mas sobre Especificaciones
### Lenguajes naturales y formales
A la hora de describir tenemos estas dos opciones:
- **Lenguajes naturales**: Aquellos de mayor poder expresivo, como los Idiomas, con el plus del conocimiento del contexto y suposiciones. Pueden traer inconvenientes para especificar por su ambiguedad y no poseen un calculo formal para transformar expresiones validas en otras mas sencillas o equivalentes.
- **Lenguajes formales**: Aquellos de sintaxis sencilla, limitan la expresion, explicitan suposiciones y establecen una relacion formal entre lo escrito (sintaxis) y su significado (semantica), y a cambio nos dan un calculo para transformar expresiones validas en otras validas.
### El contrato
A la hora de crear una especificacion, estamos creando un **contrato**, un acuerdo entre quien **usa** una función y quien la **implementa**:
- **Usuario:** Debera cumplir las *precondiciones* (proveer parametros validos) y podra esperar los resultados que necesita.
- **Programador:** Debera cumplir las *postcondiciones* (prover resultados validos) y podra esperar los parametros que necesita.

### Partes de una Especificacion

| Parte                       | Qué fija                                                                                     | Ejemplo: `raíz(x)`                  |
| --------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------- |
| **Encabezado**              | Nombre de la funcion, parametros/argumentos que espera y tipo de salida que podemos esperar. | Entrada: `x`; salida: un real.      |
| **Requiere** (precondición) | Condiciones sobre los parametros o argumentos. Que requiere la funcion para hacer su tarea.  | `x ≥ 0`.                            |
| **Asegura** (postcondición) | Lo que debe valer al terminar, si se cumplió `requiere`.                                     | `resultado² = x` y `resultado ≥ 0`. |
Los **parámetros** o argumentos son datos de entrada cuyo valor se conoce al ejecutar. Cada uno tiene su **tipo de datos**: un conjunto de valores provisto de operaciones permitidas sobre ellos. Ej.: fecha (comparar, obtener año) o dinero (sumar, restar).

## Paradigmas: dos formas de programar

| Paradigma       | Idea                                                                                                                                                                                                                                                                                                                                                                                                                 | En la materia                                                                                                              |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Declarativo** | Describe el resultado, relaciones o transformaciones; no necesariamente los pasos de ejecución. Puede ser de **Paradigma Logico** (los programas estan construidos unicamente por expresiones logicas) o **Funcional** (basado en el modelo matematico de composicion funcional, donde el resultado de un calculo es la entrada del siguiente, sucesivamente hasta componer el valor deseado).                       | **Haskell**. También existe el lógico (Prolog).                                                                            |
| **Imperativo**  | Indica una secuencia de comandos que cambia el estado del programa. Pueden ser de **Paradigma Estructurado** (los programas se dividen en bloques de procedimientos y funciones que pueden o no comunciarse entre si, y estructuras de control dirigen el flujo de ejecucion) o **Orientados a Objetos**, donde se encapsulan estados y comportmientos en objetos, entidades que se comunican entre si por mensajes. | **Python**. Incluye estilos estructurado y orientado a objetos. Es tambien multiparadigma, no es estrictamente imperativo. |



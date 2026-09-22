---
dg-publish: true
tags:
  - algo1
  - resumen
---
# Semana 6 - Intro a la Verificacion
**Validacion y Verificacion**: Proceso de comprobar que un sistema de software cumpla las especificaciones y proposito previsto. Tambien denominado **control de calidad del software**.
- **Validacion**: ¿Estamos haciendo el producto correcto? El software deberia hacer lo que el usuario requiere de el.
- **Verificacion**: ¿Estamos haciendo el producto correctamente? El software deberia realizar lo que su especificacion indica.
- **Falla**: Una diferencia entre los resultados esperados y los reales.
- **Defecto/Bug**: Desperfecto en algun componente del sistema que origina una o mas fallas.
- **Error**: Equivacion humana. Lleva a uno o mas defectos, presentes en un producto de software. Una falla es una manifestacion del defecto.
- **El proceso**: Se debera aplicar en cada instancia del proceso de desarrollo. En rigor no solo el codigo debera ser sometido a esto si no tambien todos los subproductos generados durante el desarrollo del software
	- **Objetivos Principales**: Descubrir defectos en el sistema, asegurar que el software respeta la especificacion y determinar si satisface las necesidades de sus usuarios.
- **Metas**: Establecer la confianza de que el software es adecuado a su proposito, lo cual no significa que este completamente libre de defectos, si no que es lo suficientemente bueno para su uso previsto, y el tipo de uso determianra el grado de confianza que se necesita.

**Calidad en Software**: Uno de nuestros objetivos principales sera obtener productos de alta calidad, lo cual se medira por atributos como **Confiabilidad, Usabilidad, Correccion, Robustez, Facilidad de Mantenimiento, Seguridad, Reusabilidad, Funcionalidad, Verificabilidad + Claridad, Interoperabilidad**, entre otros. La calidad no puede **inyectarse al final**, ya que dependera de las tareas realizadas durante todo el proceso. Detectar errores en forma temprana ahorra esfuerzos y tiempo.

Una forma de realizar tareas de V&V es a traves de analisis, en particular para el codigo tenemos el **dinamico** (Ejecutar y observar el comportamiento de un producto, tecnicas incluyen testing, run-time monitoring, entre otras) y el **estatico** (Analizar una representacion estatica del sistema para descubrir problemas, tecnicas incluyen inspecciones, revisiones, analisis de reglas sintacticas sobre codigo, analisis de data flow sobre codigo, model checking, prueba de teoremas, etc).

### Testing
Ejecutar un producto para verificar que satisface los requerimientos, e identificar diferencias entre el comportamiento real y el esperado. Su objetivo es encontrar defectos en el software, representa el 30% al 50% del costo de un software confiable.
![[Pasted image 20260921193534.png]]

#### Niveles de Test
- Test de sistema: Comprende todo el sistema, por lo general constituye el test de aceptacion.
- Test de integracion: Orientado a verificar que las partes de un sistema que funcionan bien aisladamente, tambien lo hagan en conjunto. testeamos interaccion, comunicacion entre partes.
- Test de unidad: Se realiza sobre una unidad de codigo pequeña, claramente definida.
	- Test input: Dato de prueba, asignacion concreta de valores a los parametros de entrada para ejecutar el programa bajo test.
	- Test case: Caso de prueba, conjunto de condiciones sobre las etnradas y resultados esperados diseñado para verificar si una parte del software funciona correctamente. Define que se probara y que se espera para determinalo un exito.
	- Test suite: Conjunto de casos de prueba.

### Limitaciones del testing
Al no ser exhaustivo, el testing no puede probar/demostrar que el software funcione correctamente. *El testing puede demostrar la presencia de errores, nunca su ausencia. (Dijkstra)*.
- Necesitamos encontrar el conjunto de tests adecuado:
	- Suficientemente grande para abarcar el dominio y maximizar la probabilidad de encontrar errores.
	- Suficientement epequeño para poder ejecutarlo con cada elemento del conjunto y minimizar el costo de testing.

#### Casos de test a elegir
No hay un algoritmo que proponga casos tales que encuentren todos los errores en cualquier programa, ninguna tecnica puede ser efectiva para detectar todos los errores en un programa arbitrario. Por ello, tenemos dos tipos de criterois para elegir datos de test:
- Test de Caja Negra: Los casos de test se generan analizando la especificacion sin considerar la implementacion.
- Test de caja blanca: Los casos de test se generan analizando la implementacion para determinar los casos de test.

## Automatizacion del testing
El diseño de casos de test no solo permite organizar u optimizar el trabajo de la persona que ejecutara los casos buscando fallas, hay herramientas que permiten programar estos casos de pruebas. Como vimos, el nivel mas basico del testing es el unitario, la ran mayoria de lenguajes de programacion tienen herramientas que permiten programar casos de prueba, en Haskell tenemos HUnit.

## Metodo de Particion de Categorias
Consiste en una tecnica que permite generar casos de prueba de una manera metodica, es aplicable a espceificaciones formales, semiforamales e inclusive informales.
Consiste en los sguientes pasos:
1. Listar todos los problemas que queremos testear.
	1. Enumeramos todas las operaciones, funciones, funcionalidades o probleams que se probaran.
2. Elegir una unidad funcional
	1. Lo ideal es llegar a testear todas las unidades funcionales, un buen criterio es empezar por aquellas que son utilizadas por otras.
3. Identificar factores
	1. Esto pueden ser los parametros del problema a testear, si el sistema es mas complejo podrian ser otros factores.
4. Determinar categorias
	1. Las categorias seran distintas caracteristicas de cada factor, o caracteristicas que relacionan diferentes factores, que tienen influencia en los resultados. Son el resultado dle analisis de toda la info disponible sobre la funcionalidad a testear.
5. Determinar elecciones
	1. Se trata de buscar los conjuntos de valores donde se espera un comportamiento similar, se basa en especificaciones, experiencia y conocimiento de errores.
6. Clasificar las elecciones
	1. Se trata de identificar algunas propiedades o restricciones de las elecciones en el marco de la unidad funcional. Las clasificaciones mas comunes son 
		1. **Error**  (Aquellas elecciones que por si mismas determinan que resultado de la ejecucion el sistema debe detectar un error o que no esta definido su comportamiento), 
		2. **Unico** (nos libra de realizar todas las combinaciones con esta eleccion) o 
		3. **Restriccion** (una condicion que se debe cumplir para combinar con esta eleccion)
7. Armar los casos de test
	1. Por cada caso, debemos describir su resultado esperado, es importante indicar si el resultado sera un posible resultado correcto u esperable o un error o comportamiento indefinido. 
	2. Los casos de prueba definidos seran una herramienta para que eventualmente otra persona pueda ejecutar los test, eligiendo datos concretos y comparando el resultado obtenido con el esperado.
	
# Jugador automático de NIM

**Enunciado**: Construcción de un Jugador Automático para el Juego Nim usando Árboles y el Algoritmo Minimax

**Descripción del Juego Nim**:

El juego Nim es un juego matemático estratégico en el que dos jugadores se turnan para retirar al menos un objeto de una o más pilas. El jugador que retire el último objeto pierde. Un ejemplo típico de configuración inicial podría tener tres pilas con 3, 4 y 5 objetos cada una. Los jugadores pueden retirar cualquier cantidad de objetos de una sola pila en su turno.

**Objetivo**:
Desarrollar un programa que implemente un jugador automático que use el algoritmo Minimax para tomar decisiones óptimas en el juego Nim. Este jugador automático se enfrentará a un jugador humano y tratará de ganarle utilizando la estrategia más eficiente posible.

**Detalles de la Implementación**:

* Entrada: Solicitar al jugador humano el número de pilas iniciales y la cantidad de objetos en cada pila.
* Implementar una interfaz de consola básica que permita al jugador humano realizar movimientos (seleccionar una pila y el número de objetos a retirar).
* Estrategia Automática con Minimax: Construir un árbol de juego donde cada nodo represente el estado de las pilas tras un movimiento.
* Utilizar el algoritmo Minimax para analizar todos los movimientos posibles y elegir el mejor movimiento que maximice las posibilidades de ganar.
* Implementar una evaluación heurística que identifique posiciones ganadoras y perdedoras.
* Jugabilidad:
  * Alternar entre el jugador humano y el jugador automático en cada turno.
  * Mostrar el estado actual de las pilas después de cada movimiento.
  * Indicar el ganador al final del juego.


## Evaluación y entrega
* Implementación: 40% (depende de la sustentación como se explicó al inicio del semestre)
* Sustentación: 60%
  * La sustentación es completamente práctica e individual. 
  * Incluye la adición, modificación o eliminación de alguna funcionalidad.
* Se pueden hacer solos o en parejas
* Fecha de entrega propuesta: 23 y 24 de mayo
* Si hace la opción II, no tendrá que hacer parcial. La nota que saque en la práctica se le asignará al parcial.

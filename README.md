# Mascota Virtual

Proyecto desarrollado para la asignatura **Tópicos C**.

## Integrantes

* **Guillermo Vargas**

* **Alejandro Carrasco**

## Descripción y Alcance

El objetivo general del proyecto es desarrollar una aplicación interactiva de mantenimiento de una mascota virtual (estilo Tamagotchi) que combine una interfaz web fluida con una arquitectura orientada a objetos en Python para la gestión del estado, economía y lógica del juego.

### Objetivos Principales:

1. **Gestión de Necesidades:** Monitorear e interactuar con la mascota para satisfacer sus necesidades básicas (Alimentación, Diversión y Presencia).

2. **Sistema de Economía:** Implementar un flujo económico donde cuidar a la mascota requiere recursos (monedas) que el jugador puede ganar realizando actividades o minijuegos.

3. **Persistencia y Simulación de Tiempo:** Calcular el impacto de la ausencia del usuario según el tiempo transcurrido entre sesiones.

4. **Arquitectura Escalable:** Separar la interfaz de usuario (Frontend) de la lógica de negocio (Backend) para una eventual integración vía API.

## Avance Actual (Fase 1 - Prototipo Funcional)

Actualmente el proyecto cuenta con dos componentes principales estructurados:

### 1. Frontend e Interfaz Web (`index.html`)

* **Gráficos vectoriales (SVG):** Mascota animada con expresiones faciales dinámicas (feliz, normal, triste, abandonada) y seguimiento de pupilas al movimiento del cursor.

* **Mecánica de Economía e Interacción:**

  * Indicadores visuales en tiempo real de Alimentación, Diversión, Presencia y saldo de Monedas (`🪙`).

  * Botones de acción con costos asociados (`Alimentar`, `Jugar`, `Acompañar`).

  * Botón provisional para generación de monedas (`Trabajar`).

* **Lógica del Cliente (JavaScript):**

  * Cálculo de decaimiento temporal de las barras mientras la página está abierta y al retomar sesión.

  * Persistencia local ligera mediante `localStorage`.

### 2. Modelo de Dominio (`mascota.py`)

* **Programación Orientada a Objetos (POO):**

  * Clase `Estado`: Controla los niveles de necesidades con validaciones de límites ($0 - 100$).

  * Clase `Mascota`: Define la entidad principal, calculando el estado de ánimo, descontando recursos según acciones y registrando un historial de interacciones con marca de tiempo.

##  Próximos Pasos (Fase 2)

1. **Conexión Frontend-Backend:** Crear un servidor de API RESTful (utilizando *FastAPI* o *Flask*) para conectar `index.html` con `mascota.py`.

2. **Minijuegos:** Reemplazar la ganancia directa de dinero por minijuegos interactivos en HTML5 Canvas.

3. **Tienda e Inventario:** Implementar la compra y uso de ítems específicos (alimentos premium, juguetes) almacenados en un inventario.
"""

Activa la fase final del juego.

[cite: 57]

"""
"""

--- VARIABLES GLOBALES (Abasto de variables) ---

"""
# Funcionalidad Extra: Dibuja un mini-indicador de progreso en pantalla.
def dibujarInterfazTecnica():
    global i
    # Dibuja un fondo para el mini-mapa/inventario en la esquina
    screen.fill_rect(2, 2, 22, 8, 15)
    while i <= len(inventario) - 1:
        # Dibuja un punto verde por cada objeto en el inventario
        screen.set_pixel(4 + i * 6, 5, 7)
        i += 1
# Lógica técnica para procesar el daño de los enemigos.
# [cite: 39]
def procesarDano():
    miJugador: Sprite = None
    info.change_life_by(-1)
    scene.camera_shake(4, 500)
    miJugador.say("¡ERROR!", 500)
    # Pequeño retroceso para evitar perder vidas seguidas
    miJugador.x += 10
# Gestiona la recolección de objetos de forma modular.
# @param objeto Nombre del ítem recogido
# [cite: 39, 59]
def gestionarInventario(objeto: str):
    inventario.append(objeto)
    music.ba_ding.play()
    game.splash("Recuperado: " + objeto)
    # Verifica si se ha alcanzado el objetivo para el final del juego [cite: 57]
    if len(inventario) >= paquetesNecesarios:
        desbloquearFinal()
# Inicializa los valores técnicos del sistema.
# [cite: 39, 59]
def inicializarSistema():
    global inventario
    inventario = []
    info.set_score(0)
    info.set_life(3)
# Aquí Persona B debería cambiar el mapa o abrir una puerta
def desbloquearFinal():
    game.show_long_text("SISTEMA REPARADO. Busca la salida.", DialogLayout.BOTTOM)
inventario: List[str] = []
i = 0
paquetesNecesarios = 0
# Estructura de datos compleja: Vector/Lista
paquetesNecesarios = 3
# Evento que se ejecuta constantemente para actualizar la GUI técnica [cite: 58]

def on_on_update():
    dibujarInterfazTecnica()
game.on_update(on_on_update)



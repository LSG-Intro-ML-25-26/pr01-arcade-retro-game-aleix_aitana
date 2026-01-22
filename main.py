# --- VARIABLES GLOBALES ---
mi_jugador: Sprite = None
def inicializar_juego():
    global mi_jugador
    """
    Configura el mapa y coloca al robot en la zona azul.
    """
    # 1. CARGAR EL MAPA
    # Función corregida para Python
    tiles.set_current_tilemap(tilemap("""
        level
        """))
    # 2. POSICIONAMIENTO EN ZONA AZUL
    mi_jugador = sprites.create(assets.image("""
        robot_front
        """), SpriteKind.player)
    # Coordenadas ajustadas al círculo azul de tu imagen:
    # Columna 22, Fila 13 (Esquina inferior de la sala derecha)
    tiles.place_on_tile(mi_jugador, tiles.get_tile_location(34, 16))
    # Configurar movimiento y cámara
    controller.move_sprite(mi_jugador)
    scene.camera_follow_sprite(mi_jugador)
    info.set_life(3)
    # 3. GENERAR ENEMIGOS (Lejos de la zona azul)
    spawn_bugs(5)
def spawn_bugs(cantidad: number):
    """
    Crea enemigos en las salas de la izquierda para dar tiempo al jugador.
    """
    for i in range(cantidad):
        bug = sprites.create(assets.image("""
            bug_down
            """), SpriteKind.enemy)
        # Generar aleatoriamente en columnas 1 a 18 (lado izquierdo/centro)
        col_azar = randint(1, 18)
        fil_azar = randint(1, 14)
        tiles.place_on_tile(bug, tiles.get_tile_location(col_azar, fil_azar))
        # Función de seguimiento corregida
        bug.follow(mi_jugador, 30)
def gestionar_animaciones():
    """
    Actualiza las imágenes del robot y enemigos según su dirección.
    """
    # --- Animación Robot ---
    if mi_jugador.vx > 0:
        mi_jugador.set_image(assets.image("""
            robot_right
            """))
    elif mi_jugador.vx < 0:
        mi_jugador.set_image(assets.image("""
            robot_left
            """))
    elif mi_jugador.vy < 0:
        mi_jugador.set_image(assets.image("""
            robot_up
            """))
    elif mi_jugador.vy > 0:
        mi_jugador.set_image(assets.image("""
            robot_front
            """))
    # --- Animación Enemigos ---
    # Corrección de sintaxis 'in' y 'all_of_kind'
    for bug2 in sprites.all_of_kind(SpriteKind.enemy):
        if bug2.vx > 0:
            bug2.set_image(assets.image("""
                bug_right
                """))
        elif bug2.vx < 0:
            bug2.set_image(assets.image("""
                bug_left
                """))
        elif bug2.vy < 0:
            bug2.set_image(assets.image("""
                bug_up
                """))
        elif bug2.vy > 0:
            bug2.set_image(assets.image("""
                bug_down
                """))
def bloquear_enemigos_puentes():
    """
    Opcional: Impide que los enemigos crucen a tu sala.
    """
    for bug3 in sprites.all_of_kind(SpriteKind.enemy):
        c = Math.idiv(bug3.x, 16)
        # Si intentan cruzar el puente de la columna 19 (entrada a tu sala)
        if c == 19:
            bug3.vx = 0
            bug3.x -= 2
# --- BUCLE PRINCIPAL ---

def on_update():
    gestionar_animaciones()
    bloquear_enemigos_puentes()
game.on_update(on_update)

# Iniciar
inicializar_juego()
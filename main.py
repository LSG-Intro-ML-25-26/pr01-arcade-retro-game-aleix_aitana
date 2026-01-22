# --- VARIABLES GLOBALES ---
mi_jugador: Sprite = None

def inicializar_juego():
    """Configura el mapa, el jugador y los enemigos iniciales."""
    global mi_jugador
    
    # 1. Cargar el mapa (Corregido: tiles.set_current_tilemap)
    tiles.set_current_tilemap(tilemap("""level"""))
    
    # 2. Crear jugador y situarlo en la HABITACIÓN DERECHA
    # Usamos coordenadas de la zona derecha del mapa
    mi_jugador = sprites.create(assets.image("""robot_front"""), SpriteKind.player)
    tiles.place_on_tile(mi_jugador, tiles.get_tile_location(22, 8))
    
    controller.move_sprite(mi_jugador)
    scene.camera_follow_sprite(mi_jugador)
    
    info.set_life(3)
    
    # 3. Crear enemigos aleatorios (en las salas de la izquierda/centro)
    crear_bugs_iniciales(5)

def crear_bugs_iniciales(cantidad: number):
    """Reparte enemigos aleatoriamente fuera de la zona del jugador."""
    for i in range(cantidad):
        bug = sprites.create(assets.image("""bug_down"""), SpriteKind.enemy)
        
        # Spawn solo en la parte izquierda y central (columnas 1 a 18)
        col_azar = randint(1, 18)
        fil_azar = randint(1, 14)
        tiles.place_on_tile(bug, tiles.get_tile_location(col_azar, fil_azar))
        
        # Hacer que sigan al jugador (Corregido: bug.follow)
        bug.follow(mi_jugador, 30)

def actualizar_animaciones():
    """Cambia el estilo visual según la dirección del movimiento."""
    # Animación del Robot
    if mi_jugador.vx > 0: mi_jugador.set_image(assets.image("""robot_right"""))
    elif mi_jugador.vx < 0: mi_jugador.set_image(assets.image("""robot_left"""))
    elif mi_jugador.vy < 0: mi_jugador.set_image(assets.image("""robot_up"""))
    elif mi_jugador.vy > 0: mi_jugador.set_image(assets.image("""robot_front"""))

    # Animación de los Bugs (Corregido: sprites.all_of_kind)
    for bug in sprites.all_of_kind(SpriteKind.enemy):
        if bug.vx > 0: bug.set_image(assets.image("""bug_right"""))
        elif bug.vx < 0: bug.set_image(assets.image("""bug_left"""))
        elif bug.vy < 0: bug.set_image(assets.image("""bug_up"""))
        elif bug.vy > 0: bug.set_image(assets.image("""bug_down"""))

def restringir_enemigos():
    """Impide que los enemigos crucen hacia las escaleras o pasillos estrechos."""
    for enemigo in sprites.all_of_kind(SpriteKind.enemy):
        # Localizamos la columna actual del enemigo en el mapa
        col_enemigo = enemigo.x // 16
        
        # Lógica: Si el enemigo intenta entrar en la zona de escaleras (Cols 19-20)
        # que conectan con la habitación derecha, lo frenamos.
        if col_enemigo >= 19 and col_enemigo <= 20:
            enemigo.vx = 0
            enemigo.vy = 0
            # Lo empujamos un poco atrás para que no se quede pegado
            enemigo.x -= 2

# --- BUCLE PRINCIPAL ---
def on_update():
    actualizar_animaciones()
    restringir_enemigos()

game.on_update(on_update)

# Ejecutar inicio
inicializar_juego()
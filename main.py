"""
--- VARIABLES GLOBALES ---
"""
mi_jugador: Sprite = None
menu: miniMenu.MenuSprite = None

def inicializar_juego():
    global mi_jugador
    # Configura el mapa y coloca al robot en la zona azul.
    # 1. CARGAR EL MAPA
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
    
    # NUEVO: Ponemos el contador a 0
    info.set_score(0)
    
    # 3. GENERAR ENEMIGOS (Lejos de la zona azul)
    spawn_bugs(5)
    
    # NUEVO: Llamamos a la función que crea las piezas
    repartir_piezas()

# NUEVO: FUNCIÓN PARA REPARTIR LAS PIEZAS
def repartir_piezas():
    # --- PIEZA 1 ---
    piece1 = sprites.create(assets.image("""piece1"""), SpriteKind.food)
    tiles.place_on_tile(piece1, tiles.get_tile_location(16,2))

    # --- PIEZA 2 ---
    piece2 = sprites.create(assets.image("""piece2"""), SpriteKind.food)
    # EDITA AQUÍ LAS COORDENADAS DE LA PIEZA 2 (Columna, Fila)
    tiles.place_on_tile(piece2, tiles.get_tile_location(27, 17))

    # --- PIEZA 3 ---
    piece3 = sprites.create(assets.image("""piece3"""), SpriteKind.food)
    # EDITA AQUÍ LAS COORDENADAS DE LA PIEZA 3 (Columna, Fila)
    tiles.place_on_tile(piece3, tiles.get_tile_location(2, 2))

# NUEVO: LÓGICA AL RECOGER LAS PIEZAS
def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.confetti, 500)
    info.change_score_by(1)
    music.ba_ding.play()
    
    if info.score() == 3:
        game.show_long_text("¡NÚCLEO ACCESIBLE! Has salvado el servidor NEXUS-CORE.", DialogLayout.BOTTOM)
        game.game_over(True)

sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def narrar_historia():
    # Muestra cuadros de texto explicando el Lore del juego.
    game.show_long_text("Año 2149." + "Los servidores corporativos se han convertido en mundos digitales conscientes",
        DialogLayout.BOTTOM)
    game.show_long_text("El servidor NEXUS-CORE ha sido infectado." + "Un virus ha tomado el control del sistema.",
        DialogLayout.BOTTOM)
    game.show_long_text("Protocolo activado: 404." + "Reinicio total inminente.",
        DialogLayout.BOTTOM)
    game.show_long_text("Antes del borrado final, se libera una última defensa.",
        DialogLayout.BOTTOM)
    game.show_long_text("Tú eres un Data Sweeper." + "Un robot diseñado para limpiar datos corruptos.",
        DialogLayout.BOTTOM)
    game.show_long_text("El servidor es ahora un laberinto inestable." + "Los Bugs patrullan cada sector.",
        DialogLayout.BOTTOM)
    game.show_long_text("Tu misión:" + "Recuperar 3 Paquetes de Datos Vitales.",
        DialogLayout.BOTTOM)
    game.show_long_text("Cada paquete es clave para detener el reinicio.",
        DialogLayout.BOTTOM)
    game.show_long_text("El virus tiene un núcleo." + "Su nombre es Root-Overwrite.",
        DialogLayout.BOTTOM)
    game.show_long_text("Cuando recuperes los 3 paquetes, el acceso al núcleo se abrirá.",
        DialogLayout.BOTTOM)
    game.show_long_text("Derrota a Root-Overwrite." + "Restaura el sistema.",
        DialogLayout.BOTTOM)
    game.show_long_text("El tiempo corre." + "Inicia la limpieza.",
        DialogLayout.BOTTOM)

def mostrar_menu_inicio():
    global menu
    # 1. Configuramos el fondo
    scene.set_background_image(img("""
        8888888888888888888888888888aaaaaaaaaaa88888888888888888888888888888888888888aaaaaaaaaaa88888888888888888888888888888888888cc8fff8f8fff8c88f8c8f8f8ffffffffffff
        88888888888888888888888888aaaaaaaaaaaa88888888888888888888888888888888888888888aaaaaaaaaa888888888888888888888888888888888fffffffffffffffffffffffffffffffffffff
        88888888a88888888888aaaaaaaaaaaaaaaaa888888888888888888888888888888888888888888aaaaaaaaaaa88888888888888888888aaaaaaaaaaaffffffffffffffffffffffffffffffffffffff
        88888aaaaaaaaaaa88aaaaaaaaaaaaaaaaa88888888888888888888888888888888888888888888aaaaaaaaaaa888888aaaaa88a88888aaaaaaaaaaaaffffffffffffffffffffffffffffffffffffff
        8888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa888888888888888888888888888888888888888888888888aaa8aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8ffffffc88aaaaaaaaafffffffffff
        88aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8aaaaa888888888888888888888888888888888888888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffaaaaaaaaaaafffffffffff
        aaaaaaaaaaaaaaaaaaaaaaaaaaaa8888888aaaaaa88aa88888888888888888888888aaaaaaaaa8aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafcccccfaaaaaaaaaafffffffffff
        aaaaaaaaaaaaaaaaaaaa8aaa888888888aaaaaaaaaa8888888888888a8888a88aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa88faaaaafaaaaaaaaafffffffffff
        aaaaaaaaaaaaaaaaaaaa8a888888888aaaaaaaaaaaa888888888aaaaaa8aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa88accccccaaaaaaaaafffffffffff
        888aaaa88aaaaaaaaa8888888888888aa8aaaaaaaa8a888888a88aaa888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa888ffffffcaaaaaaafffffffffff
        888888888888888888888888888888888aa8aaaaaaaa8888888888888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8aafffffffaaaaaaafffffffffff
        8888888888888888888888888888888888aa8aaaaaa888aa88888888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacffffffaaaaaafffffffffff
        888888888888888888888888888888888888aaaaaa8888888888888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8af8ffffff88c888ff88fffffffffffffffffff
        88888888888888888888888888888888888888888888888888888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa88af8ffccff88fff8fff8ff8ffffffffffffffff
        88888888888888888888888888888888888888888888888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa88f8888cff888888fff88f8f8f8ffffffffffff
        88888888888888888888888888888888888888888888888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa888aaaaaaaaaaaaaa88888f8888fff88888888fffffff88ffffffffffff
        888888888888888888888888888888888888888aaa8888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa88888aaaaa888aaaaa888888fffffffffffffffffffffffffffffffffffff
        88888888888888888888888888888888888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa888888888888888888888888888888f888f8f8f8f8f8c888ffffff8ffffffffffff
        8888888888888888888888888888888888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa88888888888888888888888888888888ff88c8f8f8f8f8cffffc8f8f8ffffffffffff
        888888888888888888888888888888888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa88888aaaa88aaa88888888888888888ffffffffffffffffffffffffffffffffffffff
        888888888a888888888888888888888888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8aaaaaa8888888888888888888888ffffffffffffffffffffffffffffffffffffff
        88888888aa888888888888888888aa88aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa888888888888888888888888888888fffffffffffffffffffffffffffffffffffff
        8888888aaa8888888888888888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8888888888888888888888888888888888888f88888f8888888888fffffffffff
        88888888aa88888888888ac8aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa88888888888888888888888888888888888888888f88888f888888888fffffffffff
        88888888c88888aaaaaacccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa888888888888888888888888888888888888888888ffffff888888888fffffffffff
        88888888f8888aaaaaaaaacaaaaaaaaaacaaaaaaaaaaaaaaaaaaaaa88aaaaaaaaaa8888888aaaaaaaaaaaaaaaa88888888888888888888888888888888888888888888ffffff88888a8afffffffffff
        88888888ff88aaaaaaaaaacaaaaacaaaaffaaaaaaaaaaaaaaaaaaaa88888aa8888888888888888aaaaaaaaaaaaa8888888888888888888888888888888888888888888fffffffaaaaa88fffffffffff
        8888cffffffffffaaaaaaacaaaaafaaaaffaaaaaaaaaaaaaaaaaaa888888888888888888888888888888aaaa888888888888888888888888888888888888a8888888888f88888faa8888fffffffffff
        88888fffffffffcaaaaaaffacccffaaaaffaaaaaaaaa888aaaaa888888888888888888888888888888888888888888888888888888888888888888888888aa8888888888f88888c88888fffffffffff
        fff8ffffffffefcaffffcffffffffaccffffffccaaa88aa88aaa88a888888888888888888888888888888888888888888aaa888888888888888888888888aa88888888888fcccccf8aaafffffffffff
        fffffffffffffffffffffffffffffffffffffffffffc88888aaaa88888888888888888888888888888888888888888888aaaa88888888888888888888888aa88888888888cffffffaaaffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffc8888888888888888888888888888888888888aaaaa888888888888888888888888888888888888ffaaaa8888888fffffffaaffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffc888888888888888888888888888888888888aaaaaaaa88888888888888888888a88888888888888ffff88aa88888fffffffaffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffc888888888888888888888aaa888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8aaaaaaa888888aaaaffffffffffffffffffffffffffffffffffff
        ffffffffffffcccccccccccccccccbddbcccccccccccccc888888888888aaa888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacacafffafafacaccacacafaffffffffffff
        ffffffffffffccccccccccccccaddddddddaccccccccccc888aaa8aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacacafcfafafacaccafccafaffffffffffff
        ffffffffffffccccccccccccddddaccccaddddcccccccccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacffcfcfcfafacaccacfffffffffffffffff
        ffffffffffffccccccccccccdddbbcb3cbbbddcccccccccaaaaaaaaaaaaaaaaaaaaaaaaaa8aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffffffffffffffffffffffffffffffffff
        ffffffffcfffccccccccccccdddada3dababddcccccccccaaaaaaaaaaaaaaaaaaaaaaaaaa8aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccffffffffffffffffffffffffffffffffffffff
        ffffffffffffccccccccccccdddccdcc3ccbddccccccccaa2aaaaaaaaaaaaaaaaaaaaa8888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacaaacccffaaaacccfffffffffff
        ffffffffffffccccccccccccddddbcbbab3dddcccccccccccccaaaaaaaccaaaaaaaaaa8888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafccfffffcccaacffffffffffff
        ffffffffffffccccccccccccccbddddddddbccccccccccccccaacccccccc8ccaaaaaaa8888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacacccccccaaacaccffffffffcccaaaffffffffffff
        ffffffffffffcccccccccccccccccbddbccccccccccccccccccaccccccccacaaaaaaaa8888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacaccaaccaaaaeccccfffffffccffffffffffffffff
        ffffffffffffffffffffffcffcccfcccccccffffffffffccccacccccccccaccaaaaaaa8888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccfffccffffffffccaccffffffffffffffffffffff
        ffffffffffffffffffffcd3bf3cdfbb3ccdcccbbbffffffcccaacaceacaaaaaaaaaaaa8888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffccffccfcccfffcffcfffffffacfccaaecca2aa8aaaaaaaaa8868aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8f2eee2fcffcfcccccccccfffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffccc68c886aaabaaaaaaaaaa8868aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8f2eeeefffccfcfffcccbcccfffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffcccc88668889aaa9aaaaaaaa8868aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8f22fe2fffccfccccbcffbfffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffccaca68ca6caabbaaaaaaaaa8868aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8ffffffccfcffccfcccccccccffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffcacccc6c8668cbbaaabaaaaaaa8868aaaaaa888888888888888888888aaaaaaaaaaaafccfcfccc8cfcccccccccccccfffffffffffffffffffff
        fffffffffffffffcffffcffffcfffccffcffccfcfccccacccc8668889aaa9aaaaaaaaaa868aaaa8f8fffffffffffffffffff6aaaaaaaaaaabcccfccccfccccccbcccccccccfffffffffffffffffffff
        cccccccccccccccccccccccccccccc666666666666666cccc86aca68cabbaaaaaaaaaaa668a88cff8fcfccacffffffcccccc6aaaaaaaaabbbccccccccfccfcfffffcfffffcfffffffffffffffffffff
        88888888888666666666666666666666666666666666666cc8c866cc6bccccaaacaaaa86668fffff8fccfffffffffffccaac6aaaaaaaaabbbaccccccccccfcfcfcfcfefcfcfffffffffffffffffffff
        88888888886666666666666666666666699999999999999cccccc886ccffffccccccca86668f8fff8ffcaaaaaccfffcfccac6aaaaaaaa33bbaaacccccccccccafcfbfcfcccfffffffffffffffffffff
        8888f888888686668666c66666666666666969966999699ccccca68ccbcffcccccccca66668fffff8fcfcfcccffcfcfccaac6aaaaaaadddb33baaacccc8ffffffffffcfffcfffffffffffffffffffff
        88888888888686666686866666666666668669966999699cccaa8cc8bcccfccaaaccc866668fafcf8fcccccccccccccaaaac6aaaaaabddbaa23baaacaffffffffffffffffffffffffffffffffffffff
        88888888888886668888866688888666888899966688899cffff8668fcccfccccfccc866668fffff8cccccfcfcccccccaccc6aaaaabbbbaaaaa2aaaeaffffffffffffffffffffffffffffffffffffff
        88888888888866666666666666666666666666666666666acfcc6caabcccfccb888aca66668fffff8fcccccccccccccacccc6ccccdddbaccccab3baaaeaaeceecfffffffccfffffffffffffffffffff
        8888cccccccc8888888888866666666666666666666666cccccccfcaccccfcc888cbc866688faccc8ccccccccccccaaacccc6cccbbdbcacccaaa23aaaeaaecaaaafcccfcfcfffffffffffffffffffff
        fffffffffffffffcffffcffffcfffccffcffccfcfccccccccccccccacbcccccc8888c888888ccf8c8cccccccccccaccccccc6aaebaaaaaaaaaaaaaaaacaceaffffffffffcffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffccccccccccc8caccfccaaaa8c888888fffff8fcccccccccaaccccccc6aacccccccccccaacaaaaeaaecffffffffffcffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffccccccccaaaa8cc88888ffffc8ccccaaccccccccccccc6aaaccccccfffccccaceeeaaeafffffffffffffffffffffffffffffffff
        ffffffffffffffffffffcfffffffffffffffffffffafffffcfcfcfccccaaccccaaacc888868ccfcc8cccccccccccccccccac6ccccacfccffffaffaaaaeaacafffffffffffffffffffffffffffffffff
        fffcfffffffffffffffffffcffffcffffffffffffffffffffffffffcccccccaaaaa8c888888fcccc8cccccccccccccccaacc6ccccccffcfcffaffaaccecaccfffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffccffffacfffffffffffffffffffffffffcccaacccaaaacaaaaaaaccccc8cccaacccccccccfcccc8cccacfffcffffaffaccacacecfefefffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffcccaccccaaaac66688ccc8ccc8ccacacacfccccfffccaacccacfffccfffaffacaceccecffffffffffcffffffffffffffffffffff
        ffffffffffffffffffcffffffffffffffffffffffffffcccccfffffcccccccaaaaff668888888ccc8cccffffccfffcffcccacfccacfffcffffaffacacecceafffffffffffffffffffffffffffffffff
        ffffffffffffffffffcffffffaaffffffffffffffffffcffccffffccccccccccccccccccccccccccccffffffffc666ccffffffffacfffcffffaffacaaaaacafffffffffffffffffffffffffffffffff
        fffffffffffffcfffccffffffccffffffffffff6fffffccfcfffffffacaafffffffffffffffffffffffffffff68cc886cfffffffacfccafcffaffacaccffecffffffeffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffff8fffffffffffccfffcccafcccfcccffcfcffcfcfcccffffffc6896966cffffffffffffffffffffacaccfffffffffffffffffffffffffffffffffffff
        f8fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcff6c8fcffcfcfff6ffffffc66c8c66cfffffffffffffffffcffacaccfffcffffffffffcffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc666c6fcff8c888c6fffffffc8888ccffffffffffcffcfff66ffacaccffecfcfcfcfffccffffffffffffffffffffff
        fffffffffffffffffffffffffffffcffffffffffffffffffffffffffffffffffffcc6c8f8ff8f8ccc8fcccccccccccccccccccfffffffcfcfffffacaccfffffffffffffffffffffffffffffffffffff
        ffffffffffccfffffffffffffafffaffffffffffffcfffffffffffffffffcffffffccc8fcffcf8cffcfffffcfffffffffffffffffffffcccccccfacacffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffcffffffffffcfffffffffffffffffcccccfffffffffffccffffccfcccccfcfffffcfffffffffffffffffccfffffffffffcffffffffffffffffffffffffffffffffffffffff
        fffff8fffffffffffffffcffffffffffcfffffffffffffffffffffffffffffffffaaffff8fc8cfccccfcccccccccccccccccccffffffffffffffcfcffffffffcfcfffffffcfffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8fc8ccccccfffccffffffffcffffffffffffffccffffcfcfffffcfccfcfffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccffffcfccccccccfffffffffffffffffffffff8fffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffaffffffffffffffffffffffffffffffffffffcfffccfffcccc8ccccccfcccccccccccccccccccffffffffcccfcfcffffffffffcfcfffccfcffffffffffffffffffffff
        fffffff8fffffffffffffffffaffffffffffffffffffffffffffffffffffffffffccccccccccccccccfffffffffffffffffffffffffffffffffffffffffffffffffffee22efffffffffffffffffffff
        fffffffffffffffffffffffffffffffccfffffffffffffffffffffffffffffffffccfcccccccccccccfffcfffffffbfff6fffffffffffffffffffffffffffffffffffdebbbfffffffffffffffffffff
        fffffffffffffffffffffffffccfffffffffffffffffffffffffffffffffccffffcccccccccccccccafffffffffffffffffffffffffffffffffffffffffffffffffffb2ffffffffffffffffffffffff
        fffffffffffffffffffffffffaaffffffffffffffffffffffffffffff888888fccccccccccccffcfffffcccccccfccccccccccfffffffffffffffffffffffffffffffe22fffffffffffffffffffffff
        fffffffffffffffffffffffc666666666666666666666666fffffffff88ff888ccacccccccccffffffffffccffffccccfccfffffff8ffffffffffffffffffffffffff2eecffffffffffffffffffffff
        fffffffffffffffffffffffc61fccccaab1d11baaccc1cf6ffffffffffffffffffccccccccccffffffffccfcfffffffffffffffffffffaccffffffffffffffaccffffefc66fffffffffffffffffffff
        ffffffffffffffffffffffff6fccccbadda3a3abaaccccb6fffff88fff8fff88fffffccccccccff9ccc9ccbbcc9c6c6acccffffffffffffffffffffffffffffffffff2fffffffffffffffffffffffff
        ffffffffffffffffffffffff6fafacacdd3adddbeacacbb6fffffffffffffffffffffffffffffff999f97666699f967ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffc6dccccccad11adaaacccdcf6fffff88fffffffffff68fffffffffffffffffffffffffffffffccffffffffcffffffffcfffcffffffffffee2fffffffffffffffffffffff
        fffffffffffffffffffffffc66666666666666666666666cffffffffffffffffffffffcffcfffccc6ffcf6cfffccfc6c6fffccffffcfffcccfffffcfcffffffffffffeeefffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff8fffffffffff6cff6cfffffffffff66ffcf66fffffffffffffbcdcfffffffffffffffffffffffffffffffffefffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccfffffffffffccffcccccfffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffccfcfcffcfffffffffffffffffffffffffffffffffffcffcfffffffff6fccfcc66cc6ccffcffcfcccffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffcfccfccfcfffffffffffffffffffffffffffffffffffcfcc6cf66c6fffffffff66cffc6ffcffbffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfcfcffffffffffcfcffcccfcffcffcccffffffcccccccfffffffffffffffffffffffffffeffeefffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffcaaaeffffffffcfffcfffffffffcffccccffcfccfffffcffffccccccccccfcffffcfffffffffffffffffffb2eebfffffffffffffffffffff
        ffffffffffffffffaaaaafeeeeeffffffffffffffffffffabdecffcfffcfffccfcccffffffffffffffffffffffcbccb6fbbffbbfcbcccebfccbccffffffffffffffffffffffffffffffffffffffffff
        ffffffefffffffffeeeeefcffffffffffffffffffffffffaeeecffcfffcfffcfffccfffffffffffffffffffcffffffc6ffbbfeeccccfbeefcbccfffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffaeeeecccfffffffffffffffcfccccfccccffffccffffffffc66666666cccc6666666cfffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffc3aacffaeeeecfffffcffeeffffffffffffcfcbcbffbcbcfbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffeaacffaeeeecfffffffffffffffffffffffffffccfcfcccccccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffabdeecfffffffffffffffffffffffffffcfffffffccffccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffbbbbafffffffffffffaedecffffffffffffffffffffffffffffffffffffffffffffffffffcccfeffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffeaaaafffffffffffffaeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffaeeeeecefffff66ffffffffffff43c66ffffffefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff66ffffffffffffeec66fffffffffffffffffffffffcccfcffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffcfaacfffeefffccfffffffffffffffccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff66ffffffffffffffffffffffffffcaffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffeeffffffffffffffffffffffffffffffffffffffffffffffffff66ffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffeeefffffffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
    # 2. Creamos el menú directamente como una variable local primero
    menu = miniMenu.create_menu(miniMenu.create_menu_item("JUGAR"),
        miniMenu.create_menu_item("LORE"))
    # 3. Estética
    menu.set_frame(assets.image("""
        MenuFrame
        """))
    menu.set_style_property(miniMenu.StyleKind.SELECTED,
        miniMenu.StyleProperty.BACKGROUND,
        8)
    menu.bottom = 110
    menu.left = 50
    # 4. Lógica de selección
    # Usamos una función anónima (lambda)
    
    def on_button_pressed(selection, selectedIndex):
        menu.close()
        if selection == "LORE":
            narrar_historia()
            mostrar_menu_inicio()
        else:
            inicializar_juego()
    menu.on_button_pressed(controller.A, on_button_pressed)
    
def bloquear_enemigos_puentes():
    # Opcional: Impide que los enemigos crucen a tu sala.
    for bug3 in sprites.all_of_kind(SpriteKind.enemy):
        c = Math.idiv(bug3.x, 16)
        # Si intentan cruzar el puente de la columna 19 (entrada a tu sala)
        if c == 19:
            bug3.vx = 0
            bug3.x -= 2

def spawn_bugs(cantidad: number):
    # Crea enemigos en las salas de la izquierda para dar tiempo al jugador.
    for index in range(cantidad):
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
    # Actualiza las imágenes del robot y enemigos según su dirección.
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

# --- INICIO DEL PROGRAMA ---
# En lugar de llamar a inicializar_juego() directo, llamamos al menú
mostrar_menu_inicio()

# --- BUCLE PRINCIPAL ---
def on_on_update():
    if mi_jugador:
        # Solo si el jugador ya fue creado
        gestionar_animaciones()
        bloquear_enemigos_puentes()

game.on_update(on_on_update)
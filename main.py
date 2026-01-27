"""
--- VARIABLES GLOBALES --- 
"""
mi_jugador: Sprite = None
menu: miniMenu.MenuSprite = None
# Variable global para el jefe final
jefe_final: Sprite = None
# Variables para recordar hacia dónde mira el robot y poder disparar en esa dirección
dir_x = 0
dir_y = 100
# Cotadores de piezas
cantidad_p1 = 0
cantidad_p2 = 0
cantidad_p3 = 0
iventario_abierto = False
juego_pausado = False
def inicializar_juego():
    global mi_jugador
    # 1. CARGAR EL MAPA
    tiles.set_current_tilemap(tilemap("""
        level
        """))
    # 2. POSICIONAMIENTO EN ZONA AZUL
    mi_jugador = sprites.create(assets.image("""
        robot_front
        """), SpriteKind.player)
    # Coordenadas personaje:
    tiles.place_on_tile(mi_jugador, tiles.get_tile_location(34, 16))
    # Configurar movimiento y cámara
    controller.move_sprite(mi_jugador)
    scene.camera_follow_sprite(mi_jugador)
    # --- VIDAS Y CRONÓMETRO ---
    info.set_life(3)
    info.start_countdown(180)
    # 180 segundos = 3 minutos
    # Ponemos el contador a 0
    info.set_score(0)
    # 3. GENERAR ENEMIGOS POR HABITACIONES
    spawn_bugs()
    # Llamamos a la función que crea las piezas
    repartir_piezas()
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
        8888888888888888888888888888888888888888aaa8888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa88888aaaaa888aaaaa888888fffffffffffffffffffffffffffffffffffff
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
        fffffffffffffffffffffffffffffffffffffffc88888aaaa88888888888888888888888888888888888888888888aaaa88888888888888888888888aa88888888888cffffffaaaffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffc8888888888888888888888888888888888888aaaaa888888888888888888888888888888888888ffaaaa8888888fffffffaaffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffc888888888888888888888888888888888888aaaaaaaa88888888888888888888a88888888888888ffff88aa88888fffffffaffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffc888888888888888888888aaa888aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8aaaaaaa888888aaaaffffffffffffffffffffffffffffffffffff
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
        fffffffffffffffffffffffffffffffffffffffffffccc68c886aaabaaaaaaaaaa8868aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8f2eeeefffccfcfffcccbcccfffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffcccc88668889aaa9aaaaaaaa8868aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8f22fe2fffccfccccbcffbfffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffccaca68ca6caabbaaaaaaaaa8868aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa8ffffffccfcffccfcccccccccffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffcacccc6c8668cbbaaabaaaaaaa8868aaaaaa888888888888888888888aaaaaaaaaaaafccfcfccc8cfcccccccccccccfffffffffffffffffffff
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
        ffffffffffffffffffffffffffffffffffffffffccccccccccc8caccfccaaaa8c888888fffff8fcccccccccaaccccccc6aacccccccccccaacaaaaeaaecffffffffffcffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffccccccccaaaa8cc88888ffffc8ccccaaccccccccccccc6aaaccccccfffccccaceeeaaeafffffffffffffffffffffffffffffffff
        ffffffffffffffffffffcfffffffffffffffffffffafffffcfcfcfccccaaccccaaacc888868ccfcc8cccccccccccccccccac6ccccacfccffffaffaaaaeaacafffffffffffffffffffffffffffffffff
        fffcfffffffffffffffffffcffffcffffffffffffffffffffffffffcccccccaaaaa8c888888fcccc8cccccccccccccccaacc6ccccccffcfcffaffaaccecaccfffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffccffffacfffffffffffffffffffffffffcccaacccaaaacaaaaaaaccccc8cccaacccccccccfcccc8cccacfffcffffaffaccacacecfefefffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffcccaccccaaaac66688ccc8ccc8ccacacacfccccfffccaacccacfffccfffaffacaceccecffffffffffcffffffffffffffffffffff
        ffffffffffffffffffcffffffffffffffffffffffffffcccccfffffcccccccaaaaff668888888ccc8cccffffccfffcffcccacfccacfffcffffaffacacecceafffffffffffffffffffffffffffffffff
        ffffffffffffffffffcffffffaaffffffffffffffffffcffccffffccccccccccccccccccccccccccccffffffffc666ccffffffffacfffcffffaffacaaaaacafffffffffffffffffffffffffffffffff
        fffffffffffffcfffccffffffccffffffffffff6fffffccfcfffffffacaafffffffffffffffffffffffffffff68cc886cfffffffacfccafcffaffacaccffecffffffeffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffff8fffffffffffccfffcccafcccfcccffcfcffcfcfcccffffffc6896966cffffffffffffffffffffacaccfffffffffffffffffffffffffffffffffffff
        f8fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcff6c8fcffcfcfff6ffffffc66c8c66cfffffffffffffffffcffacaccfffcffffffffffcffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffc666c6fcff8c888c6fffffffc8888ccffffffffffcffcfff66ffacaccffecfcfcfcfffccffffffffffffffffffffff
        fffffffffffffffffffffffffcffffffffffffffffffffffffffffffffffffcc6c8f8ff8f8ccc8fcccccccccccccccccccfffffffcfcfffffacaccfffffffffffffffffffffffffffffffffffff
        ffffffffffccfffffffffffffafffaffffffffffffcfffffffffffffffffcffffffccc8fcffcf8cffcfffffcfffffffffffffffffffffcccccccfacacffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffcffffffffffcfffffffffffffffffcccccfffffffffffccffffccfcccccfcfffffcfffffffffffffffffccfffffffffffcffffffffffffffffffffffffffffffffffffffff
        fffff8fffffffffffffffcffffffffffcfffffffffffffffffffffffffffffffffaaffff8fc8cfccccfcccccccccccccccccccffffffffffffffcfcffffffffcfcfffffffcfffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8fc8ccccccfffccffffffffcffffffffffffffccffffcfcfffffcfccfcfffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccffffcfccccccccfffffffffffffffffffffff8fffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffaffffffffffffffffffffffffffffffffffffcfffccfffcccc8ccccccfcccccccccccccccccccffffffffcccfcfcffffffffffcfcfffccfcffffffffffffffffffffff
        fffffff8fffffffffffffffffaffffffffffffffffffffffffffffffffffffffffccccccccccccccccfffffffffffffffffffffffffffffffffffffffffffffffffffee22efffffffffffffffffffff
        fffffffffffffffffffffffffffccfffffffffffffffffffffffffffffffffccfcccccccccccccfffcfffffffbfff6fffffffffffffffffffffffffffffffffffdebbbfffffffffffffffffffff
        fffffffffffffffffffffffffccfffffffffffffffffffffffffffffffffccffffcccccccccccccccafffffffffffffffffffffffffffffffffffffffffffffffffffb2ffffffffffffffffffffffff
        fffffffffffffffffffffffffaaffffffffffffffffffffffffffffff888888fccccccccccccffcfffffcccccccfccccccccccfffffffffffffffffffffffffffffffe22fffffffffffffffffffffff
        fffffffffffffffffffffffc666666666666666666666666fffffffff88ff888ccacccccccccffffffffffccffffccccfccfffffff8ffffffffffffffffffffffffff2eecffffffffffffffffffffff
        fffffffffffffffffffffffc61fccccaab1d11baaccc1cf6ffffffffffffffffffccccccccccffffffffccfcfffffffffffffffffffffaccffffffffffffffaccffffefc66fffffffffffffffffffff
        ffffffffffffffffffffffff6fccccbadda3a3abaaccccb6fffff88fff8fff88fffffccccccccff9ccc9ccbbcc9c6c6acccffffffffffffffffffffffffffffffffff2fffffffffffffffffffffffff
        ffffffffffffffffffffffff6fafacacdd3adddbeacacbb6fffffffffffffffffffffffffffffff999f97666699f967ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffc6dccccccad11adaaacccdcf6fffff88fffffffffff68fffffffffffffffffffffffffffffffccffffffffcffffffffcfffcffffffffffee2fffffffffffffffffffffff
        fffffffffffffffffffffffc66666666666666666666666cffffffffffffffffffffffcffcfffccc6ffcf6cfffccfc6c6fffccffffcfffcccfffffcfcffffffffffffeeefffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff8fffffffffff6cff6cfffffffffff66ffcf66fffffffffffffbcdcfffffffffffffffffffffffffffffffffefffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccfffffffffffccffcccccfffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffccfcfcffcfffffffffffffffffffffffffffffffffffcffcfffffffff6fccfcc66cc6ccffcffcfcccffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffcfccfccfcfffffffffffffffffffffffffffffffffffcfcc6cf66c6fffffffff66cffc6ffcffbffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffcfcfcffffffffffcfcffcccfcffcffcccffffffcccccccfffffffffffffffffffffffffffeffeefffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffcaaaeffffffffcfffcfffffffffcffccccffcfccfffffcffffccccccccccfcffffcfffffffffffffffffffb2eebfffffffffffffffffffff
        ffffffffffffffffaaaaafeeeeeffffffffffffffffffffabdecffcfffcfffccfcccffffffffffffffffffffffcbccb6fbbffbbfcbcccebfccbccffffffffffffffffffffffffffffffffffffffffff
        ffffffefffffffffeeeeefcffffffffffffffffffffffffaeeecffcfffcfffcfffccfffffffffffffffffffcffffffc6ffbbfeeccccfbeefcbccfffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffaeeeecccfffffffffffffffcfccccfccccffffccffffffffc66666666cccc6666666cfffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffc3aacffaeeeecfffffcffeeffffffffffffcfcbcbffbcbcfbbbbfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffeaacffaeeeecfffffffffffffffffffffffffffccfcfcccccccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffabdeecfffffffffffffffffffffffffffcfffffffccffccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffbbbbafffffffffffffaedecffffffffffffffffffffffffffffffffffffffffffffffffffcccfeffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffeaaaafffffffffffffaeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffaeeeeecefffff66ffffffffffff43c66ffffffefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff66ffffffffffffeec66fffffffffffffffffffffffcccfcffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffeeffffffffffffffffffffffffffffffffffffffffffffffffffffccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffcfaacfffeefffccfffffffffffffffccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff66ffffffffffffffffffffffffffcaffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffeeffffffffffffffffffffffffffffffffffffffffffffff66ffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffeeefffffffffffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
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
    
    def on_button_pressed(selection, selectedIndex):
        menu.close()
        if selection == "LORE":
            narrar_historia()
            mostrar_menu_inicio()
        else:
            inicializar_juego()
    menu.on_button_pressed(controller.A, on_button_pressed)
    
# --- DISPARAR CON EL BOTÓN A ---

def on_a_pressed():
    if mi_jugador:
        # Crea un proyectil de plasma azul cian
        disparo = sprites.create_projectile_from_sprite(img("""
                . . 9 9 . .
                . 9 6 6 9 .
                9 6 1 1 6 9
                9 6 1 1 6 9
                . 9 6 6 9 .
                . . 9 9 . .
                """),
            mi_jugador,
            dir_x,
            dir_y)
        music.pew_pew.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# --- COLISIÓN DEL DISPARO CONTRA LOS ENEMIGOS ---
# Asignamos el evento de choque Proyectil - Enemigo

def on_on_overlap_disparo(sprite, otherSprite):
    # Destruye el disparo al chocar
    sprite.destroy()
    # Busca la barra de vida del enemigo golpeado
    barra_vida = statusbars.get_status_bar_attached_to(StatusBarKind.health, otherSprite)
    if barra_vida:
        barra_vida.value -= 1
        # Efecto de daño
        otherSprite.start_effect(effects.blizzard, 200)
        # Si la vida llega a 0, el enemigo muere
        if barra_vida.value <= 0:
            otherSprite.destroy(effects.disintegrate, 200)
            music.zapped.play()
            # ¡SI EL QUE MUERE ES EL JEFE FINAL, GANAS EL JUEGO!
            if otherSprite == jefe_final:
                game.show_long_text("¡NÚCLEO ELIMINADO! El sistema se ha restablecido.",
                    DialogLayout.BOTTOM)
                tiempo_final = info.countdown()
                info.set_score(tiempo_final)
                game.game_over(True)
sprites.on_overlap(SpriteKind.projectile,
    SpriteKind.enemy,
    on_on_overlap_disparo)

# --- COLISIÓN DEL JUGADOR CONTRA ENEMIGOS (PIERDES VIDA) ---

def on_on_overlap_enemigo(sprite2, otherSprite2):
    # Quitamos una vida
    info.change_life_by(-1)
    if info.life() <= 0:
        info.set_score(0)
    # Efecto de dolor
    music.knock.play()
    scene.camera_shake(4, 500)
    # Pausa de 1 segundo (1000 ms) para dar invulnerabilidad y que no mueras al instante
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap_enemigo)

def repartir_piezas():
    # --- PIEZA 1 ---
    piece1 = sprites.create(assets.image("""
        piece1
        """), SpriteKind.food)
    tiles.place_on_tile(piece1, tiles.get_tile_location(17, 2))
    # --- PIEZA 2 ---
    piece2 = sprites.create(assets.image("""
        piece2
        """), SpriteKind.food)
    tiles.place_on_tile(piece2, tiles.get_tile_location(27, 17))
    # --- PIEZA 3 ---
    piece3 = sprites.create(assets.image("""
        piece3
        """), SpriteKind.food)
    tiles.place_on_tile(piece3, tiles.get_tile_location(2, 2))
def aparecer_jefe():
    global jefe_final
    game.show_long_text("¡PELIGRO! El núcleo Root-Overwrite ha despertado.",
        DialogLayout.BOTTOM)
    # Creamos al jefe final
    jefe_final = sprites.create(assets.image("""
        boss_front
        """), SpriteKind.enemy)
    # COORDENADAS DONDE APARECERA EL JEFE FINAL (Columna, Fila)
    tiles.place_on_tile(jefe_final, tiles.get_tile_location(10, 10))
    # Le ponemos su barra de vida gigante de 15 puntos
    barra_jefe = statusbars.create(40, 6, StatusBarKind.health)
    barra_jefe.attach_to_sprite(jefe_final)
    barra_jefe.max = 15
    barra_jefe.value = 15
    # Hacemos que persiga al jugador (El jefe SÍ te persigue siempre)
    jefe_final.follow(mi_jugador, 40)

def on_on_overlap(sprite3, otherSprite3):
    otherSprite3.destroy(effects.confetti, 500)
    info.change_score_by(1)
    music.ba_ding.play()
    if info.score() == 3:
        aparecer_jefe()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def abrir_iventario():
    global iventario_abierto
    if iventario_abierto:
        return
    iventario_abierto = True
    juego_pausado2 = True
    iv = miniMenu.create_menu(miniMenu.create_menu_item("PIEZA 1 x" + ("" + str(cantidad_p1)),
            assets.image("""
                piece1
                """)),
        miniMenu.create_menu_item("PIEZA 2 x" + ("" + str(cantidad_p2)),
            assets.image("""
                piece2
                """)),
        miniMenu.create_menu_item("PIEZA 3 x" + ("" + str(cantidad_p3)),
            assets.image("""
                piece3
                """)),
        miniMenu.create_menu_item("CERRAR"))
    iv.set_stay_in_screen(True)
    iv.set_frame(assets.image("""
        MenuFrame
        """))
    iv.set_title("INVENTARIO")
    
    def on_button_pressed2(selection2, index):
        global iventario_abierto
        iventario_abierto = False
        iv.close()
    iv.on_button_pressed(controller.A, on_button_pressed2)
    

def on_b_pressed():
    if mi_jugador:
        abrir_iventario()
        juego_pausado3 = False
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def narrar_historia():
    # Muestra cuadros de texto explicando el Lore del juego.
    game.show_long_text("Año 2149." + "Los servidores corporativos se han convertido en mundos digitales conscientes",
        DialogLayout.BOTTOM)
    game.show_long_text("El servidor NEXUS-CORE ha sido infectado." + "Un virus ha tomado el control del sistema.",
        DialogLayout.BOTTOM)
    game.show_long_text("Protocolo activado: 404." + "Reinicio total inminente.",
        DialogLayout.BOTTOM)
    game.show_long_text("Tú eres un Data Sweeper." + "Un robot diseñado para limpiar datos corruptos.",
        DialogLayout.BOTTOM)
    game.show_long_text("Tu misión:" + "Recuperar 3 Paquetes de Datos Vitales.",
        DialogLayout.BOTTOM)
    game.show_long_text("El virus tiene un núcleo." + "Su nombre es Root-Overwrite.",
        DialogLayout.BOTTOM)
    # INSTRUCCIONES DE DISPARO
    game.show_long_text("Llevas equipado un Cañón de Limpieza de Datos. Usa el BOTÓN A para disparar.",
        DialogLayout.BOTTOM)
    game.show_long_text("Los bugs caerán con 2 impactos. El núcleo requerirá 15.",
        DialogLayout.BOTTOM)
    game.show_long_text("El tiempo corre." + "Inicia la limpieza.",
        DialogLayout.BOTTOM)
# --- APARICIÓN DE ENEMIGOS: LISTA DE COORDENADAS ---
def spawn_bugs():
    lista_coordenadas = [[3, 3],
        [9, 3],
        [6, 4],
        [4, 9],
        [8, 8],
        [17, 4],
        [19, 6],
        [18, 7],
        [25, 14],
        [27, 15],
        [28, 16],
        [3, 15],
        [7, 16],
        [17, 14],
        [19, 15],
        [26, 5],
        [26, 4]]
    # Habitación Pieza 3 
    # Habitación Pieza 1
    # Habitación Pieza 2
    # Sala Neutral
    # Sala Neutral
    # Sala Neutral
    # Función auxiliar interna
    def crear_bug(c: number, f: number):
        bug = sprites.create(assets.image("""
            bug_down
            """), SpriteKind.enemy)
        # Colocamos al enemigo en la baldosa exacta
        tiles.place_on_tile(bug, tiles.get_tile_location(c, f))
        # Les ponemos su barra de vida (2 puntos)
        barra = statusbars.create(16, 2, StatusBarKind.health)
        barra.attach_to_sprite(bug)
        barra.max = 2
        barra.value = 2
        # Movimiento inicial aleatorio (para que no parezcan estatuas)
        bug.vx = randint(-25, 25)
        bug.vy = randint(-25, 25)
    # Bucle que lee tu lista y crea los enemigos
    for coordenada in lista_coordenadas:
        # coordenada[0] es la columna, coordenada[1] es la fila
        crear_bug(coordenada[0], coordenada[1])
# --- DETECCIÓN DE CERCANÍA ---
def gestionar_ia_enemigos():
    for bug2 in sprites.all_of_kind(SpriteKind.enemy):
        # El jefe no patrulla, siempre persigue
        if bug2 == jefe_final:
            continue
        # Calcular distancia en píxeles (5 baldosas * 16 px = 80 píxeles)
        dist_x = abs(bug2.x - mi_jugador.x)
        dist_y = abs(bug2.y - mi_jugador.y)
        if dist_x < 80 and dist_y < 80:
            # ESTÁS EN RANGO: Te ha visto, te persigue
            bug2.follow(mi_jugador, 35)
        else:
            # FUERA DE RANGO: Deja de perseguirte
            bug2.follow(mi_jugador, 0)
            # Si se ha quedado quieto al chocar con un muro del mapa, le damos un nuevo empujón
            if bug2.vx == 0 and bug2.vy == 0:
                bug2.vx = randint(-25, 25)
                bug2.vy = randint(-25, 25)
def gestionar_animaciones():
    global dir_x, dir_y
    # --- Animación y Dirección del Robot ---
    # Guardamos la dirección (dir_x, dir_y) para saber a dónde disparar luego
    if mi_jugador.vx > 0:
        dir_x = 100
        dir_y = 0
        mi_jugador.set_image(assets.image("""
            robot_right
            """))
    elif mi_jugador.vx < 0:
        dir_x = -100
        dir_y = 0
        mi_jugador.set_image(assets.image("""
            robot_left
            """))
    elif mi_jugador.vy < 0:
        dir_x = 0
        dir_y = -100
        mi_jugador.set_image(assets.image("""
            robot_up
            """))
    elif mi_jugador.vy > 0:
        dir_x = 0
        dir_y = 100
        mi_jugador.set_image(assets.image("""
            robot_front
            """))
    # --- Animación Jefe Final ---
    if jefe_final:
        if jefe_final.vx > 0:
            jefe_final.set_image(assets.image("""
                boss_right
                """))
        elif jefe_final.vx < 0:
            jefe_final.set_image(assets.image("""
                boss_left
                """))
        elif jefe_final.vy < 0:
            jefe_final.set_image(assets.image("""
                boss_up
                """))
        elif jefe_final.vy > 0:
            jefe_final.set_image(assets.image("""
                boss_front
                """))
    # --- Animación Enemigos ---
    for bug22 in sprites.all_of_kind(SpriteKind.enemy):
        if bug22 == jefe_final:
            continue
        if bug22.vx > 0:
            bug22.set_image(assets.image("""
                bug_right
                """))
        elif bug22.vx < 0:
            bug22.set_image(assets.image("""
                bug_left
                """))
        elif bug22.vy < 0:
            bug22.set_image(assets.image("""
                bug_up
                """))
        elif bug22.vy > 0:
            bug22.set_image(assets.image("""
                bug_down
                """))
# --- INICIO DEL PROGRAMA ---
mostrar_menu_inicio()
# --- BUCLE PRINCIPAL ---

def on_on_update():
    if mi_jugador:
        gestionar_ia_enemigos()
        gestionar_animaciones()
game.on_update(on_on_update)

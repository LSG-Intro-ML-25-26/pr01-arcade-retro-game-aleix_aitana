/** --- VARIABLES GLOBALES --- */
let mi_jugador : Sprite = null
let menu : miniMenu.MenuSprite = null
//  Variable global para el jefe final
let jefe_final : Sprite = null
//  Variables para recordar hacia dónde mira el robot y poder disparar en esa dirección
let dir_x = 0
let dir_y = 100
function inicializar_juego() {
    
    //  Configura el mapa y coloca al robot en la zona azul.
    //  1. CARGAR EL MAPA
    tiles.setCurrentTilemap(tilemap`
        level
        `)
    //  2. POSICIONAMIENTO EN ZONA AZUL
    mi_jugador = sprites.create(assets.image`
        robot_front
        `, SpriteKind.Player)
    //  Coordenadas ajustadas al círculo azul de tu imagen:
    tiles.placeOnTile(mi_jugador, tiles.getTileLocation(34, 16))
    //  Configurar movimiento y cámara
    controller.moveSprite(mi_jugador)
    scene.cameraFollowSprite(mi_jugador)
    info.setLife(3)
    //  Ponemos el contador a 0
    info.setScore(0)
    //  3. GENERAR ENEMIGOS (Lejos de la zona azul)
    spawn_bugs(5)
    //  Llamamos a la función que crea las piezas
    repartir_piezas()
}

//  --- NUEVO: DISPARAR CON EL BOTÓN A ---
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    let disparo: Sprite;
    if (mi_jugador) {
        //  Crea un proyectil de plasma azul cian
        disparo = sprites.createProjectileFromSprite(img`
            . . 9 9 . .
            . 9 6 6 9 .
            9 6 1 1 6 9
            9 6 1 1 6 9
            . 9 6 6 9 .
            . . 9 9 . .
        `, mi_jugador, dir_x, dir_y)
        music.pewPew.play()
    }
    
})
//  --- NUEVO: COLISIÓN DEL DISPARO CONTRA LOS ENEMIGOS ---
//  Asignamos el evento de choque Proyectil - Enemigo
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap_disparo(sprite: Sprite, otherSprite: Sprite) {
    //  Destruye el disparo al chocar
    sprite.destroy()
    //  Busca la barra de vida del enemigo golpeado
    let barra_vida = statusbars.getStatusBarAttachedTo(StatusBarKind.Health, otherSprite)
    if (barra_vida) {
        barra_vida.value -= 1
        //  Efecto de daño
        otherSprite.startEffect(effects.blizzard, 200)
        //  Si la vida llega a 0, el enemigo muere
        if (barra_vida.value <= 0) {
            otherSprite.destroy(effects.disintegrate, 200)
            music.zapped.play()
            //  ¡SI EL QUE MUERE ES EL JEFE FINAL, GANAS EL JUEGO!
            if (otherSprite == jefe_final) {
                game.showLongText("¡NÚCLEO ELIMINADO! El sistema se ha restablecido.", DialogLayout.Bottom)
                game.gameOver(true)
            }
            
        }
        
    }
    
})
function repartir_piezas() {
    //  --- PIEZA 1 ---
    let piece1 = sprites.create(assets.image`piece1`, SpriteKind.Food)
    tiles.placeOnTile(piece1, tiles.getTileLocation(16, 2))
    //  --- PIEZA 2 ---
    let piece2 = sprites.create(assets.image`piece2`, SpriteKind.Food)
    tiles.placeOnTile(piece2, tiles.getTileLocation(27, 17))
    //  --- PIEZA 3 ---
    let piece3 = sprites.create(assets.image`piece3`, SpriteKind.Food)
    tiles.placeOnTile(piece3, tiles.getTileLocation(2, 2))
}

function aparecer_jefe() {
    
    game.showLongText("¡PELIGRO! El núcleo Root-Overwrite ha despertado.", DialogLayout.Bottom)
    //  Creamos al jefe final
    jefe_final = sprites.create(assets.image`boss_front`, SpriteKind.Enemy)
    //  ⬇️ EDITA AQUÍ LAS COORDENADAS DONDE APARECERÁ EL JEFE FINAL (Columna, Fila) ⬇️
    tiles.placeOnTile(jefe_final, tiles.getTileLocation(10, 10))
    //  NUEVO: Le ponemos su barra de vida gigante de 15 puntos
    let barra_jefe = statusbars.create(40, 6, StatusBarKind.Health)
    barra_jefe.attachToSprite(jefe_final)
    barra_jefe.max = 15
    barra_jefe.value = 15
    //  Hacemos que persiga al jugador
    jefe_final.follow(mi_jugador, 40)
}

sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy(effects.confetti, 500)
    info.changeScoreBy(1)
    music.baDing.play()
    if (info.score() == 3) {
        aparecer_jefe()
    }
    
})
function narrar_historia() {
    //  Muestra cuadros de texto explicando el Lore del juego.
    game.showLongText("Año 2149." + "Los servidores corporativos se han convertido en mundos digitales conscientes", DialogLayout.Bottom)
    game.showLongText("El servidor NEXUS-CORE ha sido infectado." + "Un virus ha tomado el control del sistema.", DialogLayout.Bottom)
    game.showLongText("Protocolo activado: 404." + "Reinicio total inminente.", DialogLayout.Bottom)
    game.showLongText("Tú eres un Data Sweeper." + "Un robot diseñado para limpiar datos corruptos.", DialogLayout.Bottom)
    game.showLongText("Tu misión:" + "Recuperar 3 Paquetes de Datos Vitales.", DialogLayout.Bottom)
    game.showLongText("El virus tiene un núcleo." + "Su nombre es Root-Overwrite.", DialogLayout.Bottom)
    //  NUEVAS INSTRUCCIONES DE DISPARO
    game.showLongText("Llevas equipado un Cañón de Limpieza de Datos. Usa el BOTÓN A para disparar.", DialogLayout.Bottom)
    game.showLongText("Las cucarachas caerán con 2 impactos. El núcleo requerirá 15.", DialogLayout.Bottom)
    game.showLongText("El tiempo corre." + "Inicia la limpieza.", DialogLayout.Bottom)
}

function mostrar_menu_inicio() {
    
    //  1. Configuramos el fondo
    scene.setBackgroundImage(img`
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
        `)
    //  2. Creamos el menú directamente como una variable local primero
    menu = miniMenu.createMenu(miniMenu.createMenuItem("JUGAR"), miniMenu.createMenuItem("LORE"))
    //  3. Estética
    menu.setFrame(assets.image`
        MenuFrame
        `)
    menu.setStyleProperty(miniMenu.StyleKind.Selected, miniMenu.StyleProperty.Background, 8)
    menu.bottom = 110
    menu.left = 50
    //  4. Lógica de selección
    menu.onButtonPressed(controller.A, function on_button_pressed(selection: any, selectedIndex: any) {
        menu.close()
        if (selection == "LORE") {
            narrar_historia()
            mostrar_menu_inicio()
        } else {
            inicializar_juego()
        }
        
    })
}

function bloquear_enemigos_puentes() {
    let c: number;
    //  Opcional: Impide que los enemigos crucen a tu sala.
    for (let bug3 of sprites.allOfKind(SpriteKind.Enemy)) {
        c = Math.idiv(bug3.x, 16)
        if (c == 19) {
            bug3.vx = 0
            bug3.x -= 2
        }
        
    }
}

function spawn_bugs(cantidad: number) {
    let bug: Sprite;
    let col_azar: number;
    let fil_azar: number;
    let barra: StatusBarSprite;
    for (let index = 0; index < cantidad; index++) {
        bug = sprites.create(assets.image`
            bug_down
            `, SpriteKind.Enemy)
        col_azar = randint(1, 18)
        fil_azar = randint(1, 14)
        tiles.placeOnTile(bug, tiles.getTileLocation(col_azar, fil_azar))
        //  NUEVO: Barra de vida de las cucarachas (2 puntos)
        barra = statusbars.create(16, 2, StatusBarKind.Health)
        barra.attachToSprite(bug)
        barra.max = 2
        barra.value = 2
        bug.follow(mi_jugador, 30)
    }
}

function gestionar_animaciones() {
    
    //  --- Animación y Dirección del Robot ---
    //  Guardamos la dirección (dir_x, dir_y) para saber a dónde disparar luego
    if (mi_jugador.vx > 0) {
        dir_x = 100
        dir_y = 0
        mi_jugador.setImage(assets.image`robot_right`)
    } else if (mi_jugador.vx < 0) {
        dir_x = -100
        dir_y = 0
        mi_jugador.setImage(assets.image`robot_left`)
    } else if (mi_jugador.vy < 0) {
        dir_x = 0
        dir_y = -100
        mi_jugador.setImage(assets.image`robot_up`)
    } else if (mi_jugador.vy > 0) {
        dir_x = 0
        dir_y = 100
        mi_jugador.setImage(assets.image`robot_front`)
    }
    
    //  --- Animación Jefe Final ---
    if (jefe_final) {
        if (jefe_final.vx > 0) {
            jefe_final.setImage(assets.image`boss_right`)
        } else if (jefe_final.vx < 0) {
            jefe_final.setImage(assets.image`boss_left`)
        } else if (jefe_final.vy < 0) {
            jefe_final.setImage(assets.image`boss_up`)
        } else if (jefe_final.vy > 0) {
            jefe_final.setImage(assets.image`boss_front`)
        }
        
    }
    
    //  --- Animación Enemigos ---
    for (let bug2 of sprites.allOfKind(SpriteKind.Enemy)) {
        if (bug2 == jefe_final) {
            continue
        }
        
        if (bug2.vx > 0) {
            bug2.setImage(assets.image`bug_right`)
        } else if (bug2.vx < 0) {
            bug2.setImage(assets.image`bug_left`)
        } else if (bug2.vy < 0) {
            bug2.setImage(assets.image`bug_up`)
        } else if (bug2.vy > 0) {
            bug2.setImage(assets.image`bug_down`)
        }
        
    }
}

//  --- INICIO DEL PROGRAMA ---
mostrar_menu_inicio()
//  --- BUCLE PRINCIPAL ---
game.onUpdate(function on_on_update() {
    if (mi_jugador) {
        gestionar_animaciones()
        bloquear_enemigos_puentes()
    }
    
})

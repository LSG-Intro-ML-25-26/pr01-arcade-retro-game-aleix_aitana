//  --- VARIABLES GLOBALES ---
let mi_jugador : Sprite = null
function inicializar_juego() {
    /** Configura el mapa, el jugador y los enemigos iniciales. */
    
    //  1. Cargar el mapa (Corregido: tiles.set_current_tilemap)
    tiles.setCurrentTilemap(tilemap`level`)
    //  2. Crear jugador y situarlo en la HABITACIÓN DERECHA
    //  Usamos coordenadas de la zona derecha del mapa
    mi_jugador = sprites.create(assets.image`robot_front`, SpriteKind.Player)
    tiles.placeOnTile(mi_jugador, tiles.getTileLocation(22, 8))
    controller.moveSprite(mi_jugador)
    scene.cameraFollowSprite(mi_jugador)
    info.setLife(3)
    //  3. Crear enemigos aleatorios (en las salas de la izquierda/centro)
    crear_bugs_iniciales(5)
}

function crear_bugs_iniciales(cantidad: number) {
    let bug: Sprite;
    let col_azar: number;
    let fil_azar: number;
    /** Reparte enemigos aleatoriamente fuera de la zona del jugador. */
    for (let i = 0; i < cantidad; i++) {
        bug = sprites.create(assets.image`bug_down`, SpriteKind.Enemy)
        //  Spawn solo en la parte izquierda y central (columnas 1 a 18)
        col_azar = randint(1, 18)
        fil_azar = randint(1, 14)
        tiles.placeOnTile(bug, tiles.getTileLocation(col_azar, fil_azar))
        //  Hacer que sigan al jugador (Corregido: bug.follow)
        bug.follow(mi_jugador, 30)
    }
}

function actualizar_animaciones() {
    /** Cambia el estilo visual según la dirección del movimiento. */
    //  Animación del Robot
    if (mi_jugador.vx > 0) {
        mi_jugador.setImage(assets.image`robot_right`)
    } else if (mi_jugador.vx < 0) {
        mi_jugador.setImage(assets.image`robot_left`)
    } else if (mi_jugador.vy < 0) {
        mi_jugador.setImage(assets.image`robot_up`)
    } else if (mi_jugador.vy > 0) {
        mi_jugador.setImage(assets.image`robot_front`)
    }
    
    //  Animación de los Bugs (Corregido: sprites.all_of_kind)
    for (let bug of sprites.allOfKind(SpriteKind.Enemy)) {
        if (bug.vx > 0) {
            bug.setImage(assets.image`bug_right`)
        } else if (bug.vx < 0) {
            bug.setImage(assets.image`bug_left`)
        } else if (bug.vy < 0) {
            bug.setImage(assets.image`bug_up`)
        } else if (bug.vy > 0) {
            bug.setImage(assets.image`bug_down`)
        }
        
    }
}

function restringir_enemigos() {
    let col_enemigo: number;
    /** Impide que los enemigos crucen hacia las escaleras o pasillos estrechos. */
    for (let enemigo of sprites.allOfKind(SpriteKind.Enemy)) {
        //  Localizamos la columna actual del enemigo en el mapa
        col_enemigo = Math.idiv(enemigo.x, 16)
        //  Lógica: Si el enemigo intenta entrar en la zona de escaleras (Cols 19-20)
        //  que conectan con la habitación derecha, lo frenamos.
        if (col_enemigo >= 19 && col_enemigo <= 20) {
            enemigo.vx = 0
            enemigo.vy = 0
            //  Lo empujamos un poco atrás para que no se quede pegado
            enemigo.x -= 2
        }
        
    }
}

//  --- BUCLE PRINCIPAL ---
game.onUpdate(function on_update() {
    actualizar_animaciones()
    restringir_enemigos()
})
//  Ejecutar inicio
inicializar_juego()

//  --- VARIABLES GLOBALES ---
let mi_jugador : Sprite = null
function inicializar_juego() {
    
    /** Configura el mapa y coloca al robot en la zona azul. */
    //  1. CARGAR EL MAPA
    //  Función corregida para Python
    tiles.setCurrentTilemap(tilemap`
        level
        `)
    //  2. POSICIONAMIENTO EN ZONA AZUL
    mi_jugador = sprites.create(assets.image`
        robot_front
        `, SpriteKind.Player)
    //  Coordenadas ajustadas al círculo azul de tu imagen:
    //  Columna 22, Fila 13 (Esquina inferior de la sala derecha)
    tiles.placeOnTile(mi_jugador, tiles.getTileLocation(34, 16))
    //  Configurar movimiento y cámara
    controller.moveSprite(mi_jugador)
    scene.cameraFollowSprite(mi_jugador)
    info.setLife(3)
    //  3. GENERAR ENEMIGOS (Lejos de la zona azul)
    spawn_bugs(5)
}

function spawn_bugs(cantidad: number) {
    let bug: Sprite;
    let col_azar: number;
    let fil_azar: number;
    /** Crea enemigos en las salas de la izquierda para dar tiempo al jugador. */
    for (let i = 0; i < cantidad; i++) {
        bug = sprites.create(assets.image`
            bug_down
            `, SpriteKind.Enemy)
        //  Generar aleatoriamente en columnas 1 a 18 (lado izquierdo/centro)
        col_azar = randint(1, 18)
        fil_azar = randint(1, 14)
        tiles.placeOnTile(bug, tiles.getTileLocation(col_azar, fil_azar))
        //  Función de seguimiento corregida
        bug.follow(mi_jugador, 30)
    }
}

function gestionar_animaciones() {
    /** Actualiza las imágenes del robot y enemigos según su dirección. */
    //  --- Animación Robot ---
    if (mi_jugador.vx > 0) {
        mi_jugador.setImage(assets.image`
            robot_right
            `)
    } else if (mi_jugador.vx < 0) {
        mi_jugador.setImage(assets.image`
            robot_left
            `)
    } else if (mi_jugador.vy < 0) {
        mi_jugador.setImage(assets.image`
            robot_up
            `)
    } else if (mi_jugador.vy > 0) {
        mi_jugador.setImage(assets.image`
            robot_front
            `)
    }
    
    //  --- Animación Enemigos ---
    //  Corrección de sintaxis 'in' y 'all_of_kind'
    for (let bug2 of sprites.allOfKind(SpriteKind.Enemy)) {
        if (bug2.vx > 0) {
            bug2.setImage(assets.image`
                bug_right
                `)
        } else if (bug2.vx < 0) {
            bug2.setImage(assets.image`
                bug_left
                `)
        } else if (bug2.vy < 0) {
            bug2.setImage(assets.image`
                bug_up
                `)
        } else if (bug2.vy > 0) {
            bug2.setImage(assets.image`
                bug_down
                `)
        }
        
    }
}

function bloquear_enemigos_puentes() {
    let c: number;
    /** Opcional: Impide que los enemigos crucen a tu sala. */
    for (let bug3 of sprites.allOfKind(SpriteKind.Enemy)) {
        c = Math.idiv(bug3.x, 16)
        //  Si intentan cruzar el puente de la columna 19 (entrada a tu sala)
        if (c == 19) {
            bug3.vx = 0
            bug3.x -= 2
        }
        
    }
}

//  --- BUCLE PRINCIPAL ---
game.onUpdate(function on_update() {
    gestionar_animaciones()
    bloquear_enemigos_puentes()
})
//  Iniciar
inicializar_juego()

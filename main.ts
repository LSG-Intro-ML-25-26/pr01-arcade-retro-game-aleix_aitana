// --- VARIABLES GLOBALES (Abasto de variables) ---
let miJugador: Sprite = null
let inventario: string[] = [] // Estructura de datos compleja: Vector/Lista 
let paquetesNecesarios = 3

/**
 * Inicializa los valores técnicos del sistema.
 * [cite: 39, 59]
 */
function inicializarSistema() {
    inventario = []
    info.setScore(0)
    info.setLife(3)
}

/**
 * Gestiona la recolección de objetos de forma modular.
 * @param objeto Nombre del ítem recogido
 * [cite: 39, 59]
 */
function gestionarInventario(objeto: string) {
    inventario.push(objeto)
    music.baDing.play()
    game.splash("Recuperado: " + objeto)

    // Verifica si se ha alcanzado el objetivo para el final del juego [cite: 57]
    if (inventario.length >= paquetesNecesarios) {
        desbloquearFinal()
    }
}

/**
 * Lógica técnica para procesar el daño de los enemigos.
 * [cite: 39]
 */
function procesarDano() {
    info.changeLifeBy(-1)
    scene.cameraShake(4, 500)
    miJugador.say("¡ERROR!", 500)
    // Pequeño retroceso para evitar perder vidas seguidas
    miJugador.x += 10
}

/**
 * Funcionalidad Extra: Dibuja un mini-indicador de progreso en pantalla.
 * 
 */
function dibujarInterfazTecnica() {
    // Dibuja un fondo para el mini-mapa/inventario en la esquina
    screen.fillRect(2, 2, 22, 8, 15)
    for (let i = 0; i < inventario.length; i++) {
        // Dibuja un punto verde por cada objeto en el inventario
        screen.setPixel(4 + (i * 6), 5, 7)
    }
}

/**
 * Activa la fase final del juego.
 * [cite: 57]
 */
function desbloquearFinal() {
    game.showLongText("SISTEMA REPARADO. Busca la salida.", DialogLayout.Bottom)
    // Aquí Persona B debería cambiar el mapa o abrir una puerta
}

// Evento que se ejecuta constantemente para actualizar la GUI técnica [cite: 58]
game.onUpdate(function () {
    dibujarInterfazTecnica()
})
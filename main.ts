/**
 * Activa la fase final del juego.
 * 
 * [cite: 57]
 */
/**
 * --- VARIABLES GLOBALES (Abasto de variables) ---
 */
// Funcionalidad Extra: Dibuja un mini-indicador de progreso en pantalla.
function dibujarInterfazTecnica () {
    //  Dibuja un fondo para el mini-mapa/inventario en la esquina
    screen.fillRect(2, 2, 22, 8, 15)
    while (i <= inventario.length - 1) {
        //  Dibuja un punto verde por cada objeto en el inventario
        screen.setPixel(4 + i * 6, 5, 7)
        i += 1
    }
}
// Lógica técnica para procesar el daño de los enemigos.
// [cite: 39]
function procesarDano () {
    let miJugador: Sprite = null
    info.changeLifeBy(-1)
    scene.cameraShake(4, 500)
    miJugador.say("¡ERROR!", 500)
    // Pequeño retroceso para evitar perder vidas seguidas
    miJugador.x += 10
}
// Gestiona la recolección de objetos de forma modular.
// @param objeto Nombre del ítem recogido
// [cite: 39, 59]
function gestionarInventario (objeto: string) {
    inventario.push(objeto)
    music.baDing.play()
    game.splash("Recuperado: " + objeto)
    // Verifica si se ha alcanzado el objetivo para el final del juego [cite: 57]
    if (inventario.length >= paquetesNecesarios) {
        desbloquearFinal()
    }
}
// Inicializa los valores técnicos del sistema.
// [cite: 39, 59]
function inicializarSistema () {
    inventario = []
    info.setScore(0)
    info.setLife(3)
}
// Aquí Persona B debería cambiar el mapa o abrir una puerta
function desbloquearFinal () {
    game.showLongText("SISTEMA REPARADO. Busca la salida.", DialogLayout.Bottom)
}
let inventario: string[] = []
let i = 0
let paquetesNecesarios = 0
// Estructura de datos compleja: Vector/Lista
paquetesNecesarios = 3
// Evento que se ejecuta constantemente para actualizar la GUI técnica [cite: 58]
game.onUpdate(function () {
    dibujarInterfazTecnica()
})

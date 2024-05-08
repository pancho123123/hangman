word_list = [
	"elefante", "oso", "perro", "gato", "caballo", "tigre", "rinoceronte", 
	"gacela", "hipopotamo","cocodrilo", "caiman", "iguana", "lagarto", "camello",
	"foca", "avestruz", "mono", "chimpance", "orangutan", "jirafa", "sapo", "loro", 
	"paloma", "tortola", "ballena", "tiburon", "serpiente", "boa", "alce", "venado",
	"aguila", "halcon", "leon", "pantera", "puma", "llama", "alpaca", "cachalote",
	"orca", "delfin", "cangrejo", "jaiba", "calamar", "pulpo", "atun", "jurel", 
	"kanguro", "ardilla", "velociraptor", "triceratop", "buey", "pinguino", "bufalo",
	"araña", "escorpion", "alacran", "escarabajo", "golondrina", "mariposa", "oruga",
	"culebra", "pato", "ganzo", "morsa", "hormiga", "langosta", "medusa", "oxigeno",
	"carbon", "fosil", "vida", "origen", "tierra", "mucho", "año", "cierto", "rayo", 
	"metano", "habia", "verdad", "disminuyendo", "temperatura", "pintura", "brocha", 
	"pincel", "lapiz", "tijera", "martillo", "sacapunta", "regla", "gases", "sencillo",
	"primitiva", "sabemos", "desarrollarse", "caracteristica", "hace", "vivo", "vital",
	"vidrio", "metal", "madera", "mosaico", "muerte", "moho", "hongo", "planta",
	"arbol", "manzana", "fruta", "guinda", "frambueza", "conejo", "liebre", "dormilon",
	"fortuna", "tuna", "camote", "mote", "hueso", "mina", "material", "celula", 
	"cigueña", "rueda", "rata", "raton", "hamster", "terapia", "tierra", "barro",
	"humedad", "caso", "cabo", "cerdo", "chancho", "gallina", "gusano", "lombriz",
	"caracol", "molusco", "invertebrado", "reptil", "mamifero", "concha", "cosa", 
	"letra", "letrina", "lento", "lenteja", "poroto", "bototo", "garbanzo",
	"arroz", "bistec", "hamburgueza", "crocante", "simio", "tren", "bus", "estado",
	"pais", "esquina", "cuartel", "soldado", "militar", "calle", "aire", "especie",
	"albondiga", "diga", "decil", "dime", "docil","duende","dormir", "duerma",
	"donde", "cuando", "llegue", "llego", "llave", "ostra", "costra", "dado",
	"roca", "piedra", "piedad","pobre", "pobreza", "poco", "posa", "palo",
	"paso", "tambor", "trompeta", "saxofon", "cilindro","persona","personalidad",
	"pepa", "peca", "pesado", "pesca", "mineria", "agricultura","avion",
	"jet", "agua", "harto", "escazo", "era", "conde", "dracula", "vaso", "bebe",
	"guagua", "brazo", "bravo", "brava", "breve", "brevedad", "brea", "rosa"
	"gancho", "argolla", "aro", "arete", "tatuaje", "negro", "blanco", "azul",
	"amarillo", "verde", "morado", "marron", "mora", "piña", "celeste", 
	"coco", "glandula", "saliva", "sabia", "sobre", "bajo", "contra", "aqui",
	"alli", "hasta", "corbata", "corbatin", "techo","techumbre", "aprieto",
	"piraña", "percha", "puerco", "axila", "pie", "combate", "silla", "sillon",
	"sofa", "cama", "camarote", "estufa", "celo", "celosa", "golosa", "goloso",
	"celoso", "juez", "juzga", "ley", "leyes", "abogado", "escalera", "cielo",
	"bufanda", "cuello", "collar", "pera", "montaña", "monte", "cima", 
	"mamut", "buho", "maña", "mañoso", "mañosa", "mano", "manos", "moso",
	"ordena", "recibe", "ordeña", "ordeñar", "orden", "ordenado", "ordenada",
	"caos", "horrible", "oscuro", "claro", "confianza", "pozo", "rodrigo", 
	"ricardo", "esteban", "gerardo", "jorge", "jarro", "jarra", "felipe",
	"ignacio", "cristian", "francisco", "francisca", "ignacia", "olla",
	"sarten", "salsa", "tallarin", "espinaca", "lechuga", "lechuza",
	"fuego", "fogata", "raro", "rara", "salto", "saltar", "emprender",
	"empanada", "huevo", "hueco", "huella", "hueca", "paracaidas", "granada"
	"gozo", "paz", "tranquilidad", "alegria", "honesto", "honesta", "rifle"
	"principe", "princesa", "rey", "reyes", "matias", "fernando", "fernanda",
	"carol", "carolina", "karla", "carlos", "diego", "marcos", "marco", "escopeta"
	"mellado", "mella", "cavidad", "entrada", "salida", "salir", "salgo",
	"sarro", "zarza", "arena", "abrir", "abra", "abriendo", "tarro", "campana"
	"tostada", "calentar", "caliente", "bella", "bello", "exclamar", "oro"
	"cinturon", "camisa", "terno", "tierno", "flor", "alfombra", "corona"
	"rescate", "rescatar", "reta", "reto", "romper", "rompa", "ocio", "paraguas"
	"romecabeza", "pizza", "pez", "poro", "saco", "saca", "sacar", "muralla"
	"soldar", "soldadura", "cierra", "sierra", "casar", "cazar", "guata",
	"bocado", "clavo", "clavada", "clavel", "piñata", "embarrar", "mural",
	"pistola", "bala", "baño", "ducha", "cuchillo", "tenedor", "plato", "plata",
	"numero", "numeros", "oregano", "pimenton", "pimienta", "comino", "domino",
	"dominar", "sucio", "refrigerador", "termo", "enchufe", "camino", "sendero",
	"balde", "burro", "anaconda", "ana", "fisura", "bosque", "pino", "vegetal",
	"verdura", "dulce", "amargo", "sal", "luz", "sol", "solo", "sola", "soleado",
	"escoba", "escondite", "esconder", "encender", "encendido", "encendio", "encendia",
	"verbo", "palabra", "computador", "monasterio", "valle", "lago", "rio", "mar",
	"oceano", "continente", "largo", "angosto", "rodamiento", "aceite", "cuchara",
	"cucaracha", "pasto", "hierba", "botella", "frio", "congelado", "hielo", "hierro",
	"congelar", "cono", "costra", "guante", "anillo", "dedo", "pierna", "muslo",
	"hombro", "hombre", "mujer", "niño", "niña", "juguete", "oscar", "leandro",
	"maria", "daniel", "daniela", "dante", "diente", "duro", "dureza", "dorar",
	"doro", "dorado", "dorada", "maravilla", "mastil", "babor", "estribor", "posterior",
	"anterior", "asco", "zorro", "lobo", "ladera", "barranco", "esto", "eso", "bara", "barra",
	"colosal", "espiraculo", "cueva", "cigarro", "cigarra", "humo", "vapor", "nube", 
	"lluvia", "esmerar", "espuma", "raso", "rastro", "arrastrar", "invocar", "orar", "rodilla",
	"rodillo", "cuerda", "nudo", "escalar", "boca", "lengua", "muela", "paro", "lunes", 
	"martes", "miercoles", "jueves", "viernes", "sabado", "domingo", "festivo", "calendario",
	"feriado", "feria", "vendedor", "ambulante", "ambulancia", "bombero", "incendio",
	"canasta", "rabia", "enojo", "enojar", "desanimar", "animar", "mimo", "payaso",
	"mancha", "sondear", "sonda", "sordo", "sorda", "sordera", "zurco", "zapato",
	"bota", "zapatilla", "calzado", "calzada", "calzar", "calcio", "potasio", "palta",
	"pasa", "pomelo", "naranja", "lavatorio", "cuarto", "cuarta", "primero", "segundo",
	"segunda", "primera", "uva", "parra", "estiercol", "piscina", "estanque", "estanca",
	"estaca", "carpa", "caro", "barato", "economia", "cobra", "falta", "sabemos", "tierra",
	"aparecio", "mayor", "menor", "microscopico", "microscopio", "microbio", "conservacion",
	"algunos", "historia", "dividimos", "dejaron", "nuestro", "sonido", "color", "canto",
	"funcion", "parada", "reclamo", "reclamar", "pajaro", "diversidad", "hembra", "izquierda",
	"derecha", "migracion", "migrar", "golondrina", "establecido", "alimento", "vuelan", 
	"direccion", "sentido", "frecuencia", "ruido", "producen", "prioridad", "intensidad",
	"intenso", "profundo", "nervioso", "nerviosa", "medida", "indica", "indicar", "grande", 
	"foto", "medio", "exceso", "punto", "ola", "unidad", "podemos", "partir", "parir",
	"ambiente", "reproduccion", "oido", "altura", "altitud", "hoyo", "bajo", "orquesta", 
	"astronauta", "espacio", "espacial", "encima", "procedente", "mortal", "litro", "rapido",
	"cierto", "ojo", "ojos", "pestaña", "celda", "cerca", "rostro", "desaparecen", "bastante",
	"gravedad", "radiacion", "kilometro", "longitud", "desencajado", "precaucion", "fisico",
	"ejercicio", "tejido", "tejer", "rastro", "debido", "deuda", "falta", "fuera", "fuerza",
	"simulan", "desplazarse", "traje", "alejarse", "autonomia", "gracias", "perdon", 
	"ademas", "suma", "sumar", "restan", "restar", "empezar", "comienzo", "comiendo",
	"comer", "comida", "aspecto", "gradual", "parece", "ultravioleta", "otras",
	"nosotros", "general", "guardar", "formados", "problemas", "problema", "peso",
	"cuerpo", "sacudir", "sacudida", "meses", "mes", "semana", "momento", "murcielago",
	"brisa", "mosca", "zancudo", "area", "desplaza", "presion", "insecto", "alado", "aliado",
	"viaje", "viajan", "forastero", "ermitaño", "vampiro", "tropical", "causa", "casual",
	"casualidad", "veces", "llenarse", "inversion", "empresa", "nombre", "situado", "animal",
	"desaparecio", "desaparecido", "percibir", "ingreso", "ingresa", "mediante", "calcula",
	"calcular", "culpa", "estudio", "estudiar", "siglo", "sigla", "siglos", "indirecta",
	"indirecto", "trayecto", "trayectoria", "consecuencia", "ultimo", "exterminio", 
	"evidente", "evidencia", "ciencia", "acelerado", "acelerar", "abundante", "dramatico",
	"drama", "teatro", "mascara", "careta", "disfraz", "globo", "pradera", "patas",
	"manera", "voluntad", "doble", "doblar", "doblado", "doblada", "enderezar", "extincion",
	"eventual", "evento", "corre", "amenazado", "divierte", "peligro", "concreto", "iglesia",
	"desastre", "amanecer", "atardecer", "esclavo", "recoleccion", "enseñar", "distribuido",
	"particular", "zona", "selva", "jungla", "precipitacion", "roedor", "distinguir", 
	"pulga", "pulgar", "mamifero", "traicionar", "emboscada", "emboscar", "ambicion",
	"espada", "katana", "pulpa", "trozo", "traza", "linea", "lado", "asado", "pelota", 
	"muro", "estampida", "estampar", "estampa", "estampado", "burbuja", "brujula",
	"barco", "navegar", "navegacion", "nada", "nadar", "teclado", "flauta", "acordeon",
	"acuerdo", "recordar", "olvidar", "fastidiar", "pelaje", "gelatina", "espejo", 
	"reflejo", "alumbrar", "acontecer", "mirar", "observar", "escurrir", "convento",
	"contento", "contienda", "tienda", "local", "rural", "curva", "curvo", "curvar",
	"cuervo", "aluminio", "plata", "hidrogeno", "combustible", "helio", "carbon",
	"viene", "venir", "llegada", "llegar", "aproximar", "subir", "elevar", "oxido",
	"oxidado", "oxidada", "plomo", "panda", "pandero", "helado", "helada", "incierto",
	"papel", "naturaleza", "libro", "libreta", "pregunta", "dinosaurio", "ayuda",
	"empapar", "sueño", "radio", "telescopio", "recinto", "tumba", "tumbar", "tumbado",
	"reja", "suelo", "ceniza", "coro", "leña", "leche", "almendra", "nuez", "mani", 
	"uña", "foco", "lente", "guerra", "hambre", "marea", "sabor", "sabroso", "sabrosa",
	"tela", "galleta", "galletas", "tabla", "tablero", "pastilla", "tableta",
	"ventana", "puerta", "umbral", "apagar", "transparente", "inclinado",
	"inclinar", "inclinarse", "broma", "chiste", "polera", "falda", "inflar",
	"inflada", "inflado", "inflama", "inflamar", "inflamado", "inflamado",
	"blanco", "carpeta", "palmera", "playa", "rocas", "servilleta", "billete",
	"pago", "pagado", "pagada", "pagar", "impuesto", "reloj", "canoa",
	"bote", "balsa", "velero", "velorio", "funeral", "desodorante", "jabon",
	"shampoo", "agua", "miel", "ajo", "pepino", "gramo", "ganas", "ganar", "vencer",
	"conquista", "conquistar", "señalar", "señal", "señalado", "señalada", 
	"cachalote", "anguila", "despegar", "aterrizar", "desierto", "duna", "monje",
	"peldaño", "bolsa", "bolso", "amasar", "maestro", "señor", "cana", "carcel",
	"abanico", "angosto", "saturno", "jupiter", "venus", "mercurio", "fiesta", 
	"nevada", "nevar", "nevado", "nevera", "mojado", "mojada", "socio", "sociedad",
	"tapa", "tapar", "tapado", "tapada", "templado", "sebastian", "bruno", "nicolas", 
	"esparragos", "laberinto", "terminal", "termino", "terminacion", "nutria",
	"nutrir", "nutrido", "nutricion", "nutrida", "cactus", "gigante", "encuentran", 
	"raices", "gorgojo", "nocturno", "nocturna", "circular", "circulacion", 
	"externo", "exterminar", "examinar", "examen", "experimentar",
	"experimento", "experimentado", "experimentada", "experiencia", "experto",
	"exponente", "orbita", "orbitar", "silvestre", "rubio", "rubia", "moreno",
	"morena", "pelirrojo", "pelirroja", "pan", "panadero", "pesebre", 
	"mantequilla", "te", "cafe", "azucar", "ensalada", "piramide", "palacio",
	"sombra", "mover", "terremoto", "sismo", "temblor", "tembloroso",
	"gota", "zorzal", "uno", "dos", "tres", "cuatro", "cinco", "seis", "perla", 
	"siete", "ocho", "pinocho", "nariz", "nueve", "muñeco", "crustaceo",
	"marioneta", "titere", "tetera", "hierve", "peine", "peinar", "sentencia",
	"escandalo", "errar", "equivocarse", "pelicula", "cuadro", "cuadrado", 
	"redondo", "redondear", "hondo", "honda", "racimo", "rama", "arbusto",
	"lapida", "moneda", "huir", "delincuente", "ladron", "policia", "arma",
	"armamento", "armado", "armada", "marinero", "marina", "marino", "muelle",
	"puerto", "helicoptero", "submarino", "acuatico", "anfibio", "animacion",
	"anis", "angel", "angela", "andamio", "anima", "carie", "candado", "cargado",
	"caricatura", "carga", "carisma", "carismatico", "codicia", "avaricia", 
	"codigo", "colaborar", "coladero", "cordero", "colador", "encendedor",
	"colacion", "cojera", "cohibir", "cofre", "codificado", "colado",
	"colapso", "colonia", "colgar", "colectivo", "colocar", "colegio",
	"colombia", "peru", "copia", "copiar", "colateral", "colorado", "comando",
	"coma", "comedor", "compatible", "compañia", "compra", "comprado", "comprender",
	"complicar", "compasion", "competencia", "completar", "completo", "compactar",
	"compositor", "componente", "componer", "compartimiento", "compañero", "comparar",
	"complice", "comun", "concurrido", "conceder", "deseo", "desde", "comunicar",
	"concordar", "concavo", "concepto", "concebir", "presionar", "pretender",
	"preferir", "preferencia", "opcion", "presupuesto", "preste", "prestar",
	"presentar", "presente", "primario", "prestigio", "presumir", "publicar",
	"pua", "pulgada", "puente", "puesta", "seca", "sacudir", "sabotear",
	"purificar", "atrapar", "capturar", "cautiverio", "jugo", "jugoso", "juega",
	"jugar", "jugando", "jugador", "juguera", "banquete", "balneario", "bahia",
	"vasto", "impacto", "impactar", "impactado", "astro", "luna",
	"satelite", "fresco", "añejo", "añejar", "enjambre", "bandada", "banda",
	"cardumen", "carne", "carnivoro", "lleno", "llenado", "yema", "heno",
	"yeso", "adorno", "consolar", "corazon", "pulmon", "costilla", "hospital",
	"hospitalario", "huesped", "papa", "padre", "paño", "hundir",
	"huracan", "silaba", "tuerca", "silbar", "silbido", "poder", "oculto",
	"castillo", "fuerte", "taladro", "taladrar", "destornilldor", "nave",
	"embarcacion", "lava", "volcan", "estepa", "escama", "placa",
	"bifurcacion", "delta", "gobierno", "aseguro", "impunidad", "sentar",
	"oscuridad", "brillante", "lucero", "tentaculo", "limon", "durazno",
	"damasco", "platano", "chocolate", "vainilla", "crema", "cremoso",
	"batir", "justo", "jenjibre", "omitir", "ronquido", "roncar", "mugir",
	"graznido", "graznar", "granizo", "caudal", "rivera", "polar", "museo",
	"pasillo", "pausa", "liberar", "liderar", "ladera", "ladrido", "ladra",
	"amor", "amo", "amaba", "ame", "amoroso", "amarra", "amarro", "hamaca",
	"amonestar", "honrar", "encandilar", "patron", "empadronado", "patria",
	"pago", "pagar", "impuesto", "apertura", "fin", "vibora", "rana", "temporal",
	"temporada", "temporizador", "descender", "temprano", "tempano", "timpano",
	"molde", "moldear", "molido", "muela", "solido", "liquido", "gaseoso",
	"trompa", "trompo", "derrapar", "rapero", "barba", "barbero", "barberia",
	"mueble", "rampa", "quitar", "toxico", "cabeza", "frente", "quijada",
	"escudo", "roble", "victoria", "zanjar", "zanja", "funebre", "carroza",
	"carruaje", "carro", "auto", "automatico", "aturdir", "ceñir", 
	"circunvalacion", "estoque", "bramido", "brasa", "america", "copa",
	"encendido", "apagado", "apagar", "garantia", "gane", "ganar", "ganado",
	"falta", "faltante", "espina", "empinado", "inclinado", "borde", "limite",
	"region", "masa", "tobogan", "acarreo", "cargamento", "loza", "relleno",
	"rosca", "clavado", "directo", "indirecto", "recto", "extender",
	"extendido", "servir", "limpiar", "hector", "agustin", "salado",
	"exaltar", "tenebroso", "salar", "cuspide", "congrio", "pelar",
	"pelado", "pelada", "hebra", "hibrido", "correr", "corrida", 
	"aplanar", "adosar", "adorar", "erguir", "enderezar", "crecer",
	"acortar", "achicar", "alargar", "mascar", "goma", "dibujo", 
	"dibujar", "dibuje", "dibujando", "dividir", "division", "disputa",
	"discriminar", "discutir", "disecar", "discurso", "disponible",
	"disponer", "disimular", "simular", "disipar", "par", "impar",
	"distar", "distincion", "disfrutar", "diseñar", "disperso",
	"disparar", "disgusto", "dispensa", "distribucion", "adicion", 
	"adicto", "adiccion", "diverso", "diversidad", "divino",
	"diurno", "documentar", "documental", "monumento", "monumental",
	"divinidad", "doblez", "doctrina", "doctor", "doctorado", "doler",
	"frito", "fritura", "fuga", "fugitivo", "fugaz", "fuente", "frialdad",
	"frescura", "lunar", "luna", "lonja", "genero", "letra", "real", 
	"ficticio", "tercio", "tenia", "tango", "hoja", "giro", 
	"vena", "capilar", "arteria", "dilatacion", "degustar",
	"isla" "completa", "siguiente", "frase", "irma", "importa",
	"importar", "importado", "doris", "dormido", "rabano", "malla",
	"pedazo", "pedal", "patada", "petardo", "pantano", "esquimal", "iglu",
	"piña", "conversar", "crucero", "drama", "dramatico", "partido",
	"partida", "pasta", "valorar", "valor", "realizada", "realizar",
	"saludo", "saludar", "aplaudir", "martin", "marta", "mario",
	"primitivo", "canal", "transmitir", "transcurrir",
	"transcurso", "transversal", "atravesar", "acostumbrar",
	"acompañar", "calcinar", "monitorear", "monitor", 
	"brecha", "seguridad", "caracteristica", "erradicar",
	"sensor", "seleccionar", "seleccion", "mencionar",
	"frasco", "utensilio", "casa", "hogar", "tomo", "lomo",
	"espalda", "dorso", "empeine", "rodilla", "oreja",
	"delantal", "dentadura", "filo", "filoso", "fila",
	"columna", "invertebrado", "ecologico", "logico", "enumerar",
	"gorra", "casino", "poker", "recolectar", "basura", "basural",
	"posar", "pito", "pitilla", "guardar", "confeccionar",
	"hostigar", "rebalsar", "rellenar", "embravecer", "mecer",
	"enfurecer", "apunar","esperar", "abrazar", "abrasar",
	"enardecer", "arder", "ponderar", "promediar", "promedio",
	"pondera", "meta", "mental", "esquizofrenia", "paranoia",
	"alucinar", "relieve", "peninsula", "naufragar", "naufragio",
	"accidente", "deposito", "depositar", "cita", "conciliar",
	"reconciliar", "sonar", "eco", "pulso", "latido", "hemorragia",
	"hematoma", "globulo", "ocular", "binocular", "monopatin", "patin",
	"pare", "paren", "estancado", "estaño", "castaño", "tez", "contextura",
	"textura", "grueso", "delgado", "normal", "ajustado", "cinturon",
	"correa", "artefacto", "artropodo", "moluzco", "pendulo", "ondulacion",
	"ondulatorio", "observatorio", "planeta", "galaxia", "aristocracia",
	"onda", "efecto", "afeccion", "plano", "grado", "minuto", "hora",
	"horario", "tenso", "tensor", "tensionar", "tensa", "extenso", "trenza",
	"trenzado", "tenaz", "tenaza", "garfio", "raya", "rayado", "rayas", "rato",
	"resta", "restar", "sustraer", "mitigar", "auspiciar", "auspicio", "forma",
	"formacion", "formado", "formon", "forrado", "forraje", "follaje", "fauna",
	"flora", "florido", "floreado", "fuma", "fumador", "fumada", "fumar", "fumas",
	"funesto", "forjado", "forzado", "forzudo", "zurdo", "zurda", "ambidiestro",
	"chacal", "buitre", "leopardo", "chita", "hiena", "toro", "asqueroso",
	"vicera", "viceral", "intestino", "higado", "tendon", "normalizado",
	"bondad", "elipsis", "vocal", "violin", "contrabajo", "trabajo", "trabajar",
	"trajo", "trago", "tragar", "atragantar", "asficciar", "oxigenar", "calambre",
	"acalambrar", "acalambrado", "costumbre", "vislumbrar", "veloz", "velocidad",
	"velocidades", "inagural", "inauguracion", "argumentar", "frenar", "frenada",
	"freno", "frenazo", "frenado", "fregar", "fregado", "fregada", "frigorifico",
	"lola", "loco", "lenguado", "lenguaje", "lenguas", "lona", "alumbrado", "luciernaga",
	"lustrar", "ilustrar", "ilustrado", "ilustre", "futuro", "sucediendo",
	"sucesor", "suceso", "exceso", "conceder", "ceder", "dejar", "algoritmo",
	"ritmo", "rima", "riña", "riñon", "centolla", "cebolla", "picante", "picor",
	"pinza", "punzada", "agudizado", "agudo", "grave", "ventisquero", "viento",
	"ventolera", "venezuela", "bolivia", "argentina", "uruguay", "occidente",
	"gimnasio", "gimnasia", "ballesta", "arco", "arcoiris", "iris", "nombrado",
	"nombramiento", "china", "europa", "europeo", "italia", "brasil", "canada",
	"pergola", "gargola", "siniestro", "ardiente", "ron", "congestionar",
	"gestion", "gestionar", "asalto", "asaltar", "saltear", "atiborrar", "borrar",
	"dimension", "dimensionar", "broca", "cinta", "adhesivo", "adherente",
	"absorto", "abisal", "abono", "abrigar", "abstracto", "abrigo", "absoluto",
	"abril", "abrochar", "abrumado", "acelerar", "acantilado", "abundancia",
	"acaparar", "acaramelar", "caramelo", "acechar", "acecho", "acelga",
	"acequia", "acariciar", "academia", "aburrido", "academico", "accion",
	"acento", "aceptar", "accionar", "acampar", "aburrir", "acabar", "aclarar",
	"acordar", "acotacion", "acta", "acto", "acordonar", "acoger", "acogida", "acomodado",
	"acomodador", "acolchar", "acido", "acostar", "acribillar", "acorde", "acomplejado",
	"acrilico", "actividad", "activo", "adelantar", "achicoria", "acuchillar",
	"acuoso", "aderezo", "aderezar", "adiestrar", "adivinar", "adivinanza", "adivino",
	"adherir", "adentro", "adelantado", "acusar", "acuso", "acustica", "achaque", "acudir",
	"adelgazamiento", "adecuado", "alergia", "adjuntar", "adjetivo", "adaptar", "administracion",
	"acumular", "acumulacion", "adios", "estatua", "estatura", "estambre", "estadistica",
	"estatuto", "estela", "estallido", "estallar", "estadio", "estafa", "estacionamiento",
	"estadia", "estatico", "estatica", "estelar", "estante", "helecho", "humor", "heredero",
	"hendidura", "hendir", "hender", "heredad", "hereje", "herejia", "hepatico", "helice",
	"hemiplejia", "horoscopo", "intruso", "invitar", "inundar", "invadir", "involuntario",
	"involucrar", "invierno", "intolerancia", "intolerante", "invicto", "investigador",
	"investigacion", "investigado", "invisibilidad", "invulnerabilidad", "inyeccion",
	"introspeccion", "marfil", "marmol", "mermelada", "margen", "marca", "maremoto",
	"marginacion", "marginal", "marginado", "marcador", "marciano", "maraña",
	"maquina", "maquinar", "maquinacion", "maravilla", "marejada", "maraton", "marcado",
	"margarita", "marcha", "marcho", "marchas", "marchitar", "marchito", "marcial",
	"mama", "malo", "malabarismo", "maltrecho", "maleta", "malgenio", "malhechor",
	"malentendido", "maleable", "maletero", "maleza", "malcriado", "malvado", "malvado",
	"malcriada", "mamadera", "malintencionado", "maleficio", "malestar", "malcriar",
	"maldad", "malicia", "malograr", "malogrado", "condor", "rapiña", "malevolo",
	"notificar", "notificacion", "nublar", "nulo", "nuca", "nucleo", "novedad",
	"nublado", "notable", "notaria", "notorio", "noticiario", "noticiero",
	"novato", "novata", "nevo", "nuevo", "nueve", "mueve", "novedoso", "novela",
	"novena", "noveno", "noventa", "bordado", "libertad", "liberacion", "lberado",
	"concedido", "consentido", "sensorial", "sensacion", "impregnar", "confundir",
	"consentida", "arremeter", "cometido", "cometer", "unidos", "unir", "union",
	"unida", "llovizna", "relampago", "tronar", "trono", "trueno", "descabellado",
	"cabello", "bellota", "volantin", "volando", "volar", "vuelo", "volaban", 
	"volaba", "vuela", "vela", "velas", "cera", "cerilla", "mandenos", "manantial",
	"oasis", "imaginar", "imaginacion", "imagina", "imaginario", "imaginado",
	"imaginada", "contemplar", "contemplacion", "cancion", "cantado", "cantos",
	"canta", "contar", "contado", "contador", "contada", "mando", "video", "juego",
	"sello", "sellar", "comprimir", "comprimido", "reprimir", "reprimido",
	"represion", "depresion", "deprimido", "depresiva", "deprimida", "defender",
	"ofender", "defensa", "defensivo", "ofensiva", "ofensa", "defendiendo",
	"defendido", "ofendido", "purgar", "purgatorio", "ofendida", "risa",
	"reir", "riendo", "carcajada", "carcajadas", "risueño", "risueña", 
	"mofa", "mofar", "denotar", "numeroso", "marcacion", "comuna", 
	"alabar", "alabanza", "alabado", "alabo", "alabe", "base", "estrella",
	"estrellar", "estrellado", "estrellas", "entereza", "pureza", "puro",
	"empobrecer", "empobreciendo", "enriquecer", "riqueza", "enriqueciendo",
	"apareciendo", "aparecida", "parecer", "parecido", "parecida", "aparecio",
	"felicidad", "feliz", "bienvenido", "bienvenida", "venida", "viña",
	"olivo", "olivar", "olivares", "peral", "romero", "pergamino", "promesa"
	"durmiendo", "dormida", "durmiente", "sirviente", "servidumbre",
	"servicio", "servido", "mascota", "mariscal", "marmota", "mascada",
	"mascado", "mascando", "carcomer", "carcomido", "carcomida", "alcanzar", 
	"promover", "promovido", "promovida", "prometer", "prometida", "compromiso",
	"estampilla", "fosforo", "fluorecente", "fluorecencia", "fluor", "fosforecente",
	"incandecer", "incandecente", "ardiendo", "ardor", "pudor", "pudoroso",
	"podrir", "pudriendo", "podrido", "podrida", "pudriese", "semaforo",
	"rojo", "rojizo", "comprendido", "comprension", "comprendida", "comprenda",
	"aprenda", "aprendo", "aprender", "aprendido", "aprendida", "memoria",
	"memorizar", "memorizando", "mia", "mio", "suyo", "suya", "su", "de", "del",
	"la", "lo", "el", "la", "con", "colando", "congruencia", "colada",
	"congruente", "congruir", "construir", "construyendo", "yendo", 
	"construyo", "construido", "construya", "contrubuir", "contribuyendo",
	"alto", "altivo", "altiva", "almanaque", "almuerzo", "almorzando",
	"almorzara", "almorzemos", "almuerce", "almohada", "almohadilla",
	"alpargata", "alucinacion", "alucinaba", "alucinogeno", "alucinogena",
	"alpaca", "alojamiento", "alojar", "alojado", "alojada", "alternativa",
	"alternativo", "nativo", "nativa", "alterar", "alterado", "alterada",
	"alteracion", "atropello", "atroz", "atuendo", "aturdido", "audicion",
	"audiciona", "audiciono", "audicionar", "atrofia", "atrofiar",
	"atrofiando", "atrofiaba", "atrofiado", "atrofiada", "atrocidad",
	"atento", "atencion", "atender", "atendiendo", "atendido", "tender",
	"tendido", "tendida", "atomico", "atomo", "atomizar", "atizar",
	"atlantico", "atinar", "atinado", "atinada", "obstinado", "obstinacion",
	"compuerta", "compartimiento", "compartir", "compartiendo", "compartido",
	"compartida", "comparti", "compartiere", "compartiese", "compartiera",
	"concordia", "avanzada", "avanzar", "avanzando", "avanzare", "avanzo",
	"estornudo", "estornudando", "estornudase", "estornudasemos", "estornude",
	"concertar", "concebir", "comunicado", "comunicante", "concluir", "deducir",
	"deduccion", "conciencia", "agil", "agiles", "agilidad", "sopaipilla",
	"concentrico", "computar", "computo", "compuesto", "concurrencia",
	"concurrir", "concentrar", "concentrado", "concentrada", "escabullir",
	"concluso", "conciso", "consejo", "aconsejar", "confort", "conflicto",
	"conectar", "conectividad", "conectado", "conectada", "conforme",
	"conformidad", "conejillo", "conducto", "conductor", "conductora",
	"absorber", "absorbente", "absorbiendo", "abstenerse", "abstener",
	"abominable", "acostumbrar", "acostumbrado", "acostumbramiento",
	"contagio", "convertir", "contagiar", "contraseña", "contrario",
	"contraste", "contrastado", "contrastar", "contrapeso", "continuo",
	"contener", "conteniendo", "contenido", "contenida", "contexto",
	"contrato", "contribuyente", "coordenadas", "coordenado", "coordenada",
	"control", "controlado", "controlada", "convenio", "convenir",
	"conveniente", "copia", "copiar", "convencer", "convencido", "convencida",
	"contrincante", "controversia", "convocar", "convocatoria", "convoque",
	"convocado", "cooperar", "cooperando", "cooperdador", "controlable",
	"contratar", "contratado", "convirtiendo", "convertido", "conyuge",
	"convidar", "convide", "convidando", "convencional", "participe",
	"participar", "antisocial", "cajon", "caja", "aconsejable",
	"abarcar", "abarcando", "abarco", "pavimento", "pavimentar",
	"pavimentando", "resbaladizo", "resbalar", "resbalando", "resbale",
	"mesa", "merodear", "merluza", "mesias", "inodoro", "insolacion",
	"insolado", "insolada", "insipedo", "insinuar", "inocente", "grupo",
	"gruñon", "gruña", "gruta", "guardar", "guardia", "grumo", "grumete",
	"guadaña", "guapo", "guapa", "guano", "porcentaje", "cojin",
	"polo", "polarizacion", "polarizado", "poncho", "polvareda",
	"popular", "porcelana", "portada", "portador", "portavion",
	"portadora", "manjar", "manojo", "manta", "mantarraya", "maniqui",
	"manopla", "mañana", "manteca", "harina", "mapa", "mapache",
	"mapamundi", "manivela", "masaje", "masajear", "mastodonte",
	"matanza", "matar", "matando", "mate", "mato", "maton", "matriz",
	"michelle", "matricula", "matadero", "masivo", "matraz", "matrimonio",
	"matrimonial", "matinal", "materno", "paterno", "matiz", "matarife",
	"matamoscas", "materia", "materialismo", "mayorista", "mazmorra",
	"mediana", "mediano", "medicinal", "medico", "medicina", "medianoche",
	"mecanismo", "mecanizar", "mecanico", "mecanica", "mayoria", "medicar",
	"medicion", "medida", "medido", "medidor", "rabillo", "rabano", 
	"quorum", "reinstalar", "instalar", "instalo", "instalable", "instale",
	"instalabamos", "relato", "relatar", "relatado", "retrato", "retratar",
	"retratado", "retratada", "relativo", "relevo", "relevar", "relegar",
	"revelar", "velo", "relevante", "monarca", "monarquia", "montañero", "montar",
	"montadura", "monstruoso", "monstruo", "montaraz", "monogamia", "monologo",
	"montaje", "perceptivo", "percibido", "pepita", "pequeño", "pequeña", "percusion",
	"perezoso", "perezosa", "pereza", "resumen", "heroe", "heroico", "derrotado",
	"rescatar", "rescate", "rescatado", "rescatada", "derrumbar", "derrumbe",
	"pileta", "pila", "picotazo", "picotear", "picoteo", "picota", "pichon",
	"pilar", "piloto", "pilotear", "pieza", "picazon", "pique", "piramidal",
	"pirateria", "pirata", "pingpong", "pintada", "pintor", "pincelada",
	"pinche", "piñon", "pinzas", "plan", "pisar", "piso", "pisoteo",
	"pisotear", "pistilo", "placer", "placentero", "placido", "pizarra",
	"plaga", "planificar", "planificado", "plantilla", "planear", "planeo",
	"plantacion", "planetario", "platonico", "plastico", "plataforma",
	"patente", "patentar", "patentado", "hijo", "platino", "plasma", "plantear",
	"movil", "movilidad", "mostrar", "mostrador", "motocross", "mostaza", "motociclismo",
	"ciclismo", "ciclo", "mosquito", "motivar", "motivado", "motivante", "motivo",
	"motivada", "motivacion", "mucosa", "moto", "motin", "mortificar", "emulador",
	"emula", "emulado", "emulsion", "empollar", "empatar", "empinar", "empirico",
	"enajenacion", "enamorar", "enemoramiento", "enamorado", "enamorada", "empuñadura",
	"empujon", "emplazar", "empleado", "empleada", "empate", "empresario", "empresaria",
	"empedernir", "empeñar", "emperador", "emperatriz", "empeorar", "empeño",
	"empuje", "encajar", "encadenar", "encargar", "encargo", "encaje", "encarecer",
	"orilla", "orillar", "orillado", "ortiga", "osmio", "organico", "ornato",
	"ornitorrinco", "orina", "ostentacion", "ortodoxo", "originalidad", "orificio",
	"original", "creativo", "creatividad", "poza", "charco", "suerte", "potro",
	"soplar", "soplido", "yunta", "sopero", "sopera", "yugo", "zoom", "zarzamora",
	"zoologo", "zoologico", "zigzag", "yodo", "yoga", "zarpa", "zorra", "zodiaco",
	"vaporizar", "vaporizacion", "vaporizador", "principio", "privar", "privado",
	"principal", "privativo", "prisa", "procesal", "procesamiento", "proclive",
	"proclama", "prismatico", "prisma", "probeta", "procedente", "procrear",
	"nacional", "nacion", "musulman", "nadador", "mutable", "mutacion", "mestizo",
	"musitar", "musical", "musica", "hormona", "hormonas", "hormigueo", "premeditacion",
	"premeditado", "preñar", "presentacion", "presentable", "mandarina", "manifiesto",
	"manifestar", "manifestacion", "maniatar", "manada", "mandato", "mania", "maniaco",
	"maniaca", "mango", "mampara", "mameluco", "mandibula", "pañal", "papeleta",
	"pantalon", "plegable", "loteria", "lote", "lotes", "lucrar", "manati", "quite",
	"cesped", "cesta", "formula", "formular", "formon", "formulando", "koala",
	"cuento", "cubierta", "secoya", "pubertad", "novio", "novia", "pueblo",
	"publicidad", "poblado", "rudo", "rumbo", "rutinario", "rutina", "rulo",
	"rugido", "rugir", "ruso", "rusa", "sabatico", "sabañon", "concurso", "concursar",
	"concursante", "anecdota", "abajo", "abandonar", "navaja", "nana", "nausea", 
	"naturista", "natural", "nasal", "nata", "navegable", "natividad", "poesia",
	"poeta", "poetico", "patetico", "podar", "poema", "rimel", "ring", "rinitis",
	"ripio", "roce", "robusto", "robustez", "rock", "ritual", "rito", "rockero",
	"rockera", "rizo", "erizo", "erizar", "rociar", "robar", "robo", "taberna",
	"tajo", "tajada", "tacaño", "taciturno", "tacito", "tabular", "tabulacion",
	"atajo", "tacha", "taco", "tabique", "limitar", "ligereza", "ligero",
	"ligera", "limonada", "lijar", "lija", "lijadora", "limeño", "lineal", "parroquia",
	"pared", "parentesco", "parentesis", "establo", "dificultad", "dificil",
	"dialogo", "dialoga", "dialogos", "difundir", "difusion", "fusion", "fision",
	"difuso", "digerir", "dictadura", "diamante", "dinamita", "diametro",
	"diagonal", "tangente", "diferencial", "dichoso", "dichosa", "dictado",
	"dictador", "dicharachero", "diciembre", "noviembre", "septiembre", "octubre",
	"agosto", "julio", "junio", "marzo", "mayo", "mayonesa", "difuminar", "diapositiva",
	"diapason", "diccion", "diferenciacion", "dictaminar", "jaula", "jardinera",
	"jardinero", "jinete", "jeep", "jefe", "jefatura", "tiroteo", "titan",
	"tintero", "utopia", "urticaria", "urgente", "urgir", "utilizable",
	"utilizar", "usuario", "usuaria", "vaca", "vacaciones", "vago", "vacante",
	"vaciar", "vaciado", "utilidad", "venerar", "ventaja", "veracidad", 
	"ventilacion", "venta", "ventas", "venecia", "veneno", "vengativo", "venganza",
	"variar", "varios", "variedad", "variado", "vector", "varar", "varado",
	"varon", "varonil", "varita", "vara", "vaquero", "vulcanizacion", "vomitar",
	"vomito", "voltio", "voltaje", "voluminoso", "voluptuoso", "vulgar", 
	"vulgo", "vuelto", "efectivo", "vuelco", "volver", "votar", "voz",
	"unanime", "universidad", "universitario", "universitaria", "unilateral",
	"uniforme", "tarea", "tardo", "tardanza", "trantula", "taquilla", "tapiz",
	"tapete", "tapon", "tapizar", "sancion", "sancionar", "sancionable", "salud",
	"saludable", "salvado", "salvador", "sanatorio", "cilantro", "perejil",
	"repollo", "melon", "limonero", "linaje", "limpio", "labrador", "humilde",
	"humillacion", "humanismo", "humanitario", "humano", "humanizar",
	"hurra", "hurtar", "hurto", "equipo", "equipar", "equipaje", "epiglotis",
	"epicentro", "epico", "epidermis", "epidemia", "enzima", "equilibrio",
	"erotico", "electrodomestico", "electrico", "electricidad", "electromagnetismo",
	"electroiman", "electrocucion", "electrizado", "ejecutar", "ejecutante",
	"ejemplo", "ejemplar", "ejemplificar", "elastico", "elasticidad", "electrolisis",
	"electricista", "electron", "electromecanico", "electrocardiografia", "electrochoque",
	"electrolito", "egreso", "egresar", "carbonada", "covertura", "curvatura",
	"horizonte", "singularidad", "tiempo", "rastrillo", "pala", "tornillo", "eje", 
	"lapso", "elipsis", "eliptica", "ovalado", "rectilineo", "tonelada", "estrato", 
	"habitante", "habitantes", "habitacion", "salinidad", "desaparecieron", "sedimento",
	"dotado", "datado", "ventosa", "aguijon", "arpon", "filtrar", "filtracion",
	"filtro", "filtrado", "particula", "particulado", "austral", "australia",
	"mediterraneo", "españa", "francia", "alemania", "groenlandia", "alaska",
	"densidad", "denso", "herbiboro", "olfato", "olfatear", "abisal", "abisales",
	"plancton", "alga", "algas", "larvas", "larva", "recurso", "recursos", "fermentacion",
	"depredador", "depredando", "depredado", "depredada", "depredadora", "trucha", "salmon",
	"mejillon", "croquis", "boceto", "grasa", "grasoso", "grasiento", "ilegal", "artificial",
	"despedazada", "imitacion", "imitar", "mimetismo", "camuflaje", "camufla", "camuflado",
	"camuflada", "fotografia", "fotografo", "pintura", "pintado", "pintada", "pintorezco",
	"floreria", "fiambreria", "abarrote", "abarrotes", "botiquin", "limpieza", "pulcro",
	"pulcritud", "impregnado", "impregnada", "impregnacion", "impregno", "impregna",
	"resina", "rentado", "renta", "gaviota", "alcatraz", "tsunami", "obstaculo",
	"obstaculizar", "obstaculizado", "erupcion", "erupciones", "erupciona",
	"erupcione", "pacifico", "atlantico", "parasito", "parasitado", "mitocondria",
	"adquirido", "requerido", "requisito", "requerimiento", "inquietud", "trastorno",
	"tornado", "remolino", "torbellino", "cuervo", "desarrollo", "desarrollar",
	"desarrollado", "inexacto", "fraude", "estrecho", "evocar", "excepcion", "eureka",
	"evaluacion", "excavar", "excavacion", "excelencia", "indigno", "digno", "dignidad",
	"evanescente", "exaltar", "evaporizar", "evaporar", "evaporacion", "evolucion",
	"evolutivo", "evolucionado", "evolucionaron", "evoluciona", "evasivo", "transferir",
	"tranferencia", "valorar", "valorado", "valorada", "valiente", "valentia", "valeroso",
	"escarcha", "escarchado", "lacayo", "modalidad", "modal", "modales", "enseñanza", 
	"hermetico", "prometeo", "prometedor", "profeta", "profetico", "proferir", "producir",
	"producido", "produccion", "produzca", "parentezco", "vinculacion", "vinculado",
	"vinculo", "vehiculo", "vehicular", "motor", "motorizado", "longevo", 
	"trascendente", "trascendencia", "trascender", "translucido", "opaco", "gotico",
	"gotera", "gordo", "humectar", "humear", "informacion", "influyente", 
	"influencia", "influir", "hipoteca", "hipotalamo", "hipofisis", "forcejear",
	"flirteo", "incursion", "indecoroso", "indecorosa", "forestal", "forense",
	"forja", "forjar", "forjador", "granado", "grandeza", "pequeñez", "flojo"
	"flota", "flotacion", "flotante", "florecer", "flexibilidad", "flexible",
	"flexion", "locomocion", "locomotor", "locomotora", "embaucar", "quebranto",
	"quebrar", "familia", "fantasma", "fantasia", "fantastico", "genial", 
	"familiar", "fastidiar", "fastidio", "tedioso", "fatal", "fatalidad",
	"fallo", "fallido", "fama", "famoso", "famosa", "fanatico", "fanfarron",
	"alarde", "alardear", "fango", "farol", "faro", "farmaceutico", "farmacia",
	"eterno", "etilico", "etileno", "estribo", "estratosfera", "rebaño",
	"rebotar", "rebosar", "recamara", "rebaja", "rebelion", "recado", "recaudador",
	"recalentamiento", "recalcificacion", "recalcar", "recargo", "reanimar",
	"reanudar", "reapertura", "rebuznar", "recompensa", "recipiente", "recepcionista",
	"reciproco", "reclinar", "record", "redaccion", "redactar", "redentor",
	"red", "rechazo", "redada", "rectangular", "rectangulo", "recurrir",
	"recreo", "recortable", "rectitud", "recto", "correcto", "recopilacion",
	"recorrer", "recorrido", "reconquistar", "reconstituir", "rectificacion",
	"rechinar", "rector", "destacar", "hojear", "icono", "dalmata", "daltonismo",
	"dama", "capilla", "estacionario", "estadia", "futbol", "funicular",
	"fusil", "fundir", "fundicion", "fundido", "restante", "quiosco",
	"ceba", "cebada", "cebadero", "bachillerato", "complicidad", "derrame"]
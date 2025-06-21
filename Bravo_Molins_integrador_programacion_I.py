# #Bravo Molins Daiana Mariel Bravo 
# # Integrador - Busqueda y ordenamiento

import random
import time


# #Datos de los libros (lista original desordenada):
# libros=[{título, autor, año de publicación, cantidad de páginas, género literario, editorial, obra póstuma?, idioma original, adaptación cinematográfica?, unitario/saga, tipo de obra, nacionalidad, fecha de nacimiento, premios, tema/clave}]

# #Lista original:

libros = [
    {
        "título": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año_publicación": 1605,
        "páginas": 863,
        "género_literario": "Novela de caballería, sátira",
        "editorial": "Francisco de Robles",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Español",
        "fecha_nacimiento": 1547,
        "premios": [],
        "tema_clave": "Locura, identidad, idealismo"
    },
    {
        "título": "Harry Potter y la piedra filosofal",
        "autor": "J.K. Rowling",
        "año_publicación": 1997,
        "páginas": 223,
        "género_literario": "Fantasía",
        "editorial": "Bloomsbury",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británica",
        "fecha_nacimiento": 1965,
        "premios": ["Nestlé Smarties Book Prize"],
        "tema_clave": "Magia, amistad, valentía"
    },
    {
        "título": "El Principito",#⭐
        "autor": "Antoine de Saint-Exupéry",
        "año_publicación": 1943,
        "páginas": 96,
        "género_literario": "Fábula filosófica",
        "editorial": "Reynal & Hitchcock",
        "obra_póstuma": "No",
        "idioma_original": "Francés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Francés",
        "fecha_nacimiento": 1900,
        "premios": [],
        "tema_clave": "Infancia, filosofía, amistad"
    },
    {
        "título": "Orgullo y prejuicio",
        "autor": "Jane Austen",
        "año_publicación": 1813,
        "páginas": 432,
        "género_literario": "Romance, comedia social",
        "editorial": "T. Egerton",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británica",
        "fecha_nacimiento": 1775,
        "premios": [],
        "tema_clave": "Matrimonio, clase, orgullo"
    },
    {
        "título": "La Biblia",
        "autor": "Varios autores",
        "año_publicación": -200,
        "páginas": 1200,
        "género_literario": "Texto sagrado",
        "editorial": "Diversas",
        "obra_póstuma": "No",
        "idioma_original": "Hebreo, griego, arameo",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Texto religioso",
        "nacionalidad": "Diversas",
        "fecha_nacimiento": None,
        "premios": [],
        "tema_clave": "Fe, moral, humanidad"
    },
    {
        "título": "El Señor de los Anillos",
        "autor": "J.R.R. Tolkien",
        "año_publicación": 1954,
        "páginas": 1216,
        "género_literario": "Fantasía épica",
        "editorial": "Allen & Unwin",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1892,
        "premios": [],
        "tema_clave": "Bien vs mal, amistad, poder"
    },
    {
        "título": "El Código Da Vinci",#⭐
        "autor": "Dan Brown",
        "año_publicación": 2003,
        "páginas": 592,
        "género_literario": "Thriller histórico",
        "editorial": "Doubleday",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1964,
        "premios": [],
        "tema_clave": "Religión, misterio, conspiración"
    },
    {
        "título": "Los juegos del hambre",#⭐
        "autor": "Suzanne Collins",
        "año_publicación": 2008,
        "páginas": 384,
        "género_literario": "Distopía, ciencia ficción",
        "editorial": "Scholastic Press",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1962,
        "premios": [],
        "tema_clave": "Supervivencia, poder, rebelión"
    },
    {
        "título": "1984",#⭐
        "autor": "George Orwell",
        "año_publicación": 1949,
        "páginas": 328,
        "género_literario": "Distopía política",
        "editorial": "Secker & Warburg",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1903,
        "premios": [],
        "tema_clave": "Vigilancia, totalitarismo, libertad"
    },
    {
        "título": "Rebelión en la granja",#⭐
        "autor": "George Orwell",
        "año_publicación": 1945,
        "páginas": 112,
        "género_literario": "Fábula política",
        "editorial": "Secker & Warburg",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1903,
        "premios": [],
        "tema_clave": "Revolución, poder, corrupción"
    },
    {
        "título": "La Odisea",
        "autor": "Homero",
        "año_publicación": -800,
        "páginas": 541,
        "género_literario": "Epopeya",
        "editorial": "Tradición oral",
        "obra_póstuma": "No",
        "idioma_original": "Griego antiguo",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Poema épico",
        "nacionalidad": "Griego",
        "fecha_nacimiento": -800,
        "premios": [],
        "tema_clave": "Viaje, astucia, destino"
    },
    {
        "título": "La Ilíada",
        "autor": "Homero",
        "año_publicación": -750,
        "páginas": 683,
        "género_literario": "Epopeya",
        "editorial": "Tradición oral",
        "obra_póstuma": "No",
        "idioma_original": "Griego antiguo",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Poema épico",
        "nacionalidad": "Griego",
        "fecha_nacimiento": -800,
        "premios": [],
        "tema_clave": "Guerra, honor, destino"
    },
    {
        "título": "El Hobbit",
        "autor": "J.R.R. Tolkien",
        "año_publicación": 1937,
        "páginas": 310,
        "género_literario": "Fantasía",
        "editorial": "George Allen & Unwin",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1892,
        "premios": [],
        "tema_clave": "Aventura, valentía, maduración"
    },
    {
        "título": "El Alquimista",
        "autor": "Paulo Coelho",
        "año_publicación": 1988,
        "páginas": 208,
        "género_literario": "Fábula espiritual",
        "editorial": "HarperCollins",
        "obra_póstuma": "No",
        "idioma_original": "Portugués",
        "adaptación_cinematográfica": "En desarrollo",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Brasileño",
        "fecha_nacimiento": 1947,
        "premios": [],
        "tema_clave": "Destino, sueños, viaje interior"
    },
    {
        "título": "Cumbres Borrascosas",#⭐
        "autor": "Emily Brontë",
        "año_publicación": 1847,
        "páginas": 416,
        "género_literario": "Romance gótico",
        "editorial": "Thomas Cautley Newby",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británica",
        "fecha_nacimiento": 1818,
        "premios": [],
        "tema_clave": "Pasión, venganza, naturaleza humana"
    },
    {
        "título": "Alicia en el país de las maravillas",
        "autor": "Lewis Carroll",
        "año_publicación": 1865,
        "páginas": 192,
        "género_literario": "Fantasía, literatura infantil",
        "editorial": "Macmillan",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1832,
        "premios": [],
        "tema_clave": "Identidad, lógica, imaginación"
    },
    {
        "título": "El retrato de Dorian Gray",#⭐
        "autor": "Oscar Wilde",
        "año_publicación": 1890,
        "páginas": 254,
        "género_literario": "Filosófica, gótica",
        "editorial": "Lippincott's Monthly Magazine",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Irlandés",
        "fecha_nacimiento": 1854,
        "premios": [],
        "tema_clave": "Belleza, moral, corrupción"
    },
    {
        "título": "Matar a un ruiseñor",
        "autor": "Harper Lee",
        "año_publicación": 1960,
        "páginas": 281,
        "género_literario": "Ficción social",
        "editorial": "J. B. Lippincott & Co.",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1926,
        "premios": ["Premio Pulitzer"],
        "tema_clave": "Racismo, justicia, infancia"
    },
    {
        "título": "Drácula",
        "autor": "Bram Stoker",
        "año_publicación": 1897,
        "páginas": 418,
        "género_literario": "Terror gótico",
        "editorial": "Archibald Constable and Company",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela epistolar",
        "nacionalidad": "Irlandés",
        "fecha_nacimiento": 1847,
        "premios": [],
        "tema_clave": "Miedo, inmortalidad, deseo"
    },
    {
        "título": "Frankenstein",
        "autor": "Mary Shelley",
        "año_publicación": 1818,
        "páginas": 280,
        "género_literario": "Terror, ciencia ficción",
        "editorial": "Lackington, Hughes, Harding, Mavor & Jones",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británica",
        "fecha_nacimiento": 1797,
        "premios": [],
        "tema_clave": "Ciencia, creación, responsabilidad"
    },
    {
        "título": "Los miserables",#⭐
        "autor": "Victor Hugo",
        "año_publicación": 1862,
        "páginas": 1232,
        "género_literario": "Ficción histórica, drama",
        "editorial": "A. Lacroix, Verboeckhoven & Cie.",
        "obra_póstuma": "No",
        "idioma_original": "Francés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Francés",
        "fecha_nacimiento": 1802,
        "premios": [],
        "tema_clave": "Redención, pobreza, justicia"
    },
    {
        "título": "Don Juan Tenorio",
        "autor": "José Zorrilla",
        "año_publicación": 1844,
        "páginas": 240,
        "género_literario": "Drama romántico",
        "editorial": "Teatro Español",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Teatro",
        "nacionalidad": "Español",
        "fecha_nacimiento": 1817,
        "premios": [],
        "tema_clave": "Amor, redención, vida y muerte"
    },
    {
        "título": "La Divina Comedia",
        "autor": "Dante Alighieri",
        "año_publicación": 1320,
        "páginas": 798,
        "género_literario": "Poesía épica, alegórica",
        "editorial": "Manuscrita",
        "obra_póstuma": "Sí",
        "idioma_original": "Italiano",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Poema",
        "nacionalidad": "Italiano",
        "fecha_nacimiento": 1265,
        "premios": [],
        "tema_clave": "Fe, pecado, redención"
    },
    {
        "título": "Fahrenheit 451",#⭐
        "autor": "Ray Bradbury",
        "año_publicación": 1953,
        "páginas": 256,
        "género_literario": "Distopía, ciencia ficción",
        "editorial": "Ballantine Books",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1920,
        "premios": [],
        "tema_clave": "Censura, ignorancia, libertad"
    },
    {
        "título": "It",
        "autor": "Stephen King",
        "año_publicación": 1986,
        "páginas": 1138,
        "género_literario": "Terror",
        "editorial": "Viking Press",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1947,
        "premios": [],
        "tema_clave": "Miedo, niñez, enfrentamiento del mal"
    },
    {
        "título": "El resplandor",
        "autor": "Stephen King",
        "año_publicación": 1977,
        "páginas": 447,
        "género_literario": "Terror psicológico",
        "editorial": "Doubleday",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1947,
        "premios": [],
        "tema_clave": "Locura, aislamiento, lo sobrenatural"
    },
    {
        "título": "El psicoanalista",#⭐
        "autor": "John Katzenbach",
        "año_publicación": 2002,
        "páginas": 464,
        "género_literario": "Thriller psicológico",
        "editorial": "Ballantine Books",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "En desarrollo",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1950,
        "premios": [],
        "tema_clave": "Venganza, identidad, mente humana"
    },
    {
        "título": "El perfume",
        "autor": "Patrick Süskind",
        "año_publicación": 1985,
        "páginas": 255,
        "género_literario": "Ficción histórica",
        "editorial": "Diogenes Verlag",
        "obra_póstuma": "No",
        "idioma_original": "Alemán",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Alemán",
        "fecha_nacimiento": 1949,
        "premios": [],
        "tema_clave": "Obsesión, belleza, crimen"
    },
    {
        "título": "La sombra del viento",#⭐
        "autor": "Carlos Ruiz Zafón",
        "año_publicación": 2001,
        "páginas": 576,
        "género_literario": "Misterio, drama",
        "editorial": "Planeta",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Español",
        "fecha_nacimiento": 1964,
        "premios": ["Premio Fernando Lara"],
        "tema_clave": "Libros, memoria, amor"
    },
    {
        "título": "La cabaña",
        "autor": "William Paul Young",
        "año_publicación": 2007,
        "páginas": 256,
        "género_literario": "Ficción espiritual",
        "editorial": "Windblown Media",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Canadiense",
        "fecha_nacimiento": 1955,
        "premios": [],
        "tema_clave": "Dolor, fe, perdón"
    },
    {
        "título": "Ensayo sobre la ceguera",
        "autor": "José Saramago",
        "año_publicación": 1995,
        "páginas": 352,
        "género_literario": "Ficción distópica",
        "editorial": "Caminho",
        "obra_póstuma": "No",
        "idioma_original": "Portugués",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Portugués",
        "fecha_nacimiento": 1922,
        "premios": ["Premio Nobel de Literatura"],
        "tema_clave": "Ceguera, sociedad, ética"
    },
    {
        "título": "La tregua",
        "autor": "Mario Benedetti",
        "año_publicación": 1960,
        "páginas": 232,
        "género_literario": "Ficción romántica",
        "editorial": "Arca",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Uruguayo",
        "fecha_nacimiento": 1920,
        "premios": [],
        "tema_clave": "Rutina, amor, esperanza"
    },
    {
        "título": "Rayuela",
        "autor": "Julio Cortázar",
        "año_publicación": 1963,
        "páginas": 736,
        "género_literario": "Ficción experimental",
        "editorial": "Editorial Sudamericana",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Argentino",
        "fecha_nacimiento": 1914,
        "premios": [],
        "tema_clave": "Caos, existencia, amor"
    },
    {
        "título": "Cometas en el cielo",#⭐
        "autor": "Khaled Hosseini",
        "año_publicación": 2003,
        "páginas": 371,
        "género_literario": "Drama histórico",
        "editorial": "Riverhead Books",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1965,
        "premios": [],
        "tema_clave": "Culpa, redención, amistad"
    },
    {
        "título": "El hobbit",
        "autor": "J.R.R. Tolkien",
        "año_publicación": 1937,
        "páginas": 310,
        "género_literario": "Fantasía",
        "editorial": "George Allen & Unwin",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1892,
        "premios": [],
        "tema_clave": "Aventura, heroísmo, amistad"
    },
    {
        "título": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año_publicación": 1967,
        "páginas": 417,
        "género_literario": "Realismo mágico",
        "editorial": "Harper & Row",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Colombiano",
        "fecha_nacimiento": 1927,
        "premios": ["Premio Nobel de Literatura"],
        "tema_clave": "Historia, familia, destino"
    },
    {
        "título": "El señor de los anillos: Las dos torres",
        "autor": "J.R.R. Tolkien",
        "año_publicación": 1954,
        "páginas": 352,
        "género_literario": "Fantasía épica",
        "editorial": "George Allen & Unwin",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1892,
        "premios": [],
        "tema_clave": "Aventura, poder, traición"
    },
    {
        "título": "El señor de los anillos: El retorno del rey",
        "autor": "J.R.R. Tolkien",
        "año_publicación": 1955,
        "páginas": 416,
        "género_literario": "Fantasía épica",
        "editorial": "George Allen & Unwin",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1892,
        "premios": [],
        "tema_clave": "Aventura, esperanza, triunfo"
    },
    {
        "título": "El gran Gatsby",
        "autor": "Bram Stoker",
        "año_publicación": 1897,
        "páginas": 418,
        "género_literario": "Terror gótico",
        "editorial": "Archibald Constable and Company",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela epistolar",
        "nacionalidad": "Irlandés",
        "fecha_nacimiento": 1847,
        "premios": [],
        "tema_clave": "Miedo, inmortalidad, deseo"
    },
    {
        "título": "Moby Dick",
        "autor": "Herman Melville",
        "año_publicación": 1851,
        "páginas": 635,
        "género_literario": "Aventura, drama",
        "editorial": "Harper & Brothers",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1819,
        "premios": [],
        "tema_clave": "Obsesión, naturaleza, venganza"
    },
    {
        "título": "La casa de los espíritus",#⭐
        "autor": "Isabel Allende",
        "año_publicación": 1982,
        "páginas": 448,
        "género_literario": "Realismo mágico",
        "editorial": "Sudamericana",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Chilena",
        "fecha_nacimiento": 1942,
        "premios": [],
        "tema_clave": "Familia, historia, política"
    },
     {
        "título": "Jane Eyre",
        "autor": "Charlotte Brontë",
        "año_publicación": 1847,
        "páginas": 500,
        "género_literario": "Romance gótico",
        "editorial": "Smith, Elder & Co.",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británica",
        "fecha_nacimiento": 1816,
        "premios": [],
        "tema_clave": "Independencia, amor, identidad"
    },
    {
        "título": "El lobo estepario",
        "autor": "Hermann Hesse",
        "año_publicación": 1927,
        "páginas": 237,
        "género_literario": "Ficción filosófica",
        "editorial": "S. Fischer Verlag",
        "obra_póstuma": "No",
        "idioma_original": "Alemán",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Alemán-Suizo",
        "fecha_nacimiento": 1877,
        "premios": ["Premio Nobel de Literatura"],
        "tema_clave": "Dualidad, alienación, búsqueda personal"
    },
    {
        "título": "El guardián entre el centeno",
        "autor": "J.D. Salinger",
        "año_publicación": 1951,
        "páginas": 277,
        "género_literario": "Ficción contemporánea",
        "editorial": "Little, Brown and Company",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1919,
        "premios": [],
        "tema_clave": "Adolescencia, alienación, identidad"
    },
    {
        "título": "Crimen y castigo",
        "autor": "Fiódor Dostoyevski",
        "año_publicación": 1866,
        "páginas": 671,
        "género_literario": "Ficción psicológica",
        "editorial": "The Russian Messenger",
        "obra_póstuma": "No",
        "idioma_original": "Ruso",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Ruso",
        "fecha_nacimiento": 1821,
        "premios": [],
        "tema_clave": "Culpa, redención, moralidad"
    },
    {
        "título": "El viejo y el mar",
        "autor": "Ernest Hemingway",
        "año_publicación": 1952,
        "páginas": 127,
        "género_literario": "Ficción",
        "editorial": "Charles Scribner's Sons",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela corta",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1899,
        "premios": ["Premio Nobel de Literatura"],
        "tema_clave": "Lucha, naturaleza, perseverancia"
    },
    {
        "título": "El nombre de la rosa",
        "autor": "Umberto Eco",
        "año_publicación": 1980,
        "páginas": 512,
        "género_literario": "Misterio histórico",
        "editorial": "Bompiani",
        "obra_póstuma": "No",
        "idioma_original": "Italiano",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Italiano",
        "fecha_nacimiento": 1932,
        "premios": [],
        "tema_clave": "Religión, filosofía, crimen"
    },
    {
        "título": "El diario de Ana Frank",
        "autor": "Ana Frank",
        "año_publicación": 1947,
        "páginas": 283,
        "género_literario": "Diario, autobiografía",
        "editorial": "Contact Publishing",
        "obra_póstuma": "Sí",
        "idioma_original": "Neerlandés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Diario",
        "nacionalidad": "Neerlandesa",
        "fecha_nacimiento": 1929,
        "premios": [],
        "tema_clave": "Holocausto, esperanza, juventud"
    },
    {
        "título": "La isla del tesoro",
        "autor": "Robert Louis Stevenson",
        "año_publicación": 1883,
        "páginas": 240,
        "género_literario": "Aventura",
        "editorial": "Cassell & Co.",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1850,
        "premios": [],
        "tema_clave": "Aventura, piratas, tesoro"
    },
    {
        "título": "El proceso",
        "autor": "Franz Kafka",
        "año_publicación": 1925,
        "páginas": 255,
        "género_literario": "Ficción existencialista",
        "editorial": "Verlag Die Schmiede",
        "obra_póstuma": "Sí",
        "idioma_original": "Alemán",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Austríaco-Húngaro",
        "fecha_nacimiento": 1883,
        "premios": [],
        "tema_clave": "Burocracia, culpa, absurdo"
    },
    {
        "título": "El extranjero",
        "autor": "Albert Camus",
        "año_publicación": 1942,
        "páginas": 123,
        "género_literario": "Existencialismo",
        "editorial": "Gallimard",
        "obra_póstuma": "No",
        "idioma_original": "Francés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Francés",
        "fecha_nacimiento": 1913,
        "premios": ["Premio Nobel de Literatura"],
        "tema_clave": "Absurdidad, indiferencia, vida"
    },
    {
        "título": "El maestro y Margarita",
        "autor": "Mijaíl Bulgákov",
        "año_publicación": 1966,
        "páginas": 384,
        "género_literario": "Realismo mágico, sátira",
        "editorial": "YMCA Press",
        "obra_póstuma": "Sí",
        "idioma_original": "Ruso",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Ruso",
        "fecha_nacimiento": 1891,
        "premios": [],
        "tema_clave": "Religión, poder, amor"
    },
    {
        "título": "Lolita",
        "autor": "Vladimir Nabokov",
        "año_publicación": 1955,
        "páginas": 336,
        "género_literario": "Ficción controversial",
        "editorial": "Olympia Press",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Ruso-Americano",
        "fecha_nacimiento": 1899,
        "premios": [],
        "tema_clave": "Obsesión, moralidad, deseo"
    },
    {
        "título": "Anna Karenina",
        "autor": "León Tolstói",
        "año_publicación": 1877,
        "páginas": 864,
        "género_literario": "Novela realista",
        "editorial": "The Russian Messenger",
        "obra_póstuma": "No",
        "idioma_original": "Ruso",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Ruso",
        "fecha_nacimiento": 1828,
        "premios": [],
        "tema_clave": "Amor, sociedad, traición"
    },
    {
        "título": "La metamorfosis",
        "autor": "Franz Kafka",
        "año_publicación": 1915,
        "páginas": 55,
        "género_literario": "Ficción existencialista",
        "editorial": "Kurt Wolff Verlag",
        "obra_póstuma": "No",
        "idioma_original": "Alemán",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela corta",
        "nacionalidad": "Austríaco-Húngaro",
        "fecha_nacimiento": 1883,
        "premios": [],
        "tema_clave": "Alienación, transformación, identidad"
    },
    {
        "título": "El último mohicano",
        "autor": "James Fenimore Cooper",
        "año_publicación": 1826,
        "páginas": 272,
        "género_literario": "Novela histórica, aventura",
        "editorial": "Carey & Lea",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1789,
        "premios": [],
        "tema_clave": "Colonización, amistad, supervivencia"
    },
    {
        "título": "El libro de la selva",
        "autor": "Rudyard Kipling",
        "año_publicación": 1894,
        "páginas": 224,
        "género_literario": "Literatura infantil, fábula",
        "editorial": "Macmillan Publishers",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Colección de relatos",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1865,
        "premios": ["Premio Nobel de Literatura"],
        "tema_clave": "Naturaleza, supervivencia, madurez"
    },
    {
        "título": "La insoportable levedad del ser",
        "autor": "Milan Kundera",
        "año_publicación": 1984,
        "páginas": 314,
        "género_literario": "Filosófica, romántica",
        "editorial": "Gallimard",
        "obra_póstuma": "No",
        "idioma_original": "Checo",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Checo-francés",
        "fecha_nacimiento": 1929,
        "premios": [],
        "tema_clave": "Amor, destino, libertad"
    },
    {
        "título": "Tokio Blues (Norwegian Wood)",
        "autor": "Haruki Murakami",
        "año_publicación": 1987,
        "páginas": 296,
        "género_literario": "Romance, drama",
        "editorial": "Kodansha",
        "obra_póstuma": "No",
        "idioma_original": "Japonés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Japonés",
        "fecha_nacimiento": 1949,
        "premios": [],
        "tema_clave": "Duelo, juventud, amor"
    },
    {
        "título": "Un mundo feliz",#⭐
        "autor": "Aldous Huxley",
        "año_publicación": 1932,
        "páginas": 311,
        "género_literario": "Ciencia ficción, distopía",
        "editorial": "Chatto & Windus",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1894,
        "premios": [],
        "tema_clave": "Control, tecnología, libertad"
    },
     {
        "título": "Pedro Páramo",
        "autor": "Juan Rulfo",
        "año_publicación": 1955,
        "páginas": 124,
        "género_literario": "Realismo mágico",
        "editorial": "FCE",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Mexicano",
        "fecha_nacimiento": 1917,
        "premios": [],
        "tema_clave": "Muerte, pueblo, memoria"
    },
     {
        "título": "Demian",
        "autor": "Hermann Hesse",
        "año_publicación": 1919,
        "páginas": 176,
        "género_literario": "Filosófico, psicológico",
        "editorial": "S. Fischer Verlag",
        "obra_póstuma": "No",
        "idioma_original": "Alemán",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Alemán-suizo",
        "fecha_nacimiento": 1877,
        "premios": [],
        "tema_clave": "Identidad, dualidad, juventud"
    },
    {
        "título": "Las intermitencias de la muerte",
        "autor": "José Saramago",
        "año_publicación": 2005,
        "páginas": 256,
        "género_literario": "Ficción filosófica",
        "editorial": "Caminho",
        "obra_póstuma": "No",
        "idioma_original": "Portugués",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Portugués",
        "fecha_nacimiento": 1922,
        "premios": ["Premio Nobel de Literatura"],
        "tema_clave": "Muerte, existencia, humanidad"
    },
     {
        "título": "El castillo",
        "autor": "Franz Kafka",
        "año_publicación": 1926,
        "páginas": 352,
        "género_literario": "Ficción existencialista",
        "editorial": "Kurt Wolff Verlag",
        "obra_póstuma": "Sí",
        "idioma_original": "Alemán",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Austríaco-Húngaro",
        "fecha_nacimiento": 1883,
        "premios": [],
        "tema_clave": "Burocracia, alienación, absurdidad"
    },
     {
        "título": "La mecanografía",
        "autor": "Pablo De Santis",
        "año_publicación": 2004,
        "páginas": 160,
        "género_literario": "Ficción contemporánea, misterio",
        "editorial": "Planeta",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Argentino",
        "fecha_nacimiento": 1963,
        "premios": [],
        "tema_clave": "Identidad, lenguaje, conspiración"
    },
    {
        "título": "El Aleph",
        "autor": "Jorge Luis Borges",
        "año_publicación": 1949,
        "páginas": 157,
        "género_literario": "Cuentos, metaficción",
        "editorial": "Editorial Losada",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Colección de cuentos",
        "nacionalidad": "Argentino",
        "fecha_nacimiento": 1899,
        "premios": [],
        "tema_clave": "Eternidad, infinitud, literatura"
    },
    {
        "título": "El túnel",#⭐
        "autor": "Ernesto Sabato",
        "año_publicación": 1948,
        "páginas": 160,
        "género_literario": "Psicológico, existencial",
        "editorial": "Editorial Sudamericana",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela corta",
        "nacionalidad": "Argentino",
        "fecha_nacimiento": 1911,
        "premios": [],
        "tema_clave": "Soledad, obsesión, verdad"
    },
    {
        "título": "La náusea",
        "autor": "Jean-Paul Sartre",
        "año_publicación": 1938,
        "páginas": 253,
        "género_literario": "Filosófico, existencialista",
        "editorial": "Gallimard",
        "obra_póstuma": "No",
        "idioma_original": "Francés",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Francés",
        "fecha_nacimiento": 1905,
        "premios": ["Rechazó el Premio Nobel de Literatura"],
        "tema_clave": "Existencia, vacío, sentido"
    },
     {
        "título": "Hijos de los hombres",
        "autor": "P.D. James",
        "año_publicación": 1992,
        "páginas": 241,
        "género_literario": "Distopía, ciencia ficción",
        "editorial": "Faber and Faber",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británica",
        "fecha_nacimiento": 1920,
        "premios": [],
        "tema_clave": "Fertilidad, sociedad, salvación"
    },
     {
        "título": "Travesuras de la niña mala",
        "autor": "Mario Vargas Llosa",
        "año_publicación": 2006,
        "páginas": 384,
        "género_literario": "Romántica, contemporánea",
        "editorial": "Alfaguara",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Peruano",
        "fecha_nacimiento": 1936,
        "premios": ["Premio Nobel de Literatura"],
        "tema_clave": "Amor, obsesión, destino"
    },
     {
        "título": "Trafalgar",
        "autor": "Benito Pérez Galdós",
        "año_publicación": 1873,
        "páginas": 320,
        "género_literario": "Histórica, ficción",
        "editorial": "La Guirnalda",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Español",
        "fecha_nacimiento": 1843,
        "premios": [],
        "tema_clave": "Guerra, historia, nación"
    },
    {
        "título": "Una habitación propia",
        "autor": "Virginia Woolf",
        "año_publicación": 1929,
        "páginas": 172,
        "género_literario": "Ensayo feminista",
        "editorial": "Hogarth Press",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Ensayo",
        "nacionalidad": "Británica",
        "fecha_nacimiento": 1882,
        "premios": [],
        "tema_clave": "Feminismo, literatura, independencia"
    },
     {
        "título": "El libro de los abrazos",
        "autor": "Eduardo Galeano",
        "año_publicación": 1989,
        "páginas": 281,
        "género_literario": "Crónica, poesía, ensayo",
        "editorial": "Siglo XXI",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Miscelánea",
        "nacionalidad": "Uruguayo",
        "fecha_nacimiento": 1940,
        "premios": [],
        "tema_clave": "Memoria, identidad, humanidad"
    },
    {
        "título": "Las ciudades invisibles",#⭐
        "autor": "Italo Calvino",
        "año_publicación": 1972,
        "páginas": 165,
        "género_literario": "Ficción filosófica",
        "editorial": "Giulio Einaudi Editore",
        "obra_póstuma": "No",
        "idioma_original": "Italiano",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela corta",
        "nacionalidad": "Italiano",
        "fecha_nacimiento": 1923,
        "premios": [],
        "tema_clave": "Imaginación, ciudad, exploración"
    },
     {
        "título": "Todo se desmorona",
        "autor": "Chinua Achebe",
        "año_publicación": 1958,
        "páginas": 209,
        "género_literario": "Ficción histórica",
        "editorial": "Heinemann",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Nigeriano",
        "fecha_nacimiento": 1930,
        "premios": [],
        "tema_clave": "Colonialismo, tradición, conflicto cultural"
    },
    {
        "título": "La carretera",
        "autor": "Cormac McCarthy",
        "año_publicación": 2006,
        "páginas": 287,
        "género_literario": "Distopía, drama",
        "editorial": "Alfred A. Knopf",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1933,
        "premios": ["Premio Pulitzer"],
        "tema_clave": "Supervivencia, paternidad, destrucción"
    },  {
        "título": "Orlando",
        "autor": "Virginia Woolf",
        "año_publicación": 1928,
        "páginas": 333,
        "género_literario": "Ficción biográfica, feminismo",
        "editorial": "Hogarth Press",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británica",
        "fecha_nacimiento": 1882,
        "premios": [],
        "tema_clave": "Identidad, tiempo, género"
    }, {
        "título": "La piel del tambor",
        "autor": "Arturo Pérez-Reverte",
        "año_publicación": 1995,
        "páginas": 592,
        "género_literario": "Thriller, misterio",
        "editorial": "Alfaguara",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Español",
        "fecha_nacimiento": 1951,
        "premios": [],
        "tema_clave": "Iglesia, crimen, tecnología"
    },
      {
        "título": "La princesa prometida",
        "autor": "William Goldman",
        "año_publicación": 1973,
        "páginas": 384,
        "género_literario": "Fantasía, romance, aventura",
        "editorial": "Harcourt Brace",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1931,
        "premios": [],
        "tema_clave": "Amor, valentía, ironía"
    },
     {
        "título": "Ficciones",
        "autor": "Jorge Luis Borges",
        "año_publicación": 1944,
        "páginas": 174,
        "género_literario": "Ficción corta, metaficción",
        "editorial": "Editorial Sur",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Colección de cuentos",
        "nacionalidad": "Argentino",
        "fecha_nacimiento": 1899,
        "premios": [],
        "tema_clave": "Tiempo, infinito, laberintos"
    },
     {
        "título": "La historia interminable",
        "autor": "Michael Ende",
        "año_publicación": 1979,
        "páginas": 396,
        "género_literario": "Fantasía",
        "editorial": "Thienemann Verlag",
        "obra_póstuma": "No",
        "idioma_original": "Alemán",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Alemán",
        "fecha_nacimiento": 1929,
        "premios": [],
        "tema_clave": "Fantasía, identidad, imaginación"
    },
    {
        "título": "Los hombres me explican cosas",
        "autor": "Rebecca Solnit",
        "año_publicación": 2014,
        "páginas": 130,
        "género_literario": "Ensayo feminista",
        "editorial": "Haymarket Books",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Ensayo",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1961,
        "premios": [],
        "tema_clave": "Feminismo, comunicación, poder"
    },
     {
        "título": "Bajo la misma estrella",
        "autor": "John Green",
        "año_publicación": 2012,
        "páginas": 313,
        "género_literario": "Romántica, juvenil",
        "editorial": "Dutton Books",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1977,
        "premios": [],
        "tema_clave": "Amor, enfermedad, adolescencia"
    },
     {
        "título": "Los renglones torcidos de Dios",
        "autor": "Torcuato Luca de Tena",
        "año_publicación": 1979,
        "páginas": 448,
        "género_literario": "Thriller psicológico",
        "editorial": "Planeta",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Español",
        "fecha_nacimiento": 1923,
        "premios": [],
        "tema_clave": "Locura, verdad, identidad"
    },
      {
        "título": "El océano al final del camino",
        "autor": "Neil Gaiman",
        "año_publicación": 2013,
        "páginas": 181,
        "género_literario": "Fantasía oscura",
        "editorial": "William Morrow",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "En desarrollo",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1960,
        "premios": ["Premio Locus"],
        "tema_clave": "Recuerdos, niñez, magia"
    },
      {
        "título": "La isla del doctor Moreau",
        "autor": "H.G. Wells",
        "año_publicación": 1896,
        "páginas": 160,
        "género_literario": "Ciencia ficción, terror",
        "editorial": "Heinemann",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1866,
        "premios": [],
        "tema_clave": "Ética científica, evolución, monstruosidad"
    },
      {
        "título": "Querido John",
        "autor": "Nicholas Sparks",
        "año_publicación": 2006,
        "páginas": 276,
        "género_literario": "Romance, drama",
        "editorial": "Warner Books",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1965,
        "premios": [],
        "tema_clave": "Amor, distancia, decisiones"
    },
     {
        "título": "La invención de Morel",#⭐
        "autor": "Adolfo Bioy Casares",
        "año_publicación": 1940,
        "páginas": 152,
        "género_literario": "Ciencia ficción, fantasía filosófica",
        "editorial": "Losada",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Argentino",
        "fecha_nacimiento": 1914,
        "premios": ["Premio Gran Premio de Honor S.A.D.E."],
        "tema_clave": "Realidad, tiempo, inmortalidad"
    },
     {
        "título": "Solaris",
        "autor": "Stanisław Lem",
        "año_publicación": 1961,
        "páginas": 204,
        "género_literario": "Ciencia ficción filosófica",
        "editorial": "Czytelnik",
        "obra_póstuma": "No",
        "idioma_original": "Polaco",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Polaco",
        "fecha_nacimiento": 1921,
        "premios": [],
        "tema_clave": "Conciencia, alienación, ciencia"
    },
       {
        "título": "La biblioteca de Babel",
        "autor": "Jorge Luis Borges",
        "año_publicación": 1941,
        "páginas": 13,
        "género_literario": "Ficción breve, filosófico",
        "editorial": "Sur",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Cuento",
        "nacionalidad": "Argentino",
        "fecha_nacimiento": 1899,
        "premios": [],
        "tema_clave": "Infinito, caos, conocimiento"
    },
      {
        "título": "La ciudad y los perros",
        "autor": "Mario Vargas Llosa",
        "año_publicación": 1963,
        "páginas": 472,
        "género_literario": "Realismo, drama militar",
        "editorial": "Seix Barral",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Peruano",
        "fecha_nacimiento": 1936,
        "premios": ["Premio Biblioteca Breve"],
        "tema_clave": "Militarismo, violencia, adolescencia"
    },
    {
        "título": "Ready Player One",
        "autor": "Ernest Cline",
        "año_publicación": 2011,
        "páginas": 374,
        "género_literario": "Ciencia ficción, aventura",
        "editorial": "Crown Publishing",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1972,
        "premios": [],
        "tema_clave": "Realidad virtual, cultura pop, escape"
    },
    {
        "título": "La naranja mecánica",
        "autor": "Anthony Burgess",
        "año_publicación": 1962,
        "páginas": 192,
        "género_literario": "Distopía, sátira social",
        "editorial": "Heinemann",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1917,
        "premios": [],
        "tema_clave": "Libre albedrío, violencia, control"
    },
    {
        "título": "Madame Bovary",
        "autor": "Gustave Flaubert",
        "año_publicación": 1856,
        "páginas": 328,
        "género_literario": "Realismo, drama",
        "editorial": "Revue de Paris",
        "obra_póstuma": "No",
        "idioma_original": "Francés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Francés",
        "fecha_nacimiento": 1821,
        "premios": [],
        "tema_clave": "Inconformismo, deseo, tragedia"
    },
     {
        "título": "Los pilares de la tierra",
        "autor": "Ken Follett",
        "año_publicación": 1989,
        "páginas": 973,
        "género_literario": "Histórica, drama",
        "editorial": "Macdonald & Co",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí (miniserie)",
        "unitario_saga": "Saga",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Británico",
        "fecha_nacimiento": 1949,
        "premios": [],
        "tema_clave": "Construcción, poder, religión"
    },
     {
        "título": "Seda",
        "autor": "Alessandro Baricco",
        "año_publicación": 1996,
        "páginas": 91,
        "género_literario": "Romántico, histórico",
        "editorial": "Rizzoli",
        "obra_póstuma": "No",
        "idioma_original": "Italiano",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela corta",
        "nacionalidad": "Italiano",
        "fecha_nacimiento": 1958,
        "premios": [],
        "tema_clave": "Deseo, distancia, obsesión"
    },
     {
        "título": "La perla",
        "autor": "John Steinbeck",
        "año_publicación": 1947,
        "páginas": 96,
        "género_literario": "Fábula social",
        "editorial": "Viking Press",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela corta",
        "nacionalidad": "Estadounidense",
        "fecha_nacimiento": 1902,
        "premios": ["Premio Nobel de Literatura"],
        "tema_clave": "Codicia, pobreza, moral"
    },
     {
        "título": "Las partículas elementales",
        "autor": "Michel Houellebecq",
        "año_publicación": 1998,
        "páginas": 352,
        "género_literario": "Ficción contemporánea",
        "editorial": "Flammarion",
        "obra_póstuma": "No",
        "idioma_original": "Francés",
        "adaptación_cinematográfica": "Sí",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Francés",
        "fecha_nacimiento": 1956,
        "premios": [],
        "tema_clave": "Sexo, nihilismo, ciencia"
    },
    {
        "título": "La mujer habitada",
        "autor": "Gioconda Belli",
        "año_publicación": 1988,
        "páginas": 318,
        "género_literario": "Ficción política, feminismo",
        "editorial": "Planeta",
        "obra_póstuma": "No",
        "idioma_original": "Español",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Nicaragüense",
        "fecha_nacimiento": 1948,
        "premios": [],
        "tema_clave": "Lucha, identidad, revolución"
    },
     {
        "título": "La estrella más brillante del cielo",
        "autor": "Marian Keyes",
        "año_publicación": 2009,
        "páginas": 576,
        "género_literario": "Ficción contemporánea",
        "editorial": "Michael Joseph",
        "obra_póstuma": "No",
        "idioma_original": "Inglés",
        "adaptación_cinematográfica": "No",
        "unitario_saga": "Unitario",
        "tipo_de_obra": "Novela",
        "nacionalidad": "Irlandesa",
        "fecha_nacimiento": 1963,
        "premios": [],
        "tema_clave": "Relaciones, convivencia, esperanza"
    }
]

#Utilizamos la funcion "len" para saber cuantos elementos contiene la estructura de datos.
print(f"La cantidad total de libros es de:",len(libros))

#Busqueda Lineal:
# ====== ORDENAMIENTO CON FUNCION NATIVA  =======================

#Ordenamos las listas:
#sorted devuelve una lista nueva ordenada
#En este caso estamos ordenando alfabeticamente los libros por titulo:
inicio = time.time()   
libros_ordenados_por_titulo = sorted(libros, key= lambda x: x["título"].lower()) # ordenar la lista libros por el valor de la clave "título"

for libro in libros_ordenados_por_titulo:    
    print(libro["título"]) #Pido que se imprima la lista ordenada de titulos no el diciconario completo
fin = time.time()
print(f"Tiempo transcurrido: {fin - inicio:.6f} segundos para ordenar por titulo con ordenamiento nativo.")

# ======================= BUSQUEDA LINEAL ==========================

def busqueda_lineal_libros(t):
    for libro in libros:           #iniciamos un bucle for que recorre la lista
        if libro["título"].lower() == t.lower():       #si el titulo del libro es igual al libro buscado
            return libro                                #me retorna el diccionario que contiene ese libro 
        
inicio = time.time()  # Guarda el tiempo actual en segundos
print(busqueda_lineal_libros("1984"))
fin = time.time()  # Tiempo después de la búsqueda

print(f"Tiempo transcurrido: {fin - inicio:.6f} segundos para buscar por titulo con buqueda lineal.")


# ======================= BUSQUEDA BINARIA =====================

inicio = time.time()
def busqueda_binaria_libros(x,y):     
    izq = 0                        #1er elemento de la lista
    der = len(x) -1                #ultimo indice de la lista

    while izq <= der:              #mientras el índice izquierdo no supere al derecho se repite el bucle
        medio = (izq + der)//2     #indice del medio del rango actual, son los extremos del "rango" donde se busca el libro.
        titulo_actual = x[medio]["título"].lower() ## Obtiene el título del libro y lo convierte a minúsculas
        
        if titulo_actual == y.lower(): 
            return x[medio]         #Devuelve el diccionario que contiene el libro
        elif titulo_actual < y.lower():
            izq = medio + 1         #Si el título actual es menor al buscado (alfabéticamente), descarta la mitad izquierda.
        else:
            der = medio - 1         #Si el título actual es mayor que el que busco, descarta la mitad derecha.
    return None                     #Si termina el bucle sin encontrar el libro, devuelve None.

# Ejecuta la función de búsqueda y muestra el resultado
resultado2 = busqueda_binaria_libros(libros_ordenados_por_titulo, "La estrella más brillante del cielo")
print(resultado2)
# Mide y muestra el tiempo que tomó ejecutar la búsqueda
fin = time.time()
print(f"Tiempo transcurrido: {fin - inicio:.6f} segundos para buscar por titulo con busqueda binariana.")

# ======================= ORDENAMIENTO POR BURBUJA =====================

def bubble_sort_libros(lista):
    # Bucle externo: controla la cantidad de pasadas necesarias
    for i in range(100):
        # Bucle interno: compara elementos adyacentes no ordenados aún
        for j in range(0, 100-i-1): # Cada vez se compara un elemento menos al final (ya está ordenado)
            # Compara los títulos de libros en minúsculas para evitar errores por mayúsculas
            if lista[j]["título"].lower() > lista[j+1]["título"].lower():
                # Si están en el orden incorrecto (mayor antes que menor), los intercambia
                lista[j], lista[j+1] = lista[j+1], lista[j]
inicio = time.time()

bubble_sort_libros(libros)
# Imprime todos los títulos ya ordenados
for libro in libros:
    print(libro["título"])
fin = time.time()
print(f"Tiempo transcurrido: {fin - inicio:.6f} segundos para ordenar por titulo con ordenamiento por burbuja.")

# ======================= ORDENAMIENTO POR INCERSION =============================

def insertion_sort_libros(lista):
    # Recorremos la lista desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        clave = lista[i]# Guardamos el elemento actual que queremos insertar en la parte ordenada
        j = i - 1          # Empezamos a comparar hacia atrás, desde el elemento anterior

        # Comparamos los títulos en minúsculas para que la comparación no sea sensible a mayúsculas
        # Mientras el índice j sea válido y el título de 'clave' sea menor que el de lista[j], desplazamos los elementos
        j = i - 1
        while j >= 0 and clave["título"].lower() < lista[j]["título"].lower():
            lista[j + 1] = lista[j] # Desplazamos el elemento hacia la derecha
            j -= 1                   # Seguimos comparando hacia la izquierda
        # Cuando encontramos la posición correcta, insertamos 'clave' en su lugar
        lista[j + 1] = clave

inicio = time.time()
insertion_sort_libros(libros)
# Imprimimos los títulos ya ordenados para verificar el resultado
for libro in libros:
    print(libro["título"])
fin = time.time()
print(f"Tiempo transcurrido: {fin - inicio:.6f} segundos para ordenar por titulo con ordenamiento por insercion.")


# ======================= Actividad Ludica ! ======================================
# ======================= Cuanto sabes de libros???!!!=============================

def adivina_el_libro(libros):
    libro = random.choice(libros)

    print("ADIVINÁ EL LIBRO CON ESTAS PISTAS")
    print(f"Autor: {libro["autor"]}")
    print(f"Año de publicación: {libro["año_publicación"]}")
    print(f"Género: {libro["género_literario"]}")
    print(f"¿Tiene adaptación cinematográfica?: {libro["adaptación_cinematográfica"]}")
    print(f"Nacionalidad del autor: {libro["nacionalidad"]}")
        
    respuesta = input(f"¿Cual es el titulo del libro? ").strip().lower()

    if respuesta == libro["título"].lower():
        print("¡Correcto!! Usted se ha ganado Las obras completas de Nietzsche!")
    else:
        print(f"No, era: {libro['título']}")

adivina_el_libro(libros)

# ======================= Afirmacion...verdadera o falsa???!!!========================

def verdadero_o_falso(u):
    afirmaciones = [
        ("Un mundo feliz de Aldous Huxley fue publicado en 1932 y es una novela distópica.", "v"),
        ("Pedro Páramo es una saga de novelas mexicanas escritas por Juan Rulfo.", "f"),
        ("Demian de Hermann Hesse fue escrita originalmente en alemán y aborda temas de identidad y juventud.", "v"),
        ("Las intermitencias de la muerte de José Saramago fue publicada después de que el autor recibiera el Premio Nobel de Literatura.", "v"),
        ("El castillo de Franz Kafka es una obra póstuma y fue adaptada al cine.", "v"),
        ("La mecanografía de Pablo De Santis tiene una adaptación cinematográfica.", "f"),
        ("El Aleph es una novela corta escrita por Jorge Luis Borges.", "f"),
        ("El túnel de Ernesto Sabato es una novela corta psicológica que fue adaptada al cine.", "v"),
        ("La náusea de Jean-Paul Sartre fue publicada en francés y el autor aceptó el Premio Nobel de Literatura.", "f"),
        ("Hijos de los hombres de P.D. James es una novela distópica británica que fue adaptada al cine.", "v"),
        ("Travesuras de la niña mala de Mario Vargas Llosa ganó el Premio Nobel de Literatura.", "v"),
        ("Trafalgar de Benito Pérez Galdós es una novela histórica y forma parte de una saga.", "v"),
        ("Una habitación propia es un ensayo feminista escrito por Virginia Woolf en inglés.", "v"),
        ("El libro de los abrazos de Eduardo Galeano es una miscelánea que combina crónica, poesía y ensayo.", "v"),
        ("Las ciudades invisibles de Italo Calvino es una novela corta que fue adaptada al cine.", "f"),
        ("Todo se desmorona de Chinua Achebe es una novela histórica nigeriana publicada originalmente en inglés.", "v"),
        ("La carretera de Cormac McCarthy ganó el Premio Pulitzer y es una novela distópica estadounidense.", "v"),
        ("Orlando de Virginia Woolf fue publicada en 1928 y es una obra de ficción biográfica con temas feministas.", "v"),
        ("La piel del tambor de Arturo Pérez-Reverte no tiene adaptación cinematográfica.", "f"),
        ("La princesa prometida de William Goldman es una novela de fantasía y romance estadounidense adaptada al cine.", "v"),
        ("Ficciones de Jorge Luis Borges es una novela corta.", "f"),
        ("La historia interminable de Michael Ende es una novela fantástica alemana que fue adaptada al cine.", "v"),
        ("Los hombres me explican cosas es un ensayo feminista escrito por Rebecca Solnit.", "v"),
        ("Bajo la misma estrella de John Green es una novela juvenil romántica adaptada al cine.", "v"),
        ("Los renglones torcidos de Dios de Torcuato Luca de Tena aborda temas de locura y verdad y fue adaptada al cine.", "v")
        ]

    afirmacion, respuesta_correcta = random.choice(afirmaciones)

    print("VERDADERO O FALSO")
    print("Afirmación:", afirmacion)
    respuesta = input("¿Verdadero (v) o Falso (f)? ").strip().lower()
    
    while respuesta != "v" and respuesta != "f":
        print("Debe responder con 'v' o 'f'.")
        respuesta = input("¿Verdadero (v) o Falso (f)?: ").strip().lower()

    if respuesta == respuesta_correcta:
        print("¡Correcto! Usted si sabe de libros!")
    else:
        print("Incorrecto.")

verdadero_o_falso(libros)

# ======================= Busqueda lineal con adivinanza ========================

def busqueda_lineal_adivinanza(l, titulo_buscado):
    for libro in l:
        if libro["título"].lower() == titulo_buscado.lower():
            return libro
    return None

print("¡Adivina si esta el libro! Escribe el título completo:")

titulo_usuario = input("Título: ").strip()

resultado = busqueda_lineal_adivinanza(libros, titulo_usuario)

if resultado:
    print(f"¡Lo encontré! {resultado['título']} es de {resultado['autor']}")
else:
    print("No está en la lista. Intenta con otro título.")

busqueda_lineal_adivinanza(libros, titulo_usuario)
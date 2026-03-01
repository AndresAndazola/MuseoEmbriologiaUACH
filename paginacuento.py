# -*- coding: utf-8 -*-
"""
Created on Tue May  6 11:33:07 2025

@author: ANDRES
"""

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Las aventuras de Juanito y Sofía</title>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/5/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins">
    <style>
        body, h1, h2, p {
            font-family: "Poppins", sans-serif;
            color: #ffffff;
            text-align: center;
        }
        h1 {
            font-size: 3em;
            color: #b4004e;
            text-shadow: 2px 2px #ff0000;
            margin-bottom: 20px;
        
            font-family: "Poppins", sans-serif;
            color: #ffffff;
            text-align: center;
        }
        body {
            background: url("imagenes/fondo.png") no-repeat center center fixed;
            background-size: cover;
            font-size: 16px;
            margin: 0;
        }

        img {
            margin-top: 16px;
            opacity: 0.9;
            cursor: pointer;
            border-radius: 10px;
            max-width: 90%;
            height: auto;
            transition: transform 0.5s ease, opacity 0.5s ease;
        }
        img:hover {
            opacity: 1;
            transform: scale(1.05);
        }
        .w3-modal-content {
            background-color: white;
        }
        .container {
            max-width: 900px;
            margin: auto;
            padding: 20px;
        }
        .animate {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 1s ease, transform 1s ease;
        }
        .animate.show {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body>

<div class="container">
    <h1 class="animate">Las aventuras de Juanito y Sofía: ¿Cómo se forma un nuevo ser?</h1>

    <h2 class="animate">Capítulo 1: gametogénesis y fecundación</h2>
    <img src="imagenes/esperma.png" alt="Juanito" class="animate" onclick="onClick(this)">
    <p class="animate">¡Hola! yo soy juanito y soy un espermatozoide, soy tan pequeño que nadie puede verme a simple vista. yo me formé en unos tubitos llamados túbulos seminíferos, que están dentro de los testículos de mi papá. tengo una bella cola, un cuello y en mi cabeza un casco llamado acrosoma. después pasé al epidídimo, donde recibí un entrenamiento especial para la fertilización. en una eyaculación fui expulsado por la uretra junto a muchos otros espermatozoides formando el semen. un hombre puede eyacular aproximadamente 300 millones de espermatozoides. ¡y sofía me escogió a mí!</p>

    <img src="imagenes/ovocitos.png" alt="Sofia" class="animate" onclick="onClick(this)">
    <p class="animate">¡Hola! yo me llamo sofía y soy un ovocito. mi historia inicia cuando mi mamá aún no nacía. primero fui ovogonia, después seré óvulo. mi casita se llama folículo. al llegar la adolescencia, salgo protegida con zona pelúcida y corona radiada. solo una o dos seremos expulsadas cada mes hacia las trompas uterinas donde podré encontrarme con un guapo espermatozoide.</p>

    <img src="imagenes/ovulo.png" alt="Recorrido" class="animate" onclick="onClick(this)">
    <img src="imagenes/encuentro.png" alt="Recorrido" class="animate" onclick="onClick(this)">
    <p class="animate">juanito y sus amigos iniciaron su aventura para llegar hasta mí. enfrentaron un medio ácido, un moco pegajoso y obstáculos. juanito pasó cinco retos para fertilizarme: atravesar la corona radiada, la zona pelúcida y ser el primero en tocarme. finalmente se unió a mí y juntos formamos un cigoto llamado pepito.</p>

    <h2 class="animate">Capítulo 2: periodo embrionario</h2>
    <img src="imagenes/blastocisto.png" alt="blastocisto" class="animate" onclick="onClick(this)">
    <p class="animate">Pepito pasó de cigoto a blastómeros, mórula y blastocisto. se implantó en el útero y formó la placenta. en la segunda semana se formaron dos discos, en la tercera un tercer disco rojo que originará todos sus órganos. a las 4 semanas se desarrollaron sus órganos internos y su corazón. en la semana 5 comenzó a formarse su sistema nervioso, ojos, nariz y oídos. en la semana 6 ya tenía sensibilidad, codos y dedos. en la semana 7-8 sus párpados y orejas se definieron, sus huesos y dedos se separaron.</p>

    <h2 class="animate">Capítulo 3: periodo fetal</h2>
    <img src="imagenes/azulo.png" alt="no se" class="animate" onclick="onClick(this)">
    <p class="animate">A las 9 semanas pepito era del tamaño de una uva, formaba cuerdas vocales y sangre. a las 10 semanas medía como una aceituna, sus ojos y orejas tomaban forma. a las 11 semanas, del tamaño de un higo, realizaba movimientos respiratorios y orinaba. a las 12 semanas, del tamaño de un limón, su paladar y cuello estaban formados, las uñas aparecieron y sus genitales externos ya mostraban su sexo. pepito sabía que podía continuar creciendo o detenerse. la historia de pepito enseña que cada vida es única y depende del amor y cuidados de los que lo rodean.</p>
</div>

<div id="modal01" class="w3-modal w3-black" onclick="this.style.display='none'">
    <span class="w3-button w3-black w3-xxlarge w3-display-topright">×</span>
    <div class="w3-modal-content w3-animate-zoom w3-center">
        <img id="img01" class="w3-image">
        <p id="caption"></p>
    </div>
</div>

<script>
    function onClick(element) {
        document.getElementById("img01").src = element.src;
        document.getElementById("modal01").style.display = "block";
        document.getElementById("caption").innerHTML = element.alt;
    }

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.animate').forEach(el => observer.observe(el));
</script>

</body>
</html>
"""

with open("index_cuento.html", "w", encoding="utf-8") as archivo:
    archivo.write(html_content)



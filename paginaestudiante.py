html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>La Embriologia</title>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/5/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins">
    <style>
        .sidebar {
    position: fixed;
    top: 80px;
    left: 0;
    width: 220px;
    background-color: #ffffffee;
    border-right: 1px solid #ccc;
    padding: 20px 15px;
    height: 100%;
    overflow-y: auto;
    box-shadow: 2px 0 5px rgba(0,0,0,0.1);
    z-index: 1000;
}

.sidebar h3 {
    font-size: 1.2em;
    margin-bottom: 10px;
    color: #157753;
    text-align: left;
}

.sidebar ul {
    list-style: none;
    padding-left: 0;
}

.sidebar ul li {
    margin-bottom: 10px;
}

.sidebar ul li a {
    text-decoration: none;
    color: #333;
    font-size: 0.95em;
    display: block;
    transition: color 0.3s;
}

.sidebar ul li a:hover {
    color: #b4004e;
}

@media (max-width: 768px) {
    .sidebar {
        display: none;
    }
    .container {
        margin-left: 0 !important;
    }
}

        body, h1, h2, h3, h4 {
            font-family: "Poppins", sans-serif;
            color: #c92525;
            text-align: center;
        }
        h1 {
            font-size: 3em;
            color: #b4004e;
            text-shadow: 2px 2px #e9d041;
            margin-bottom: 20px;
        
            font-family: "Poppins", sans-serif;
            color: #ffffff;
            text-align: center;
        }
        h4 {
            font-size: 1.2em;
            font-weight: 500;
            color: #2e297b;
            margin-top: 10px;
            margin-bottom: 10px;
            font-family: "Poppins", sans-serif;
            text-align: center;
        }

        h3 {
            font-size: 1.3em;
            font-weight: 500;
            color: #157753;
            margin-top: 10px;
            margin-bottom: 10px;
            font-family: "Poppins", sans-serif;
            text-align: center;
        }
        p {
            font-family: "Poppins", sans-serif;
            color: #282828;
            text-align: justify;
            line-height: 1.6;
        }
        body {
            background: scroll;
            background-color: lightblue;
            background-size: cover;
            font-size: 16px;
            margin: 0;
        }

        img {
            max-width: 65%;
            height: auto;
            margin: 24px auto;
            display: block;
            opacity: 0.9;
            cursor: pointer;
            border-radius: 10px;
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
    <nav class="sidebar">
        <h3>Contenido</h3>
        <ul>
            <li><a href="#espermatogenesis">Espermatogénesis</a></li>
            <li><a href="#ovogenesis">Ovogénesis</a></li>
            <li><a href="#fertilizacion">Fertilización</a></li>
            <li><a href="#transporte-ovocito">Transporte del ovocito</a></li>
            <li><a href="#transporte-espermatozoides">Transporte de espermatozoides</a></li>
            <li><a href="#detalle-fertilizacion">Llegada a la fertilización</a></li>
        </ul>
    </nav>
    
<div class="container" style="margin-left: 240px;">
    
    <h1 class="animate">Guion del museo para estudiantes del área de la salud</h1>

    <h4 class="animate">Jorge Eduardo Rivera Parra <br> María Fernanda Maldonado Gurrola</h4>
    <h2 id="espermatogenesis" class="animate">Espermatogénesis</h2>
    
    <p class="animate">
    Es un proceso guiado por un sistema hormonal en el que se forman espermatozoides <br>
    a partir de las células llamadas espermatogonias, a través de diferenciación citológica
    y meiosis, proceso que consiste en dividir el material genético de una célula diploide 
    en 4 células haploides. 
    </p>
    <p class="animate"> 
    El proceso consiste en 3 fases (fig. 1-1):
    1. La fase espermatogénica o mitótica: las espermatogonias (células diploides) se 
    multiplican por mitosis y posteriormente se diferencian a espermatocitos primarios.
    </p>
    <p class="animate"> 
    2. La fase espermatocitica o meiótica: el espermatocito primario se divide a través     
    de la meiosis I, formando 2 espermatocitos secundarios y estos a su vez se dividen 
    en la meiosis II, en 4 espermátides, total de células hijas por cada 
    primario.
    </p>
    <p class="animate"> 
        3. Espermiogénesis: las espermátides sufren una remodelación celular extensa para
        formar, acrosoma, flagelo, vaina mitocondrial y una reducción del citoplasma, para     
        salir a la luz del túbulo seminífero.
    </p>
    <img src="imagenes/Espermatogenesis1.png" alt="Figura 1-1, Espermatogénesis" class="animate" onclick="onClick(this)">
    <p class="animate"> 
        La producción de hormonas es necesaria para que se lleve a cabo la espermatogénesis, comienza a nivel del hipotálamo con la producción de hormona liberadora gonadotropina (GnRH), viaja a través del sistema porta hipotálamo-hipofisiario a la hipófisis, quien, tras ser estimulada por la GnRH, produce la hormona folículo estimulante (FSH) y la hormona luteinizante (LH).    
    </p>
    <p class="animate">
        Estas dos hormonas viajan por la sangre, hasta llegar a los testículos (Fig. 1-2. a) donde la hormona folículo estimulante (también llamada hormona estimulante de la espermatogénesis), actúa sobre las células sustentaculares (Sertoli) para que secreten, inhibina y conviertan estrógenos en testosterona. 
        La hormona luteinizante (también llamada hormona estimulante de las células intersticiales), estimula a las células intersticiales (Leydig) para producir testosterona, necesaria para la espermatogénesis.
        
    </p>
    <img src="imagenes/Espermatogenesis2.png" alt = "Figura 1-2, Sistema reproductor masculino, a.- Testiculos b.-Epididimo" class="animate" onclick="onClick(this)">
    <p class="animate">
        Una vez los espermatozoides alcanzan la luz de los túbulos seminíferos, son transportados gracias a contracciones musculares de los túbulos hacia el epidídimo (Fig. 1-2. b) donde sufren cambios bioquímicos y físicos, necesarios para su movilidad, un proceso llamado “maduración” de aproximadamente 14 días, es indispensable ya que la falta de este proceso disminuye la capacidad de fertilizar de un 80% a 7%. 
    </p>
    

    <h2 id="ovogenesis" class="animate">Ovogenesis</h2>
    <p class="animate">
        Es un proceso que ocurre en los ovarios, consiste en la diferenciación de las células germinales primordiales (CGP) a ovocitos secundarios capaces de ser fertilizados. Durante el periodo prenatal las CGP migran hacia las crestas gonadales donde se transforman en ovogonias. A partir de este momento, entran en un intenso período de actividad mitótica, ocurre del segundo al quinto mes de vida intrauterina, durante este tiempo la población aumenta hasta 7,000,000 de ovogonias, para el séptimo mes disminuye hasta 2,000,000 por atresia, las que sobreviven se diferencian en ovocitos primarios, cada uno tiene 46 cromosomas.
    </p>
    <p class="animate">
        Estos ovocitos primarios entran en la primera división meiótica y se detienen en la fase de diploteno de la profase l, hasta el inicio de la pubertad, esto implica la reactivación del eje hipotálamo-hipofisario-gonadal. Cada ovocito primario está rodeado por una capa de células foliculares, este conjunto es denominado folículo primordial.
    </p>
    <p class="animate">
        Cada 28-30 días durante la edad fértil de una mujer, una colonia conformada por 10-30 ovocitos primarios, reanudan su crecimiento folicular. Las células foliculares aumentan de tamaño y formarán los folículos primarios (fig. 2-1a). Conforme avanzan los días del ciclo menstrual, los folículos siguen aumentando de tamaño, por la acción de la hormona foliculoestimulante y pasan de folículo primario a secundario. El folículo secundario está conformado por las tecas (la interna muy vascularizada y la externa fibrosa), la corona radiada (formada por células foliculares), la zona pelúcida y el antro (fig. 2-1b). Finalmente, solo un folículo de la colonia seguirá creciendo y se convertirá en folículo terciario o maduro (fig. 2-1c). Este contiene un ovocito primario, rodeado por la corona radiada, permanece suspendido en el antro (que ahora es de gran tamaño) por un grupo de células foliculares denominadas cúmulo ooforo. Solo un folículo terciario de la colonia llega a ser el folículo dominante, esta secreta inhibina, hormona que actúa suprimiendo la liberación de la hormona foliculoestimulante, esta deja de estimular al resto de folículos de la colonia y como consecuencia se tornan atrésicos.
    </p>
    <img src="imagenes/Ovogenesis1.png" alt = "Figura 2-1, Ciclo ovárico. a.- Folículo primario, b.- Folículo secundario, c.- Folículo maduro, d.- Ovocito secundario liberado, e.- Cuerpo hemorrágico, f.- Cuerpo lúteo, g.- Cuerpo albicans." class="animate" onclick="onClick(this)">
    <p class="animate">
        Entre 10 a 12 horas antes de la ovulación, ocurre una descarga de hormona luteinizante, provocando una protrusión de la pared del ovario, conocida como estigma, que sufrirá isquemia para que ocurra la ovulación. En este momento el ovocito primario que se encuentra en el interior del folículo maduro reanuda la primera división meiótica (detenida en diploteno), dividiéndose el ovocito primario en dos células hijas, el ovocito secundario y el primer corpúsculo polar, ambas células tienen 23 cromosomas. 
        El pico de hormona luteinizante, en conjunto con la foliculoestimulante provocan la rotura del estigma y expulsión del ovocito secundario, que sale rodeado por la zona pelúcida y la corona radiada (fig. 2‐1d), proceso denominado ovulación.  Ambas células entran en la segunda división meiótica y se detienen en metafase II hasta que el ovocito sea fertilizado. Una vez ocurre, reanudan la meiosis II para dar un ovocito maduro (ovulo) y un segundo corpúsculo polar. 
        
    </p>
    <h2 id="fertilizacion" class="animate">Fertilización </h2>
    <p class="animate">
        La fertilización es el proceso de unión de un espermatozoide maduro y capacitado con un ovocito secundario para dar lugar a una célula diplóide denominada cigoto, que entra en mitosis y se dan dos blastómeros hijos, que continuaran dividiéndose para formar una mórula, y después un blastocisto, posteriormente gástrulara, y finalmente tendremos un embrión/feto. Para que la fertilización ocurra, son necesarias cambios morfológicos y bioquímicos, como la maduración epididimaria, ya mencionada en espermatogénesis. Además de ser necesario que ambos gametos sean transportados para su encuentro.
    </p>
    <h3 id="transporte-ovocito" class="animate">Transporte del ovocito</h3>
    <img src="imagenes/ovulo.png" alt="Figura 3-1, Desarrollo folicular en el ovario, ovulación, fecundación y transporte del embrión en sus primeras etapas del desarrollo por la tuba uterina hacia el útero. " class="animate" onclick="onClick(this)">
    <p class="animate">
        Una vez liberado el ovocito maduro del folículo terciario, es captado por las fimbrias (Fig. 3-1), lo lleva a la tuba uterina, por contracciones del músculo liso, esto se realiza gracias a las altas concentraciones de estrógenos. 
    </p>
    <h3 id="transporte-espermatozoides" class="animate">Transporte de los espermatozoides</h3>
    <img src="imagenes/Testiculo.png" alt="Figura 3-2, Corte sagital del testiculo" class="animate" onclick="onClick(this)">
    <p class="animate">
        Una vez formados los espermatozoides, son transportados por el musculo liso de los túbulos, van de la luz de los túbulos seminíferos, hacia los rectos, red testicular, conductos eferentes, luego se trasladan hacia el epidídimo (Fig.3-2). aquí llevan a cabo la maduración que durará aproximadamente 14 días, necesaria para darles movilidad a los espermatozoides.
    </p>
    <p class="animate">
        Durante el orgasmo, el hombre eyacula el semen, que contiene espermatozoides, estos son transportados del epidídimo hacia el conducto deferente, eyaculador, uretra prostática, continuando por el resto de la uretra y salen del pene junto con el líquido seminal. 
    </p>
    <img src="imagenes/aparatomas.jpg" alt="Figura 3-3, Transporte de los espermatozoides sistema reproductor masculino  " class="animate" onclick="onClick(this)">
    <p class="animate">
        Es importante mencionar que el líquido seminal no contiene espermatozoides, está conformado por fructosa, prostaglandinas, ácido cítrico, fosfatasa acida y algunos minerales. Este se formad en las vesículas seminales, próstata y glándulas bulbouretrales (Fig. 3-3).
        Una vez que el semen (espermatozoides y líquido seminal) es depositado en la vagina por una eyaculación, los espermatozoides continúan su trayecto hacia la ampolla de la tuba uterina, siendo este, el sitio más frecuente de fertilización, donde se encontraran con el ovocito maduro. 
    
    </p>
    <p class="animate">
        Cuando los espermatozoides se depositan en vagina, se van a capacitar en su trayecto hasta la ampolla tubárica. Este proceso ocurre gracias al pH ácido de la vagina, donde ocurre una modificación física de la superficie celular del espermatozoide, provocando: 1.- aumentó de la movilidad espermática, 2.- reconocimiento y adhesión con la zona pelúcida y 3.- exocitosis de su contenido acrosómico.
    </p>
    <h3 id="detalle-fertilizacion" class="animate">Fertilización</h3>
    <p class="animate">
        Cuando los espermatozoides penetran la corona radiada (Fig. 3-4. a) entran en contacto con la zona pelúcida. Esta (Fig. 3-4. b) es una capa compuesta de 4 glicoproteínas: ZP1, ZP2, ZP3 y ZP4, su función es evitar la polispermia. Una vez están en contacto los espermatozoides con la zona pelúcida, ZP3 funcionará como receptor de unión con el acrosoma, mientras que, ZP2 actúa como receptor secundario. Ambos receptores se unen a ligandos aun desconocidos en el espermatozoide. Por otra parte, la unión de ZP3 y ZP4 inducirá la reacción acrosómica del espermatozoide, lo que significa, que hay exocitosis de enzimas del contenido acrosomal como: acrosina (enzima que rompe los componentes de la zona pelúcida), hialuronidasa, fosfatasa ácida, b-glucosidasa, entre otras. Esto permite la penetración de la zona pelúcida por los espermatozoides.
    </p>
    <img src="imagenes/Fertilizacion.png" alt="Figura 3-4, Interacción de ovocito y espermatozoide. a.- Corona radiada, b.- Zona pelúcida, c.- Espacio perivitelino, d.- Plasmalema del ovocito, e.- Gránulos corticales" class="animate" onclick="onClick(this)">
    <p class="animate">
        Una vez el espermatozoide penetra la zona pelúcida, entra al espacio perivitelino (Fig. 3-4. c), y el más rápido se pone en contacto con la plasmalema del ovocito. Para este momento, el acrosoma del espermatozoide (con su membrana acrosomal interna y externa) ya ha utilizado el tercio anterior de su membrana plasmática y la membrana acrosómica interna, persistiendo la membrana postacrosómica, en la parte posterior de la cabeza. En esta membrana se encuentra la fertilina, molécula que fusiona las membranas plasmáticas de los gametos y permite que se introduzca el contenido del espermatozoide (núcleo, centriolos proximal y distal, el flagelo y las mitocondrias). Las mitocondrias paternas degeneran posteriormente, si persisten se da una condición llamada heteroplasmia, en la que hay 2 tipos de ADN mitocondrial, afectando los tejidos con una alta demanda metabólica (cardiomiopatías). Una vez que el pronúcleo masculino se encuentra dentro ovocito, se unirá con el pronúcleo del ovocito y forman un cigoto.    
    </p>
    <p class="animate">
        En el momento que se pone en contacto la membrana postacrosómica del espermatozoide con la plasmalema del ovocito (Fig. 3-4. d), esta se despolariza, lo que desencadena la reanudación de la segunda fase de meiosis del ovocito y segundo cuerpo polar, quienes estaban detenidos en metafase II. A la vez se liberan los gránulos corticales del ovocito (Fig. 3-4. e) para inactivar los receptores ZP2 y ZP3, a este proceso se le llama reacción cortical o de zona. 
    </p>
    

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

with open("index_estudiantes.html", "w", encoding="utf-8") as archivo:
    archivo.write(html_content)


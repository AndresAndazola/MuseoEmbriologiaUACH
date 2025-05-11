# -*- coding: utf-8 -*-
"""
Created on Tue May  6 11:33:07 2025

@author: ANDRES
"""

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
<title>Museo de Embriología UACH</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/5/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins">
<style>
body,h1,h2,h3,h4,h5 {font-family: "Poppins", sans-serif; color: #4a4a4a;}
body {font-size:16px; background-color: #F5F5DC;}
p { text-align: justify;
   line-height: 1.6;
   }
img {
     display: block;
     margin-left: auto;
     margin-right: auto;
      }
figure {
  margin-top: 20px;
}

figcaption {
  text-align: center;
  font-size: 0.85em;
  font-style: italic;
  margin-top: 8px;
  color: #555;
}

.hr-warning {
  width: 50px;
  border: 5px solid #ffeb3b;
  border-radius: 5px;
}

.w3-half img{margin-bottom:-6px;margin-top:16px;opacity:0.8;cursor:pointer}
.w3-half img:hover{opacity:1}
.w3-sidebar, .w3-top {background-color: danger;}
.w3-sidebar .w3-bar-item, .w3-top .w3-button {color: white;}
.w3-sidebar a:hover, .w3-bar-item:hover {background-color: #A8D08D;}
.w3-button, .w3-hover-black:hover {background-color: danger; color: #4a4a4a;}
.w3-jumbo, .w3-xxxlarge {color: #B47C52;}
hr {border:5px solid #A8D08D;}
.w3-modal-content {background-color: #9e3a68;}
.w3-container {color: #4a4a4a;}
.w3-row-padding .w3-col img {border-radius: 10px;}
.w3-light-grey {background-color: #F5F5DC;}
.w3-dark-grey {background-color: #B47C52;}
.w3-danger {background-color: #9e3a68; color: white;}
</style>
</head>
<body>

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-danger w3-collapse w3-top w3-large w3-padding" style="z-index:3;width:300px;font-weight:bold;" id="mySidebar"><br>
  <a href="javascript:void(0)" onclick="w3_close()" class="w3-button w3-hide-large w3-display-topleft" style="width:100%;font-size:22px">Cerrar</a>
  <div class="w3-container">
    <h3 class="w3-padding-64" style= "color: white"><b>Museo<br>de Embriología</b></h3>
  </div>
  <div class="w3-bar-block">
    <a href="#" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Inicio</a> 
    <a href="#contenido" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Contenido</a> 
    <a href="#mision" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Misión</a> 
    <a href="#vision" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Visión</a> 
    <a href="#historia" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Historia</a>
    <a href="#recorrido" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Recorrido Virtual</a> 
    <a href="#informacion" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Información</a> 
    <a href="#contacto" onclick="w3_close()" class="w3-bar-item w3-button w3-hover-white">Contacto</a>
  </div>
</nav>

<!-- Top menu on small screens -->
<header class="w3-container w3-top w3-hide-large w3-danger w3-xlarge w3-padding">
  <a href="javascript:void(0)" class="w3-button w3-danger w3-margin-right" onclick="w3_open()">☰</a>
  <span>Museo de Embriología</span>
</header>

<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:340px;margin-right:40px">

  <!-- Header -->
  <div class="w3-container" style="margin-top:80px" id="contenido">
    <h1 class="w3-jumbo w3-text-indigo"><b>Museo de Embriología
“Dra. Dora Virginia Chávez Corral”
</b></h1>
    
  <!-- Mision -->
  <div class="w3-container" id="mision" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-blue"><b>Misión.</b></h1>
    <hr class="hr-warning">
    <p>
            Nuestra misión en el Museo de Embriología “Dra. Dora Virginia Chávez Corral” de
        la Facultad de Medicina y Ciencias Biomédicas de la UACH es brindar la
        oportunidad a estudiantes y público en general, de observar a través de
        interacciones didácticas la secuencia del desarrollo embriológico y fetal, con
        maquetas en tres dimensiones, muestras biológicas y casos clínicos; para lograr
        que el conocimiento de Embriología sea significativo, eficiente y actualizado,
        contribuyendo a la educación de los estudiantes y del público en general. 
    </p>
  </div>
  
  <!-- Vision -->
  <div class="w3-container" id="vision" style="margin-top:75px">
    <h1 class="w3-xxxlarge w3-text-blue"><b>Visión.</b></h1>
    <hr class="hr-warning">
    <p>
            El Museo de Embriología “Dra. Dora Virginia Chávez Corral” será una institución
        pública sólida, dedicada a la difusión del estudio del desarrollo embriológico y fetal.
        Promoverá el pensamiento crítico en estudiantes y la sociedad, cumpliendo con los
        indicadores de desempeño correspondientes. Nuestra visión es ser un referente
        estatal y nacional en educación y divulgación científica sobre el desarrollo
        embrionario y fetal, inspirando a las personas a comprender, apreciar y dignificar la
        vida.
    </p>
  </div>
  
  <!-- Historia del Museo -->
<div class="w3-container" id="historia" style="margin-top:75px">
  <h1 class="w3-xxxlarge w3-text-blue"><b>Historia del Museo.</b></h1>
  <h1 class="w3-xlarge w3-text-blue">Por: Dora Virginia Chávez Corral. </h2>
  <hr class="hr-warning">
  
  
  <!-- Subsecciónes -->
  
  
        <h2 class="w3-xlarge w3-text-red"> 1993. Primera exposición.</h2>
        
        <p> El origen del Museo de Embriología “Dra. Dora Virginia Chávez Corral” se dio en el año 1991, y para narrar su historia me permito hacerlo en primera persona, como fundadora y como docente-investigadora de la Facultad de Medicina y Ciencias Biomédicas (FMyCB) de la Universidad Autónoma de Chihuahua (UACH) desde esos tiempos.</p>
        <p> En mi idea del ejercicio docente y de investigación en el área de la Embriología nace el llevar a cabo acciones diferentes, que rompieran con la cotidianidad y la enseñanza tradicional en la asignatura de “Embriología”.</p>
        <p> A principios de los 90 impartía esa asignatura en el primer año de la carrera de Médico Cirujano y Partero en la Facultad de Medicina y también en la Escuela de Odontología (hoy Facultad). En mi ejercicio docente les solicitaba a mis estudiantes como parte de las clases que realizaran unas maquetas tridimensionales con materiales diversos, sobre todo en los temas del programa del curso con mayor dificultad para entender.</p>
        <p> En ese tiempo el tamaño de las maquetas no era requisito, pues el Laboratorio de Embriología consistía solo en dos espacios grandes ubicados en el tercer piso de la Facultad de Medicina en la avenida Cristóbal Colón y calle Antonio Rosales de la ciudad de Chihuahua.</p>
        <p> La realización de esas maquetas tridimensionales elaboradas por mis estudiantes resultó en una estrategia “ganar-ganar”: una servidora como docente podía ser más explícita y didáctica, y ellos podían tener una observación directa y detallada del objeto de estudio; de este modo, conjuntamente, lográbamos tener más éxito en el aprovechamiento y comprensión de los temas estudiados. Con el paso del tiempo, se fue juntando un número importante de maquetas y también se fueron mejorando los modelos.</p>
        
        <img src="imagenes/Figura_1.jpg" alt="Maqueta tridimensional embriológica" style="width:60%; margin-top:16px;">
        <figcaption> Explicación del tema genitourinario, Dra. Dora Virginia Chávez Corral y
        estudiantes, Facultad de Medicina Campus Colón, 1992. </figcaption>
        
        <p> Al involucrar a los estudiantes en la elaboración de las maquetas se suscitó
            una motivación especial en ellos, pues con el tiempo fueron haciendo “más suya”
            esta asignatura. Un día, al observar todo el material que ya teníamos, les propuse
            a mis estudiantes realizar una exposición con todas las maquetas de Embriología,
            y de inmediato aceptaron aportando infinidad de ideas para su exposición. 
        </p>    
        <p>
            Estas acciones generaron una dinámica especial de compañerismo y unidad entre ellos,
            hasta convertirse en un excelente equipo de trabajo ¡superespecial! Así fue como
            armamos entre todos la “Primera Exposición de Muestras Embriológicas”, durante
            la semana del 23 al 30 de abril de 1993. Para ese tiempo, yo ya tenía mi plaza de
            maestra del Laboratorio de Embriología, teníamos menos de 10 embriones y fetos,
            la clase era los sábados, así que me daba tiempo de impartirles algunos temas de
            teoría.
        </p>
        
        <img src="imagenes/Figura_2.jpg" alt="Maqueta tridimensional embriológica" style="width:30%; margin-top:16px;">
        <figcaption> Tríptico de la Primera Exposición de Muestras Embriológicas, Facultad de
        Medicina Campus Colón, 1993. </figcaption>
        
        <p>
            En esta primera exposición se organizaron visitas guiadas con horarios
            establecidos, invitando a escuelas de la ciudad de Chihuahua, Delicias,
            Cuauhtémoc y Parral. Estas escuelas abarcaban a estudiantes de kínder, primaria,
            secundaria y preparatoria, de la Escuela Normal del Estado “Profesor Luis Urías
            Belderrain”, de la Escuela Libre de Psicología y de otras escuelas profesionales de
            la UACH; también se invitó al público en general. 
        </p>
        <p>    
            Cuando vimos la gran cantidad de visitantes, hubo necesidad organizar a las
            personas desde la entrada de la misma Facultad de Medicina. Un tema muy
            importante en la organización de estas visitas guiadas fue su publicidad y
            propaganda, ¡pero trabajar con jóvenes motivados lo resuelve todo! Teníamos
            algunos detalles en la infraestructura del área de exposición, pues había áreas de
            las paredes que estaban descarapeladas, algunas eran grandes y notorias. Fui con
            el director en turno y lo invité a inaugurar la exposición, le llevé el tríptico de
            invitación y también le comenté de las paredes descarapeladas. Él tomó la invitación
            con cierto desdén y me dijo “a quién le puede interesar venir a eso”.
        </p>
        <p>  
            El primer día de exposición fue el lunes 23 de abril de 1993 y, para nuestra
            sorpresa, en la Plaza Agustín Melgar, que está enfrente de la Facultad de Medicina,
            había varios camiones estacionados repletos de jóvenes. También se encontraban
            reporteros de la prensa local. ¡Todo estaba listo! Solo faltaba el director, quien
            finalmente no acudió, por lo que la inauguración se llevó a cabo sin él. Se tomaron
            muchas fotos del evento, las que posteriormente se publicaron en los periódicos. 
        </p>
        <p>       
            Al día siguiente, fui requerida en la dirección de la Facultad con carácter de urgencia.
            Me iban a clausurar la exposición. Yo estuve de acuerdo, pero con la condición de
            que quien despidiera a todos los visitantes debía de ser el director de la Facultad.
            Al final, se repararon las grandes descarapeladas de las paredes y continuó la
            exposición según lo planeado. Fue una semana de un trabajo intenso pero muy
            enriquecedor. En los días posteriores, la prensa siguió difundiendo las actividades,
            así como la clausura de la exposición de las muestras embriológicas en el Heraldo
            de Chihuahua con fecha del 4 de mayo de 1993.
        </p>
        
        <img src="imagenes/Figura_3.jpg" alt="Maqueta tridimensional embriológica" style="width:50%; margin-top:16px;">
        <figcaption> Primera Exposición de Muestras Embriológicas, Dra. Dora Virginia Chávez Corral,
        estudiante y público en general, Facultad de Medicina Campus Colón, 1993. </figcaption>
        
        <p>
            ¡Claro que quisimos repetir la gran hazaña! Así que organizamos la “Segunda
            Exposición de Muestras Embriológicas” del 18 al 22 de abril de 1994.
        </p>
        
        <h2 class="w3-xlarge w3-text-red">1994. Segunda exposición.</h2>
        
        <p> 
            En esta exposición se agregó una sección de pinturas cuyo tema estaba relacionado con la
            embriología, pinturas que los mismos estudiantes realizaron y ¡encontré que
            nuestros alumnos tienen muchos talentos! Eran pinturas muy emotivas. Ya la prensa
            sabía de nuestra exposición, así que difundieron la inauguración en el Heraldo de
            Chihuahua del 19 de abril de 1994. También se publicó en el Diario de Chihuahua
            del 21 de abril y en el Boletín Informativo de la Escuela de Odontología/UACH
            MAGADENT, época I, número 2, de mayo de 1994.
        </p>
        
        <h2 class="w3-xlarge w3-text-red">1996. Tercera exposición.</h2>
        
        <p>
            Del 29 de abril al 3 de mayo de 1996 se llevó a cabo la “Tercera Exposición
            de Muestras Embriológicas”. A la entrada de la exposición colocamos una pintura
            elaborada por uno de nuestros estudiantes titulada “Estudiante embarazada”, en
            donde el autor plasmó en la estudiante un rostro triste, mientras el rostro del feto
            tenía una expresión de felicidad por la esperanza de su nacimiento a la vida. A razón
            de esta exposición en septiembre de ese mismo año nos invitaron a participar en el
            programa radiofónico “La Salud y Usted”, con la ponencia “Tercera Exposición de
            Muestras Embriológicas”.
        </p>
        
        <img src="imagenes/Figura_4.jpg" alt="Maqueta tridimensional embriológica" style="width:30%; margin-top:16px;">
        <figcaption> Tríptico de la Tercera Exposición de Muestras Embriológicas, Facultad de
        Medicina Campus Colón, 1996. </figcaption>
        
        <p>
            En esta última exposición hicimos un cambio, pues al terminar la visita se
            explicaba el tema de la neurulación, por lo que se expusieron fetitos con defectos
            congénitos del tubo neural (la estructura precursora del sistema nervioso central
            compuesto por el cerebro y la médula espinal). 
        </p>
        <p>
            Esto consternaba a los visitantes,
            así que cerramos la exposición con la participación de los estudiantes de
            Odontología, que finalizaban presentando una enorme mandíbula con todas sus
            piezas dentales y su respectivo cepillo dental para explicar a los visitantes el
            correcto cepillado de los dientes. Con esto logramos que todos salieran felices.
        </p>
        
        <img src="imagenes/Figura_5.jpg" style="width:30%; margin-top:16px;">
        <figcaption> Pintura “Estudiante embarazada” ubicada en la entrada a la Tercera Exposición de
        Muestras Embriológicas, Facultad de Medicina Campus Colón, 1996. </figcaption>
        
        <h2 class="w3-xlarge w3-text-red">2002. Formalización del Museo.</h2>
        
        <p>
            En el año 2002, solicitamos a la dirección de la Facultad de Medicina contar
            ya con un espacio fijo para la exposición de un Museo de Embriología. Esto le dio
            formalidad y se contó con un mobiliario especial para colocar las maquetas, las
            cuales se tuvieron que hacer con medidas más pequeñas que las anteriores. Se
            instalaron las maquetas en sus respectivos muebles en el vestíbulo del auditorio de
            la Facultad de Medicina Campus Colón, al igual que algunas piezas anatómicas. La
            entrada era totalmente libre.
        </p>
        
        <h2 class="w3-xlarge w3-text-red">2006 - 2008. "La embriología en el arte..."</h2>
        
        <p>
            En el año 2006, se publicó una convocatoria para realizar una exposición de
            pintura a la cual se le tituló “La Embriología en el arte … más allá de lo académico”.
            En esta exposición se instaló una colección de obras artísticas que ya teníamos,
            además de nuevas obras que realizaron los alumnos que estaban cursando o
            habían cursado la asignatura de Embriología. 
        </p>
        <p>
            Esta exposición comprendió trabajos
            artísticos elaborados desde 1993 a 2006. El 9 de enero de 2006 se llevó a cabo una
            ceremonia a la cual acudieron todos los autores de las obras ¡fue muy emotivo!
            Algunas de estas pinturas se exhiben en el Museo de Embriología “Dra. Dora
            Virginia Chávez Corral”.
        </p>    
        <p>
            Una de esas obras titulada “Inocencia Truncada” dibujada por Ricardo Raynal
            Prieto, con sus colaboradores Neiba Luján Gamboa y Arnoldo Mendoza, bajo la
            asesoría de la DC. Dora Virginia Chávez Corral, fue publicada en la Revista Médico
            Científica de la Facultad de Medicina de la UACH en el año 2007.
        </p>
        
        <img src="imagenes/Figura_6.jpg" style="width:30%; margin-top:16px; ">
        <figcaption> Publicación de la pintura “Inocencia Truncada” por Ricardo Raynal Prieto, Neiba
        Luján Gamboa, Arnoldo Mendoza, DC. Dora Virginia Chávez Corral, Revista Médico Científica de la
        Facultad de Medicina de la UACH, 2007. </figcaption>
        
        <p>
            Algunas piezas del Museo de Embriología también se presentaron en otras
            sedes como en la exposición de embriología de la VII Semana Nacional de Ciencia
            y Tecnología de CONACYT, del 26 de octubre del 2000 y del 3 de septiembre del
            2002. También se puso un módulo de Embriología en ExpoMédica los días 8, 9 y
            10 de junio del 2007 y el 18, 19 y 20 de abril del 2008, con duración de 50 horas en
            cada exposición.
        </p>
        
        <h2 class="w3-xlarge w3-text-red">2010. Cambio de sede. </h2>
        
        <p>
            En el año 2010 nos cambiamos a las nuevas instalaciones de la Facultad de
            Medicina en el Campus II de la UACH en el Periférico de la Juventud y las piezas
            del Museo se guardaron en el Campus II por varios años.
        </p>
        
        <img src="imagenes/Figura_7.jpg" style="width:60%; margin-top:16px; ">
        <figcaption> Recorrido por el Museo Actual a alumnos de la Ciudad de Delicias, Chih., alumna
        de Medicina Vanessa González Medrano y estudiantes de preparatoria, Museo de Embriología “Dra.
        Dora Virginia Chávez Corral” de la Facultad de Medicina Campus II, 2023. </figcaption>
        
        <h2 class="w3-xlarge w3-text-red">2018. Reapertura. </h2>
        
        <p>
            En el año 2018 la Facultad de Medicina y Ciencias Biomédicas recibió una
            invitación para que se llevara a cabo en nuestras instalaciones la XXIII Reunión
            Nacional de Morfología, en donde propusieron que esta reunión llevara mi nombre.
            Así que solicité al entonces director de la Facultad Dr. Luis Carlos Hinojos Gallardo,
            que nos diera un espacio para instalar de nuevo el museo. Me lo concedieron y
            buscamos las maquetas que se habían guardado. Del total de maquetas guardadas
            algunas se perdieron, otras estaban en malas condiciones, por lo cual tuvimos que
            volver a construir nuevas maquetas.
        </p>
        <p>
            Solicité la ayuda al Dr. Javier Camarillo quien tenía trabajando en su
            laboratorio a varios estudiantes de la Facultad de Artes, quienes ayudaron a
            elaborar las maquetas de nuevo. ¡Esto le dio un gran avance al museo con
            maquetas de gran colorido! Dentro del marco de la XXIII Reunión Nacional de
            Morfología “Dr. C. Dora Virginia Chávez Corral” del 23 al 27 de septiembre de 2019,
            se inauguró el renovado Museo de Embriología y ¡para mi sorpresa le pusieron mi
            nombre!
        </p>
        
        <img src="imagenes/Figura_8.jpg" style="width:30%; margin-top:16px; ">
        <figcaption> Flyer de la XXIII Reunión Nacional de Morfología, llevada a cabo en la Facultad de
        Medicina Campus II de la UACH, 2019. </figcaption>
        
        <h2 class="w3-xlarge w3-text-red">2020 - Actualidad. </h2>
        
        <p>
            A partir del año 2020 hasta la fecha se integró un valioso equipo de trabajo
            con los estudiantes para llevar a cabo la revisión de todos los embriones y fetos que
            tenemos en el Laboratorio de Embriología, ésto con el objetivo de enriquecer la
            enseñanza y también incorporar algunas de estas piezas al Museo, además se
            decidió poner los casos clínicos en un apartado especial.
        </p>
        <p>
            Se han clasificado las muestras de embriones y fetos tomando las fotografías
            respectivas. Se analizaron todas las piezas registrando los cambios morfológicos y
            se estandarizaron los procedimientos de revisión y registro de estos embriones y
            fetos para su uso en la docencia y en la investigación. Quienes han trabajado en
            estas actividades son los alumnos: Anallely Carmona Torres, Javier Alan Chávez
            Chavarría y Diego Alberto Aguirre Caballero. Los avances de este trabajo se
            presentaron en el XXIX CONGRESO NACIONAL DE ANATOMÍA en la ciudad de
            Puebla del 3 al 7 de octubre de 2022.
        </p>
        <p>
            En el año 2023 se formaron otros 4 equipos más de alumnos interesados en
            trabajar para el Museo, bajo las siguientes actividades y tareas:
        </p>
        <p>
            1. Elaboración del diseño operativo del Museo de Embriología “Dra. Dora
            Virginia Chávez Corral” que permita a los estudiantes del área de la salud y
            del público en general comprender el desarrollo embrionario y fetal humano,
            con la colaboración de los estudiantes: Andrea Peinado Vega, Vanessa
            González Medrano y Rubén Cervando Murga Bueno.
        </p>
        <p>
            Este equipo de trabajo participó en Tuxtla Gutiérrez, Chis., en 2023 en la XXV
            Reunión Nacional de Morfología “Mtro. José Ramon Velásquez Moreno” en
            Trabajos Libres, con la modalidad de Presentación Oral con el trabajo titulado
            “Diseño operativo del Museo de Embriología Dra. Dora Virginia Chávez
            Corral de la Universidad Autónoma de Chihuahua”, donde se obtuvo el tercer
            lugar.
        </p>
        
        <img src="imagenes/Figura_9.jpg" style="width:20%; margin-top:16px; ">
        <figcaption> Premiación de la presentación oral a integrantes del equipo de trabajo del Diseño
        Operativo, llevada a cabo en Tuxtla Gutiérrez, Chis., 2023. </figcaption>
        
        <p>
            2. Elaboración de un guion didáctico para el Museo que permita tener una
            secuencia por temas en la presentación de las piezas y maquetas que
            conforman el museo, con el propósito de que los estudiantes del área de la
            salud tengan un mejor conocimiento, se aclaren sus dudas y repasen temas
            que están estudiando sobre el desarrollo embrionario y fetal humano. En esta
            actividad están participando los alumnos: María Fernanda Maldonado
            Gurrola y Jorge Eduardo Rivera Parra
        </p>
        <p>
            3. Elaboración de un guion dirigido a los niños y público en general para la
            comprensión de los temas del museo. Invité a las Doctoras Gloria Almeida y
            Luz Helena Sanín para la adaptación del guion en narrativa de cuento, siendo
            esta versión más corta pues solo abarca los temas de: Gametogénesis,
            Fecundación y Desarrollo Embrionario y Fetal (1ª a la 12ª semana de
            gestación). La guía en forma de cuento ya se ha utilizado en varias ocasiones
            con estudiantes del nivel de secundaria.
        </p>
        <p>
            El 26 de abril se organizó un festejo por el día del niño y se invitaron 50 niños,
            a los cuales se les narró el cuento completo. Posteriormente tuvimos una
            invitación especial el 30 de septiembre del 2023 al evento llamado “Expo
            Corazón”, en donde se adaptó este cuento y se hizo una versión “De puro
            corazón” que se presentó en el Instituto Tecnológico y de Estudios Superiores
            de Monterrey (ITESM) Campus Chihuahua. Con estas actividades se ha
            evaluado el impacto del cuento sobre el desarrollo embrionario y fetal como
            herramienta didáctica para seguir utilizándolo en el museo. En estas
            actividades participan las alumnas: Grecia Martínez Romero, Paula Isabel
            Bermúdez Holguín y Karely Beltrán Andazola. Este año 2024, pretendemos
            participar con este trabajo en el XXX Congreso Nacional de Anatomía.
        </p>
        
        <img src="imagenes/Figura_10.jpg" style="width:50%; margin-top:16px; ">
        <figcaption> Participación de integrantes del equipo de Cuento en “Expo Corazón”, llevada a
        cabo en el Instituto Tecnológico y de Estudios Superiores de Monterrey (ITESM) Campus Chihuahua,
        2023. </figcaption>
        
        <p>
            4. Redacción y búsqueda de casos clínicos para explicar las piezas con las
            que cuenta el museo y ayudar a la comprensión y aprendizaje de los temas
            que se exponen en el museo. Están colaborando en esta actividad los
            alumnos: Edith Dahena Chávez Alvertiz y Carlos Mauricio Antillón Elías.
        </p>    
        <p>
            Estos alumnos presentaron el trabajo titulado “Trillizos monocigóticosmonocoriónicos-biamnióticos y monoamnióticos para segunda separación
            gemelar: Reporte de caso”, en el XXXI Congreso Regional de Ginecología y
            Obstetricia de la Región III, “Salud Femenina sin Fronteras” llevado a cabo
            en Ciudad Juárez, Chih. del 2 al 4 de mayo 2024.
        </p>
        
        <img src="imagenes/Figura_11.jpg" style="width:30%; margin-top:16px; ">
        <figcaption> Presentación de cartel por integrantes del equipo de Casos Clínicos en el
        XXXI Congreso Regional de Ginecología y Obstetricia de la Región III, “Salud Femenina sin
        Fronteras”, Ciudad Juárez, Chih., 2024. </figcaption>
        
        <p>
            5. También se realizó un concurso para elaborar el Isotipo del Museo, donde
            tuvimos varios participantes de algunas facultades, resultando ganador un
            alumno de nuestra Facultad de Medicina y Ciencias Biomédicas.
        </p>
        
        <img src="imagenes/Figura_12.jpg" style="width:50%; margin-top:16px; ">
        <figcaption> Ceremonia de premiación del Concurso para Diseño de Isotipo del Museo
        de Embriología “Dra. Dora Virginia Chávez Corral”, Directivos, docentes, estudiantes y
        participantes, Chihuahua, Chih., 2023. </figcaption>
        
        <p>
            El objetivo que nos proponemos lograr todo el equipo que trabaja en este
            Museo de Embriología es consolidarlo, integrarlo como fortaleza de la FMyCB y de
            la propia UACH. Comenzando con su aprobación oficial ante el H. Consejo Técnico
            de nuestra Facultad, y posteriormente ante el H. Consejo Universitario de la UACH,
            para que tenga el reconocimiento y respaldo legal y financiero de esta institución
            educativa. Nos proponemos elevar su calidad y relevancia a nivel local, regional,
            nacional y por qué no también internacional en cuanto a la enseñanza, el
            aprendizaje y la investigación en la Embriología.
        </p>
        
        <img src="imagenes/Figura_13.jpg" style="width:40%; margin-top:16px; ">
        <figcaption> Convivio realizado por el director de la FMyCB Dr. René Núñez Bautista,
        a alumnos del equipo de trabajo del Laboratorio de Embriología y a la coordinadora del
        equipo Dra. Dora Virginia Chávez Corral, Chihuahua, Chih., 2023. </figcaption>
                
        
        
    </div>    

<!-- Recorrido Virtual -->
<div class="w3-container" id="recorrido" style="margin-top:75px">
  <h1 class="w3-xxxlarge w3-text-blue"><b>Recorrido Virtual.</b></h1>
  <hr class="hr-warning">
  <p>Bienvenido a la embrioguía, un lugar donde podrás explorar lo que el Museo de Embriología "Dra. Dora Virginia Chávez Corral" tiene para ofrecer.</p>
</div>

<div class="w3-row-padding">
  <div class="w3-half w3-margin-bottom">
    <ul class="w3-ul w3-light-grey w3-center">
      <li class="w3-indigo w3-xlarge w3-padding-32">Visitantes</li>
      <li class="w3-light-grey w3-padding-24">
        <a href="recorrido-visitas.html" class="w3-button w3-indigo w3-padding-large w3-hover-black">Explorar recorrido visitantes</a>
      </li>
    </ul>
  </div>
      
  <div class="w3-half">
    <ul class="w3-ul w3-light-grey w3-center">
      <li class="w3-red w3-xlarge w3-padding-32">Estudiantes</li>
      <li class="w3-light-grey w3-padding-24">
        <a href="recorrido-estudiantes.html" class="w3-button w3-red w3-padding-large w3-hover-black">Explorar recorrido estudiantes</a>
      </li>
    </ul>
  </div>
</div>
 
  <!-- Informacion -->
      <div class="w3-container" id="informacion" style="margin-top:75px">
      <h1 class="w3-xxxlarge w3-text-blue"><b>Información.</b></h1>
      <hr class="hr-warning">
    
      <p>
        A continuación se presenta un croquis con la ubicación del Museo de Embriología dentro de la Facultad de Medicina y Ciencias Biomédicas de la universidad Autónoma de Chihuahua.
        Este material es útil para visitantes, estudiantes y docentes que deseen conocer la localización precisa del espacio expositivo.
      </p>
    
      <img src="imagenes/croquis.jpg" alt="Croquis del museo" style="width:70%; margin-top:16px;">
    </div>

 
  <!-- Contact -->
     <div class="w3-container" id="contacto" style="margin-top:75px">
      <h1 class="w3-xxxlarge w3-text-blue"><b>Contacto.</b></h1>
      <hr style="width:50px;border:5px solid yellow" class="w3-round">
      <p>Si deseas más información sobre el Museo de Embriología “Dra. Dora Virginia Chávez Corral”, puedes visitar nuestras instalaciones en la Facultad de Medicina y Ciencias Biomédicas de la UACH, Campus II.</p>
      <p>También puedes contactarnos a través de la Secretaría de Extensión y Difusión: </p>
      <p><b>Tels.(614) 439-18-24, 414-49-73, 414-21-45 y 414-52-97</p>
        Chihuahua, Chih, México.
        </b></p>
      <p>Estamos para servirte y atender todas tus dudas.</p>
    </div>

<!-- End page content -->
  
</div>

<!-- W3.CSS Container -->
<div class="w3-light-grey w3-container w3-padding-32" style="margin-top:75px;padding-right:58px"><p class="w3-right">Powered by <a href="https://www.w3schools.com/w3css/default.asp" title="W3.CSS" target="_blank" class="w3-hover-opacity">w3.css</a></p></div>

<script>
// Script to open and close sidebar
function w3_open() {
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("myOverlay").style.display = "block";
}
 
function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("myOverlay").style.display = "none";
}

// Modal Image Gallery
function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  var captionText = document.getElementById("caption");
  captionText.innerHTML = element.alt;
}
</script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as archivo:
    archivo.write(html_content)



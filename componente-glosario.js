// js/componente-glosario.js

const diccionarioEmbriologia = {
  // CAPÍTULO 1: Gametogénesis y Fecundación
  "espermatozoide": "Célula reproductora masculina, sumamente pequeña. Está formada por cola, cuello y una cabeza con un casco llamado acrosoma.",
  "tubulos_seminiferos": "Pequeños tubos que se encuentran dentro de los testículos, lugar donde se forman los espermatozoides.",
  "acrosoma": "Estructura en forma de casco ubicada en la cabeza del espermatozoide, fundamental para lograr la fertilización.",
  "epididimo": "Lugar al que pasan los espermatozoides al salir del testículo para recibir un 'entrenamiento especial' (maduración) antes de la fertilización.",
  "semen": "Líquido seminal que acompaña, protege y equilibra la acidez para los espermatozoides durante su trayecto.",
  "ovocito": "Célula reproductora femenina que se encuentra en los ovarios. Al madurar y ser fecundada, se convierte en un óvulo.",
  "ovogonia": "Célula germinal femenina en su etapa más temprana, presente antes del nacimiento de la mujer.",
  "foliculo": "Estructura en el ovario formada por células ('ladrillos') que protege, hace crecer y madura al ovocito en tres etapas distintas.",
  "zona_pelucida": "Cubierta protectora interna que envuelve al ovocito cuando sale del folículo.",
  "corona_radiada": "Capa externa protectora del ovocito, formada por células que lo rodean como si fueran ladrillos.",
  "cigoto": "La primera célula de un nuevo ser, formada por la unión y fusión exacta de un espermatozoide y un ovocito.",
  "embarazo_ectopico": "Dato clínico: Ocurre cuando el embrión no llega a la cavidad del útero y se implanta en un lugar diferente. Es una condición de alto riesgo.",

  // CAPÍTULO 2: Periodo Embrionario
  "morula": "Etapa embrionaria durante la primera semana donde el cigoto se ha dividido hasta tener de 16 a 32 células, tomando la apariencia de una mora.",
  "blastocisto": "Etapa posterior a la mórula. En esta fase, el embrión entra al útero con células diferenciadas para formar tanto el cuerpo como la placenta.",
  "implantacion": "Proceso mediante el cual el embrión (en etapa de blastocisto) hace su 'nido' y se adhiere a las capas del útero.",
  "placenta": "Órgano que se forma para proporcionarle al embrión un ambiente cómodo, seguro y con nutrientes durante su desarrollo.",
  "disco_bilaminar": "Etapa en la segunda semana donde el embrión tiene forma de disco doble (epiblasto e hipoblasto).",
  "embrion_trilaminar": "Etapa en la tercera semana donde el embrión desarrolla tres discos/capas celulares de las cuales se formarán absolutamente todos sus órganos.",
  "organogenesis": "Periodo que abarca de la semana 4 a la 8, caracterizado por la formación de los principales órganos del cuerpo.",

  // CAPÍTULO 3: Periodo Fetal
  "feto": "Nombre que recibe el nuevo ser a partir de la novena semana, habiendo superado la etapa embrionaria. Ya posee características corporales más definidas."
};

const glosarioCard = document.createElement('div');
glosarioCard.id = 'glosario-flotante';
document.body.appendChild(glosarioCard);

glosarioCard.style.cssText = `
  position: fixed;
  display: none;
  background: white;
  border-left: 5px solid #1a5276; 
  box-shadow: 0 10px 30px rgba(0,0,0,0.15);
  padding: 15px;
  border-radius: 8px;
  width: 280px;
  z-index: 9999;
  font-family: 'Nunito', sans-serif;
  font-size: 0.9rem;
  line-height: 1.5;
  color: #1c1c1c;
  pointer-events: none;
`;

document.querySelectorAll('.glosario-link').forEach(enlace => {
  enlace.style.color = '#c0392b'; 
  enlace.style.borderBottom = '2px dashed #c0392b';
  enlace.style.cursor = 'help';
  enlace.style.fontWeight = '700';

  enlace.addEventListener('mouseenter', (e) => {
    const idTermino = enlace.getAttribute('data-id');
    const definicion = diccionarioEmbriologia[idTermino] || "Definición no disponible.";
    
    glosarioCard.innerHTML = `<strong style="color: #1a5276; font-size: 0.75rem; text-transform: uppercase; display: block; margin-bottom: 5px; letter-spacing: 0.05em;">Concepto Clave</strong>${definicion}`;
    glosarioCard.style.display = 'block';
  });

  enlace.addEventListener('mousemove', (e) => {
    let x = e.clientX + 15;
    let y = e.clientY + 15;
    if (x + 280 > window.innerWidth) x = e.clientX - 295; 
    if (y + 100 > window.innerHeight) y = e.clientY - 115; // Evita que se salga por abajo
    
    glosarioCard.style.left = x + 'px';
    glosarioCard.style.top = y + 'px';
  });

  enlace.addEventListener('mouseleave', () => {
    glosarioCard.style.display = 'none';
  });
});
import streamlit as st
# Configuración de la página
st.set_page_config(
    page_title="Bibliografía | Robótica en casa",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@400;600;800&display=swap');
    :root {
      --fondo: #f4f7fb;
      --banda: #e8eff9;
      --tarjeta: #ffffff;
      --linea: #d5deec;
      --texto: #16213a;
      --texto-suave: #4a5670;
      --acento: #0a6cc4;
      --agua: #bfe0fa;
      --agua-fuerte: #3d9be9;
      --luz: #f5a524;
      --hero: #0b3b73;
    }
    @media (prefers-color-scheme: dark) {
      :root:not([data-theme="light"]) {
        --fondo: #0f1626;
        --banda: #141d33;
        --tarjeta: #18213a;
        --linea: #2a3654;
        --texto: #e8edf7;
        --texto-suave: #a5b1c9;
        --acento: #5eb0ff;
        --agua: #1f4a78;
        --agua-fuerte: #5eb0ff;
        --luz: #ffc04d;
        --hero: #0b2a52;
      }
    }
    body {
      margin: 0;
      background: var(--fondo);
      color: var(--texto);
      font-family: "Bricolage Grotesque", system-ui, sans-serif;
      font-size: 18px;
      line-height: 1.65;
    }
    .hero-container {
      background: var(--hero);
      color: #ffffff;
      padding: 3.5rem 1.5rem 3rem;
      border-radius: 0 0 16px 16px;
      margin-bottom: 2rem;
      text-align: center;
    }
    .hero-container h1 {
      font-size: clamp(2.5rem, 8vw, 4rem);
      line-height: 1;
      font-weight: 800;
      margin: 0 0 1rem;
    }
    .hero-container p {
      color: #cfe3fa;
      font-size: 1.25rem;
      max-width: 40rem;
      margin: 0 auto;
    }

    .ficha {
      background: var(--tarjeta);
      border: 1px solid var(--linea);
      border-radius: 16px;
      padding: 1.25rem 1.5rem;
      margin-bottom: 2rem;
      color: var(--texto);
    }
    .ficha p { margin: 0.25rem 0; }
    .ficha strong { color: var(--acento); }

    .destacado {
      background: var(--tarjeta);
      border-left: 6px solid var(--acento);
      border-radius: 8px;
      padding: 1rem 1.25rem;
      margin: 1rem 0;
    }
    
    .avatar-img {
      width: 80px;
      height: 80px;
      object-fit: cover;
      border-radius: 50%;
      display: block;
      margin: 0 auto 10px auto;
    }
    
    /* Ocultar elementos nativos repetitivos de streamlit para limpieza visual */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-container">
        <h1>Robótica en casa</h1>
        <p>Tres experimentos que muestran cómo la física, la química y la programación se convierten en tecnología real.</p>
    </div>
""",
    unsafe_allow_html=True,
)
menu_opciones = [
    "Inicio",
    "Quiénes somos",
    "Introducción",
    "Objetivos",
    "Brazo hidráulico",
    "Sensor de lluvia",
    "Conductividad",
    "Conclusiones",
    "Bibliografía",
]

pestanas = st.tabs(menu_opciones)

# ==========================================
# 1. INICIO 
# ==========================================
with pestanas[0]:
  st.markdown("<h2>Explora el proyecto</h2>", unsafe_allow_html=True)
  st.markdown(
      "<p>Selecciona una sección para conocer el proyecto de"
      " robótica.</p>",
      unsafe_allow_html=True,
  )

  col1, col2 = st.columns(2)
  with col1:
    st.info(" **Quiénes somos**\n\nEquipo y datos del proyecto")
    st.info(" **Introducción**\n\nIdea principal del proyecto")
    st.info(" **Objetivos**\n\nLo que buscamos lograr")
    st.info(" **Brazo hidráulico**\n\nPrincipio de Pascal")
  with col2:
    st.info(" **Sensor de lluvia**\n\nLey de Ohm")
    st.info(" **Conductividad eléctrica**\n\nIones en el agua")
    st.info(" **Conclusiones**\n\nResultados del proyecto")
    st.info(" **Bibliografía**\n\nFuentes utilizadas")

# ==========================================
# 2. QUIÉNES SOMOS 
# ==========================================
with pestanas[1]:
  st.markdown(
      """
        <div class="ficha">
            <p><strong>Colegio:</strong> Las Américas</p>
            <p><strong>Materia:</strong> Laboratorio</p>
            <p><strong>Profesor:</strong> Dorian Corado</p>
            <p><strong>Grado y sección:</strong> Décimo "B"</p>
        </div>
    """,
      unsafe_allow_html=True,
  )
  st.markdown("<h2>Quiénes somos</h2>", unsafe_allow_html=True)

  integrantes = [
      ("Daniel Sandoval", "INTEGRANTES/Daniel Sandoval.jpeg"),
      ("Dulce P. Araujo", "INTEGRANTES/Dulce P. Araujo.jpeg"),
      ("Ignacio Evans", "INTEGRANTES/Ignacio Evans.jpeg"),
      ("Izabella Piedrasanta", "INTEGRANTES/Valentina Piedrasanta.jpeg"),
      ("Nelson Mazariegos", "INTEGRANTES/Gianluca Mazariegos.jpeg"),
      ("Marcos Melgar", "INTEGRANTES/Marcos Melgar.jpeg"),
  ]

  cols = st.columns(3)
  for i, (nombre, foto) in enumerate(integrantes):
    with cols[i % 3]:
      try:
        st.image(foto, width=80)
      except:
        st.markdown(
            '<div style="width:80px;height:80px;background:#0a6cc4;'
            'border-radius:50%;margin:0 auto 10px auto;"></div>',
            unsafe_allow_html=True,
        )
      st.markdown(
          f"<p style='text-align: center;'><strong>{nombre}</strong></p>",
          unsafe_allow_html=True,
      )

# ==========================================
# 3. INTRODUCCIÓN 
# ==========================================
with pestanas[2]:
  st.markdown("<h2>Introducción</h2>", unsafe_allow_html=True)
  st.markdown(
      "<h3>La robótica no es algo lejano ni costoso. Se puede hacer en"
      " casa.</h3>",
      unsafe_allow_html=True,
  )
  st.write(
      "Con física, química y programación básica podemos construir máquinas que"
      " sirven en la vida diaria, sin necesidad de un laboratorio"
      " profesional."
  )
  st.write(
      "Recreamos tres experimentos para ampliar lo que entendemos por robótica:"
      " uno muestra cómo funcionan las máquinas a gran escala, otro cómo la"
      " robótica nos ayuda cada día, y el tercero cómo ha estado con nosotros"
      " desde hace años sin que lo notemos."
  )
  st.write(
      "Lo que aprendemos en el salón de clases puede convertirse en soluciones"
      " reales."
  )

# ==========================================
# 4. OBJETIVOS 
# ==========================================
with pestanas[3]:
  st.markdown("<h2>Objetivos</h2>", unsafe_allow_html=True)
  st.markdown("<h3>Objetivo general</h3>", unsafe_allow_html=True)
  st.markdown(
      """
        <div class="destacado">
            <p>Desarrollar prototipos de brazo hidráulico, sensor de lluvia y conductividad eléctrica que demuestren cómo la química, la física y la programación forman parte de la tecnología actual y mejoran tareas cotidianas, como poner ropa a secar al aire libre, mover objetos o tener electricidad.</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown("<h3>Objetivos específicos</h3>", unsafe_allow_html=True)
  st.markdown(
      "- Integrar tres asignaturas que a simple vista no parecen tener nada en"
      " común."
  )
  st.markdown(
      "- Aplicar el principio de Pascal para construir un brazo que levante,"
      " mueva y agarre objetos."
  )
  st.markdown(
      "- Aplicar la ley de Ohm y la automatización para detectar agua y, por"
      " lo tanto, lluvia."
  )
  st.markdown(
      "- Aplicar la conductividad de partículas químicas a través del"
      " movimiento del agua."
  )
  st.markdown(
      "- Fomentar el interés por la innovación tecnológica en estudiantes y"
      " comunidad educativa."
  )

# ==========================================
# 5. BRAZO HIDRÁULICO 
# ==========================================
with pestanas[4]:
  st.markdown("<h2>Brazo hidráulico</h2>", unsafe_allow_html=True)
  st.markdown(
      '<ul class="chips" style="display:flex;gap:0.5rem;list-style:none;'
      'padding:0;"><li style="border:1px solid #0a6cc4;border-radius:999px;'
      'padding:0.2rem 0.8rem;color:#0a6cc4;">Física</li><li'
      ' style="border:1px solid #0a6cc4;border-radius:999px;padding:0.2rem'
      ' 0.8rem;color:#0a6cc4;">Hidráulica</li></ul>',
      unsafe_allow_html=True,
  )
  st.write(
      "Es una máquina que levanta cosas, gira y agarra objetos delicados con"
      " mucha precisión. Se mueve con líquido: la hidráulica estudia cómo se"
      " comportan los líquidos y cómo pueden transmitir fuerza."
  )

# ==========================================
# 6. SENSOR DE LLUVIA 
# ==========================================
with pestanas[5]:
  st.markdown("<h2>Sensor de lluvia</h2>", unsafe_allow_html=True)
  st.markdown(
      '<ul class="chips" style="display:flex;gap:0.5rem;list-style:none;'
      'padding:0;"><li style="border:1px solid #0a6cc4;border-radius:999px;'
      'padding:0.2rem 0.8rem;color:#0a6cc4;">Física</li><li'
      ' style="border:1px solid #0a6cc4;border-radius:999px;padding:0.2rem'
      ' 0.8rem;color:#0a6cc4;">Programación</li><li style="border:1px solid'
      ' #0a6cc4;border-radius:999px;padding:0.2rem'
      ' 0.8rem;color:#0a6cc4;">Ley de Ohm</li></ul>',
      unsafe_allow_html=True,
  )
  st.write(
      "Es un dispositivo electrónico que detecta agua y la convierte en una"
      " señal eléctrica. Nuestro prototipo es una casa domotizada con un sensor"
      " de lluvia."
  )

  st.markdown("<h3>Cómo detecta la lluvia</h3>", unsafe_allow_html=True)
  st.markdown("1. Llueve y las gotas caen sobre el sensor.")
  st.markdown(
      "2. El agua toca varias pistas a la vez. Como tiene iones disueltos, forma"
      " un camino para la electricidad."
  )
  st.markdown("3. La resistencia baja y el circuito mide ese cambio.")
  st.markdown("4. Se activa una señal y la casa reacciona.")
  st.write(
      "El sensor no sabe que cayó una gota: solo detecta un cambio eléctrico"
      " causado por el agua."
  )

  st.markdown("<h3>La ley de Ohm</h3>", unsafe_allow_html=True)
  st.markdown(
      "<h3 style='text-align:center;'>$V = I \\times R$</h3>",
      unsafe_allow_html=True,
  )

  c1, c2, c3 = st.columns(3)
  with c1:
    st.markdown("**Voltaje (V)**")
    st.write("Empuja las cargas por el circuito. Se mide en voltios.")
  with c2:
    st.markdown("**Corriente (I)**")
    st.write(
        "Flujo de electrones. Se mide en amperios (A) o miliamperios (mA)."
    )
  with c3:
    st.markdown("**Resistencia (R)**")
    st.write("Qué tanto se opone un material al paso de la corriente.")

  st.markdown("<h3>Tipos de sensores</h3>", unsafe_allow_html=True)
  st.markdown(
      "- **Cucharón:** Cada vez que se llena y se voltea un recipiente, cuenta"
      " una cantidad fija de lluvia."
  )
  st.markdown(
      "- **Ópticos:** Usan luz infrarroja para detectar gotas. Comunes en"
      " autos."
  )
  st.markdown(
      "- **Piezoeléctricos:** Convierten la presión de las gotas en señales"
      " eléctricas."
  )
  st.markdown(
      "- **De pesaje:** Pesan el agua acumulada. Muy precisos y más caros."
  )

  st.markdown("<h3>Dónde se usan</h3>", unsafe_allow_html=True)
  st.markdown(
      "- **Agricultura:** saber cuánta agua reciben los cultivos y cuánto regar."
  )
  st.markdown(
      "- **Autos:** activan los limpiaparabrisas y ajustan su velocidad."
  )
  st.markdown(
      "- **Ciudades:** activan drenajes, compuertas y alertas de inundación."
  )
  st.markdown(
      "- **Energía solar:** protegen los paneles ajustando su inclinación o"
      " limpiándolos."
  )

  st.write(
      "Los sensores necesitan mantenimiento y calibración, porque el polvo, la"
      " suciedad o el viento fuerte pueden alterar las mediciones."
  )
  st.markdown(
      "[Ver simulación](https://vt.tiktok.com/ZSVT5GUSb/)",
      unsafe_allow_html=True,
  )

# ==========================================
# 7. CONDUCTIVIDAD ELÉCTRICA 
# ==========================================
with pestanas[6]:
  st.markdown("<h2>Conductividad eléctrica</h2>", unsafe_allow_html=True)
  st.markdown(
      '<ul class="chips" style="display:flex;gap:0.5rem;list-style:none;'
      'padding:0;"><li style="border:1px solid #0a6cc4;border-radius:999px;'
      'padding:0.2rem 0.8rem;color:#0a6cc4;">Química</li><li'
      ' style="border:1px solid #0a6cc4;border-radius:999px;padding:0.2rem'
      ' 0.8rem;color:#0a6cc4;">Física</li><li style="border:1px solid'
      ' #0a6cc4;border-radius:999px;padding:0.2rem'
      ' 0.8rem;color:#0a6cc4;">Circuitos</li></ul>',
      unsafe_allow_html=True,
  )

  st.write(
      "Es la capacidad de un material o sustancia para dejar pasar la corriente"
      " eléctrica. Se mide en siemens por metro (S/m) y su símbolo es la letra"
      " griega sigma (σ)."
  )
  st.write(
      "En el agua, la corriente la llevan los iones: partículas con carga"
      " eléctrica. El agua pura conduce muy poco. Cuando se disuelven sales o"
      " minerales, se separan en iones positivos y negativos (por ejemplo Na⁺"
      " y Cl⁻) que se mueven hacia lados opuestos y permiten el paso de la"
      " corriente. Más iones significan más conductividad."
  )

  st.markdown("<h3>Cómo funciona el experimento</h3>", unsafe_allow_html=True)
  st.markdown("1. La pila aplica un voltaje a los dos electrodos.")
  st.markdown(
      "2. El carbonato de potasio (K₂CO₃) se disuelve en el agua y forma iones."
  )
  st.markdown(
      "3. Los iones se mueven hacia los electrodos y transportan la corriente."
  )
  st.markdown("4. Si la corriente es suficiente, el LED se enciende.")
  st.write(
      "El LED debe conectarse respetando su polaridad y, si hace falta, con"
      " una resistencia que limite la corriente para protegerlo."
  )

  st.markdown(
      "<h3>Conexión con el sensor de lluvia</h3>", unsafe_allow_html=True
  )
  st.write(
      "La lluvia absorbe partículas, sales y minerales del ambiente. Eso le da"
      " la conductividad necesaria para cambiar la resistencia del sensor. Es"
      " el mismo principio que enciende el LED."
  )

  st.markdown("<h3>Para qué sirve</h3>", unsafe_allow_html=True)
  st.markdown(
      "- **En física:** entender circuitos, cables y aparatos eléctricos."
  )
  st.markdown(
      "- **En química:** saber si una sustancia produce iones, analizar la"
      " calidad del agua y medir las sales disueltas."
  )

  st.markdown(
      "[Ver simulación](https://youtube.com/shorts/Hh8PDryv3UY?si=14hr037DYw5RecJ9)",
      unsafe_allow_html=True,
  )

# ==========================================
# 8. CONCLUSIONES 
# ==========================================
with pestanas[7]:
  st.markdown("<h2>Conclusiones</h2>", unsafe_allow_html=True)
  st.markdown(
      "<h3>Física, química y programación trabajan mejor juntas.</h3>",
      unsafe_allow_html=True,
  )
  st.write(
      "Estos proyectos no son solo experimentos creativos y divertidos: son una"
      " herramienta educativa que muestra cómo la ciencia y la tecnología"
      " resuelven problemas, crean mejores herramientas y nos acercan a un"
      " futuro donde la ciencia esté al servicio de las personas."
  )
  st.write(
      "También nos enseñaron que temas que parecen muy distintos pueden"
      " combinarse para crear cosas fuera de lo común, y nos dejaron con ganas"
      " de descubrir cómo se relacionan en otros proyectos."
  )

# ==========================================
# 9. BIBLIOGRAFÍA 
# ==========================================
with pestanas[8]:
  st.markdown("<h2>Bibliografía</h2>", unsafe_allow_html=True)
  st.markdown(
      """
        <ul style="color: var(--texto-suave); font-size: 0.95rem;">
            <li>Arduino. (2024). <em>Arduino Reference &amp; Documentation: Servo Library.</em> Arduino Foundation. <a href="https://www.arduino.cc/reference/en/libraries/servo/" target="_blank">arduino.cc</a></li>
            <li>Google Creative Lab. (2017). <em>Teachable Machine.</em> <a href="https://teachablemachine.withgoogle.com/" target="_blank">teachablemachine.withgoogle.com</a></li>
            <li>Prieto, M., &amp; García, J. (2019). Extracción y viraje de color de antocianinas como indicador natural de pH. <em>Revista de Educación e Investigación Química, 15</em>(2), 45-52.</li>
            <li><a href="https://plantae.garden/pluviometro-agricultura-precision" target="_blank">Plantae: pluviómetro y agricultura de precisión</a></li>
            <li><a href="https://www.agurotech.com/pluviometro-digital" target="_blank">Agurotech: pluviómetro digital</a></li>
            <li><a href="https://learningdata.hubiberiaagrotech.eu/sensores-de-lluvia/" target="_blank">Hub Iberia Agrotech: sensores de lluvia</a></li>
            <li><a href="https://www.niuboltech.com/Product-knowledge/What-is-a-rainfall-sensor.html" target="_blank">Niubol: what is a rainfall sensor</a></li>
            <li><a href="https://chem.libretexts.org/Bookshelves/General_Chemistry/Chem1_%28Lower%29/08%3A_Solutions/8.10%3A_Ions_and_Electrolytes" target="_blank">LibreTexts: Ions and Electrolytes</a></li>
            <li><a href="https://openstax.org/books/f%C3%ADsica-universitaria-volumen-2/pages/9-3-resistividad-y-resistencia" target="_blank">OpenStax: Resistividad y resistencia</a></li>
        </ul>
    """,
      unsafe_allow_html=True,
  )

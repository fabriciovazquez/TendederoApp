import streamlit as st

# Configuración de la interfaz con enfoque moderno, claro y accesible
st.set_page_config(
    page_title="TenderoApp - Prototipo de Alta Fidelidad",
    page_icon="🏪",
    layout="centered"
)

# Inicialización de estados de sesión para mantener la interactividad en vivo
if 'total_ventas' not in st.session_state:
    st.session_state.total_ventas = 45.50
if 'saldo_segundo' not in st.session_state:
    st.session_state.saldo_segundo = 14.50
if 'saldo_maria' not in st.session_state:
    st.session_state.saldo_maria = 6.20
if 'inventario' not in st.session_state:
    st.session_state.inventario = [
        {"producto": "Leche entera la Vaquita (4 unidades) - Mover al frente de percha de inmediato.", "cant": 4, "estado": "VENCE HOY", "color": "rojo"},
        {"producto": "Yogurt Familiar de Fresa (6 unidades) - Sugerencia de la IA: Crear promoción o combo rápido.", "cant": 6, "estado": "7 DÍAS", "color": "amarillo"},
        {"producto": "Arroz Enfundado de 1kg (45 unidades) - Stock estable sin riesgos de caducidad.", "cant": 45, "estado": "SEGURO", "color": "verde"}
    ]
if 'mostrar_modal_voz' not in st.session_state:
    st.session_state.mostrar_modal_voz = False

# ==========================================
# 🎨 NUEVO DISEÑO: INTERFAZ CLARA DE ALTO CONTRASTE
# ==========================================
st.markdown("""
    <style>
    /* Fondo Claro Limpio y Moderno para evitar errores de herencia */
    .stApp {
        background-color: #F8F9FA;
        color: #212529 !important;
    }
    
    /* Asegurar que los textos principales sean siempre oscuros y legibles */
    h1, h2, h3, h4, label, p, span {
        color: #212529 !important;
    }
    
    /* 🛠️ DISEÑO DE BOTONES NATIVOS (Texto oscuro, bordes verdes nítidos) */
    div.stButton > button {
        color: #155724 !important;
        background-color: #E2F0D9 !important;
        border: 2px solid #28A745 !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        opacity: 1 !important;
        padding: 10px 20px !important;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover, div.stButton > button:focus, div.stButton > button:active {
        color: #FFFFFF !important;
        background-color: #28A745 !important;
        border: 2px solid #28A745 !important;
    }

    /* Inputs de Texto Limpios */
    input {
        background-color: #FFFFFF !important;
        color: #212529 !important;
        border: 2px solid #CED4DA !important;
        border-radius: 8px !important;
    }
    
    input::placeholder {
        color: #6C757D !important;
    }

    /* Tarjetas del Menú Principal (Estilo Dashboard Moderno) */
    .big-button {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-left: 6px solid #28A745;
        border-radius: 12px;
        padding: 22px;
        text-align: center;
        margin-bottom: 5px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    }
    
    .button-title {
        font-size: 22px;
        font-weight: bold;
        color: #28A745 !important;
    }

    /* Contenedores de Clientes (Tarjetas Blancas Elegantes) */
    .client-card {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #E0E0E0;
        margin-bottom: 10px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.02);
    }

    /* Etiquetas del Semáforo con excelente contraste */
    .badge-rojo { background-color: #DC3545 !important; color: #FFFFFF !important; padding: 6px 14px; border-radius: 20px; font-weight: bold; display: inline-block; }
    .badge-amarillo { background-color: #FFC107 !important; color: #212529 !important; padding: 6px 14px; border-radius: 20px; font-weight: bold; display: inline-block; }
    .badge-verde { background-color: #28A745 !important; color: #FFFFFF !important; padding: 6px 14px; border-radius: 20px; font-weight: bold; display: inline-block; }
    
    /* 🟢 EL BOTÓN FLOTANTE DEL MICRÓFONO */
    .floating-mic-container {
        position: fixed;
        bottom: 35px;
        right: 35px;
        background-color: #28A745 !important;
        color: #FFFFFF !important;
        border-radius: 50% !important;
        width: 70px !important;
        height: 70px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 32px !important;
        box-shadow: 0px 6px 16px rgba(40, 167, 69, 0.4) !important;
        z-index: 999999 !important;
        cursor: pointer;
        transition: transform 0.2s ease-in-out;
    }
    .floating-mic-container:hover {
        transform: scale(1.1);
        background-color: #218838 !important;
    }
    
    /* Ocultar el disparador de backend */
    div.element-container:has(button[key="trigger_invisible"]) {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# 🏪 ENCABEZADO
st.title("🏪 TenderoApp")
st.subheader("El ayudante de tu tienda (Modo Seguro - 100% Offline)")
st.markdown("---")

# ==========================================
# 🎙️ VENTANA EMERGENTE DE DICTADO POR VOZ
# ==========================================
if st.session_state.mostrar_modal_voz:
    st.markdown("""
        <div style="background-color: #E2F0D9; padding: 20px; border-radius: 12px; border: 2px solid #28A745; margin-bottom: 25px;">
            <b style='color:#28A745; font-size:16px;'>🎙️ ASISTENTE DE VOZ LOCAL ACTIVADO</b><br>
            <span style="font-size: 14px; color: #212529;">La IA está escuchando tu dictado. Escribe abajo el comando:</span>
        </div>
    """, unsafe_allow_html=True)
    
    comando_voz = st.text_input("Dictado de voz detectado:", placeholder="Ej: 'Anotar 5 a Don Segundo'", key="input_dictado_actual")
    
    if comando_voz:
        cmd = comando_voz.lower()
        if "segundo" in cmd and any(x in cmd for x in ["anotar", "fiar", "debe", "suma"]):
            st.session_state.saldo_segundo += 5.0
            st.success("🤖 IA Local: ¡Entendido! Se sumaron $5.00 a la cuenta de Don Segundo Chimbo.")
        elif ("maría" in cmd or "maria" in cmd) and any(x in cmd for x in ["anotar", "fiar", "debe", "suma"]):
            st.session_state.saldo_maria += 3.0
            st.success("🤖 IA Local: ¡Entendido! Se sumaron $3.00 a la cuenta de Doña María Elena Morocho.")
        elif any(x in cmd for x in ["vender", "venta", "registrar"]):
            st.session_state.total_ventas += 10.0
            st.session_state.inventario[0]["cant"] -= 1
            st.success("🤖 IA Local: Venta de $10.00 añadida.")
        else:
            st.info("🤖 IA Local: Comando analizado con éxito.")
    st.markdown("---")

# 📊 SECCIÓN DE ACCESOS DIRECTOS CORREGIDA (Apilada vertical)
# Bloque Ventas
st.markdown('<div class="big-button"><div class="button-title">💰 Mis Ventas</div></div>', unsafe_allow_html=True)
st.write("Caja")
st.markdown(f"<h2>${st.session_state.total_ventas:.2f}</h2>", unsafe_allow_html=True)
if st.button("Abrir Mis Ventas", key="btn_ventas", use_container_width=True):
    st.info("Abriendo el módulo inteligente...")

st.markdown("<br>", unsafe_allow_html=True)

# Bloque Inventario
st.markdown('<div class="big-button"><div class="button-title">📦 Mi Inventario</div></div>', unsafe_allow_html=True)
st.write("Alertas")
st.markdown("<h2>1</h2>", unsafe_allow_html=True)
if st.button("Abrir Mi Inventario", key="btn_inventario", use_container_width=True):
    st.info("Abriendo lista predictiva de existencias...")

st.markdown("---")

# 2. 🚨 MÓDULO: ALERTAS DE FIADOS
st.header("🔴 Lo que me deben (Alertas de Cobro)")
st.markdown('<div class="client-card">', unsafe_allow_html=True)
c1, c2 = st.columns([2, 1])
with c1:
    st.markdown("**Don Segundo Chimbo**")
    st.markdown(f"⚠️ Saldo: **${st.session_state.saldo_segundo:.2f}**")
with c2:
    if st.button("📲 Avisar", key="ws_segundo", use_container_width=True):
        st.success("💬 Mensaje listo.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="client-card">', unsafe_allow_html=True)
c3, c4 = st.columns([2, 1])
with c3:
    st.markdown("**Doña María Elena Morocho**")
    st.markdown(f"⚠️ Saldo: **${st.session_state.saldo_maria:.2f}**")
with c4:
    if st.button("📲 Avisar", key="ws_maria", use_container_width=True):
        st.success("💬 Mensaje listo.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# 3. 🟢🟡🔴 FEED VISUAL TIPO SEMÁFORO
st.header("📆 Semáforo de Caducidad Inteligente")
for prod in st.session_state.inventario:
    col_sem, col_txt = st.columns([1, 3])
    with col_sem:
        if prod['color'] == 'rojo': st.markdown(f'<span class="badge-rojo">{prod["estado"]}</span>', unsafe_allow_html=True)
        elif prod['color'] == 'amarillo': st.markdown(f'<span class="badge-amarillo">{prod["estado"]}</span>', unsafe_allow_html=True)
        else: st.markdown(f'<span class="badge-verde">{prod["estado"]}</span>', unsafe_allow_html=True)
    with col_txt:
        st.markdown(f"**{prod['producto']}**")

st.markdown("<br><br><br>", unsafe_allow_html=True)

# 🚀 INTERRUPTOR INVISIBLE
if st.button("click_trigger", key="trigger_invisible"):
    st.session_state.mostrar_modal_voz = not st.session_state.mostrar_modal_voz
    st.rerun()

st.markdown("""
    <div class="floating-mic-container" onclick="document.querySelector('button[key=\\'trigger_invisible\\']').click()">
        🎙️
    </div>
""", unsafe_allow_html=True)
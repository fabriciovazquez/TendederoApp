import streamlit as st
import time

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
    /* Fondo Claro Limpio y Moderno */
    .stApp {
        background-color: #F8F9FA;
        color: #212529 !important;
    }
    
    /* Asegurar que los textos principales sean siempre oscuros y legibles */
    h1, h2, h3, h4, label, p, span {
        color: #212529 !important;
    }
    
    /* 🛠️ DISEÑO DE BOTONES NATIVOS */
    div.stButton > button {
        color: #155724 !important;
        background-color: #E2F0D9 !important;
        border: 2px solid #28A745 !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
    }

    div.stButton > button:hover {
        color: #FFFFFF !important;
        background-color: #28A745 !important;
    }

    /* Tarjetas del Menú Principal */
    .big-button {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-left: 6px solid #28A745;
        border-radius: 12px;
        padding: 22px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    }
    
    .button-title {
        font-size: 22px;
        font-weight: bold;
        color: #28A745 !important;
        margin-bottom: 5px;
    }
    
    .client-card {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #E0E0E0;
        margin-bottom: 10px;
    }

    .badge-rojo { background-color: #DC3545 !important; color: #FFFFFF !important; padding: 6px 14px; border-radius: 20px; font-weight: bold; }
    .badge-amarillo { background-color: #FFC107 !important; color: #212529 !important; padding: 6px 14px; border-radius: 20px; font-weight: bold; }
    .badge-verde { background-color: #28A745 !important; color: #FFFFFF !important; padding: 6px 14px; border-radius: 20px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 🏪 ENCABEZADO
st.title("🏪 TenderoApp")
st.subheader("El ayudante de tu tienda (Modo Seguro - 100% Offline)")
st.markdown("---")

# ==========================================
# 🎙️ VENTANA DE VOZ
# ==========================================
if st.button("🎙️ Alternar Voz"):
    st.session_state.mostrar_modal_voz = not st.session_state.mostrar_modal_voz
    st.rerun()

if st.session_state.mostrar_modal_voz:
    comando = st.text_input("Dictado:")
    if comando:
        cmd = comando.lower()
        if "leche" in cmd and "segundo" in cmd:
            st.success("Listo: se añadió a la cuenta de Don Segundo una leche")
        elif "segundo" in cmd: 
            st.session_state.saldo_segundo += 5.0
            st.success("🤖 IA Local procesada.")
        elif "maría" in cmd: 
            st.session_state.saldo_maria += 3.0
            st.success("🤖 IA Local procesada.")
    st.markdown("---")

# 📊 ACCESOS DIRECTOS
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="big-button"><div class="button-title">💰 Mis Ventas</div></div>', unsafe_allow_html=True)
    st.metric("Caja", f"${st.session_state.total_ventas:.2f}")
    st.button("Abrir Mis Ventas", key="btn_ventas", use_container_width=True)
with col2:
    st.markdown('<div class="big-button"><div class="button-title">📦 Mi Inventario</div></div>', unsafe_allow_html=True)
    st.metric("Alertas", "1")
    st.button("Abrir Mi Inventario", key="btn_inventario", use_container_width=True)

st.markdown("---")

# 2. 🚨 MÓDULO: ALERTAS DE FIADOS
st.header("🔴 Lo que me deben")

st.markdown('<div class="client-card">', unsafe_allow_html=True)
st.markdown(f"**Don Segundo Chimbo** - Saldo: **${st.session_state.saldo_segundo:.2f}**")
if st.button("📲 Avisar a Don Segundo", key="ws_segundo"):
    with st.spinner("Enviando..."):
        time.sleep(1)
    st.success("Listo: se envió el saldo de Don Segundo Chimbo a su contacto")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="client-card">', unsafe_allow_html=True)
st.markdown(f"**Doña María Elena Morocho** - Saldo: **${st.session_state.saldo_maria:.2f}**")
if st.button("📲 Avisar a Doña María", key="ws_maria"):
    with st.spinner("Enviando..."):
        time.sleep(1)
    st.success("Listo: se envió el saldo de Doña María Elena Morocho a su contacto")
st.markdown('</div>', unsafe_allow_html=True)

# 3. 🟢🟡🔴 SEMÁFORO
st.header("📆 Semáforo de Caducidad")
for prod in st.session_state.inventario:
    clase = "badge-rojo" if prod['color']=='rojo' else "badge-amarillo" if prod['color']=='amarillo' else "badge-verde"
    st.markdown(f'<span class="{clase}">{prod["estado"]}</span> **{prod["producto"]}**', unsafe_allow_html=True)
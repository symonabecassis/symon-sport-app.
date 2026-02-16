import streamlit as st
import pandas as pd

# Configuração visual Dark Mode
st.set_page_config(page_title="Symon Sport Remans", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #121926; color: white; }
    .card {
        background-color: #1c2536;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #2d3748;
        margin-bottom: 10px;
    }
    .label { color: #94a3b8; font-size: 14px; font-weight: bold; text-transform: uppercase; }
    .value-blue { color: #60a5fa; font-size: 32px; font-weight: bold; }
    .value-green { color: #4ade80; font-size: 32px; font-weight: bold; }
    .value-yellow { color: #fbbf24; font-size: 32px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Título
st.title("Symon Sport Remans")
st.caption("QUANTITATIVE ANALYTICS & TRADING ENGINE")

# Barra Lateral para controle de dados
st.sidebar.header("⚙️ Gestão de Banca")
banca_total = st.sidebar.number_input("Banca Inicial (R$)", value=1000.0)
lucro_sessao = st.sidebar.number_input("P&L Sessão (R$)", value=0.0)
win_rate = st.sidebar.slider("Win Rate (%)", 0.0, 100.0, 0.0)

# Layout dos Cartões (Igual à sua imagem)
col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="card"><div class="label">💼 BANCA TOTAL</div><div class="value-blue">R$ {banca_total:,.2f}</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="card"><div class="label">📈 P&L SESSÃO</div><div class="value-green">R$ {lucro_sessao:,.2f}</div></div>', unsafe_allow_html=True)

col3, col4 = st.columns([1.5, 1])
with col3:
    st.markdown(f'<div class="card"><div class="label">🎯 WIN RATE</div><div class="value-yellow">{win_rate}%</div></div>', unsafe_allow_html=True)
with col4:
    st.write("Ações")
    c1, c2 = st.columns(2)
    c1.button("📈", help="Gráfico")
    c2.button("🗑️", help="Limpar")

# Área de Análise
st.divider()
st.subheader("🛠️ Nova Análise Técnica")
camp = st.selectbox("Selecione o Campeonato", ["Brasileirão A/B", "Champions League", "Premier League", "Outros"])
if st.button("Iniciar Análise com Gemini"):
    st.write(f"Buscando dados de {camp}...")

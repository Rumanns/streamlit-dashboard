import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Meu Primeiro App",
    page_icon="✅",
    layout="centered"
)

# Título do app
st.title("🎈 Meu Primeiro App Streamlit")
st.write("Este é o projeto mais simples possível!")

# Adiciona uma linha divisória
st.divider()

# Contador de cliques usando session state
if 'contador' not in st.session_state:
    st.session_state.contador = 0

# Botão para incrementar o contador
if st.button("Clique aqui!"):
    st.session_state.contador += 1
    st.balloons()  # Efeito visual de balões

# Mostra o contador
st.subheader(f"Total de cliques: {st.session_state.contador}")

# Botão para zerar o contador
if st.button("Zerar contador"):
    st.session_state.contador = 0
    st.rerun()

# Adiciona uma linha divisória
st.divider()

# Um pouco mais de interatividade
st.subheader("📝 Adicione seu nome:")
nome = st.text_input("Digite seu nome:")

if nome:
    st.success(f"Olá, {nome}! Bem-vindo ao Streamlit!")
    
# Mostra uma barra de progresso
st.subheader("🎯 Progresso:")
progresso = st.slider("Selecione um valor:", 0, 100, 50)
st.progress(progresso)
st.write(f"Progresso: {progresso}%")

# Rodapé
st.divider()
st.caption("Feito com ❤️ usando Streamlit")

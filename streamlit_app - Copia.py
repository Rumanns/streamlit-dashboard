import streamlit as st

# Título da página
st.title("Calculadora Simples 🧮")

# Entrada de números
num1 = st.number_input("Digite o primeiro número:")
num2 = st.number_input("Digite o segundo número:")

# Operações
operacao = st.selectbox("Escolha a operação:", 
                       ["Soma", "Subtração", "Multiplicação", "Divisão"])

# Botão para calcular
if st.button("Calcular"):
    if operacao == "Soma":
        resultado = num1 + num2
    elif operacao == "Subtração":
        resultado = num1 - num2
    elif operacao == "Multiplicação":
        resultado = num1 * num2
    elif operacao == "Divisão":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: divisão por zero!"
    
    # Mostra o resultado
    st.success(f"Resultado: {resultado}")

# Rodapé
st.markdown("---")
st.caption("Feito com Streamlit ❤️")
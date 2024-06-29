import streamlit as st
import time

st.title(':blue[Conversor de Temperaturas]')
st.image('https://imagens.climatempo.com.br/climapress/galeria/2023/08/060e88615fdd183f6f26d995a270a0d3.jpg', width=280)
op1 = st.selectbox('**Qual escala termométrica você gostaria de converter?**', ('Celsius', 'Fahrenheit', 'Kelvin'))

mensagem_erro = ''

if op1 == 'Celsius':
    Celsius = st.number_input('**Temperatura em Celsius**', value=0.0, placeholder='Insira um valor')
    if Celsius < -273 or Celsius > 100:
        mensagem_erro = 'O valor inserido não é possível pois o mesmo não existe na escala Celsius'
elif op1 == 'Fahrenheit':
    Fahrenheit = st.number_input('**Temperatura em Fahrenheit**', value=0.0, placeholder='Insira um valor')
    if Fahrenheit < -459.4 or Fahrenheit > 212:
        mensagem_erro = 'O valor inserido não é possível pois o mesmo não existe na escala Fahrenheit'
elif op1 == 'Kelvin':
    Kelvin = st.number_input('**Temperatura em Kelvin**', value=0.0, placeholder='Insira um valor')
    if Kelvin < 0 or Kelvin > 373:
        mensagem_erro = 'O valor inserido não é possível pois o mesmo não existe na escala Kelvin'

op2 = st.selectbox('**Converter para:**', ('Celsius', 'Fahrenheit', 'Kelvin'))


def Celsius1(Fahrenheit):
    return (5 * Fahrenheit - 160) / 9


def Celsius2(Kelvin):
    return Kelvin - 273


def Fahrenheit1(Celsius):
    return (9 * Celsius + 160) / 5


def Fahrenheit2(Kelvin):
    return (9 * Kelvin - 2297) / 5


def Kelvin1(Celsius):
    return Celsius + 273


def Kelvin2(Fahrenheit):
    return (5 * Fahrenheit + 2297) / 9


if mensagem_erro:
    st.error(mensagem_erro)

if st.button('Converter') and not mensagem_erro:
    with st.spinner('Calculando...'):
        time.sleep(2)
    if op1 == 'Celsius' and op2 == 'Fahrenheit':
        resposta = Fahrenheit1(Celsius)
    elif op1 == 'Celsius' and op2 == 'Kelvin':
        resposta = Kelvin1(Celsius)
    elif op1 == 'Fahrenheit' and op2 == 'Celsius':
        resposta = Celsius1(Fahrenheit)
    elif op1 == 'Fahrenheit' and op2 == 'Kelvin':
        resposta = Kelvin2(Fahrenheit)
    elif op1 == 'Kelvin' and op2 == 'Celsius':
        resposta = Celsius2(Kelvin)
    elif op1 == 'Kelvin' and op2 == 'Fahrenheit':
        resposta = Fahrenheit2(Kelvin)
        
    st.write('Temperatura em {}: {:.1f}'.format(op2, resposta))

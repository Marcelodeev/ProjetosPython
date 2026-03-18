import requests
import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QMessageBox, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
from datetime import datetime


 
app = QApplication(sys.argv)

janelinha = QWidget()
janelinha.setWindowTitle('Monitor Bitcoin')
janelinha.setFixedSize(400, 420)

contador = 60
preco_anterior = None

janelinha.setStyleSheet("""
QWidget{
    background-color:#1e1e2f;
    color:white;
}
QTextEdit{
    background-color:#111;
    border-radius:6px;
    font-size:14px;
}
""")

# PREÇO GRANDE
labelPreco = QLabel("Carregando...", janelinha)
labelPreco.setAlignment(Qt.AlignCenter)
labelPreco.setGeometry(0,20,400,60)
labelPreco.setFont(QFont("Arial",26,QFont.Bold))

# CONTADOR
labelTempo = QLabel("Atualiza em: 10s", janelinha)
labelTempo.setAlignment(Qt.AlignCenter)
labelTempo.setGeometry(0,80,400,30)

# DATA
labelDataHora = QLabel(janelinha)
labelDataHora.setAlignment(Qt.AlignCenter)
labelDataHora.setGeometry(0,110,400,30)

# HISTÓRICO
historico = QTextEdit(janelinha)
historico.setGeometry(20,150,360,240)
historico.setReadOnly(True)


def formatar_moeda_brl(valor):

    valor = float(valor)

    formato = f"{valor:,.2f}"

    formato_brasil = formato.replace(",", "X").replace(".", ",").replace("X", ".")

    return f"R$ {formato_brasil}"


def atualizar_data_hora():

    agora = datetime.now()

    labelDataHora.setText(agora.strftime("%d/%m/%Y %H:%M:%S"))


def atualizar_contador():

    global contador

    contador -= 1

    labelTempo.setText(f"Atualiza em: {contador}s")

    if contador <= 0:

        atualizar_preco()

        contador = 60


def atualizar_preco():

    global preco_anterior

    try:

        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"

        resposta = requests.get(url)

        dados = resposta.json()

        preco = dados["bitcoin"]["brl"]

        preco_formatado = formatar_moeda_brl(preco)

        labelPreco.setText(preco_formatado)

        agora = datetime.now().strftime("%H:%M:%S")

        cor = "white"
        seta = "➖"

        if preco_anterior != None:

            if preco > preco_anterior:

                cor = "green"
                seta = "▲"

            elif preco < preco_anterior:

                cor = "red"
                seta = "▼"

        historico.append(f'<span style="color:{cor}">{agora} {seta} {preco_formatado}</span>')

        preco_anterior = preco

    except Exception as erro:

        QMessageBox.warning(janelinha,"Erro","Não foi possível verificar o Bitcoin agora.\nTentando novamente...")
        print(erro)


    


def mostrar_grafico():

    try:

        url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=brl&days=1"

        resposta = requests.get(url)

        dados = resposta.json()

        precos = dados["prices"]

        horas = []
        valores = []

        for item in precos:

            timestamp = item[0] / 1000
            preco = item[1]

            hora = datetime.fromtimestamp(timestamp)

            horas.append(hora.strftime("%H:%M"))
            valores.append(preco)

        plt.figure(figsize=(10,5))

        plt.plot(horas, valores)

        plt.title("Bitcoin últimas 24 horas")

        plt.xlabel("Hora")

        plt.ylabel("Preço (BRL)")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()

    except Exception as erro:

        QMessageBox.warning(janelinha,"Erro","Não foi possível carregar o gráfico.")
        print(erro)




#botão

botaoGrafico = QPushButton("📈 Gráfico", janelinha)
botaoGrafico.setGeometry(300,10,90,30)
botaoGrafico.clicked.connect(mostrar_grafico)

timerRelogio = QTimer()
timerRelogio.timeout.connect(atualizar_data_hora)
timerRelogio.start(1000)

timerContador = QTimer()
timerContador.timeout.connect(atualizar_contador)
timerContador.start(1000)

atualizar_preco()

janelinha.show()
sys.exit(app.exec_())
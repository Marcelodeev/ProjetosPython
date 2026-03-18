import requests
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
from datetime import datetime



app = QApplication(sys.argv)  

janelinha = QWidget()
janelinha.setWindowTitle('Cotação Bitcoin agora')
janelinha.setFixedSize(360, 320)

labelDataHora = QLabel(janelinha)
labelDataHora.setAlignment(Qt.AlignCenter)
labelDataHora.setGeometry(0, 250, 360, 50)
labelDataHora.setFont(QFont("Arial", 16))

# estilizar ja no codigo

##janelinha.setStyleSheet("""
#    QWidget {
#        background-color: #1e1e2f;
#        color: white;
#    }

#    QLabel {
#        color: #f5f5f5;
#    }
#
#    QPushButton {
#        border-radius: 12px;
#        font-size: 14px;
#        font-weight: bold;
#        padding: 10px;
#    }
#
#    QPushButton#btc {
#        background-color: #2ecc71;
#        color: black;
#    }
#
#    QPushButton#btc:hover {
#        background-color: #27ae60;
#    }
#
#    QPushButton#usd {
#        background-color: #3498db;
#        color: white;
#    }
#
#    QPushButton#usd:hover {
#        background-color: #2980b9;
#    }
#""")

# opção para estilizar com um arquivo separado

with open("estilo.qss","r") as arquivo_qss:
    estilo = arquivo_qss.read()
    janelinha.setStyleSheet(estilo)

preco_anterior = None

#url para cotação do bitcoin

urlbit = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl" #https://api.binance.com/api/v3/ticker/price?symbol=BTCBRL essa api mostra o valor já em reais porém nao atualiza sozinha ele mostra o valor se eu mandar atualizar
resposta1 = requests.get(urlbit)
dadosbit = resposta1.json()
preco_atual = dadosbit['bitcoin']['brl']
#url dolar 
urldolar = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd" # https://live.coinpaprika.com/stream?asset=BTC   esse manda o codigo a cada seg porém é em dolar
resposta2 = requests.get(urldolar)                                                       # parametros {"timestamp":"2026-03-02T14:37:47.647Z","asset":"BTC","price":66155.68000000001,"sources":11,"pairs":3}
dadosdolar = resposta2.json()


  #formatar o valor colocando virgulas e pontos
        

def formatar_moeda_brl(valor):
    valor = float(valor)
    formato = f"{valor:,.2f}"
    formato_brasil = formato.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {formato_brasil}"

def formatar_moeda_usd(valor):
    valor = float(valor)
    formato = f"{valor:,.2f}"  # já é padrão americano
    return f"US$ {formato}"



def mostrarcotacaodolar():
    valordolar = dadosdolar["bitcoin"]["usd"]
    valor_formatado = formatar_moeda_usd(valordolar)
    QMessageBox.information(janelinha, "Cotação do BTC em Dólar", valor_formatado)

def mostrarcotacaobit():
    valorbit = dadosbit["bitcoin"]["brl"]
    valor_formatado = formatar_moeda_brl(valorbit)
    QMessageBox.information(janelinha, "Cotação BTC em Reais", valor_formatado)


def atualizar_data_hora():
    agora = datetime.now()
    labelDataHora.setText(agora.strftime("%d/%m/%Y %H:%M:%S"))



# while True:
#     try:
#         if preco_anterior != preco_atual:
#             preco_anterior = preco_atual
#             print("Preço atualizado é {preco_atual}")
#         time.sleep(5)
#     except Exception as e:
#             print("Erro no preço", e)
#             time.sleep(10)
            
  

# AUMENTAR O TAMANHO DO TITULO PRINCIPAL
labelTitulo = QLabel("₿ BITCOIN COTAÇÃO", janelinha)
labelTitulo.setAlignment(Qt.AlignCenter)
labelTitulo.setGeometry(0, 30, 360, 60)

timer = QTimer()
timer.timeout.connect(atualizar_data_hora)
timer.start(1000)

fonte = QFont("Arial", 20, QFont.Bold)
labelTitulo.setFont(fonte)

#AUMENTANDO O TAMANHO DA FONTE
fonte = QFont()
fonte.setPointSize(25)
labelTitulo.setFont(fonte)



# botão 

botaocotacaobtc = QPushButton("💰 COTAÇÃO EM REAIS", janelinha)
botaocotacaobtc.setObjectName("btc")  # usa o estilo verde
botaocotacaobtc.setGeometry(70, 120, 220, 60)
botaocotacaobtc.clicked.connect(mostrarcotacaobit)

botaocotacaodolar = QPushButton("💵 COTAÇÃO EM DÓLAR", janelinha)
botaocotacaodolar.setObjectName("usd")  # usa o estilo azul
botaocotacaodolar.setGeometry(70, 200, 220, 60)
botaocotacaodolar.clicked.connect(mostrarcotacaodolar)


janelinha.show()
sys.exit(app.exec_())
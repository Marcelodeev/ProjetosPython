import sys
import json
import requests

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal


#  FUNÇÃO PARA PEGAR DÓLAR EM REAL -------

def pegar_dolar_brl():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data["rates"]["BRL"]


cotacao_dolar = pegar_dolar_brl()


#  THREAD STREAM BTC 

class StreamThread(QThread):
    novo_preco = pyqtSignal(float)

    def run(self):
        url = "https://live.coinpaprika.com/stream?asset=BTC"
        response = requests.get(url, stream=True)

        for line in response.iter_lines():
            if line and line.startswith(b"data:"):
                dados = json.loads(line[5:])
                preco_usd = dados["price"]
                self.novo_preco.emit(preco_usd)


#  APP 

app = QApplication(sys.argv)

janelinha = QWidget()
janelinha.setWindowTitle('Bitcoin em Dolar (Tempo Real)')
janelinha.setFixedSize(360, 320)


labelTitulo = QLabel("₿ BITCOIN DOLAR", janelinha)
labelTitulo.setAlignment(Qt.AlignCenter)
labelTitulo.setGeometry(0, 40, 360, 50)

fonte = QFont("Arial", 22, QFont.Bold)
labelTitulo.setFont(fonte)


labelPreco = QLabel("Conectando...", janelinha)
labelPreco.setAlignment(Qt.AlignCenter)
labelPreco.setGeometry(0, 120, 360, 60)

fonte_preco = QFont("Arial", 26)
labelPreco.setFont(fonte_preco)


def formatar_moeda_usd(valor):
    valor = float(valor)
    formato = f"{valor:,.2f}"  # já é padrão americano
    return f"US$ {formato}"




#  ATUALIZA PREÇO 

def atualizar_preco(preco_usd):
    preco_brl = preco_usd 
    labelPreco.setText(formatar_moeda_usd(preco_brl))


#  INICIAR STREAM 

thread = StreamThread()
thread.novo_preco.connect(atualizar_preco)
thread.start()


janelinha.show()
sys.exit(app.exec_())
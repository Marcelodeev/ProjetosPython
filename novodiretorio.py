import requests
import sys 
from PyQt5.QtWidgets import QMessageBox , QApplication, QWidget, QLabel, QLineEdit, QPushButton 
app = QApplication(sys.argv) 
#  (https://api.github.com), verifique o código de status (200 para sucesso) e imprima o conteúdo JSON da resposta.

janelinha = QWidget()
janelinha.setWindowTitle('Janela')
janelinha.setGeometry(705,270,350,350)

campo=QLabel(200,300)

url = "https://api.github.com/user"

def mostrarurl():

    try:  
        response = requests.get(url) 
        
        if response.status_code == 200:
            dadosgit = response.json()
    except Exception as e:
        QMessageBox.critical({response.status_code},janelinha)



janelinha.show()
sys.exit(app.exec_())

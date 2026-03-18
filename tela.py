#Importando a biblioteca sys
import sys  
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton, QLineEdit , QMessageBox
#Criando a aplicação
app = QApplication(sys.argv)  

#Função que será chamada ao clicar no botão
def botaoClicado():
    print('Você clicou no botão!')

def botaoClicado():
    print('Você clicou no botão.')
    QMessageBox.information(janelinha, "Texto digitado", f"Você digitou: {caixaTexto.text()}")

#Criando a janela principal
janelinha = QWidget()
janelinha.setWindowTitle('Minha primeira Janela')
janelinha.setGeometry(705,270,350,350)

#Criando um rótulo (label)
textoRotulo = QLabel('Clique aqui em baixo ! ', janelinha)
textoRotulo.move(115,30)

#Criando um botão (Button)
botao = QPushButton ('Clique aqui Animal', janelinha)
botao.move(115,80)
botao = QPushButton ('Apagar', janelinha)
botao.move(80,160)
botao = QPushButton('Mostrar mensagem' , janelinha)
botao.move(160,160)

#Conectando o clique do botão á função 
botao.clicked.connect(botaoClicado)

#Criando uma caixa de texto
caixaTexto = QLineEdit(janelinha)
caixaTexto.move(100,200)


#Exibindo a janela
janelinha.show()

#Iniciando o loop de evento
sys.exit(app.exec_())





import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton , QMessageBox

# Funçao para validar limpar os campos

def limpaCampos():
    # Colocando os objetos de retorno nas caixas de texto
    caixaTextoCEP.clear()
    caixaTextoRua.clear()
    caixaTextoBairro.clear()
    caixaTextoCidade.clear()
    caixaTextoUF.clear()
    caixaTextoCEP.setFocus()


def validaCampo():

    codigoCEP = caixaTextoCEP.text()

    if codigoCEP == "":

        QMessageBox.critical(telaCadastro,"Atenção,","CEP precisa ser informado, verifique.")
        caixaTextoCEP.setFocus()
    else:
        tratarCEP(codigoCEP)

def tratarCEP(codigoCEP):
    #url da api
    url = f"https://viacep.com.br/ws/{codigoCEP}/json"
    
    try: 
        # Fazendo a requisição GET
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()


            if dados.get("erro") == "true":
                QMessageBox.critical(telaCadastro, "Deu ruim", "CEP NÃO encontrado na base de dados do VIACEP")
            else:
                # Colocando os objetos de retorno nas caixas de texto
                caixaTextoRua.setText(dados.get('logradouro',''))
                caixaTextoBairro.setText(dados.get('bairro',''))
                caixaTextoCidade.setText(dados.get('Localidade',''))
                caixaTextoUF.setText(dados.get('UF',''))

                QMessageBox.information(telaCadastro,"Consulta de CEP","Endereço encontrado, Parabéns Amigo")
        else:
            QMessageBox.critical(telaCadastro,"Deu ruim", f"Erro na requisição. Código de status: {response.status_code}")
    except Exception as e:
        QMessageBox.critical(telaCadastro,"Erro", f"Ocorreu uma exceção{str(e)}")
                    





app = QApplication(sys.argv)

#janela
telaCadastro = QWidget()
telaCadastro.setWindowTitle("Verificação de CEP com API")
telaCadastro.setGeometry(100, 100, 600, 120)


#Criando um rótulo (label)
#cep
textoRotuloCEP = QLabel('CEP:', telaCadastro)
textoRotuloCEP.move(10,10)

#Rua
textoRotuloRua = QLabel('Rua:', telaCadastro)
textoRotuloRua.move(300,10)

#Bairro
textoRotuloBairro = QLabel('Bairro', telaCadastro)
textoRotuloBairro.move(10,60)

#Cidade 
textoRoduloCidade = QLabel('Cidade', telaCadastro)
textoRoduloCidade.move(270,60)

#UF
textoRoduloUF = QLabel("UF:", telaCadastro)
textoRoduloUF.move(530,60)

#Criando uma caixa de texto 
#cep 
caixaTextoCEP = QLineEdit(telaCadastro)

#Tamanho da caixa de texto
caixaTextoCEP.setFixedWidth(80)

#Coloca máscara de CEP no QLineEdit
caixaTextoCEP.setInputMask("00000-000") #Máscara de cep
caixaTextoCEP.move(10,30)

#Rua 
caixaTextoRua = QLineEdit(telaCadastro)
caixaTextoRua.setFixedHeight(260)
caixaTextoRua.move(300,30)
caixaTextoRua.setEnabled(False)

#Bairro
caixaTextoBairro = QLineEdit(telaCadastro)
caixaTextoBairro.setFixedHeight(250)
caixaTextoBairro.move(10,80)
caixaTextoBairro.setEnabled(False)

#Cidade
caixaTextoCidade = QLineEdit(telaCadastro)
caixaTextoCidade.setFixedHeight(250)
caixaTextoCidade.move(270,80)
caixaTextoCidade.setFixedHeight(False)

#UF
caixaTextoUF = QLineEdit(telaCadastro)
caixaTextoUF.setFixedHeight(30)
caixaTextoUF.move(530,80)
caixaTextoUF.setEnabled(False)

#Criando o botão de busca do CEP 
BotaoBuscaCEP= QPushButton('Buscar CEP', telaCadastro)
BotaoBuscaCEP.move(100,25)

#conectando o clique do botão á função
BotaoBuscaCEP.clicked.connect(validaCampo)

#Criando o botão de Limpar
botaoLimpar =QPushButton('Limpar busca', telaCadastro)
botaoLimpar.move(250,25)

#Conectando o clique do botão á função 
botaoLimpar.clicked.connect(limpaCampos)

#Exibindo a janela
telaCadastro.show()

#Iniciando o loop de eventos

sys.exit(app.exec_())




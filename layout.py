import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton , QMessageBox
app = QApplication(sys.argv)  

#Criando a janela principal
janelinha = QWidget()
janelinha.setWindowTitle('CADASTRO DE USUÁRIO!')
janelinha.setGeometry(705,270,350,350)

#DEFINIÇÕES 

def limpaCampos():
    caixaTextoCPF.clear()
    caixaTextoRG.clear()
    caixaTextoNOME.clear()
    caixaTextoIDADE.clear()
    caixaTextoMAE.clear()
    caixaTextoCEP.clear()
    caixaTextoLOUGRADOURO.clear()
    caixaTextoUF.clear()
    caixaTextoBAIRRO.clear()
    caixaTextoCOMPLEMENTO.clear()
    caixaTextoCIDADE.clear()


def validaCampo():
    codigoCEP = caixaTextoCEP.text()

    if codigoCEP == "":
        QMessageBox.critical(janelinha,"Atenção","CEP precisa ser informado, verifique.")
        caixaTextoCEP.serFocus()
    else:
        tratarCEP(codigoCEP)

def tratarCEP(codigoCEP):
    url = f"https://viacep.com.br/ws{codigoCEP}/json/"






    


botao = QPushButton('CADASTRAR', janelinha)
botao.move(60,320)

botao = QPushButton('LIMPAR', janelinha)
botao.move(230,320)

#USUÁRIO //

textoRotulo = QLabel('CADASTRE-SE ABAIXO!', janelinha)
textoRotulo.move(115,30)

textoRotulo = QLabel('NOME COMPLETO:', janelinha)
textoRotulo.move(60,90)
 
textoRotulo = QLabel('CPF:', janelinha)
textoRotulo.move(60,50)

textoRotulo = QLabel('RG:', janelinha)
textoRotulo.move(200,50)

textoRotulo = QLabel('IDADE', janelinha)
textoRotulo.move(60,130)


textoRotulo = QLabel('NOME DA MÃE', janelinha)
textoRotulo.move(60,170)







#COLOCAR ENDEREÇO //

textoRotulo = QLabel('ENDEREÇO', janelinha)
textoRotulo.move(60,210)

textoRotulo = QLabel('CEP:', janelinha)
textoRotulo.move(60,230)

textoRotulo = QLabel('LOGRADOURO:', janelinha)
textoRotulo.move(60,260)

textoRotulo = QLabel('BAIRRO:', janelinha)
textoRotulo.move(220,220)

textoRotulo = QLabel('UF:', janelinha)
textoRotulo.move(270,245)

textoRotulo = QLabel('COMPLEMENTO:', janelinha)
textoRotulo.move(60,290)

textoRotulo = QLabel('CIDADE', janelinha)
textoRotulo.move(200,190)



#CAIXAS DE TEXTOS //

#CPF
caixaTextoCPF = QLineEdit(janelinha)
caixaTextoCPF.move(60,65)

#RG
caixaTextoRG = QLineEdit(janelinha)
caixaTextoRG.move(200,65)

#NOME
caixaTextoNOME = QLineEdit(janelinha)
caixaTextoNOME.move(60,105)

#IDADE
caixaTextoIDADE = QLineEdit(janelinha)
caixaTextoIDADE.move(60,147)
#NOME DA MÃE 
caixaTextoMAE = QLineEdit(janelinha)
caixaTextoMAE.move(60,185)
#CIDADE
caixaTextoCIDADE = QLineEdit(janelinha)
caixaTextoCIDADE.move(250,185)


#CEP
caixaTextoCEP = QLineEdit(janelinha)
caixaTextoCEP.move(83,230)

#LOGRADOURO
caixaTextoLOUGRADOURO = QLineEdit(janelinha)
caixaTextoLOUGRADOURO.move(135,260)
#UF 
caixaTextoUF = QLineEdit(janelinha)
caixaTextoUF.move(290,242)
#BAIRRO
caixaTextoBAIRRO = QLineEdit(janelinha)
caixaTextoBAIRRO.move(260,217)
#COMPLEMENTO 
caixaTextoCOMPLEMENTO = QLineEdit(janelinha)
caixaTextoCOMPLEMENTO.move(140,290)





janelinha.show()

sys.exit(app.exec_())
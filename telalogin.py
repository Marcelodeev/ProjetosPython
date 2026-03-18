import sys 
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton, QLineEdit , QMessageBox


#Função para validar se os campos foram preechidos
def validaCampos():
    usuario = caixaTextoUsuario.text()
    senha = caixaTextoSenha.text()


def login (usuario, senha):
    #Verificação do usuario e senha
    if usuario == "admin" and senha == "pass123$":
        QMessageBox.information(telaLogin,"Sucesso", f"Bem-vindo,{usuario}!")
    else:
        limpaCmapos()
        QMessageBox.warning(telaLogin,"Falha no login", "Usuario ou senha invalidos.")
        

    




    
#função para limpar os campos e posicionar o curso
def limpaCmapos():
    #verificação do usuario e senha
    caixaTextoUsuario.clear()
    caixaTextoSenha.clear()
    caixaTextoUsuario.setFocus()



# Verificação do usuário e senha
if usuario == "" or senha == "":
    QMessageBox.critical(telaLogin,"Atenção","Para verificação os dois cmapos precisam ser informados.")
    limpaCampos()
else:
    login(usuario,senha)






'''
Desenhando a tela de login

'''
#Criando a aplicação 

app = QApplication(sys.argv)




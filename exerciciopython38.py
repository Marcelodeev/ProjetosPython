# Tratamento de Divisão por Zero 

# def divisao():
#     try:
#         numa = int(input("Digite o primeiro número: "))
#         numb = int(input("Digite o segundo número: "))

#         resultado = int (numa / numb) 
#         print(f"O resultado é: {resultado}")

#     except ZeroDivisionError:
#         print("Erro: Divisão por zero não é permitida")
   


# divisao()
    

# Combinação try-except-else-finally 


def abrirarquivo():
    try:
        arquivo1 = open("arquivo1.txt", "r")
        print(arquivo1.read())
        
    except FileNotFoundError:
        print("O arquivo não foi encontrado")
    else:
       print(f"O arquivo foi encontrado")
    finally:
        print("Fim da tentativa de acesso ao arquivo.")

abrirarquivo()


# Exceção Personalizada e raise 


# class IdadeInvalidaError(Exception):
#     pass

# def recebaidade(idade):
#     if idade < 0:
#         raise  IdadeInvalidaError("A idade não pode ser negativa")
#     elif  idade >= 18 :
#         print("Você é maior de idade")
#     else:
#         print("Você é menor de idade")
# try:
#     idade = int(input("Digite a idade"))
#     recebaidade(idade)

# except  IdadeInvalidaError as e :
#     print(f"Erro : {e}")




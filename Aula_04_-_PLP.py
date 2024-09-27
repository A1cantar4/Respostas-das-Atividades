#Eae my love, Ele quer que você crie um app de "banco"
#Fazer depósitos, saques (se tiver grana)
#e exibir o saldo atual

#"class" é o que define uma "classe", as classes permitem criar coisas com comportamentos,
#a classe "BancodeHadriely" vai representar uma conta bancária

#quando definisse uma função (def) para uma classe, deve ser atribuido
# um método construtor da classe, que no caso é o __init__. Ele vai iniciar os dados do objeto
# no caso, o saldo, que vai ser 0.

# já self é pra representar a classe anterior, no caso o banco.

class HadrielyBanco:
    def __init__(self):
        self.saldo = 0  # Saldo inicial é 0, a não ser que você seja burguesa

    def depositar(self, valor): #define a função depositar 
        if valor > 0: #ou seja, se o valor escrito for positivo, vai adicionar ao saldo atual (que é 0)
            self.saldo += valor
            print(f"Depósito no valor de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.") #caso digite algo q não seja positivo

    def sacar(self, valor): #definindo a função sacar (que vai usar a classe Banco pra verificar o valor)
        if valor > 0: # se valor for maior que zero ele vai criar duas instancias
            if valor <= self.saldo: # se for igual ao saldo atual ou menor, vai efetuar o saque
                self.saldo -= valor # efetuando "-="
                print(f"Saque no valor de R${valor:.2f} realizado com sucesso!")
            else: #aqui é caso o valor seja diferente de Menor ou Igual (ou seja, maior)
                print("Saldo insuficiente para realizar o saque.")
        else: #caso o valor não seja nem menor, nem maior, nem igual, ou seja, "0"
            print("Digite um número válido para saque.")
    
    def mostrar_o_saldo(self): #ele vai exibir a classe (que é o valor)
        print(f"Seu saldo atual: R${self.saldo:.2f}") 

conta = HadrielyBanco() #aqui atribui que Conta e Hadriely banco é a mesma coisa


while True: #aqui ele gera um loop "infinito" até a pessoa escolher a opção
    print("\n1. Depositar dinheiro")
    print("2. Sacar dinheiro")
    print("3. Verificar seu saldo")
    print("4. Sair e Fechar Aplicativo HadrielyBanco")
    opcao = input("Escolha apenas uma opção por vez: ") #mensagem de instrução

    if opcao == '1': #aqui é o que executar conforme foi digitado, e caso erre tem uma mensagem de erro também
        valor = float(input("Digite o valor do depósito: "))
        conta.depositar(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor do saque: "))
        conta.sacar(valor)
    elif opcao == '3':
        conta.mostrar_o_saldo()
    elif opcao == '4':
        print("Saindo do Aplicativo...")
        break
    else:
        print("Opção inválida! Tente novamente.") # caso todos os "SE's" forem digitados errados (os elifs)

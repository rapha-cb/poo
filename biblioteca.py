class Pessoa():
    def __init__(self, peso, nome, idade):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer(self, comida):
        self.comida = comida
        if self.comendo == True:
            print(f"{self.nome} já está comendo" )
        elif self.falando == True:
            print(f"{self.nome} não pode comer pois já está falando")
        elif self.dormindo == True:
            print(f"{self.nome} não pode comer pois está está dormindo ")
        else:
            print(f"como {self.nome} não está fazendo nada, ele começou a comer {self.comida}")
            self.comendo = True


    def falar(self):
        if self.falando == True:
            print(f"{self.nome} já está falando")
        elif self.comendo == True:
            print(f"{self.nome} não pode falar pois está comendo")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar pois está dormindo ")
        else:
            print(f"como {self.nome} não está fazendo nada, ele começou a falar")
            self.falando = True


    def dormir(self):
        if self.dormir == True:
            print(f"{self.nome} já está dormindo")
        elif self.comendo == True:
            print(f"{self.nome} não pode dormir pois está comendo")
        elif self.falando == True:
            print(f"{self.nome} não pode dormir pois está falando ")
        else:
            print(f"como {self.nome} não está fazendo nada, ele começou a dormir")
            self.dormindo = True
    def pararDeComer(self):
        if self.comendo == True:
            print(f"{self.nome} parou de FINALMENTE comer")
            self.comendo = False
        else:
            print(f"{self.nome} não está comendo ")

    def pararDefalar(self):
        if self.falando == True:
            print(f"{self.nome} calou a boca, AMÉM!")
            self.falando = False
        else:
            print(f"{self.nome} não está falando")
    def acordar(self):
        if self.dormindo == True:
            print(f"{self.nome} a bela adormecida acordou! ")
            self.dormindo = False
        else:
            print(f"{self.nome} está acordado")

class ContaBancaria():
    def __init__(self, nome, numero,tipo):
        self.nome = nome
        self.numero = numero
        self.saldo = 0
        self.tipo = tipo
        self.status = False
        self.limite = 0
    def depositar(self, dep):
        if self.status == False:
            print("Sua conta está desativada, não é possível fazer o depósito")
        else:
            self.saldo += dep

    def sacar(self, saque):
        if self.status == False:
            print("Sua conta está desativada, não é possível fazer o saque")
        else:
            if (self.saldo + self.limite)< saque:
                print("não foi possível fazer o saque")
            else:
                self.saldo -= saque


    def ativarConta(self):
        if self.status == False:
            print("sua conta foi ativada")
            self.status = True

        else:
            print("sua conta já está ativa")
    def verificarSaldo(self):
        print(self.saldo)

    def ajustaLimite(self, limite ):
        self.limite += limite
        print(f"limite de {self.limite} ajustado com sucesso!")



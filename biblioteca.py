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

class Animal():
    def __init__(self,nome,cor,comida):
        self.nome = nome
        self.cor = cor
        self.comida = comida


    def comer(self):
        print(f"{self.nome} foi comer ")


class Gato(Animal):
    def __init__(self,nome, cor ,comida):
        super().__init__(nome,cor,comida)
    def Miar(self):
        print(f"{self.nome} foi miando pedindo carinho")

class Vaca(Animal):
    def __init__(self, nome, cor,comida):
        super().__init__(nome,cor,comida)
    def Mugir(self):
        print(f"A {self.nome} mugiu ")
    def comer(self):
        print(f"A {self.nome} foi comer {self.comida}")

class Cachorro(Animal):
    def __init__(self,nome,cor,comida):
        super().__init__(nome,cor,comida)
    def Latir(self):
        print(f"O {self.nome} está latindo muito!")
class Coelho(Animal):
    def __init__(self,nome, cor,comida):
        super().__init__(nome,cor,comida)
    def Pular(self):
        print(f"o {self.nome} está pulando por toda a parte")


class Ingresso():
    def __init__(self, valor):
        self.valor = valor
    def imprimeValor(self):
        print(f"o valor do ingresso é: R${self.valor:.2f} reais ")
class Vip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
    def imprimeValor(self):
        print(f"o valor do ingresso vip é R${self.valor+(self.valor/2):.2f} reais")

class Forma():
    def __init__(self):
        self.area= 0
        self.perimetro = 0
class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    def calculaArea(self,base, altura):
        self.area = base * altura
        print(f"a área do retangulo é: {self.area} cm")
    def calculaPerimetro(self, base, altura):
        self.perimetro= (altura*2)+ (base*2)
        print(f"o perímetro do retangulo é: {self.perimetro} cm")
class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self,base, altura):
        self.area = (base * altura)/2
        print(f"a área do triangulo é: {self.area} cm")

    def calculaPerimetro(self, base):
        self.perimetro= base*3
        print(f"o perímetro do triangulo é: {self.perimetro} cm")

from biblioteca import *


conta01 = ContaBancaria("raphael", 9974, "corrente")
conta01.ativarConta()
conta01.depositar(1000)
conta01.ajustaLimite(1000)

conta01.sacar(1500)
conta01.verificarSaldo()
conta01.depositar(200)
conta01.verificarSaldo()

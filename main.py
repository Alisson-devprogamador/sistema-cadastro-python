class Main:
     pass

print("testando projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente ("joão", "114444-2222")
conta=Conta(c1.nome,6565,0)

print(conta.titular,"numero:" ,conta.numero, "Seu Saldo", conta.saldo)
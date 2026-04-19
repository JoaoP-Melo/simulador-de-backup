from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade  
        self.cpf = cpf


class Usuario(Pessoa):
    def __init__(self, nome, idade, cpf, plano):
        super().__init__(nome, idade, cpf)
        self.plano = plano


class Proxy():
    def __init__(self, usuario):
        self.usuario = usuario

    
    def request(self):
        if self.check() == True:
            return f'Usuario com acesso ao premium'
        else:
            return f'Usuario nao possui acesso ao premium'


    def check(self):
        return self.usuario.plano == 'PREMIUM'


user1 = Usuario('joao', 20, 87589978, 'PREMIUM')
proxy_user1 = Proxy(user1)

user2 = Usuario('pedro', 25, 999978, 'FREE')
proxy_user2 = Proxy(user2)

print(proxy_user1.request())
print()
print(proxy_user2.request())


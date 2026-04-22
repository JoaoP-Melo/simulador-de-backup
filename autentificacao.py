from abc import ABC, abstractmethod
import armazenamentos as am

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
    def __init__(self, usuario, armazenamento):
        self.usuario = usuario
        self.armazenamento =armazenamento


    def salvar(self, file):
        if isinstance(self.armazenamento, am.ArmazenamentoNuvem):
            if self.check() == False:
                return f'O usuario {self.usuario.nome} nao possui acesso ao premium'

        return self.armazenamento.salvar(file)


    def carregar(self):
        if isinstance(self.armazenamento, am.ArmazenamentoNuvem):
            if self.check() == False:
                return f'O usuario {self.usuario.nome} nao possui acesso ao premium', []
            else:
                return self.armazenamento.carregar()
        
        if isinstance(self.armazenamento, am.ArmazenamentoLocal):
            return f'O usuario {self.usuario.nome} nao possui acesso para carregar aquivos da nuvem', []
            
    
    def request(self):
        if self.check() == True:
            return f'O usuario {self.usuario.nome} esta com acesso ao premium'
        else:
            return f'O usuario {self.usuario.nome} nao possui acesso ao premium'


    def check(self):
        return self.usuario.plano == 'PREMIUM'

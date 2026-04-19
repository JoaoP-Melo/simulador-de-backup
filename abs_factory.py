from abc import ABC, abstractmethod

class AbsFactory(ABC):
    @abstractmethod
    def criar_armazenamento(self):
        pass


class FactoryLocal(AbsFactory):
    def criar_armazenamento(self):
        return ArmazenamentoLocal()
    

class FactoryNuvem(AbsFactory):
    def criar_armazenamento(self):
        return ArmazenamentoNuvem(limite=1000)


class Armazenamento(ABC):
    @abstractmethod
    def salvar(self, file):
        pass
    

    @abstractmethod
    def carregar(self, file):
        pass


class ArmazenamentoLocal(Armazenamento):
    def salvar(self, file):
        return f'Arquivo salvado localmente com sucesso'
    

    def carregar(self, file):
        return f'Arquivo carregado localmente com sucesso'


class ArmazenamentoNuvem(Armazenamento):
    def __init__(self, limite):
        self.limite = limite


    def salvar(self, file):
        if len(file) > self.limite:
            return "Arquivo muito grande"
        return "Arquivo salvo na nuvem com sucesso"
    

    def carregar(self, file):
        return f'Arquivo carregado localmente com sucesso'

fabrica_local = FactoryLocal()
storage_local = fabrica_local.criar_armazenamento()

print()

print(storage_local.salvar('arquivo.txt'))
print(storage_local.carregar('arquivo.txt'))
print()

fabrica_nuvem = FactoryNuvem()
storage_nuvem = fabrica_nuvem.criar_armazenamento()

print(storage_nuvem.salvar('arquivo.txt'))
print(storage_nuvem.carregar('arquivo.txt'))
print()



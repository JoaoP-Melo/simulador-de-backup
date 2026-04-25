from abc import ABC, abstractmethod

class Factory(ABC):
    @abstractmethod
    def criar_armazenamento(self):
        pass


class FactoryLocal(Factory):
    def criar_armazenamento(self):
        return ArmazenamentoLocal()
    

class FactoryNuvem(Factory):
    def criar_armazenamento(self):
        return ArmazenamentoNuvem(limite=3)


class Armazenamento(ABC):
    def __init__(self):
        self.conteudo = []

    @abstractmethod
    def salvar(self, file):
        pass
    

    @abstractmethod
    def carregar(self, file):
        pass


class ArmazenamentoLocal(Armazenamento):
    def __init__(self):
        super().__init__()


    def salvar(self, mementos):
        self.conteudo = mementos
        return f'O backup foi salvo localmente com sucesso'
    

    def carregar(self, pasta_vazia):
        if self.conteudo:
            mensagem_t = f'O arquivo foi carregado localmente com sucesso'
            pasta_vazia = self.conteudo
            return mensagem_t , pasta_vazia
        else:
            mensagem_f = f'Nao tem nada armazenado localmente'
            return mensagem_f, pasta_vazia


class ArmazenamentoNuvem(Armazenamento):
    def __init__(self, limite):
        self.limite = limite


    def salvar(self, mementos):
        if len(mementos) > self.limite:
            return f'O backup esta muito grande para ser salvo na nuvem'
        
        self.conteudo = mementos
        return f"O backup foi salvo na nuvem com sucesso"
    

    def carregar(self):
        if self.conteudo:
            mensagem_t = f'O arquivo foi carregado localmente com sucesso'
            pasta_vazia = self.conteudo
            return mensagem_t, pasta_vazia
        else:
            mensagem_f = f'Nao tem nada armazenado na nuvem'
            return mensagem_f, []

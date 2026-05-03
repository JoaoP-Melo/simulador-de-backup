from datetime import datetime


class Arquivo:
    def __init__(self, formato, tamanho, conteudo):
        self.formato = formato
        self.tamanho = tamanho
        self.conteudo = conteudo


class Backup:
    def __init__(self):
        self.backup_arquivos = []

    def adicionar_arquivo(self, arquivo):
        self.backup_arquivos.append(arquivo)
        return f'O arquivo {arquivo.formato} foi adicionado ao backup'

    def save(self):
        return ConcreteMemento(self.backup_arquivos.copy())
    
    def restore(self, memento):
        self.backup_arquivos = memento.get_state()


class ConcreteMemento:
    def __init__(self, state_backup):
        self._state = state_backup
        self._date = str(datetime.now())[:19]

    def get_state(self):
        return self._state

    def get_info(self):
        return f'{self._date}'


class GerenciadorBackup:
    def __init__(self, backup):
        self.backup = backup
        self.mementos = []

    def fazer_backup(self):
        self.mementos.append(self.backup.save())

        return f'O backup foi salvo no sistema com suceso'

    def restaurar_versao(self):
        if len(self.mementos) > 1:  
            self.mementos.pop()
            self.backup.restore(self.mementos[-1])  
            return f'Backup foi restaurado em uma versão anterior'
        else:
            return 'Nenhuma versão anterior disponível para restaurar'

    def imprimir_mementos(self):
        for i in self.mementos:
            print(f'Ponto salvo em: {i.get_info()}') 
            print('Arquivos no backup:')
            for arquivo in i._state:  
                print(f'  formato: {arquivo.formato}')
                print(f'  tamanho: {arquivo.tamanho}')
                print()
                

        

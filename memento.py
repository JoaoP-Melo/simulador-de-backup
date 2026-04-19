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
        return f'Arquivo adicionado ao backup'

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

    def restaurar(self):
        if self.mementos:
            memento = self.mementos.pop()
            self.backup.restore(memento)


backup1 = Backup()
gerente_backup1 = GerenciadorBackup(backup1)

conteudo_txt = ['Ex 1']
txt = Arquivo('txt', len(conteudo_txt), conteudo_txt)

conteudo_pdf = ['Ex 2']
pdf = Arquivo('pdf', len(conteudo_pdf), conteudo_pdf)

print(backup1.adicionar_arquivo(pdf))
gerente_backup1.fazer_backup()

print(backup1.adicionar_arquivo(txt))
gerente_backup1.fazer_backup()

print([a.conteudo for a in backup1.backup_arquivos])
gerente_backup1.restaurar()
gerente_backup1.restaurar()
print([a.conteudo for a in backup1.backup_arquivos])




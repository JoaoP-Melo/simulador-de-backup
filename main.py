import armazenamentos as am
import autentificacao as at
import backup as bp


conteudo_txt = 'Um exemplo de arquivo txt para realizar alguns testes'
arquivo_txt = bp.Arquivo('txt', 101, conteudo_txt)

conteudo_pdf = 'Um documento pdf para realizar testes'
arquivo_pdf = bp.Arquivo('pdf', 60, conteudo_pdf)

backup1 = bp.Backup()
gerente_backup1 = bp.GerenciadorBackup(backup1)

backup2 = bp.Backup()
gerente_backup2 = bp.GerenciadorBackup(backup1)

print('\n========= Teste adicionar arquivo ao backup1 no armazenamento ========= ')
print(backup1.adicionar_arquivo(arquivo_pdf))

print('\n========= Teste salvar backup1 no sistema ========= ')
print(gerente_backup1.fazer_backup())

print('\n========= Teste salvando mais um arquivo parar ter dois pontos no sistema 1 ========= ')
print(backup1.adicionar_arquivo(arquivo_txt))
print(gerente_backup1.fazer_backup())

print('\n========= Teste restaurar backup1 no sistema ========= ')
print(gerente_backup1.restaurar())
print(gerente_backup1.fazer_backup())

print('\n========= Teste imprimindo backup1 ========= ')
print(gerente_backup1.imprimir_mementos())


usuario1 = at.Usuario('Joao', '17', 123456789, 'FREE')
usuario2 = at.Usuario('Pedro', '20', 123456789, 'PREMIUM')

pasta_vazia1 = []
pasta_vazia2 = []

fabrica_local = am.FactoryLocal()
fabrica_nuvem = am.FactoryNuvem()

armazenamento_local = fabrica_local.criar_armazenamento()
armazenamento_nuvem = fabrica_nuvem.criar_armazenamento()

proxy_user1 = at.Proxy(usuario1, armazenamento_nuvem)
proxy_user2 = at.Proxy(usuario2, armazenamento_nuvem)
proxy_user3 = at.Proxy(usuario1, armazenamento_local)
proxy_user4 = at.Proxy(usuario2, armazenamento_local)

print('========= Teste de acesso a funcionalidade salvar na nuvem ========= ')
print(proxy_user1.salvar(gerente_backup1.mementos))
print(proxy_user2.salvar(gerente_backup2.mementos))

print('========= Teste de acesso a funcionalidade salvar na nuvem ========= ')
print(proxy_user3.salvar(gerente_backup1.mementos))
print(proxy_user4.salvar(gerente_backup2.mementos))

print('========= Teste de acesso a funcionalidade carregar ========= ')
msg, pasta_vazia1 = proxy_user1.carregar()
print(msg)
msg, pasta_vazia2= proxy_user2.carregar()
print(msg)


import armazenamentos as am
import autentificacao as at
import backup as bp


conteudo_txt = 'Um exemplo de arquivo txt'
arquivo_txt = bp.Arquivo('txt', 101, conteudo_txt)

conteudo_pdf = 'Um documento pdf'
arquivo_pdf = bp.Arquivo('pdf', 60, conteudo_pdf)

backup = bp.Backup()
gerente_backup1 = bp.GerenciadorBackup(backup)

print('\n========= Retorno ao adicionar arquivo ao backup no armazenamento ========= ')
print(backup.adicionar_arquivo(arquivo_pdf))

print('\n========= Retorno ao salvar backup no sistema ========= ')
print(gerente_backup1.fazer_backup())

print('\n========= Retorno ao salvar mais um arquivo parar ter dois pontos no sistema ========= ')
print(backup.adicionar_arquivo(arquivo_txt))
print(gerente_backup1.fazer_backup())

print('\n========= Retorno ao salvar o mesmo estado ========= ')
print(gerente_backup1.fazer_backup())

print('\n========= Retorno ao restaurar backup no sistema ========= ')
print(gerente_backup1.restaurar_versao())
print(gerente_backup1.fazer_backup())

print('\n========= Retorno ao imprimir backup ========= ')
print(gerente_backup1.imprimir_mementos())


usuario1 = at.Usuario('Joao', '17', 123456789, 'FREE')
usuario2 = at.Usuario('Pedro', '20', 123456789, 'PREMIUM')

pasta_vazia1 = []
pasta_vazia2 = []

fabrica_local = am.FactoryLocal()
fabrica_nuvem = am.FactoryNuvem()

armazenamento_local = fabrica_local.criar_armazenamento()
armazenamento_nuvem = fabrica_nuvem.criar_armazenamento()

proxy_user1 = at.Proxy(usuario2, armazenamento_nuvem)
proxy_user2 = at.Proxy(usuario1, armazenamento_local)

print('========= Retorno do acesso a funcionalidade salvar na nuvem ========= ')
print(proxy_user1.salvar(gerente_backup1.mementos))

print('========= Retorno do acesso a funcionalidade salvar local ========= ')
print(proxy_user2.salvar(gerente_backup1.mementos))

print('========= Retorno do acesso a funcionalidade carregar ========= ')
msg, pasta_vazia1 = proxy_user1.carregar()
print(msg)

msg, pasta_vazia2= proxy_user2.carregar()
print(msg)


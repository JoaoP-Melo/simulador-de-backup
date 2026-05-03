# Simulador de Versionamento de Backups (Python)

Este projeto tem como objetivo demonstrar, de forma prática, a aplicação de padrões de projeto em um cenário simples e didático. A proposta foi desenvolver um simulador de versionamento de backups, utilizando a linguagem Python, aplicando três padrões clássicos: Proxy, Abstract Factory e Memento.

## Padrões de Projeto Utilizados

### Proxy

O padrão Proxy atua como um intermediário no acesso a um objeto, controlando ou otimizando esse acesso. Ele pode ser usado para adicionar segurança, cache ou controle de chamadas sem alterar o objeto original.

### Abstract Factory

O Abstract Factory fornece uma interface para criação de famílias de objetos relacionados, sem especificar suas classes concretas. Isso permite maior flexibilidade e desacoplamento na criação de objetos.

### Memento

O padrão Memento permite salvar e restaurar o estado de um objeto sem violar seu encapsulamento. É ideal para implementar funcionalidades como desfazer/refazer ou controle de versões.

## Contexto do Projeto

O sistema simula um gerenciador de backups versionados, onde:

* Arquivos podem ser criados por meio de classes
* Estados anteriores podem ser salvos e restaurados
* O acesso a determinadas operações pode ser controlado
* Diferentes tipos de armazenamentos podem ser usados

Cada padrão foi aplicado com um propósito específico dentro desse contexto:

* Memento foi responsável por salvar e restaurar versões dos arquivos
* Proxy utilizado para controlar o acesso às operações de backup
* Abstract Factory foi utilizado para criar estruturas de armazenamentos


## Objetivo

Demonstrar na prática como padrões de projeto ajudam:

* Melhorar a organização do código
* Reduzir acoplamento
* Facilitar manutenção e evolução do sistema
* Tornar o código mais reutilizável

## Tecnologias

* Python 3.x

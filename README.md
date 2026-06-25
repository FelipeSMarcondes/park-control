### NAG DEVELOPMENT ARCHIVE

Projeto: Park Control System

Classificação: Sistema de Gerenciamento de Estacionamento

Status: Em Desenvolvimento

Versão Atual: 1.2

---

### Descrição

O Park Control é um sistema de gerenciamento de estacionamento desenvolvido para estudos e aplicações práticas de conceitos de programação, banco de dados e desenvolvimento de software.

O projeto foi desenvolvido utilizando python e SQLite, permitindo o controle de entrada e saída de veículos através da geração e validação de tickets.

O objetivo do projeto é servir como ambiente de aprendizado para desenvolvimento, banco de dados e boas práticas de software.

---

### Tecnologia Utilizadas

- Python
- SQLite
- UUID
- Datetime

---

### Funcionalidades Atuais

- Geração automática de tickets
- Registro de entrada de veículos
- Validação de tickets 
- Controle de saída de veículos
- Persistência de dados em SQLite
- Listagem de registros
- Bloqueio de múltiplos tickets ativos para a mesma placa

---

### Registro de Versão

Versão 1.0

Primeira versão funcional do sistema contendo:

- Estrutura inicial do banco de dados
- Sistema de geração de tickets
- Validação de tickets
- Controle de saída baseado em regras de permanência
- Registro persistente em SQLite

Versão 1.1

Correção e melhorias implementadas:

- Correção do controle de tickets ativos
- Bloqueio de múltiplos tickets para a mesma placa
- Correção do fluxo de liberação de saída
- Ajuste na exibição de status
- Testes funcionais realizados

Status: Estável

---

### Registro de Correções

PC-001

Problema identificado:

Uma mesma placa podia possuir múltiplos tickets ativos simultaneamente.

Status:

Resolvido na versão 1.1

PC-002

Problema identificado:

Inconsistências na exibição da listagem de tickets.

Status:

Resolvido na versão 1.1

PC-003

Problema identificado:

Falhas no fluxo de liberação de saída.

Status:

Resolvido na versão 1.1

---

### Atualizações Planejadas

Versão 1.2

- Validação de formatos de placas
- Consulta por placa
- Melhor tratamento de entradas inválidas

Versão 2.0

- Refatoração da arquitetura do projeto
- Separação em modulos
- Implementação de programação orientada a objetos

Versão 3.0

- Interface gráfica

---

### Desenvolvedor Responsável

Felipe de Siqueira Marcondes

Estudante de Análise e Desenvolvimento de Sistemas
Estagiário de Tecnologia da Informação
Desenvolvedor Python em formação

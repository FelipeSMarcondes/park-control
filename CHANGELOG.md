### CHANGELOG
Projeto: Park Control System

Arquivo de Controle de Alterações

Classificação: NAG - Registro de Evolução do Sistema

### Versão 1.1

Data de Liberação: 18/06/2026

Status: Implementada

Correções Realizadas

### PC-001

Descrição:

Identificado comportamento que permitia a existência de múltiplos tickets ativos para uma mesma placa.

Ação Corretiva:

Implementada validação para impedir a geração de novos tickets enquanto houver ticket ativo associado ao veículo.

Status:

Resolvido.

### PC-002

Descrição:

Identificadas inconsistências na exibição do status dos tickets durante consultas e listagens.

Ação Corretiva:

Ajustado o processo de exibição para garantir a apresentação correta das informações registradas no banco de dados.

Status:

Resolvido.

### PC-003

Descrição:

Identificadas falhas no fluxo de liberação de saída dos veículos.

Ação Corretiva:

Reestruturadas as validações relacionadas ao encerramento dos tickets e autorização de saída.

Status:

Resolvido.

### Resultado da Versão

Maior estabilidade do sistema.
Melhor controle das regras de negócio.
Redução de inconsistências operacionais.
Aprimoramento da confiabilidade dos registros.

### Versão 1.0

Data de Liberação: Junho/2026

Status: Implementada

Implementações Iniciais

### PC-000

Descrição:

Criação da primeira versão funcional do sistema Park Control.

Funcionalidades implementadas:

Estrutura inicial do banco de dados SQLite.
Geração automática de tickets.
Registro de entrada de veículos.
Validação de tickets.
Controle de saída de veículos.
Persistência de dados.
Listagem de registros cadastrados.

Resultado:

Primeira versão operacional do sistema disponibilizada para testes e validação.

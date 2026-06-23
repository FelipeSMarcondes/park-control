### BUGS

Projeto: Park Control System

Registro de Problemas Conhecidos

Classificação: NAG - Registro de Ocorrências Técnicas

---

### PC-001

Data de Identificação: Junho/2026

Status: Resolvido

Versão Afetada: 1.0

Descrição:

Uma mesma placa podia possuir múltiplos tickets ativos simultaneamente.

Impacto Operacional:

- Duplicidade de registros.
- Inconsistência no controle de veículos.

Correção Aplicada:

Versão 1.1

---

###  PC-002

Data de Identificação: Junho/2026

Status: Resolvido

Versão Afetada: 1.0

Descrição:

Inconsistências na exibição do status dos tickets durante consultas e listagens.

Impacto Operacional:

- Informações incorretas para o operador.
- Dificuldade de auditoria.

Correção Aplicada:

Versão 1.1

---

### PC-003

Data de Identificação: Junho/2026

Status: Resolvido

Versão Afetada: 1.0

Descrição:

Falhas no fluxo de liberação de saída dos veículos.

Impacto Operacional:

- Possibilidade de encerramento incorreto de tickets.
- Inconsistências operacionais.

Correção Aplicada:

Versão 1.1

---

### PC-004

Data de Identificação: Junho/2026

Status:  Correção em Andamento

Versão Afetada: 1.1

Descrição:

Identificado comportamento que permite a validação de tickets já finalizados.

Cenário Observado:

1. Ticket é validado.
2. Veículo realiza saída.
3. Ticket recebe status de finalizado.
4. O sistema ainda permite nova validação.

Impacto Operacional:

- Quebra da regra de negócio.
- Inconsistência dos registros.

Correção Planejada:

Versão 1.2

Classificação:

Crítica

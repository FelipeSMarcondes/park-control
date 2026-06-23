###  TESTS

Projeto: Park Control System

Registro de Testes Operacionais

Classificação: NAG - Garantia de Qualidade

---

### TS-001

Objetivo

Verificar bloqueio de múltiplos tickets ativos para uma mesma placa.

Primeira Execução

Versão:

1.0

Resultado:

Falha

Ocorrência Gerada:

PC-001

Descrição:

O sistema permitia gerar múltiplos tickets ativos para a mesma placa.

---

Reteste

Versão:

1.1

Resultado:

Sucesso

Descrição:

Após a correção do PC-001, o sistema passou a impedir a geração de tickets duplicados.

---

### TS-002

Objetivo

Validar fluxo de saída dentro do período de tolerância.

Versão:

1.1

Resultado:

Sucesso

Descrição:

Sistema permitiu a liberação da saída conforme esperado.

---

### TS-003

Objetivo

Validar ticket já finalizado.

Versão:

1.1

Resultado:

Falha

Ocorrência Gerada:

PC-004

Descrição:

O sistema permitiu validar novamente um ticket já encerrado.

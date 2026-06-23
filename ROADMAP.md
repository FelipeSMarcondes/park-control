### ROADMAP

### Projeto: Park Control System

Documento de Planejamento Estratégico

Classificação: NAG - Planejamento de Evolução do Sistema

---

### Convenções de Classificação

Os códigos utilizados neste documento seguem um padrão interno para organização e rastreabilidade das funcionalidades do sistema.

PC    - Correções de Problemas (Problem Correction)

PA    - Auditoria Operacional (Parking Audit)

PQ    - Consultas e Pesquisas (Parking Query)

PD    - Dashboard e Indicadores (Parking Dashboard)

PT    - Tarifação e Cobrança (Parking Tariff)

PS    - Segurança do Sistema (Parking Security)

PLC   - Registro de Logs (Parking Logging)

PRE   - Relatórios e Exportações (Parking Reports)

PTST  - Testes e Garantia de Qualidade (Parking Testing)

PR    - Refatoração e Organização de Código (Project Refactoring)

PV    - Evolução Arquitetural (Project Versioning)

PAPI  - APIs e Integrações Externas (Parking API)

PG    - Gestão de Vagas (Parking Garage)

PHW   - Hardware e Sensores (Parking Hardware)

PAI   - Inteligência Artificial (Parking Artificial Intelligence)

---

### Versão 1.2

Status: Planejada

Objetivo:

Aprimorar a confiabilidade operacional do sistema e expandir os recursos de consulta.

### Correções Programadas
### PC-004

Descrição:

Identificado comportamento que permite a validação de tickets já finalizados.

Ação Planejada:

Implementar validação para impedir a revalidação de tickets encerrados.

Status:

Planejado.

### PC-005

Descrição:

Reserva destinada a futuras correções identificadas durante os ciclos de testes da versão 1.1.

Ação Planejada:

Definição após identificação de novos comportamentos inesperados.

Status:

Reservado.

---

### Melhorias Planejadas
### PQ-001

Descrição:

Implementação de consulta de tickets por placa.

Objetivo:

Facilitar a localização de registros associados a veículos específicos.

Status:

Planejado.

### PQ-002

Descrição:

Implementação de consulta de tickets por código.

Objetivo:

Permitir localização rápida de registros através do identificador único do ticket.

Status:

Planejado.

### PA-001

Descrição:

Registrar motivo da saída do veículo.

Objetivo:

Melhorar a auditoria operacional.

Status:

Planejado.

### PA-002

Descrição:

Registrar tempo total de permanência do veículo.

Objetivo:

Facilitar análises operacionais.

Status:

Planejado.

Resultado Esperado:

Maior controle operacional.

Melhoria na rastreabilidade dos registros.

Aumento da confiabilidade das consultas.

---

### Versão 1.2.1

Status: Em planejamento

Objetivo:

Melhorar a visualização e organização dos registros operacionais.

### Melhorias Planejadas
### PQ-003

Descrição:

Filtro para exibição exclusiva de tickets ativos.

Status:

Planejado.

### PQ-004

Descrição:

Filtro para exibição exclusiva de tickets finalizados.

Status:

Planejado.

### PQ-005

Descrição:

Melhoria na organização visual das listagens.

Status:

Planejado.

Resultado Esperado:

Maior agilidade nas consultas.

Melhor experiência operacional.

---

###Versão 1.2.2

Status: Em planejamento

Objetivo:

Implementar monitoramento operacional através de indicadores internos.

### Dashboard Operacional
### PD-001

Descrição:

Contador de veículos ativos.

Status:

Planejado.

### PD-002

Descrição:

Contador de veículos finalizados.

Status:

Planejado.

### PD-003

Descrição:

Contador de vagas disponíveis.

Status:

Planejado.

### PD-004

Descrição:

Tempo médio de permanência.

Status:

Planejado.

Resultado Esperado:

Melhor acompanhamento da operação em tempo real.

---

### Versão 1.3

Status: Em planejamento

Objetivo:

Preparar a arquitetura do sistema para futuras expansões.

### Refatoração Estrutural
### PR-001

Descrição:

Separação dos componentes do sistema em módulos independentes.

Status:

Planejado.

### PR-002

Descrição:

Criação dos módulos:

database.py

tickets.py

consultas.py

dashboard.py

utils.py

config.py

Status:

Planejado.

Resultado Esperado:

Maior organização do código.

Facilidade de manutenção.

Melhor escalabilidade do projeto.

---

### Versão 1.4

Status: Em planejamento

Objetivo:

Implementar sistema de tarifação.

### Sistema de Cobrança
### PT-001

Configuração de preços.

Status:

Planejado.

### PT-002

Cobrança por hora.

Status:

Planejado.

### PT-003

Cobrança por fração.

Status:

Planejado.

### PT-004

Tempo de tolerância configurável.

Status:

Planejado.

### PT-005

Tratamento de ticket perdido.

Status:

Planejado.

### PT-006

Cadastro de mensalistas.

Status:

Planejado.

Resultado Esperado:

Preparação para uso comercial.

---

### Versão 1.5

Status: Em planejamento

Objetivo:

Implementar segurança operacional.

### Segurança
### PS-001

Login de operadores.

Status:

Planejado.

### PS-002

Perfil administrador.

Status:

Planejado.

### PS-003

Controle de permissões.

Status:

Planejado.

### PS-004

Troca de senha.

Status:

Planejado.

### PS-005

Registro de acessos.

Status:

Planejado.

---

### Versão 1.6

Status: Em planejamento

Objetivo:

Implementar rastreabilidade completa do sistema.

### Logs
### PLC-001

Registrar entradas.

Status:

Planejado.

### PLC-002

Registrar saídas.

Status:

Planejado.

### PLC-003

Registrar validações.

Status:

Planejado.

### PLC-004

Registrar erros.

Status:

Planejado.

### PLC-005

Registrar exclusões.

Status:

Planejado.

---

### Versão 1.7

Status: Em planejamento

Objetivo:

Implementar geração de relatórios.

### Relatórios
### PRE-001

Relatório diário.

PRE-002

Relatório mensal.

### PRE-003

Exportação CSV.

### PRE-004

Exportação Excel.

### PRE-005

Exportação PDF.

### PRE-006

Relatório de faturamento.

---

### Versão 1.8

Status: Em planejamento

Objetivo:

Padronizar testes do sistema.

### Testes
### PTST-001

Testes manuais.

### PTST-002

Testes automatizados.

### PTST-003

Testes de regressão.

### PTST-004

Cobertura de código.

---

### Versão 2.0

Status: Em planejamento

Objetivo:

Modernizar a arquitetura do sistema.

### Evolução Arquitetural
### PV-001

Implementação de POO.

### PV-002

Reestruturação da arquitetura.

### PV-003

Reaproveitamento de código.

Resultado Esperado:

Arquitetura robusta.

Escalabilidade.

---

### Versão 2.5

Status: Em planejamento

Objetivo:

Disponibilizar integração externa.

### API
### PAPI-001

API REST.

### PAPI-002

Consultar tickets.

### PAPI-003

Gerar tickets.

### PAPI-004

Dashboard API.

---

### Versão 3.0

Status: Em fase de estudo 

Objetivo:

Gerenciamento inteligente de vagas.

### Gestão de Vagas
### PG-001

Cadastro de vagas.

### PG-002

Vinculação entre ticket e vaga.

### PG-003

Controle de ocupação.

### PG-004

Mapa visual do estacionamento.

### PG-005

Dashboard de vagas.

Resultado Esperado:

Controle avançado.

Maior organização operacional.

---

### Versão 4.0

Status: Em fase de estudo

Objetivo:

Implementar Smart Parking.

### Sensores
###PHW-001

Sensor ultrassônico.

### PHW-002

Sensor magnético.

### PHW-003

Sensor de pressão.

### PHW-004

ESP32.

### OCR
### PAI-001

Leitura automática de placas.

### PAI-002

OpenCV.

### PAI-003

EasyOCR.

---

### Versão 5.0

Status: Em fase de estudo

Objetivo:

Transformar o Park Control em uma plataforma inteligente baseada em IA.

### Smart Parking AI
### PAI-004

Validação automática placa-vaga.

### PAI-005

Detecção de veículo em vaga incorreta.

### PAI-006

Alerta em tempo real para operador.

### PAI-007

Predição de ocupação.

### PAI-008

Machine Learning para análise operacional.

Resultado Esperado:

Estacionamento autônomo.

Monitoramento inteligente.

Integração IoT.

Preparação para aplicações em larga escala.

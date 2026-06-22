import sqlite3
from datetime import datetime
import uuid


# ======================
# BANCO DE DADOS
# ======================

conn = sqlite3.connect("estacionamento.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT,
    placa TEXT,
    entrada TEXT,
    validado INTEGER,
    saida TEXT
)
""")

conn.commit()


# ======================
# GERAR TICKET
# ======================

def gerar_ticket():

    print("\nExemplo de placa:")
    print("ABC1234")
    print("BRA2E19\n")

    placa = input("Digite a placa do carro: ").strip().upper()

    # Verifica se a placa já possui ticket ativo
    cursor.execute("""
        SELECT codigo
        FROM tickets
        WHERE placa = ?
        AND saida IS NULL
    """, (placa,))

    ticket_ativo = cursor.fetchone()

    if ticket_ativo:

        print("\n======================")
        print("TICKET JÁ EXISTE")
        print("======================")
        print("Placa :", placa)
        print("Código:", ticket_ativo[0])
        print("Veículo já está estacionado.")
        print("======================\n")

        return

    codigo = str(uuid.uuid4())[:8].upper()

    entrada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    cursor.execute("""
        INSERT INTO tickets (
            codigo,
            placa,
            entrada,
            validado,
            saida
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        codigo,
        placa,
        entrada,
        0,
        None
    ))

    conn.commit()

    print("\n======================")
    print("TICKET GERADO")
    print("======================")
    print("Código :", codigo)
    print("Placa  :", placa)
    print("Entrada:", entrada)
    print("======================\n")


# ======================
# VALIDAR TICKET
# ======================

def validar_ticket():

    codigo = input("Digite o código do ticket: ").strip().upper()

    cursor.execute("""
        SELECT validado
        FROM tickets
        WHERE codigo = ?
    """, (codigo,))

    ticket = cursor.fetchone()

    if not ticket:
        print("\nTicket não encontrado!\n")
        return

    if ticket[0] == 1:
        print("\nTicket já validado!\n")
        return

    cursor.execute("""
        UPDATE tickets
        SET validado = 1
        WHERE codigo = ?
    """, (codigo,))

    conn.commit()

    print("\nTicket validado!\n")


# ======================
# LIBERAR SAÍDA
# ======================

def liberar_saida():

    codigo = input("Digite o código do ticket: ").strip().upper()

    cursor.execute("""
        SELECT placa, entrada, validado, saida
        FROM tickets
        WHERE codigo = ?
    """, (codigo,))

    ticket = cursor.fetchone()

    if not ticket:
        print("\nTicket não encontrado!\n")
        return

    placa, entrada, validado, saida = ticket

    # Já saiu
    if saida is not None:
        print("\nVeículo já deixou o estacionamento.\n")
        return

    entrada_data = datetime.strptime(
        entrada,
        "%d/%m/%Y %H:%M:%S"
    )

    agora = datetime.now()

    minutos = (
        agora - entrada_data
    ).total_seconds() / 60


    if minutos <= 20:

        liberado = True
        motivo = "Menos de 20 minutos"

    elif validado == 1:

        liberado = True
        motivo = "Ticket validado"

    else:

        liberado = False
        motivo = "Necessário pagamento"


    if liberado:

        horario_saida = agora.strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        cursor.execute("""
            UPDATE tickets
            SET saida = ?
            WHERE codigo = ?
        """, (
            horario_saida,
            codigo
        ))

        conn.commit()

        print("\n======================")
        print("SAÍDA LIBERADA")
        print("======================")
        print("Placa :", placa)
        print("Motivo:", motivo)
        print("Saída :", horario_saida)
        print("======================\n")

    else:

        print("\n======================")
        print("SAÍDA BLOQUEADA")
        print("======================")
        print("Placa :", placa)
        print("Motivo:", motivo)
        print("======================\n")


# ======================
# LISTAR TICKETS
# ======================

def listar_tickets():

    cursor.execute("""
        SELECT codigo,
               placa,
               entrada,
               validado,
               saida
        FROM tickets
        ORDER BY id DESC
    """)

    tickets = cursor.fetchall()

    print("\n======================")
    print("TICKETS")
    print("======================")

    if not tickets:
        print("Nenhum ticket encontrado.")
        return

    for ticket in tickets:

        codigo, placa, entrada, validado, saida = ticket


        if saida:
            status = "FINALIZADO"

        elif validado:
            status = "VALIDADO"

        else:
            status = "PENDENTE"


        saida_exibir = saida if saida else "-"


        print(f"""
Código : {codigo}
Placa  : {placa}
Entrada: {entrada}
Status : {status}
Saída  : {saida_exibir}
----------------------
""")


# ======================
# SISTEMA
# ======================

print("""
==================================
      PARK CONTROL SYSTEM
         Versão 1.1
==================================

Sistema iniciado com sucesso!

Exemplos de placas:
ABC1234
BRA2E19

Novidade da versão 1.1:
✔ Uma placa não pode possuir
  dois tickets ativos.

==================================
""")


# ======================
# MENU
# ======================

while True:

    print("""
1 - Gerar Ticket
2 - Validar Ticket
3 - Liberar Saída
4 - Listar Tickets
0 - Sair
""")

    opcao = input("Escolha: ").strip()

    if opcao == "1":

        gerar_ticket()

    elif opcao == "2":

        validar_ticket()

    elif opcao == "3":

        liberar_saida()

    elif opcao == "4":

        listar_tickets()

    elif opcao == "0":

        print("\nSistema encerrado!")

        conn.close()

        break

    else:

        print("\nOpção inválida!\n")

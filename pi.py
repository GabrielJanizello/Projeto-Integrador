from datetime import datetime, timedelta

# Lista para armazenar os agendamentos
agenda = []

# Função para adicionar um agendamento
def adicionar_agendamento(nome_cliente, servico, data, hora):
    agendamento = {
        "nome_cliente": nome_cliente,
        "servico": servico,
        "data": data,
        "hora": hora,
    }
    agenda.append(agendamento)
    print(f"Agendamento para {nome_cliente} no serviço {servico} adicionado para {data} às {hora}.")

# Função para listar todos os agendamentos
def listar_agendamentos():
    if not agenda:
        print("Nenhum agendamento encontrado.")
    else:
        print("Agendamentos:")
        for idx, agendamento in enumerate(agenda, start=1):
            print(f"{idx}. {agendamento['data']} às {agendamento['hora']} - {agendamento['nome_cliente']} ({agendamento['servico']})")

# Função para remover um agendamento
def remover_agendamento(index):
    try:
        removed = agenda.pop(index - 1)
        print(f"Agendamento para {removed['nome_cliente']} removido com sucesso.")
    except IndexError:
        print("Agendamento não encontrado.")

# Função para verificar se um horário está disponível
def verificar_disponibilidade(data, hora):
    for agendamento in agenda:
        if agendamento["data"] == data and agendamento["hora"] == hora:
            return False
    return True

# Exemplo de uso
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar Agendamento")
    print("2. Listar Agendamentos")
    print("3. Remover Agendamento")
    print("4. Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        nome_cliente = input("Nome do Cliente: ")
        servico = input("Serviço: ")
        data = input("Data (dd/mm/yyyy): ")
        hora = input("Hora (hh:mm): ")
        
        # Verifica disponibilidade
        if verificar_disponibilidade(data, hora):
            adicionar_agendamento(nome_cliente, servico, data, hora)
        else:
            print("Horário indisponível.")
    
    elif opcao == "2":
        listar_agendamentos()
        
    elif opcao == "3":
        listar_agendamentos()
        index = int(input("Número do agendamento a remover: "))
        remover_agendamento(index)
        
    elif opcao == "4":
        print("Saindo da agenda...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
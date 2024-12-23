import socket
from datetime import datetime

# Função para desenhar a porta aberta em ASCII
def porta_aberta():
    porta = '''
         _______
        |       |
        |   O   |
        |       |
        |_______|
        /       \
       /         \
      /___________\
    '''
    print(porta)

# Função para escanear uma faixa de portas
def escanear_portas(host, portas):
    portas_abertas = []
    for porta in portas:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Tempo de espera de 1 segundo para conexão
        resultado = s.connect_ex((host, porta))
        if resultado == 0:
            print(f"Porta {porta} está ABERTA.")
            portas_abertas.append(porta)
        s.close()
    return portas_abertas

# Função para escanear um host e um intervalo de portas
def escanear_host(host, inicio_porta, fim_porta):
    print("-" * 50)
    print(f"Escaneamento de portas no host: {host}")
    print(f"Escaneando da porta {inicio_porta} até a porta {fim_porta}")
    
    portas = range(inicio_porta, fim_porta + 1)
    portas_abertas = escanear_portas(host, portas)
    
    if len(portas_abertas) == 0:
        print("Nenhuma porta aberta encontrada.")
    else:
        print("Portas abertas:", portas_abertas)
    print("-" * 50)

# Função principal
if __name__ == "__main__":
    # Exibir a porta aberta em ASCII
    porta_aberta()

    # Solicitar o host alvo
    host = input("IP ou HOST alvo: ")
    inicio_porta = int(input("Porta inicial: "))
    fim_porta = int(input("Porta final: "))
    
    # Iniciar o escaneamento
    print("\nEscaneando... ")
    inicio_tempo = datetime.now()
    escanear_host(host, inicio_porta, fim_porta)
    fim_tempo = datetime.now()
    duracao = fim_tempo - inicio_tempo
    print(f"Escaneamento concluído em {duracao} segundos.")


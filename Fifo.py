#Implementação da atividade utilizando o algoritmo FIFO (First-in, first-out, fila)

import random

processos = []
N = int(input("Digite o número de processos: "))  
tempo_troca = 1


for i in range(N):
    tempo_chegada = random.randint(1, 10)
    tempo_execucao = random.randint(1, 10)
    processos.append({
        'id': i + 1,
        'tempo_chegada': tempo_chegada,
        'tempo_execucao': tempo_execucao
    })


for j in range(len(processos) - 1):
    for k in range(len(processos) - j - 1):
        if processos[k]['tempo_chegada'] > processos[k + 1]['tempo_chegada']:
            processos[k], processos[k + 1] = processos[k + 1], processos[k]

tempo_atual = 0
tempos_retorno = []
tempos_espera = []
tempos_chegada = []
tempo_ociosidade = 0

print("Escalonamento FIFO")

for processo in processos:
    if tempo_atual < processo['tempo_chegada']:
        tempo_ociosidade += processo['tempo_chegada'] - tempo_atual
        tempo_atual = processo['tempo_chegada']
    
    inicio = tempo_atual
    fim = inicio + processo['tempo_execucao']
    tempo_retorno = fim - processo['tempo_chegada']
    tempo_espera = inicio - processo['tempo_chegada']
    
    tempos_retorno.append(tempo_retorno)
    tempos_espera.append(tempo_espera)
    tempos_chegada.append(processo['tempo_chegada'])
    tempo_atual = fim + tempo_troca


    print(f"ID: {processo['id']}, Tempo de Chegada: {processo['tempo_chegada']}, Tempo de Execução: {processo['tempo_execucao']}, Início: {inicio}, Fim: {fim}, Retorno: {tempo_retorno}, Tempo de Espera: {tempo_espera}")


media_tempo_chegada = sum(tempos_chegada) / N
media_tempo_retorno = sum(tempos_retorno) / N
media_tempo_espera = sum(tempos_espera) / N

print(f"Tempo médio de chegada: {media_tempo_chegada:.2f}")
print(f"Tempo médio de retorno: {media_tempo_retorno:.2f}")
print(f"Tempo médio de espera: {media_tempo_espera:.2f}")
print(f"Tempo de ociosidade do processador: {tempo_ociosidade}")
print(f"Tempo total de troca de processos: {tempo_troca * (N - 1)}")

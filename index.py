votantes = int(input("Quantas pessoas irão votar?"))
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
candidato5 = 0

for i in range(votantes):
    voto = int(input("Vote no seu candidato"))
    if(voto == 1):
        candidato1 = candidato1 + 1
    elif(voto == 2):
        candidato2 = candidato2 + 1
    elif(voto == 3):
        candidato3 = candidato3 + 1
    elif(voto == 4):
        candidato4 = candidato4 + 1
    elif(voto == 5):
        candidato5 = candidato5 + 1
    else:
        print("Por favor, digite um número de candidato válido!")

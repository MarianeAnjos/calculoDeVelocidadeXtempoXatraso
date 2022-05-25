
velocidade = int(input("Usuario digite a velocidade do veículo em km/h: "))
kmMedia = float(input("Usuario digite a media de consumo de km/l: "))
tempo = int(input ('Usuario digite o tempo total dirigindo na viagem em horas: '))
atraso = float(input ('Usuatio digite o total de atraso em horas, sem atraso digite'))

distancia =  (tempo - 60 ) * velocidade
distancia = tempo * velocidade
litros = distancia / kmMedia


print("Viajando ", tempo, " horas sera percorrido a distancia de: ", distancia , " km"  )
print("Para viajar ", distancia, " km sera necessario: ", litros , " litros de combustivel")

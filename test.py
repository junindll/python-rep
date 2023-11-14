total = int(input('Digite a duração em segundos: '))
horas = total / 3600
minutos = total / 60
horas_minutos = total % 60
print('{:.0f}:{:.0f}:{:.0f}'.format(horas, minutos, horas_minutos))
numero = input("Por favor, entre com o numero de segundos que deseja converter: ")
total_segs = int(numero)
a = total_segs // 86400
segs_restantes = total_segs % 86400
b = segs_restantes // 3600
segs_restantes_meio = total_segs % 3600
c = segs_restantes_meio // 60
d = segs_restantes_meio % 60

print(a, "dias,", b, "horas,", c, "minutos e", d, "segundos.")
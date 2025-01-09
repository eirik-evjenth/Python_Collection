
lån = 1000000
rente = .03
antall_terminer = 20

# Beregn annuiteten
annuitet = lån * (rente * (1 + rente) ** antall_terminer) / ((1 + rente) ** antall_terminer - 1)

print(f'Annuiteten til lånet er: {annuitet:10.2f}kr')
print(f'Total mengde penger som er betalt er: {annuitet * antall_terminer:10.2f}kr')





'''
print('Termin Lånebeløp Avdrag Rente Restlån')
restlån = lån
for termin in range(antall_terminer):
    rentebeløp = restlån * rente
    avdrag = annuitet - rentebeløp
    print(f'{termin + 1:2}', end=' ')
    print(f'{restlån:10.2f}', end=' ')
    print(f'{avdrag:10.2f}', end=' ')
    print(f'{rentebeløp:8.2f}', end=' ')
    restlån = restlån - avdrag
    print(f'{restlån:10.2f}')
'''
from datetime import datetime

data = datetime.now().strftime(("%d / %m / %Y %H:%M:%S"))


hist_extrato = [[123, '17 / 05 / 2023 16:02:21', 'Criou a conta', 1000, 0, 1000, '17 / 05 / 2023 16:02:27', 'debito', -500, 25.0, 475.0, '17 / 05 / 2023 16:02:35', 'deposito', 100, 0, 575.0]]
cliente = ['hugo', 123, 1, 1000, '123']

print(f'Nome: {cliente[0]}')
print(f'CPF: {cliente[1]}')
if cliente[3] == 1:
    print('Conta: Comum')
else:
        print('Conta: Plus')
for i in range(len(hist_extrato)):
    for x in range(0, len(hist_extrato[i]) - 1, 5):
        print(f'Data: {hist_extrato[i][1 + x]} | Operaçao: {hist_extrato[i][2 + x]} | Valor: {hist_extrato[i][3 + x]} | Tarifa: {hist_extrato[i][4 + x]} | Saldo: {hist_extrato[i][5 + x]}')
# INICIALIZAÇÃO

'''
# USUÁRIO:
usuario = {}

# - FUNÇÕES ------------------------------------------------------------
def txt_decorado():
    print('=-' * 30)

# FUNÇÃO p/ CADASTRO
def cadastro_usuario():
    senha = ''
    senha_confirmacao = '1'

    nome = input('Digite seu nome de exibição para cadastro: ').strip()
    while senha != senha_confirmacao:
        senha = input('Digite sua senha para registro: ')
        senha_confirmacao = input('Confirme a senha: ')

        if senha == senha_confirmacao:
            usuario[nome] = senha
            break

        print('Confirmação incorreta, tente novamente.')

# ---------------------------------------------------------------------
# CODIFICAÇÃO

# PONTO DE RETORNO PARA PRIMEIRO CADASTRO
while True:
    if len(usuario) == 0:                           # Caso não tenha nenhum registro,
        print('Nenhum usuário cadastrado.')         # o código não prosseguirá até
        print('Cadastre-se a seguir:')              # ter ao menos 1 pessoa cadastrada.
        cadastro_usuario()
    else:
        break

txt_decorado()
if input('Quer se cadastrar? ')[0] in 'Ss':
    txt_decorado()
    cadastro_usuario()

while True:
    txt_decorado()
    nome = input('Nome de exibição: ')
    if nome in usuario.keys():
        if input(f'seu usuário é o: {nome}, certo?').strip()[0] in 'Ss':
            while True:
                if input('Digite a senha: ') == usuario[nome]:
                    print(f'Usuário {nome} está logado.')
                    break
                else:
                    print('Senha incorreta, tente novamente.')
        else:
            print('redirecionando..')
    else:
        print(f'Nome de usuário: {nome}, não encontrado. Tente novamente.')
'''
import time
### SISTEMA ###
from time import sleep
### FUNÇÕES ###

def msg_deco(a):
    print('+=' * 30)
    print(a)
    print('+=' * 30)


# ----------------------------------------------
# Saque
def saque():
    global saldo, qnt_saque, limite_saque, menu
    if qnt_saque >= limite_saque:
        print('Limite de Saque (3) EXCEDIDO.')
        return False
    while True:
        print(f'(Saques restantes:{limite_saque - qnt_saque} )')
        saq = float(input('Quanto deseja sacar? '))

        if saq > saldo:
            print(f'Saldo indisponível, impossível sacar R${saq:.2f}.')
        else:
            saldo -= saq
            extrato.append(f'SAQUE:       -R${saq:.2f}')
            qnt_saque += 1

            print('Saque em andamento, aguarde...')
            sleep(2)
            print(f'Saque de R${saq:.2f} realizado com sucesso.')
            sleep(0.7)
            print(f'Saldo atual: R${saldo:.2f}')
            sleep(1)

            if qnt_saque >= limite_saque:
                break
            if not outro_saque():
                sleep(0.5)
                break
def outro_saque():
    while True:
        a = input('Deseja realizar outro saque? [S/N]\n').lower()
        if a not in 'sn':
            print('Resposta inválida.')
        elif a == 's':
            return True
        else:
            return False

# ----------------------------------------------
# extrato
def exibir_extrato():
    global menu
    print('Seu extrato:\n')
    for transacoes in extrato:
        print(transacoes)
    print()
    print(f'Saldo atual: R${saldo:.2f}')
    sleep(0.4)

# ----------------------------------------------
# Depósito

def deposito(a):
    global saldo, menu

    if 2 < int(time.strftime('%H', time.localtime())) > 22:
        print('Depósito bloqueado por: Horário inadequado.\n'
              'Horário para depósitos: 02h as 22h.')
        sleep(1)
        return False

    while True:
        a = float(input('Qual o valor do depósito? '))

        sleep(0.2)
        print('Validando entrada...')
        sleep(2)

        saldo += a
        extrato.append(f'DEPÓSITO:   +R${a:.2f}')
        print(f'Saldo atual: {saldo:.2f}')
        sleep(0.8)

        if not outro_deposito():
            break
        sleep(0.5)

def outro_deposito():
    while True:
        a = input('Deseja realizar outro depósito? [S/N]\n').lower()
        if a not in 'sn':
            print('Resposta inválida.')
        elif a == 's':
            return True
        else:
            return False


### VARIÁVEIS ###

depos = 0
saldo = 500
extrato = []
qnt_saque = 0
limite_saque = 3
msg = 'SEJA BEM VINDO. Escolha seu serviço:'

menu = ''
while True:
    menu = ''
    while menu != 's' and menu != 'd' and menu != 'e' and menu != '0':
        msg_deco(msg)
        menu = input('[ S ] SACAR\n[ D ] DEPÓSITO\n[ E ] EXTRATO\n[ 0 ] SAIR\n').lower()
        if menu not in 'sde0':
            print('Resposta inválida, escolha seu serviço \ndigitando o caracter dentro dos colchetes.\n')

    if menu == 's':
        saque()

    elif menu == 'e':
        exibir_extrato()

    elif menu == 'd':
        deposito(depos)

    elif menu == '0':
        break

print('Obrigado, até a próxima!')

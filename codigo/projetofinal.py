import mysql.connector

from usuario import Usuario
from pizza import Pizza
from bebidas import Bebidas
from datetime import date
from vendas import Vendas
import os

today = date.today()
print("Today's date:", today)

def pizzaria():
    print('===================================')
    print('        Pizzaria Delivery          ')
    print('===================================')

def menu():
    print('''          MENU:

               [1] - Iniciar Vendas
               [2] - Cadastrar Usuario
               [3] - Total de Vendas
               [4] - Desligar  
                                     ''')

pizzaria()
menu()
n1 = input('Digite uma opção: ')
os.system('cls')
cont01 = 0
cont02 = 0
if (n1 == '1'):

    while True:
        os.system('cls')
        pizzaria()

        inputNomeUsuario = input('Digite seu login: ')

        inputSenha = input('Digite sua senha: ')

        cnx = mysql.connector.connect(host='localhost', database='pizzaria', user='root', password='***')
        cursor = cnx.cursor()
        cursor.execute(
            f'select * from tb_usuarios where login_usuario = "{inputNomeUsuario}"')

        queryResult = cursor.fetchone()
        
        cursor.close()
        cnx.close()

        usuario = Usuario(0, "", "", "")

        if queryResult == None:
            erroUsuario = input("* Usuario incorreto *[Pressione enter]")
            cont01 = cont01 + 1
            if cont01 == 3:
                break
        else:
            usuario = Usuario(
                queryResult[0], queryResult[2], queryResult[3], queryResult[1])

        if inputSenha == usuario.senha:
            print("logado com sucesso! ")

            cnx = mysql.connector.connect(host='localhost', database='pizzaria', user='root', password='***')
            cursor = cnx.cursor()
            cursor.execute("select * from tb_pizza")
            queryResult = cursor.fetchall()
            cursor.close()
            cnx.close()
            print(queryResult)

            pizzas = []

            for i in queryResult:
                pizzas.append(Pizza(i[0], i[1], i[2]))
                os.system('cls')
                pizzaria()

            for pizza in pizzas:
                print(f'{pizza.id}        {pizza.nome}                {pizza.preco}')
                
            cnx = mysql.connector.connect(host='localhost', database='pizzaria', user='root', password='***')
            cursor = cnx.cursor()

            idPizzaSelecionada = input("Digite o numero da pizza: ")

            cursor.execute("select * from tb_bebidas")
            queryResult = cursor.fetchall()
            cursor.close()
            cnx.close()

            bebidas = []

            for i in queryResult:
                bebidas.append(Bebidas(i[0], i[1], i[2]))

            os.system('cls')
            pizzaria()

            for bebida in bebidas:
                print(
                    f'{bebida.id}        {bebida.nome}                {bebida.preco}')
                
            idBebidaSelecionada = input("Digite o numero da bebida: ")

            cnx = mysql.connector.connect(host='localhost', database='pizzaria', user='root', password='***')
            cursor = cnx.cursor()
            nomeCliente = input('Digite o nome do cliente: ')
            dataPedido = date.today()

            add_venda = (f'insert into tb_vendas(id_pizza, totalpagar, nomecliente, id_bebidas, datavenda) values("{pizzas[int(idPizzaSelecionada) - 1].id}", {pizzas[int(idPizzaSelecionada) - 1].preco + bebidas[int(idBebidaSelecionada)-1].preco}, "{nomeCliente}",{bebidas[int(idBebidaSelecionada)-1].id}, now())')
            
            vendaOk = input('Venda finalizada com sucesso! [enter]')

            cursor.execute(add_venda)
            cnx.commit()
            cursor.close()
            cnx.close()

            continuarVenda = input('Gostaria de continuar em vendas? s/n ')
        if continuarVenda == 'n':
                break

        else:
            erroSenha = input(" *Senha incorreta * [Pressione enter]")
            print('')
            cont02 = cont02 + 1
            
            if cont02 == 3:
                break

if (n1 == '2'):
    os.system('cls')
    pizzaria()

    conexao = mysql.connector.connect(host="localhost", user="root", password="***",database="pizzaria")
    cursor = conexao.cursor()

    funcao = input('Digite a função: ')
    login_usuario = input('Digite o usuario: ')
    senha_usuario = input('Digite a senha: ')

    comando = (f'insert into tb_usuarios (funcao, login_usuario, senha_usuario) VALUES ("{funcao}", "{login_usuario}", "{senha_usuario}")')
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

elif (n1 == '3'):
    os.system('cls')
    pizzaria()
    conexao = mysql.connector.connect(host="localhost",user="root",password="***",database="pizzaria")
    cursor = conexao.cursor()
    comando = f'SELECT * FROM tb_vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    vendas = []

    for i in resultado:
        vendas.append(Vendas(i[0], i[1], i[2],i[3], i[4], i[5]))

    cursor.close()
    conexao.close()
    os.system('cls')

    print('id venda      | id bebida     | id pizza     | valor     | clinte      | data     ')
    for venda in vendas:
                print(f'{venda.id}             | {venda.idBebida}             | {venda.idPizza}            | {venda.valor}      | {venda.cliente}       | {venda.data}')
                
else:
    os.system('cls')
    pizzaria()
    print(' Fim do programa! ')
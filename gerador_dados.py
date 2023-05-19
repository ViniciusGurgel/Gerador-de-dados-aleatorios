import mysql.connector
import random
from datetime import datetime, timedelta
from faker import Faker
from banco_gerador import Criar_Banco_de_dados


cnx = mysql.connector.connect(user='root', password='root', host='localhost')
print("Conectado=", cnx.is_connected())

nomes_masculinos = ["Alexandre", "Bruno", "Carlos", "Diego", "Eduardo", "Fábio", "Gustavo", "Henrique", "Igor",
                    "João", "Kleber", "Lucas", "Marcelo", "Nelson", "Otávio", "Pedro", "Rafael", "Sérgio",
                    "Thiago", "Vitor", "Wagner", "Xavier", "Yuri", "Zé"]

sobrenomes_masculinos = ["Silva", "Santos", "Oliveira", "Souza", "Costa", "Pereira", "Rodrigues", "Almeida",
                         "Nascimento", "Fernandes", "Gonçalves", "Carvalho", "Gomes", "Mendes", "Lima", "Araújo",
                         "Ribeiro", "Barbosa", "Martins", "Moreira", "Cardoso", "Teixeira", "Correia", "Cavalcanti",
                         "Ferreira"]

sobrenomes_diferentes = ["Moura", "Menezes", "Castro", "Mello", "Furtado", "Vasconcelos", "Calixto", "Bastos",
                         "Goulart",
                         "Fagundes", "Coutinho", "Lacerda", "Albuquerque", "Prado", "Guimarães", "Pimentel", "Rocha",
                         "Leal", "Fonseca", "Alcântara", "Miranda", "Xavier", "Coelho", "Camargo", "Aragão"]

nomes_femininos = ["Ana", "Bianca", "Camila", "Daniela", "Eduarda", "Fernanda", "Gabriela", "Helena", "Isabela",
                   "Julia",
                   "Kamila", "Larissa", "Mariana", "Nathalia", "Olivia", "Priscila", "Rafaela", "Sophia", "Tatiana",
                   "Valentina",
                   "Agatha", "Beatriz", "Clarissa", "Dandara", "Elisa", "Fabiana", "Gabriella", "Heloísa", "Isadora",
                   "Júlia", "Karina"]


def criar_nome(counter):
    if counter >= 300:
        nomes = random.choice(nomes_masculinos)
    else:
        nomes = random.choice(nomes_femininos)
    sobrenome = random.choice(sobrenomes_masculinos)
    nome_final = random.choice(sobrenomes_diferentes)
    return str((nomes + " " + sobrenome + " " + nome_final))


def gerar_cpf():
    cpf = [random.randint(0, 9) for i in range(9)]

    soma = sum([cpf[i] * (10 - i) for i in range(9)])
    resto = 11 - (soma % 11)
    cpf.append(resto if resto <= 9 else 0)

    soma = sum([cpf[i] * (11 - i) for i in range(10)])
    resto = 11 - (soma % 11)
    cpf.append(resto if resto <= 9 else 0)

    return f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"


def gerar_cnh():
    cnh = ""
    for _ in range(11):
        cnh += str(random.randint(0, 9))
        if _ == 2 or _ == 5:
            cnh += "."
        elif _ == 8:
            cnh += "-"
    return cnh


def gerar_rg():
    rg = ""
    for _ in range(9):
        rg += str(random.randint(0, 9))
    return rg


def gerar_data_nascimento():
    data_minima = datetime.now() - timedelta(days=365 * 100)
    data_maxima = datetime.now() - timedelta(days=365 * 18)
    data = data_minima + (data_maxima - data_minima) * random.random()
    data_str = data.strftime("%Y-%m-%d")

    return data_str


def calcular_idade(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
    hoje = datetime.today()
    diferenca = hoje - data_nascimento
    idade = int(diferenca.days / 365.25)

    return idade


def endereco():
    fake = Faker()
    address = fake.address()
    return address


def CNPJ():
    fake = Faker("pt_BR")
    cnpj = fake.cnpj()
    return cnpj


def Telefone():
    fake = Faker("pt_BR")
    telefone = fake.phone_number()
    return telefone


def pagamento():
    Pagamento = ['Boleto', 'Crédito', 'Débito', 'Pix', 'Dinheiro', 'Cheque']
    return random.choice(Pagamento)


def Plano():
    planos_aluguel = ['Econômico', 'Intermediário', 'Executivo', 'Fim de semana', 'Mensal', 'Fim de ano']
    return random.choice(planos_aluguel)


def Kilometragem():
    quilometragem = random.randint(0, 100000)
    return quilometragem


def preço():
    preço1 = random.randint(200, 500)
    return preço1


def Sigla():
    a = random.randint(0, 24)
    siglas_agencias = ['HRT', 'ALM', 'AVR', 'BUD', 'DRZ', 'EZR', 'FXR', 'GOH', 'HTZ', 'JUC', 'KED', 'LZC', 'MCO', 'NDY',
                       'OKR', 'PTL', 'QEE', 'RNT', 'SXT', 'TYM', 'VNO', 'WEM', 'XTC', 'YPL', 'ZMC']
    nomes_agencias = ['Hertz', 'Alamo', 'Avis', 'Budget', 'Dollar', 'Enterprise', 'Fox', 'Gotham Dream Cars', 'Hertz',
                      'Just 4 Wheels', 'Keddy by Europcar', 'Luzcar', 'MCar', 'National', 'Oakland Airport',
                      'Pitstop Car Rental', 'Queensboro Toyota', 'RentalCars.com', 'Sixt', 'Thrifty',
                      'Value Rent A Car', 'West Coast Rent A Car', 'Xtreme Car Rental', 'Yellowstone Vacations',
                      'Zoom Rent-A-Car']
    return siglas_agencias[a], nomes_agencias[a]


def Contato():
    fake = Faker()
    return fake.email()


def generate_car_plate():
    letters = [chr(random.randint(65, 90)) for _ in range(3)]
    digits = [str(random.randint(0, 9)) for _ in range(4)]
    return "".join(letters + digits)


def create_chassis_numbers():
    digits = [str(random.randint(0, 9)) for _ in range(17)]
    return "".join(digits)


def create_marcas():
    a = random.choice(Marca)
    return a


Cor = ["Vermelho", "Branco", "Marrom", "Cinza", "Preto", "Laranja", "Azul", "Amarelo", "Roxo", "Verde", "Prata"]

Marca = [{"Marca": "Ford",
          "Modelo": "Ford Mustang",
          "Ano": "2022-01-01",
          "Qtd_portas": "4",
          "Valor": "93.00"
          },
         {
             "Marca": "Ford",
             "Modelo": "Ford Explorer",
             "Ano": "2006-01-01",
             "Qtd_portas": "4",
             "Valor": "103.00"
         },
         {
             "Marca": "Ford",
             "Modelo": "Ford Fiesta",
             "Ano": "2019-01-01",
             "Qtd_portas": "4",
             "Valor": "81.00"
         },
         {
             "Marca": "Ford",
             "Modelo": "Ford Focus",
             "Ano": "2019-01-01",
             "Qtd_portas": "4",
             "Valor": "76.00"
         },
         {
             "Marca": "Volkswagen",
             "Modelo": "Volkswagen Voyage",
             "Ano": "2022-01-01",
             "Qtd_portas": "4",
             "Valor": "84.00"
         },
         {
             "Marca": "Fiat",
             "Modelo": "Fiat Cronos",
             "Ano": "2022-01-01",
             "Qtd_portas": "4",
             "Valor": "112.00"
         },
         {
             "Marca": "Renault",
             "Modelo": "Renault Kwid",
             "Ano": "2022-01-01",
             "Qtd_portas": "4",
             "Valor": "125.00"
         },
         {
             "Marca": "Fiat",
             "Modelo": "Fiat Argo",
             "Ano": "2021-01-01",
             "Qtd_portas": "4",
             "Valor": "100.00"
         },
         {
             "Marca": "Volkswagen",
             "Modelo": "Volkswagen Gol",
             "Ano": "2022-01-01",
             "Qtd_portas": "4",
             "Valor": "100.00"
         },
         {
             "Marca": "Fiat",
             "Modelo": "Fiat Mobi",
             "Ano": "2021-01-01",
             "Qtd_portas": "4",
             "Valor": "100.00"
         },
         {
             "Marca": "Chevrolet",
             "Modelo": "Chevrolet Onix Plus",
             "Ano": "2022-01-01",
             "Qtd_portas": "4",
             "Valor": "90.00"
         },
         {
             "Marca": "Chevrolet",
             "Modelo": "Chevrolet Onix",
             "Ano": "2022-01-01",
             "Qtd_portas": "4",
             "Valor": "80.00"
         },
         {
             "Marca": "Hyundai",
             "Modelo": "Hyundai HB20",
             "Ano": "2020-01-01",
             "Qtd_portas": "4",
             "Valor": "110.00"
         },
         {
             "Marca": "Volkswagen",
             "Modelo": "Volkswagen Polo",
             "Ano": "2021-01-01",
             "Qtd_portas": "4",
             "Valor": "140.00"
         },
         {
             "Marca": "Toyota",
             "Modelo": "Hilux Cabine Simples",
             "Ano": "2023-01-01",
             "Qtd_portas": "2",
             "Valor": "120.00"
         },
         {
             "Marca": "Toyota",
             "Modelo": "RAV4",
             "Ano": "2023-01-01",
             "Qtd_portas": "4",
             "Valor": "140.00"
         },
         {
             "Marca": "Ford",
             "Modelo": "Ford Ka",
             "Ano": "2017-01-01",
             "Qtd_portas": "2",
             "Valor": "70.00"
         },
         {
             "Marca": "MITSUBISHI",
             "Modelo": "MITSUBISHI LANCER",
             "Ano": "2018-01-01",
             "Qtd_portas": "4",
             "Valor": "70.00"
         },
         {
             "Marca": "RENAULT",
             "Modelo": "RENAULT DUSTER",
             "Ano": "2011-01-01",
             "Qtd_portas": "4",
             "Valor": "80.00"
         },
         {
             "Marca": "HYUNDAI",
             "Modelo": "HYUNDAI CRETA",
             "Ano": "2021-01-01",
             "Qtd_portas": "4",
             "Valor": "100.00"
         }]


def Agencia_de_seguro():
    fake = Faker()
    nome = fake.company()
    return nome


def data():
    year = random.randint(2017, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 29)
    Data = f"{year}-{month}-{day}"
    return Data


def Codigo():
    codigo = ""
    for i in range(10):
        codigo += str(random.randint(0, 9))
    return codigo


cursor = cnx.cursor()
create_BG = Criar_Banco_de_dados()
create_BG.main()
cursor.execute("USE BANCO_DATA_BASE;")
cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
i = 900
for z in range(300):
    x = create_marcas()
    chassi = create_chassis_numbers()
    cursor.execute("INSERT INTO Automoveis VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);", [generate_car_plate(), x['Marca'], x['Modelo'], x['Ano'], x['Valor'], '1', random.choice(Cor), x['Qtd_portas'], chassi])
    data_nascimento = gerar_data_nascimento()
    cpf = gerar_cpf()
    if i < 300:
        cursor.execute("INSERT INTO Pessoa_Fisica VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",[cpf, gerar_rg(), gerar_cnh(), criar_nome(i), data_nascimento, calcular_idade(data_nascimento), endereco(), 'F', None, None, None])
    elif 300 <= i < 900:
        cursor.execute("INSERT INTO Pessoa_Fisica VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",[cpf, gerar_rg(), gerar_cnh(), criar_nome(i), data_nascimento, calcular_idade(data_nascimento), endereco(), 'M', None, None, None])
    else:
        cursor.execute("INSERT INTO Pessoa_Fisica VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",[cpf, gerar_rg(), gerar_cnh(), criar_nome(i), data_nascimento, calcular_idade(data_nascimento), endereco(), 'M', Codigo(),'3000.00','7h às 18h'])
    cursor.execute("INSERT INTO Cliente(Plano,Telefone,fk_Pessoa_Fisica_CPF,fk_Pessoa_Juridica_CNPJ) VALUES(%s,%s,%s,%s);", [Plano(), Telefone(), cpf, 'NULL'])
    cursor.execute("INSERT INTO Pessoa_juridica VALUES(%s,%s,%s,%s);", [CNPJ(), criar_nome(i), endereco(), criar_nome(i)])
    cursor.execute("INSERT INTO Locacao(Kilometragem,Preco,Forma_pagamento,fk_Cliente_Codigo_cliente) VALUES(%s,%s,%s,%s);", [Kilometragem(), preço(), pagamento(), i])
    sigla, nome = Sigla()
    cnpj = CNPJ()
    cursor.execute("INSERT INTO Agencia VALUES(%s,%s,%s,%s);", [Contato(), sigla, nome, cnpj])
    cursor.execute("INSERT INTO Posto_de_Atendimento VALUES(%s,%s,%s,%s,%s);", [Telefone(), Contato(), endereco(), '8h às 20h', cnpj])
    cursor.execute("INSERT INTO Seguro VALUES(%s,%s,%s,%s,%s);", [Codigo(), criar_nome(i), Agencia_de_seguro(), random.randint(300,700), i])
    if i >= 900:
        cursor.execute("INSERT INTO Possui VALUES(%s,%s);", [chassi, cnpj])
        if i < 950:
            cursor.execute("INSERT INTO Entrega VALUES(%s,%s,%s);", [cnpj, i, data()])
        else:
            cursor.execute("INSERT INTO Retirada VALUES(%s,%s,%s);", [cnpj, i, data()])
        cursor.execute("INSERT INTO Contrata VALUES(%s,%s);", [cpf, cnpj])
        cursor.execute(f"INSERT INTO Tem VALUES(%s,%s);", [i, chassi])
    i += 1

cnx.commit()
cursor.close()
cnx.close()
print("DONE")
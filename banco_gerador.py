import mysql.connector


class CriarBanco:
    def __init__(self, usuario, senha):
        self.cnx = mysql.connector.connect(user=usuario, password=senha, host='localhost')
        print("Conectado= ", self.cnx.is_connected())
        self.cursor = self.cnx.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS BANCO_DATA_BASE;")
        self.cursor.execute("USE BANCO_DATA_BASE;")
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
        print("---Banco Criado com sucesso!---")

    def agencia(self):
        sql = '''CREATE TABLE IF NOT EXISTS Agencia (
        Contato VARCHAR(50),
        Sigla VARCHAR(8),
        nome VARCHAR(50),
        CNPJ VARCHAR(50) PRIMARY KEY);'''
        self.cursor.execute(sql)
        print("------Tabela Agencia criada com sucesso!------")

    def automoveis(self):
        sql = '''CREATE TABLE IF NOT EXISTS Automoveis (
        Placa VARCHAR(50),
        Marca VARCHAR(50),
        Modelo VARCHAR(50),
        Ano DATE,
        Valor_diaria DECIMAL,
        Status BOOLEAN,
        Cor VARCHAR(50),
        Qtd_Portas INT,
        chassi VARCHAR(50) PRIMARY KEY);'''
        self.cursor.execute(sql)
        print("------Tabela Automoveis criada com sucesso!------")

    def locacao(self):
        sql = '''CREATE TABLE IF NOT EXISTS Locacao (
        Codigo_locacao INT AUTO_INCREMENT PRIMARY KEY,
        Kilometragem INT,
        Preco DECIMAL,
        Forma_pagamento VARCHAR(50),
        fk_Cliente_Codigo_Cliente INT,
        CONSTRAINT FK_Locacao_2 FOREIGN KEY (fk_Cliente_Codigo_Cliente) REFERENCES Cliente (Codigo_Cliente) ON DELETE CASCADE);'''
        self.cursor.execute(sql)
        print("------Tabela Locação criada com sucesso!------")

    def pessoa_fisica(self):
        sql = '''CREATE TABLE IF NOT EXISTS Pessoa_Fisica (
        CPF VARCHAR(50) PRIMARY KEY,
        RG VARCHAR(50),
        CNH VARCHAR(50),
        Nome VARCHAR(50),
        Data_Nascimento DATE,
        Idade INT,
        Endereco VARCHAR(120),
        Sexo VARCHAR(1) NOT NULL,
        Codigo_Funcionario VARCHAR(50),
        Salario DECIMAL,
        Horas_trabalho VARCHAR(50));'''
        self.cursor.execute(sql)
        print("------Tabela Pessoa fisica criada com sucesso!------")

    def pessoa_juridica(self):
        sql = '''CREATE TABLE IF NOT EXISTS Pessoa_Juridica (
        CNPJ VARCHAR(50) PRIMARY KEY,
        nome VARCHAR(50),
        endereco VARCHAR(120),
        Dono VARCHAR(50));'''
        self.cursor.execute(sql)
        print("------Tabela Pessoa Juridica criada com sucesso!------")

    def cliente(self):
        sql = '''CREATE TABLE IF NOT EXISTS Cliente (
        Codigo_Cliente INT AUTO_INCREMENT PRIMARY KEY,
        Plano VARCHAR(50),
        Telefone VARCHAR(50),
        fk_Pessoa_Fisica_CPF VARCHAR(50),
        fk_Pessoa_Juridica_CNPJ VARCHAR(50),
        CONSTRAINT FK_Cliente_3 FOREIGN KEY (fk_Pessoa_Fisica_CPF) REFERENCES Pessoa_Fisica (CPF) ON DELETE CASCADE,
        CONSTRAINT FK_Cliente_4 FOREIGN KEY (fk_Pessoa_Juridica_CNPJ) REFERENCES Pessoa_Juridica (CNPJ) ON DELETE CASCADE);'''
        self.cursor.execute(sql)
        print("------Tabela Cliente criada com sucesso!------")

    def seguro(self):
        sql = '''CREATE TABLE IF NOT EXISTS Seguro (
        Codigo_seguro VARCHAR(50) PRIMARY KEY,
        nome VARCHAR(50),
        Agencia_de_seguro VARCHAR(50),
        Valor DECIMAL,
        fk_Locacao_Codigo_locacao INT,
        CONSTRAINT FK_Seguro_2 FOREIGN KEY (fk_Locacao_Codigo_locacao) REFERENCES Locacao (Codigo_locacao) ON DELETE CASCADE);'''
        self.cursor.execute(sql)
        print("------Tabela Seguro criada com sucesso!------")

    def posto_de_atendimento(self):
        sql = '''CREATE TABLE IF NOT EXISTS Posto_de_atendimento (
        Telefone VARCHAR(50),
        E_mail_para_contato VARCHAR(50),
        Endereco VARCHAR(120),
        Horario_Func VARCHAR(50),
        fk_Agencia_CNPJ VARCHAR(50),
        CONSTRAINT FK_Atendimento FOREIGN KEY(fk_Agencia_CNPJ) REFERENCES Agencia (CNPJ) ON DELETE CASCADE);'''
        self.cursor.execute(sql)
        print("------Tabela Posto de Atedimento criada com sucesso!------")

    def possui(self):
        sql = '''CREATE TABLE IF NOT EXISTS Possui (
        fk_Agencia_CNPJ VARCHAR(50),
        fk_Automoveis_chassi VARCHAR(50),
        PRIMARY KEY(fk_Agencia_CNPJ,fk_Automoveis_chassi),
        CONSTRAINT FK_Possui_1 FOREIGN KEY (fk_Agencia_CNPJ) REFERENCES Agencia (CNPJ) ON DELETE CASCADE,
        CONSTRAINT FK_Possui_2 FOREIGN KEY (fk_Automoveis_chassi) REFERENCES Automoveis (chassi) ON DELETE CASCADE);'''
        self.cursor.execute(sql)
        print("------Tabela Possui criada com sucesso!------")

    def tem(self):
        sql = '''CREATE TABLE IF NOT EXISTS Tem (
        fk_Locacao_Codigo_locacao INT,
        fk_Automoveis_chassi VARCHAR(50),
        PRIMARY KEY(fk_Locacao_Codigo_locacao,fk_Automoveis_chassi),
        CONSTRAINT FK_Tem_1 FOREIGN KEY (fk_Locacao_Codigo_locacao) REFERENCES Locacao (Codigo_locacao) ON DELETE CASCADE,
        CONSTRAINT FK_Tem_2 FOREIGN KEY (fk_Automoveis_chassi) REFERENCES Automoveis (chassi) ON DELETE CASCADE);'''
        self.cursor.execute(sql)
        print("------Tabela Tem criada com sucesso!------")

    def contrata(self):
        sql = '''CREATE TABLE IF NOT EXISTS Contrata (
        fk_Agencia_CNPJ VARCHAR(50),
        fk_Pessoa_Fisica_CPF VARCHAR(50),
        PRIMARY KEY(fk_Agencia_CNPJ,fk_Pessoa_Fisica_CPF),
        CONSTRAINT FK_Contrata_1 FOREIGN KEY (fk_Agencia_CNPJ) REFERENCES Agencia (CNPJ) ON DELETE RESTRICT,
        CONSTRAINT FK_Contrata_2 FOREIGN KEY (fk_Pessoa_Fisica_CPF) REFERENCES Pessoa_Fisica (CPF) ON DELETE CASCADE);'''
        self.cursor.execute(sql)
        print("------Tabela Contrata criada com sucesso!------")

    def retirada(self):
        sql = '''CREATE TABLE IF NOT EXISTS Retirada (
        fk_Agencia_CNPJ VARCHAR(50),
        fk_Locacao_Codigo_locacao INT,
        PRIMARY KEY(fk_Agencia_CNPJ,fk_Locacao_Codigo_locacao),
        Data_retira DATE,
        CONSTRAINT FK_Retirada_1 FOREIGN KEY (fk_Agencia_CNPJ) REFERENCES Agencia (CNPJ) ON DELETE CASCADE,
        CONSTRAINT FK_Retirada_2 FOREIGN KEY (fk_Locacao_Codigo_locacao) REFERENCES Locacao (Codigo_locacao) ON DELETE CASCADE);'''
        self.cursor.execute(sql)
        print("------Tabela Retirada criada com sucesso!------")

    def entrega(self):
        sql = '''CREATE TABLE IF NOT EXISTS Entrega (
        fk_Agencia_CNPJ VARCHAR(50),
        fk_Locacao_Codigo_locacao INT,
        PRIMARY KEY(fk_Agencia_CNPJ,fk_Locacao_Codigo_locacao),
        Data_entrega DATE,
        CONSTRAINT FK_Entrega_1 FOREIGN KEY (fk_Agencia_CNPJ) REFERENCES Agencia (CNPJ) ON DELETE CASCADE,
        CONSTRAINT FK_Entrega_2 FOREIGN KEY (fk_Locacao_Codigo_locacao) REFERENCES Locacao (Codigo_locacao) ON DELETE CASCADE);'''
        self.cursor.execute(sql)
        print("------Tabela Entrega criada com sucesso!------")

    def main(self):
        self.agencia()
        self.automoveis()
        self.locacao()
        self.pessoa_fisica()
        self.pessoa_juridica()
        self.cliente()
        self.seguro()
        self.posto_de_atendimento()
        self.possui()
        self.tem()
        self.contrata()
        self.retirada()
        self.entrega()
        self.cnx.commit()
        print("------Tabelas Construidas e alteradas com sucesso!------")
        self.cursor.close()
        self.cnx.close()

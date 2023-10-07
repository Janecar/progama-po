class Pessoas:
    def __init__(self, nome, idade, cpf, email, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__data_de_nascimento = data_de_nascimento

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _idade(self):
        return self.__idade

    @_idade.setter
    def _idade(self, value):
        self.__idade = value

    @property
    def _cpf(self):
        return self.__cpf

    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

    @property
    def _data_de_nascimento(self):
        return self.__data_de_nascimento

    @_data_de_nascimento.setter
    def _data_de_nascimento(self, value):
        self.__data_de_nascimento = value


   
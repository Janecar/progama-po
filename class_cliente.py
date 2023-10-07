class Cliente:
    def __init__(self, nome, telefone, cpf, email, senha):
        self.__nome = nome
        self.__telefone = telefone
        self.__cpf = cpf
        self.__email = email
        self.__senha = senha

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value

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
    def _senha(self):
        return self.__senha

    @_senha.setter
    def _senha(self, value):
        self.__senha = value



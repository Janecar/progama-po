# definição da classe
class Funcionario :
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor 
    def __init__(self, id, nome, cpf, email, senha):
        self.__id = id # __ modificador de acesso private
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__senha = senha
        
    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value
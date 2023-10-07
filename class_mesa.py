class Mesa:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor 
    def __init__(self, pedido, numero_da_mesa):
        self.__pedido = pedido # __ modificador de acesso private
        self.__numero_da_mesa = numero_da_mesa

    @property
    def _pedido(self):
        return self.__pedido

    @_pedido.setter
    def _pedido(self, value):
        self.__pedido = value

    @property
    def _numero_da_mesa(self):
        return self.__numero_da_mes
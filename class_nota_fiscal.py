class NotaFiscal:
    def __init__(self, formas_de_pagamento, pago, encerrado, detalhes):
        self.__formas_de_pagamento = formas_de_pagamento
        self.__pago = pago
        self.__encerrado = encerrado
        self.__detalhes = detalhes

    @property
    def _formas_de_pagamento(self):
        return self.__formas_de_pagamento

    @_formas_de_pagamento.setter
    def _formas_de_pagamento(self, value):
        self.__formas_de_pagamento = value

    @property
    def _pago(self):
        return self.__pago

    @_pago.setter
    def _pago(self, value):
        self.__pago = value

    @property
    def _encerrado(self):
        return self.__encerrado

    @_encerrado.setter
    def _encerrado(self, value):
        self.__encerrado = value

    @property
    def _detalhes(self):
        return self.__detalhes

    @_detalhes.setter
    def _detalhes(self, value):
        self.__detalhes = value


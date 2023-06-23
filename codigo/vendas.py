class Vendas:
    __id: int
    __idBebida: int
    __idPizza: int
    __cliente: str
    __valor: float
    __data: str

    def __init__(self, id, idBebida, idPizza, cliente, valor, data):
        self.__cliente = cliente
        self.__valor = valor
        self.__idBebida = idBebida
        self.__idPizza = idPizza
        self.__id = id
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def idPizza(self):
        return self.__idPizza

    @idPizza.setter
    def idPizza(self, idPizza):
        self.__idPizza = idPizza

    @property
    def idBebida(self):
        return self.__idBebida

    @idBebida.setter
    def idBebida(self, idBebida):
        self.__idBebida = idBebida

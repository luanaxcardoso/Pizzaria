class Bebidas:
    __id: int
    __nome: str
    __preco: str

    def __init__(self, id, nome, preco):
        self.__nome = nome
        self.__id = id
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

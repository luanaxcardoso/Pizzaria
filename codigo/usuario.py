class Usuario:
    __id: int
    __nomeUsuario: str
    __senha: str
    __funcao: str

    def __init__(self, id, nomeUsuario, senha, funcao):
        self.__nomeUsuario = nomeUsuario
        self.__senha = senha
        self.__id = id
        self.__funcao = funcao

    @property
    def funcao(self):
        return self.__funcao

    @funcao.setter
    def funcao(self, funcao):
        self.__funcao = funcao

    @property
    def nomeUsuario(self):
        return self.__nomeUsuario

    @nomeUsuario.setter
    def nomeUsuario(self, nomeUsuario):
        self.__nomeUsuario = nomeUsuario

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

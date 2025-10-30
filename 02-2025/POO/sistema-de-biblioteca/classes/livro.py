from datetime import datetime, timedelta

class LivroIndisponivelError(Exception): # erros personalizados
    pass

class LivroNaoEncontradoError(Exception):
    pass

class Livro:
    def __init__(self, titulo, autor, categoria="Geral", ano_publicacao=None):

        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("Título inválido. Deve ser uma string não vazia.")

        if not isinstance(autor, str) or not autor.strip():
            raise ValueError("Autor inválido. Deve ser uma string não vazia.")

        self.__titulo = titulo.strip()
        self.__autor = autor.strip()
        self.__categoria = categoria
        self.__ano_publicacao = ano_publicacao
        self.__disponivel = True
        self.__emprestado_para = None
        self.__data_devolucao = None

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, nova_categoria):
        self.__categoria = nova_categoria

    @property
    def ano_publicacao(self):
        return self.__ano_publicacao

    @property
    def disponivel(self):
        return self.__disponivel

    @property
    def emprestado_para(self):
        return self.__emprestado_para

    @property
    def data_devolucao(self):
        return self.__data_devolucao

    def emprestar(self, usuario):
        if not self.__disponivel:
            raise LivroIndisponivelError(f"O livro '{self.__titulo}' já está emprestado.")
        self.__disponivel = False
        self.__emprestado_para = usuario
        self.__data_devolucao = datetime.now() + timedelta(days=7)

    def devolver(self):
        self.__disponivel = True
        self.__emprestado_para = None
        self.__data_devolucao = None

    def esta_atrasado(self):
        if not self.__disponivel and self.__data_devolucao:
            return datetime.now() > self.__data_devolucao
        return False

    def detalhes(self):
        status = "Disponível" if self.__disponivel else f"Emprestado para {self.__emprestado_para.nome}"
        return f"Título: {self.__titulo} | Autor: {self.__autor} | Categoria: {self.__categoria} | Status: {status}"


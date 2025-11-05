
class LimiteEmprestimosError(Exception):
    pass

class Usuario:
    def __init__(self, nome, email, limite_emprestimos=3):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome de usuário inválido.")
        self.__nome = nome.strip()
        self.__email = email
        self.__limite_emprestimos = limite_emprestimos
        self.__livros_emprestados = []

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def limite_emprestimos(self):
        return self.__limite_emprestimos

    @property
    def livros_emprestados(self):
        return list(self.__livros_emprestados)

    def atualizar_email(self, novo_email):
        self.__email = novo_email

    def atualizar_limite(self, novo_limite):
        self.__limite_emprestimos = novo_limite

    def emprestar_livro(self, livro):

        if len(self.__livros_emprestados) >= self.__limite_emprestimos:
            raise LimiteEmprestimosError(f"{self.__nome} atingiu o limite de {self.__limite_emprestimos} empréstimos.")

        livro.emprestar(self)
        self.__livros_emprestados.append(livro)

    def devolver_livro(self, livro):

        if livro not in self.__livros_emprestados:
            raise ValueError(f"O livro '{livro.titulo}' não foi emprestado para {self.__nome}.")

        livro.devolver()
        self.__livros_emprestados.remove(livro)

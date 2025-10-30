from datetime import datetime
import os
from .livro import Livro
from .usuario import Usuario

class UsuarioNaoEncontradoError(Exception):
    pass

class LivroNaoEncontradoError(Exception):
    pass

class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__usuarios = []
        self.__historico = []  # (salva o usuario, livro, data_emprestimo e data_devolucao)
        
        self.__pasta_logs = os.path.join(os.path.dirname(__file__), '..', 'logs')
        os.makedirs(self.__pasta_logs, exist_ok=True)

    def adicionar_livro(self, livro):
        if not isinstance(livro, Livro):
            raise TypeError("Somente objetos do tipo Livro podem ser adicionados.")
        self.__livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def adicionar_usuario(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("Somente objetos do tipo Usuario podem ser adicionados.")
        self.__usuarios.append(usuario)
        print(f"Usuário '{usuario.nome}' cadastrado na biblioteca.")

    def emprestar_livro(self, usuario, livro):
        try:
            if usuario not in self.__usuarios:
                raise UsuarioNaoEncontradoError("Usuário não encontrado na biblioteca.")
            if livro not in self.__livros:
                raise LivroNaoEncontradoError("Livro não encontrado no acervo.")

            usuario.emprestar_livro(livro)
            self.__historico.append((usuario, livro, datetime.now(), None))
            print(f"Empréstimo realizado: '{livro.titulo}' para {usuario.nome}")
        except Exception as e:
            print(f"Erro ao emprestar livro: {e}")

    def devolver_livro(self, usuario, livro):
        try:
            usuario.devolver_livro(livro)
            for reg in self.__historico:
                if reg[0] == usuario and reg[1] == livro and reg[3] is None:
                    self.__historico[self.__historico.index(reg)] = (reg[0], reg[1], reg[2], datetime.now())
                    break
            print(f"Devolução realizada: '{livro.titulo}' por {usuario.nome}")
        except Exception as e:
            print(f"Erro ao devolver livro: {e}")

    # relatorios
    def listar_livros_disponiveis(self):
        disponiveis = [l for l in self.__livros if l.disponivel]
        if not disponiveis:
            print("Nenhum livro disponível.")
        else:
            print("Livros disponíveis:")
            for l in disponiveis:
                print(f"   - {l.detalhes()}")

    def listar_livros_emprestados(self):
        emprestados = [l for l in self.__livros if not l.disponivel]
        if not emprestados:
            print("Nenhum livro emprestado no momento.")
        else:
            print("Livros emprestados:")
            for l in emprestados:
                print(f"   - {l.titulo} (Emprestado para: {l.emprestado_para.nome})")

    def listar_atrasados(self):
        atrasados = [l for l in self.__livros if l.esta_atrasado()]
        if atrasados:
            print("Livros atrasados:")
            for l in atrasados:
                print(f"   - {l.titulo} (Emprestado para: {l.emprestado_para.nome})")
        else:
            print("Nenhum livro atrasado.")

    def estatisticas(self):
        total_livros = len(self.__livros)
        total_usuarios = len(self.__usuarios)
        total_emprestados = len([l for l in self.__livros if not l.disponivel])
        print(f"Total de livros: {total_livros}")
        print(f"Total de usuários: {total_usuarios}")
        print(f"Total de empréstimos em andamento: {total_emprestados}")

    # exportação e organizaçãoem txt
    def exportar_acervo(self, nome_arquivo="acervo_livros.txt"):
        caminho = os.path.join(self.__pasta_logs, nome_arquivo)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write("ACERVO LIVROS\n")
            f.write("============================\n\n")
            for l in self.__livros:
                status = "Disponível" if l.disponivel else f"Emprestado para {l.emprestado_para.nome}"
                f.write(f"Título: {l.titulo}\nAutor: {l.autor}\nCategoria: {l.categoria}\n"
                        f"Ano: {l.ano_publicacao}\nStatus: {status}\n")
                f.write("----------------------------\n")
        print(f"Acervo exportado para '{caminho}' com sucesso!")

    def exportar_historico(self, nome_arquivo="historico_emprestimos.txt"):
        caminho = os.path.join(self.__pasta_logs, nome_arquivo)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write("HISTÓRICO EMPRÉSTIMOS\n")
            f.write("============================\n\n")
            for usuario, livro, data_emp, data_dev in self.__historico:
                devolucao = data_dev.strftime("%d/%m/%Y %H:%M") if data_dev else "Ainda não devolvido"
                f.write(f"Usuário: {usuario.nome}\nLivro: {livro.titulo}\n"
                        f"Emprestado em: {data_emp.strftime('%d/%m/%Y %H:%M')}\nDevolução: {devolucao}\n")
                f.write("----------------------------\n")
        print(f"Histórico exportado para '{caminho}' com sucesso!")

    def organizar_acervo_por_categoria(self):
        ordenado = sorted(self.__livros, key=lambda l: (l.categoria.lower(), l.titulo.lower()))
        print("Acervo organizado por categoria:")
        for l in ordenado:
            print(f"   [{l.categoria}] {l.titulo}")

    def organizar_acervo_por_titulo(self):
        ordenado = sorted(self.__livros, key=lambda l: l.titulo.lower())
        print("Acervo organizado por título:")
        for l in ordenado:
            print(f"   - {l.titulo} ({l.autor})")

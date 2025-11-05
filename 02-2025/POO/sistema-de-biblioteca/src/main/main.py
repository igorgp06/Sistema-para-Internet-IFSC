from models.usuario import Usuario
from models.biblioteca import Biblioteca
from models.livro import Livro
from models.revista import Revista
from models.midia_digital import MidiaDigital

biblioteca = Biblioteca()

# usuarios
usuario1 = Usuario("Igor", "igor@email.com")
usuario2 = Usuario("Mari", "mari@email.com")
biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)

# itens do acervo
livro = Livro("Dom Casmurro", "Machado de Assis", "Romance", 1899)
revista = Revista("Superinteressante", "Diversos", "Abril", 312, "Outubro")
midia = MidiaDigital("Python para Iniciantes", "Igor Gonçalves", "PDF", 12.5)

biblioteca.adicionar_item(livro)
biblioteca.adicionar_item(revista)
biblioteca.adicionar_item(midia)

# emprestimos e listagem
biblioteca.emprestar_item(usuario1, livro)
biblioteca.listar_itens()
biblioteca.devolver_item(usuario1, livro)

from classes.usuario import Usuario
from classes.biblioteca import Biblioteca
from classes.livro import Livro  

biblioteca = Biblioteca()

livro1 = Livro("Dom Casmurro", "Machado de Assis", "Romance", 1899)
livro2 = Livro("O Hobbit", "J.R.R. Tolkien", "Fantasia", 1937)
livro3 = Livro("Diário de um Banana", "Jeff Kinney", "Infantojuvenil", 2007)

usuario1 = Usuario("Igor", "igor@email.com", limite_emprestimos=2)
usuario2 = Usuario("Mari", "mari@email.com")
    
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)

biblioteca.emprestar_livro(usuario1, livro1)
biblioteca.emprestar_livro(usuario2, livro3)
    
biblioteca.devolver_livro(usuario1, livro1)
    
biblioteca.listar_livros_disponiveis()
biblioteca.exportar_acervo()
biblioteca.exportar_historico()

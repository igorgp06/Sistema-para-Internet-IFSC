from .item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, categoria="Geral", ano_publicacao=None):
        super().__init__(titulo, autor)
        self.categoria = categoria
        self.ano_publicacao = ano_publicacao

    def detalhes(self):
        status = "Disponível" if self.disponivel else f"Emprestado para {self.emprestado_para.nome}"
        return (f"[LIVRO] Título: {self.titulo} | Autor: {self.autor} | "
                f"Categoria: {self.categoria} | Ano: {self.ano_publicacao} | Status: {status}")

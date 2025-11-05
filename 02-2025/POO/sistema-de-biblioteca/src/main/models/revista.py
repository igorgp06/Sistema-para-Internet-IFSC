from .item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):
    def __init__(self, titulo, autor, editora, edicao, mes_publicacao):
        super().__init__(titulo, autor)
        self.editora = editora
        self.edicao = edicao
        self.mes_publicacao = mes_publicacao

    def detalhes(self):
        status = "Disponível" if self.disponivel else f"Emprestada para {self.emprestado_para.nome}"
        return (f"[REVISTA] Título: {self.titulo} | Autor: {self.autor} | "
                f"Editora: {self.editora} | Edição: {self.edicao} | "
                f"Mês: {self.mes_publicacao} | Status: {status}")

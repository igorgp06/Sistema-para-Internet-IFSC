from .item_biblioteca import ItemBiblioteca

class MidiaDigital(ItemBiblioteca):
    def __init__(self, titulo, autor, formato, tamanho_MB):
        super().__init__(titulo, autor)
        self.formato = formato
        self.tamanho_MB = tamanho_MB

    def detalhes(self):
        status = "Disponível" if self.disponivel else f"Emprestada para {self.emprestado_para.nome}"
        return (f"[MÍDIA DIGITAL] Título: {self.titulo} | Autor: {self.autor} | "
                f"Formato: {self.formato} | Tamanho: {self.tamanho_MB}MB | Status: {status}")

from datetime import datetime, timedelta

class ItemBiblioteca:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        self.emprestado_para = None
        self.data_devolucao = None

    def emprestar(self, usuario):
        if not self.disponivel:
            raise Exception(f"O item '{self.titulo}' já está emprestado.")
        self.disponivel = False
        self.emprestado_para = usuario
        self.data_devolucao = datetime.now() + timedelta(days=7)

    def devolver(self):
        self.disponivel = True
        self.emprestado_para = None
        self.data_devolucao = None

    def esta_atrasado(self):
        if not self.disponivel and self.data_devolucao:
            return datetime.now() > self.data_devolucao
        return False

    def detalhes(self):
        status = "Disponível" if self.disponivel else f"Emprestado para {self.emprestado_para.nome}"
        return f"Título: {self.titulo} | Autor: {self.autor} | Status: {status}"

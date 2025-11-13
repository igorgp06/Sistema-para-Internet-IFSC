from src.data.data_manager import DataManager

class Imobiliaria:
    def __init__(self):
        self.data = DataManager()
        self.propriedades = self.data.carregar_propriedades()
        self.clientes = self.data.carregar_clientes(self.propriedades)

    # ------- PROPRIEDADES -------
    def cadastrar_propriedade(self, prop):
        self.propriedades.append(prop)
        self.data.salvar_propriedades(self.propriedades)

    def listar_propriedades(self):
        return self.propriedades

    def buscar_propriedade(self, endereco):
        return next((p for p in self.propriedades if p.endereco == endereco), None)

    def remover_propriedade(self, endereco):
        prop = self.buscar_propriedade(endereco)
        if prop:
            self.propriedades.remove(prop)
            self.data.salvar_propriedades(self.propriedades)
            return True
        return False

    def atualizar_propriedades(self):
        self.data.salvar_propriedades(self.propriedades)

    # ------- CLIENTES -------
    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.data.salvar_clientes(self.clientes)

    def listar_clientes(self):
        return self.clientes

    def buscar_cliente(self, nome):
        return next((c for c in self.clientes if c.nome == nome), None)

    def remover_cliente(self, nome):
        cliente = self.buscar_cliente(nome)
        if cliente:
            self.clientes.remove(cliente)
            self.data.salvar_clientes(self.clientes)
            return True
        return False

    def atualizar_clientes(self):
        self.data.salvar_clientes(self.clientes)

from src.data.data_manager import DataManager
from src.models.cliente import Cliente

# centro do sistema e das regras de negócio.
# mantém as coleções de clientes e propriedades e conversa com o DataManager
class Imobiliaria:
    def __init__(self):
        # ao iniciar carrega tudo do json
        self.data = DataManager()
        self.propriedades = self.data.carregar_propriedades()
        self.clientes = self.data.carregar_clientes(self.propriedades)

    # seção das propriedades
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
        # método chamado sempre que algo muda nas propriedades
        self.data.salvar_propriedades(self.propriedades)

    # seção dos clientes
    # segue a msm lógica das propriedades 
    def _validar_unicidade_cliente(self, nome, telefone, email, ignorar=None):
        for c in self.clientes:
            if ignorar is not None and c is ignorar:
                continue

            if c.nome == nome:
                raise ValueError("Já existe um cliente com esse nome.")
            if c.email == email:
                raise ValueError("Já existe um cliente com esse e-mail.")
            if c.telefone == telefone:
                raise ValueError("Já existe um cliente com esse telefone.")

    def cadastrar_cliente(self, cliente: Cliente):
        # validar unicidade antes de adicionar 
        self._validar_unicidade_cliente(cliente.nome, cliente.telefone, cliente.email)
        self.clientes.append(cliente)
        self.data.salvar_clientes(self.clientes)

    def listar_clientes(self):
        return self.clientes

    def buscar_cliente(self, nome):
        return next((c for c in self.clientes if c.nome == nome), None)

    def atualizar_cliente(self, cliente: Cliente, novo_nome: str, novo_tel: str, novo_email: str):

        # encapsulamento e reutilização
        # usamos Cliente.validar_dados para garantir que os dados editados continuam válidos.
        novo_nome, novo_tel, novo_email = Cliente.validar_dados(novo_nome, novo_tel, novo_email)

        self._validar_unicidade_cliente(novo_nome, novo_tel, novo_email, ignorar=cliente)

        cliente.nome = novo_nome
        cliente.telefone = novo_tel
        cliente.email = novo_email

        self.data.salvar_clientes(self.clientes)

    def remover_cliente(self, nome):
        cliente = self.buscar_cliente(nome)
        if cliente:
            self.clientes.remove(cliente)
            self.data.salvar_clientes(self.clientes)
            return True
        return False

    def atualizar_clientes(self):
        self.data.salvar_clientes(self.clientes)

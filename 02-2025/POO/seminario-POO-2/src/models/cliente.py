class Cliente:
    
    # metodo estatico q valida e normaliza os dados do cliente
    @staticmethod
    def validar_dados(nome, telefone, email):
        nome = (nome or "").strip()
        telefone = (telefone or "").strip()
        email = (email or "").strip()

        # validações de erros básicos
        if not nome:
            raise ValueError("Nome do cliente não pode ser vazio.")
        if len(nome) < 3:
            raise ValueError("Nome muito curto.")
        if len(nome) > 50:
            raise ValueError("Nome muito longo.")

        if not telefone:
            raise ValueError("Telefone do cliente não pode ser vazio.")
        if not telefone.isdigit():
            raise ValueError("Telefone deve conter apenas números e não pode conter espaços.")
        if len(telefone) < 8:
            raise ValueError("Telefone muito curto.")
        if len(telefone) > 15:
            raise ValueError("Telefone muito longo.")

        if not email:
            raise ValueError("Email do cliente não pode ser vazio.")
        if "@" not in email:
            raise ValueError("E-mail inválido.")

        return nome, telefone, email

    def __init__(self, nome, telefone, email):
        nome, telefone, email = self.validar_dados(nome, telefone, email)

        # uso do encapsulamento
        # antes de salvar qualquer atributo, chamamos validar_dados.
        # Se estiver inválido cai na exception e a instanciação não ocorre.
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.interesses = []  # lista de propriedades de interesse

    def atualizar_dados(self, nome, telefone, email):
        nome, telefone, email = self.validar_dados(nome, telefone, email)
        self.nome = nome
        self.telefone = telefone
        self.email = email

    # adicionar propriedade de interesse
    def adicionar_interesse(self, propriedade):
        if propriedade not in self.interesses:
            self.interesses.append(propriedade)

    def remover_interesse(self, propriedade):
        if propriedade in self.interesses:
            self.interesses.remove(propriedade)

    # converter para dicionario (json)
    # aqui não salvamos o objeto Propriedade inteiro, apenas o endereço dela
    def to_dict(self):
        return {
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email,
            "interesses": [p.endereco for p in self.interesses],
        }

    def __str__(self):
        return f"{self.nome} ({self.email})"

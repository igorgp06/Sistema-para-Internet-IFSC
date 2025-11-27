class Cliente:
    def __init__(self, nome, telefone, email):
        if not nome or not nome.strip():
            raise ValueError("Nome do cliente não pode ser vazio.")
        
        if not telefone or not telefone.strip():
            raise ValueError("Telefone do cliente não pode ser vazio.")
        
        if not email or not email.strip():
            raise ValueError("Email do cliente não pode ser vazio.")

        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.interesses = []  # lista de Propriedade

    def adicionar_interesse(self, propriedade):
        if propriedade not in self.interesses:
            self.interesses.append(propriedade)

    def remover_interesse(self, propriedade):
        if propriedade in self.interesses:
            self.interesses.remove(propriedade)

    def to_dict(self):
        return {
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email,
            "interesses": [p.endereco for p in self.interesses],
        }

    def __str__(self):
        return f"{self.nome} ({self.email})"

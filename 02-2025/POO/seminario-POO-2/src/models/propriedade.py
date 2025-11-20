class Propriedade:
    TIPOS_VALIDOS = ["casa", "apartamento", "terreno"]
    STATUS_VALIDOS = ["disponível", "em negociação", "vendido", "alugado"]

    def __init__(self, endereco, descricao, tipo, preco_venda, preco_locacao, status="disponível"):
        
        if not endereco or not endereco.strip():
            raise ValueError("A propriedade deve conter um endereço válido.")
        
        if not descricao or not descricao.strip():
            descricao = "Sem descrição disponível."

        tipo = tipo.lower()
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError("Tipo inválido. Use: casa, apartamento ou terreno.")

        if status not in self.STATUS_VALIDOS:
            raise ValueError("Status inválido.")

        try:
            preco_venda = float(preco_venda)
            preco_locacao = float(preco_locacao)
            
        except ValueError:
            raise ValueError("Preços devem ser números válidos.")

        self.endereco = endereco
        self.descricao = descricao
        self.tipo = tipo
        self.preco_venda = preco_venda
        self.preco_locacao = preco_locacao
        self.status = status

    def marcar_vendida(self):
        self.status = "vendido"

    def marcar_alugada(self):
        self.status = "alugado"

    def to_dict(self):
        return {
            "endereco": self.endereco,
            "descricao": self.descricao,
            "tipo": self.tipo,
            "preco_venda": self.preco_venda,
            "preco_locacao": self.preco_locacao,
            "status": self.status,
        }

    def __str__(self):
        return f"{self.tipo.title()} - {self.endereco} ({self.status})"


#  concentra t0das as regras de negócio de Propriedade:
# tipos válidos, status, se pode ou não alugar/vender, validação de preços
class Propriedade:
    # mapeação dos tipos e status válidos
    TIPOS_VALIDOS = ["casa", "apartamento", "terreno"]
    STATUS_VALIDOS = ["disponível", "em negociação", "vendido", "alugado"]

    def __init__(self, endereco, descricao, tipo,
                preco_venda, preco_locacao,
                pd_vender=True, pd_alugar=True,
                status="disponível",
                comprador=None, locatario=None):

        # validações básicas
        if not endereco or not endereco.strip():
            raise ValueError("A propriedade deve conter um endereço válido.")

        if len(endereco.strip()) < 5:
            raise ValueError("O endereço deve ter ao menos 5 caracteres.")

        if not descricao or not descricao.strip():
            descricao = "Sem descrição disponível."

        tipo = (tipo or "").lower()
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError("Tipo inválido. Use: casa, apartamento ou terreno.")

        if status not in self.STATUS_VALIDOS:
            raise ValueError("Status inválido.")

        try:
            preco_venda = float(preco_venda)
            preco_locacao = float(preco_locacao)
        except ValueError:
            raise ValueError("Preços devem ser números válidos.")

        if preco_venda < 0 or preco_locacao < 0:
            raise ValueError("Preços não podem ser negativos.")

        # forcar regras de negócio baseadas no tipo e disponibilidade
        if tipo == "terreno":
            pd_alugar = False
            preco_locacao = 0.0

        if not pd_vender:
            preco_venda = 0.0

        if not pd_alugar:
            preco_locacao = 0.0

        if pd_vender and preco_venda == 0.0:
            raise ValueError("Preço de venda deve ser informado se a propriedade estiver à venda.")

        if pd_alugar and preco_locacao == 0.0:
            raise ValueError("Preço de locação deve ser informado se a propriedade estiver para alugar.")

        if not (pd_vender or pd_alugar):
            raise ValueError("A propriedade deve estar disponível para venda, aluguel ou ambos.")

        # se não cair em nenhuma exceção atribui os valores
        self.endereco = endereco.strip()
        self.descricao = descricao
        self.tipo = tipo
        self.preco_venda = preco_venda
        self.preco_locacao = preco_locacao
        self.pd_vender = pd_vender
        self.pd_alugar = pd_alugar
        self.status = status
        self.comprador = comprador
        self.locatario = locatario

    def marcar_vendida(self, comprador=None):
        if comprador is not None:
            self.comprador = comprador
        self.status = "vendido"

    def marcar_alugada(self, locatario=None):
        if locatario is not None:
            self.locatario = locatario
        self.status = "alugado"

    def marcar_em_negociacao(self):
        self.status = "em negociação"

    # converter para dicionario (json)
    def to_dict(self):
        return {
            "endereco": self.endereco,
            "descricao": self.descricao,
            "tipo": self.tipo,
            "preco_venda": self.preco_venda,
            "preco_locacao": self.preco_locacao,
            "pd_vender": self.pd_vender,
            "pd_alugar": self.pd_alugar,
            "status": self.status,
            "comprador": self.comprador.nome if self.comprador else None,
            "locatario": self.locatario.nome if self.locatario else None,
        }

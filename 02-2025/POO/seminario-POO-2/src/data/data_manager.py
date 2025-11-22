import json
import os
from src.models.cliente import Cliente
from src.models.propriedade import Propriedade

class DataManager:
    def __init__(self):
        # criação do diretorio logs que contem os arquivos de dados
        self.base_path = os.path.join(os.path.dirname(__file__), 'logs')
        os.makedirs(self.base_path, exist_ok=True)

        self.file_props = os.path.join(self.base_path, "propriedades.json")
        self.file_clients = os.path.join(self.base_path, "clientes.json")

        self._criar_arquivos()

    def _criar_arquivos(self):
        if not os.path.exists(self.file_props):
            with open(self.file_props, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)

        if not os.path.exists(self.file_clients):
            with open(self.file_clients, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)

    # propriedades

    def salvar_propriedades(self, propriedades):
        data = [p.to_dict() for p in propriedades]
        with open(self.file_props, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def carregar_propriedades(self):
        with open(self.file_props, "r", encoding="utf-8") as f:
            data = json.load(f)

        propriedades = []

        for item in data:
            prop = Propriedade(
                item["endereco"],
                item["descricao"],
                item["tipo"],
                item["preco_venda"],
                item["preco_locacao"],
                item.get("pd_vender", True),
                item.get("pd_alugar", True),
                item["status"],
                None, 
                None
            )
            propriedades.append(prop)

        return propriedades

    # clientes

    def salvar_clientes(self, clientes):
        data = [c.to_dict() for c in clientes]
        with open(self.file_clients, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def carregar_clientes(self, propriedades):
        with open(self.file_clients, "r", encoding="utf-8") as f:
            data = json.load(f)

        clientes = []
        for item in data:
            c = Cliente(item["nome"], item["telefone"], item["email"])

            for end in item.get("interesses", []):
                prop = next((p for p in propriedades if p.endereco == end), None)
                if prop:
                    c.adicionar_interesse(prop)

            clientes.append(c)

        # associação de compradores e locatarios
        
        for item in data:
            if item.get("comprador"):
                cliente = next((cl for cl in clientes if cl.nome == item["comprador"]), None)
                prop = next((p for p in propriedades if p.endereco == item["endereco"]), None)
                if cliente and prop:
                    prop.comprador = cliente

            if item.get("locatario"):
                cliente = next((cl for cl in clientes if cl.nome == item["locatario"]), None)
                prop = next((p for p in propriedades if p.endereco == item["endereco"]), None)
                if cliente and prop:
                    prop.locatario = cliente

        return clientes

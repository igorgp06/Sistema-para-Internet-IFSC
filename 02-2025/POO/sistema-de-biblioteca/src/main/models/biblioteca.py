import os, json
from datetime import datetime
from .item_biblioteca import ItemBiblioteca
from .usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.__itens = []
        self.__usuarios = []
        self.__historico = []

        self.__pasta_logs = os.path.join(os.path.dirname(__file__), '..', 'logs')
        os.makedirs(self.__pasta_logs, exist_ok=True)
        self.__arquivo_dados = os.path.join(self.__pasta_logs, "dados_biblioteca.json")

    def adicionar_item(self, item):
        
        if not isinstance(item, ItemBiblioteca):
            raise TypeError("Somente objetos do tipo ItemBiblioteca podem ser adicionados.")
        
        self.__itens.append(item)
        self.salvar_dados()

    def adicionar_usuario(self, usuario):
        
        if not isinstance(usuario, Usuario):
            raise TypeError("Somente objetos do tipo Usuario podem ser adicionados.")
        
        self.__usuarios.append(usuario)
        self.salvar_dados()

    def emprestar_item(self, usuario, item):
        usuario.emprestar_livro(item)
        self.__historico.append({
            "usuario": usuario.nome,
            "item": item.titulo,
            "data_emprestimo": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "data_devolucao": None
        })
        self.salvar_dados()

    def devolver_item(self, usuario, item):
        usuario.devolver_livro(item)
        
        for reg in self.__historico:
            if reg["usuario"] == usuario.nome and reg["item"] == item.titulo and reg["data_devolucao"] is None:
                reg["data_devolucao"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                break
            
        self.salvar_dados()

    def listar_itens(self):
        return [i.detalhes() for i in self.__itens]

    def salvar_dados(self):
        dados = {
            "usuarios": [u.nome for u in self.__usuarios],
            "itens": [{"titulo": i.titulo, "autor": i.autor, "status": "disponível" if i.disponivel else "emprestado"} for i in self.__itens],
            "historico": self.__historico
        }
        
        with open(self.__arquivo_dados, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def carregar_dados(self):
        if not os.path.exists(self.__arquivo_dados):
            return
        with open(self.__arquivo_dados, "r", encoding="utf-8") as f:
            dados = json.load(f)

            for item in dados.get("itens", []):
                novo = ItemBiblioteca(item["titulo"], item["autor"])
                self.__itens.append(novo)
                
            for nome in dados.get("usuarios", []):
                self.__usuarios.append(Usuario(nome, f"{nome.lower()}@email.com"))
            self.__historico = dados.get("historico", [])

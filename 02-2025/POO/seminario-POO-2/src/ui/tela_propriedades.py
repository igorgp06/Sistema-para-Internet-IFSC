import customtkinter as ctk
from src.models.propriedade import Propriedade

class TelaPropriedades(ctk.CTkFrame):
    def __init__(self, master, imobiliaria, colors):
        super().__init__(master, fg_color=colors["background"])
        self.imobiliaria = imobiliaria
        self.colors = colors

        self.pack(expand=True, fill="both")

        self._criar_header()
        self._criar_area_cards()
        self.atualizar_cards()

    def _criar_header(self):
        header = ctk.CTkFrame(self, fg_color=self.colors["background"])
        header.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            header,
            text="Propriedades",
            font=("Segoe UI", 22, "bold"),
            text_color=self.colors["foreground"]
        ).pack(side="left")

        ctk.CTkButton(
            header,
            text="+ Nova Propriedade",
            fg_color=self.colors["primary"],
            hover_color=self.colors["primary_hover"],
            command=self.abrir_modal_nova_prop
        ).pack(side="right")

    def _criar_area_cards(self):
        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color=self.colors["background"]
        )
        self.scroll.pack(expand=True, fill="both", padx=10, pady=(0, 10))

    def atualizar_cards(self):
        # delete geral
        for widget in self.scroll.winfo_children():
            widget.destroy()

        propriedades = self.imobiliaria.listar_propriedades()

        if not propriedades:
            ctk.CTkLabel(
                self.scroll,
                text="Nenhuma propriedade cadastrada.",
                text_color=self.colors["foreground"]
            ).grid(row=0, column=0, padx=10, pady=10, sticky="w")
            return

        for i, prop in enumerate(propriedades):
            row = i // 1
            col = i % 1
            self._criar_card_propriedade(prop, row, col)

    def _cor_status(self, status):
        status = status.lower()
        if status == "disponível":
            return "#16a34a" 
        elif status == "em negociação":
            return "#eab308"  
        elif status == "vendido":
            return "#f97316"  
        elif status == "alugado":
            return "#3b82f6"
        return self.colors["foreground"]

    def _criar_card_propriedade(self, prop, row, col):
        card = ctk.CTkFrame(
            self.scroll,
            fg_color=self.colors["card"],
            border_color=self.colors["border"], # TODO deixar os cards um sob o outro não lado a lado
            border_width=2,
            corner_radius=12
        )
        card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # tipos e status
        top = ctk.CTkFrame(card, fg_color="transparent")
        top.pack(fill="x", padx=10, pady=(8, 4))

        ctk.CTkLabel(
            top,
            text=prop.tipo.title(),
            font=("Segoe UI", 16, "bold"),
            text_color=self.colors["foreground"]
        ).pack(side="left")

        ctk.CTkLabel(
            top,
            text=prop.status.upper(),
            font=("Segoe UI", 12, "bold"),
            text_color=self._cor_status(prop.status)
        ).pack(side="right")

        # endereços
        ctk.CTkLabel(
            card,
            text=prop.endereco,
            font=("Segoe UI", 13, "bold"),
            text_color=self.colors["foreground"]
        ).pack(anchor="w", padx=10)

        # desc
        ctk.CTkLabel(
            card,
            text=prop.descricao,
            font=("Segoe UI", 11),
            text_color="#9AA0A6",
            wraplength=260,
            justify="left"
        ).pack(anchor="w", padx=10, pady=(2, 4))

        # valores
        preco_frame = ctk.CTkFrame(card, fg_color="transparent")
        preco_frame.pack(fill="x", padx=10, pady=4)

        ctk.CTkLabel(
            preco_frame,
            text=f"Venda: R$ {prop.preco_venda:,.2f}",
            font=("Segoe UI", 11),
            text_color=self.colors["foreground"]
        ).pack(anchor="w")

        ctk.CTkLabel(
            preco_frame,
            text=f"Locação: R$ {prop.preco_locacao:,.2f}",
            font=("Segoe UI", 11),
            text_color=self.colors["foreground"]
        ).pack(anchor="w")

        # btns
        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(fill="x", padx=10, pady=(6, 10))

        ctk.CTkButton(
            btn_frame,
            text="Vender",
            fg_color="#f97316",
            hover_color="#fb923c",
            command=lambda p=prop: self.marcar_vendida(p)
        ).pack(side="left", expand=True, fill="x", padx=(0, 5))

        ctk.CTkButton(
            btn_frame,
            text="Alugar",
            fg_color="#3b82f6",
            hover_color="#60a5fa",
            command=lambda p=prop: self.marcar_alugada(p)
        ).pack(side="left", expand=True, fill="x", padx=5)

        ctk.CTkButton(
            btn_frame,
            text="Editar",
            fg_color=self.colors["primary"],
            hover_color=self.colors["primary_hover"],
            command=lambda p=prop: self.abrir_modal_editar(p)
        ).pack(side="left", expand=True, fill="x", padx=5)

        ctk.CTkButton(
            btn_frame,
            text="Remover",
            fg_color="#b91c1c",
            hover_color="#dc2626",
            command=lambda p=prop: self.remover_prop(p)
        ).pack(side="left", expand=True, fill="x", padx=(5, 0))

    # ---------- ações ----------

    def marcar_vendida(self, prop):
        prop.marcar_vendida()
        self.imobiliaria.atualizar_propriedades()
        self.atualizar_cards()

    def marcar_alugada(self, prop):
        prop.marcar_alugada()
        self.imobiliaria.atualizar_propriedades()
        self.atualizar_cards()

    def remover_prop(self, prop):
        self.imobiliaria.remover_propriedade(prop.endereco)
        self.atualizar_cards()

    # ---------- modais ----------

    def abrir_modal_nova_prop(self):
        self._abrir_modal_prop()

    def abrir_modal_editar(self, prop):
        self._abrir_modal_prop(prop)

    def _abrir_modal_prop(self, prop=None):
        is_edit = prop is not None

        # config janela de nova propriedade ou edição
        win = ctk.CTkToplevel(self)
        win.title("Editar Propriedade" if is_edit else "Nova Propriedade")
        win.geometry("450x450")
        win.resizable(False, False)
        win.grab_set()

        # campos
        lbl_style = {"text_color": self.colors["foreground"], "font": ("Segoe UI", 12)}

        ctk.CTkLabel(win, text="Endereço", **lbl_style).pack(anchor="w", padx=20, pady=(15, 0))
        entry_end = ctk.CTkEntry(win, width=360)
        entry_end.pack(padx=20)

        ctk.CTkLabel(win, text="Descrição", **lbl_style).pack(anchor="w", padx=20, pady=(10, 0))
        entry_desc = ctk.CTkEntry(win, width=360)
        entry_desc.pack(padx=20)

        ctk.CTkLabel(win, text="Tipo", **lbl_style).pack(anchor="w", padx=20, pady=(10, 0))
        tipo_opt = ctk.CTkOptionMenu(win, values=["casa", "apartamento", "terreno"])
        tipo_opt.pack(padx=20)

        ctk.CTkLabel(win, text="Preço de venda (R$)", **lbl_style).pack(anchor="w", padx=20, pady=(10, 0))
        entry_venda = ctk.CTkEntry(win, width=360)
        entry_venda.pack(padx=20)

        ctk.CTkLabel(win, text="Preço de locação (R$)", **lbl_style).pack(anchor="w", padx=20, pady=(10, 0))
        entry_loc = ctk.CTkEntry(win, width=360)
        entry_loc.pack(padx=20)

        if is_edit:
            entry_end.insert(0, prop.endereco)
            entry_desc.insert(0, prop.descricao)
            tipo_opt.set(prop.tipo)
            entry_venda.insert(0, str(prop.preco_venda))
            entry_loc.insert(0, str(prop.preco_locacao))

        msg_erro = ctk.CTkLabel(win, text="", text_color="#f97316")
        msg_erro.pack(pady=5)

        def salvar():
            
            try:
                endereco = entry_end.get()
                descricao = entry_desc.get()
                tipo = tipo_opt.get()
                venda = entry_venda.get()
                loc = entry_loc.get()

                if is_edit:
                    # atualiza o objeto existente
                    prop.endereco = endereco
                    prop.descricao = descricao
                    prop.tipo = tipo
                    prop.preco_venda = float(venda)
                    prop.preco_locacao = float(loc)
                    
                else:
                    nova = Propriedade(endereco, descricao, tipo, venda, loc)
                    self.imobiliaria.cadastrar_propriedade(nova)
                    

                self.imobiliaria.atualizar_propriedades()
                self.atualizar_cards()
                win.destroy()

            except ValueError as e:
                msg_erro.configure(text=str(e))

        ctk.CTkButton(
            win,
            text="Salvar",
            fg_color=self.colors["primary"],
            hover_color=self.colors["primary_hover"],
            command=salvar
        ).pack(pady=13)

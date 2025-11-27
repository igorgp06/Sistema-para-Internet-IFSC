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
            border_color=self.colors["border"],
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

        if prop.status.lower() == "disponível":
            prop_status = "Disponível"
        elif prop.status.lower() == "em negociação":
            prop_status = "Em negociação"
        elif prop.status.lower() == "vendido":
            prop_status = f"Vendido a: {prop.comprador.nome}" if prop.comprador else "Vendido"
        elif prop.status.lower() == "alugado":
            prop_status = f"Alugado a: {prop.locatario.nome}" if prop.locatario else "Alugado"
        else:
            prop_status = prop.status

        ctk.CTkLabel(
            top,
            text=prop_status,
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

        if prop.preco_venda == 0 or not prop.pd_vender:
            venda_text = "Não se aplica."
        else:
            venda_text = f"R$ {prop.preco_venda:,.2f}"

        ctk.CTkLabel(
            preco_frame,
            text=f"Venda: {venda_text}",
            font=("Segoe UI", 11),
            text_color=self.colors["foreground"]
        ).pack(anchor="w")


        if prop.preco_locacao == 0 or not prop.pd_alugar or prop.tipo == "terreno":
            loc_text = "Não se aplica."
        else:
            loc_text = f"R$ {prop.preco_locacao:,.2f}"

        ctk.CTkLabel(
            preco_frame,
            text=f"Locação: {loc_text}",
            font=("Segoe UI", 11),
            text_color=self.colors["foreground"]
        ).pack(anchor="w")

        # btns
        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(fill="x", padx=10, pady=(6, 10))

        btn_vender = ctk.CTkButton(
            btn_frame,
            text="Vender",
            fg_color="#f97316",
            hover_color="#fb923c",
            command=lambda p=prop: self.abrir_modal_vender(p)
        )
        
        btn_vender.pack(side="left", expand=True, fill="x", padx=(0, 5))
        
        if not prop.pd_vender or prop.preco_venda == 0:
            btn_vender.configure(state="disabled", fg_color="#1f2937")

        btn_alugar = ctk.CTkButton(
            btn_frame,
            text="Alugar",
            fg_color="#3b82f6",
            hover_color="#60a5fa",
            command=lambda p=prop: self.abrir_modal_alugar(p)
        )

        btn_alugar.pack(side="left", expand=True, fill="x", padx=(0, 5))

        if not prop.pd_alugar or prop.tipo == "terreno" or prop.preco_locacao == 0:
            btn_alugar.configure(state="disabled", fg_color="#1f2937")

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

    # ações

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

    # modais

    def abrir_modal_nova_prop(self):
        self._abrir_modal_prop()

    def abrir_modal_editar(self, prop):
        self._abrir_modal_prop(prop)

    def _abrir_modal_prop(self, prop=None):
        is_edit = prop is not None

        # config janela de nova propriedade ou edição
        win = ctk.CTkToplevel(self)
        win.title("Editar Propriedade" if is_edit else "Nova Propriedade")
        win.geometry("420x480")
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

        frame_checks = ctk.CTkFrame(win, fg_color="transparent")
        frame_checks.pack(fill="x", padx=20, pady=(15, 0))

        chk_vender = ctk.CTkCheckBox(frame_checks, text="Pode ser vendida")
        chk_vender.pack(side="left")

        chk_alugar = ctk.CTkCheckBox(frame_checks, text="Pode ser alugada")
        chk_alugar.pack(side="right")

        chk_vender.select()
        chk_alugar.select()

        # regras de negócio
        def aplicar_regras_tipo(tipo):
            if tipo == "terreno":
                chk_alugar.deselect()
                chk_alugar.configure(state="disabled")

                entry_loc.delete(0, "end")
                entry_loc.insert(0, "0")
                entry_loc.configure(state="disabled")
            else:
                chk_alugar.configure(state="normal")
                if chk_alugar.get() == 1:
                    entry_loc.configure(state="normal")

        def aplicar_regras_venda():
            if chk_vender.get() == 0:
                entry_venda.delete(0, "end")
                entry_venda.insert(0, "0")
                entry_venda.configure(state="disabled")
            else:
                entry_venda.configure(state="normal")

        def aplicar_regras_aluguel():
            if chk_alugar.get() == 0:
                entry_loc.delete(0, "end")
                entry_loc.insert(0, "0")
                entry_loc.configure(state="disabled")
            else:
                entry_loc.configure(state="normal")

        # eventos
        def on_tipo_change(tipo):
            aplicar_regras_tipo(tipo)

        tipo_opt.configure(command=on_tipo_change)

        chk_vender.configure(command=aplicar_regras_venda)
        chk_alugar.configure(command=aplicar_regras_aluguel)

        if is_edit:
            entry_end.insert(0, prop.endereco)
            entry_desc.insert(0, prop.descricao)
            tipo_opt.set(prop.tipo)

            entry_venda.insert(0, str(prop.preco_venda))
            entry_loc.insert(0, str(prop.preco_locacao))

            chk_vender.deselect() if not prop.pd_vender else chk_vender.select()
            chk_alugar.deselect() if not prop.pd_alugar else chk_alugar.select()

            aplicar_regras_tipo(prop.tipo)
            aplicar_regras_venda()
            aplicar_regras_aluguel()

        msg_erro = ctk.CTkLabel(win, text="", text_color="#f97316")
        msg_erro.pack(pady=5)

        def salvar():
            
            try:
                endereco = entry_end.get()
                descricao = entry_desc.get()
                tipo = tipo_opt.get()
                venda = entry_venda.get()
                locacao = entry_loc.get()
                pd_vender = chk_vender.get() == 1
                pd_alugar = chk_alugar.get() == 1

                if tipo == "terreno":
                    pd_alugar = False
                    locacao = 0

                if not (pd_vender or pd_alugar):
                    raise ValueError("Marque venda, aluguel ou ambos.")

                if is_edit:
                    # atualiza o objeto existente
                    prop.endereco = endereco
                    prop.descricao = descricao
                    prop.tipo = tipo
                    prop.preco_venda = float(venda)
                    prop.preco_locacao = float(locacao)
                    prop.pd_vender = pd_vender
                    prop.pd_alugar = pd_alugar

                else:
                    nova = Propriedade(endereco, descricao, tipo, venda, locacao, pd_vender, pd_alugar)
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
        ).pack(pady=13, padx=10)

    def abrir_modal_vender(self, prop):
        clientes = self.imobiliaria.listar_clientes()
        if not clientes:
            return 

        win = ctk.CTkToplevel(self)
        win.title("Selecionar comprador")
        win.geometry("300x200")
        win.resizable(False, False)
        win.grab_set()

        nomes = [c.nome for c in clientes]
        opt = ctk.CTkOptionMenu(win, values=nomes)
        opt.pack(pady=20)

        def confirmar():
            nome = opt.get()
            cliente = self.imobiliaria.buscar_cliente(nome)
            prop.comprador = cliente
            prop.marcar_vendida()
            self.imobiliaria.atualizar_propriedades()
            self.atualizar_cards()
            win.destroy()

        ctk.CTkButton(win, text="Confirmar",
                    fg_color=self.colors["primary"],
                    command=confirmar).pack(pady=10)

    def abrir_modal_alugar(self, prop):
        clientes = self.imobiliaria.listar_clientes()

        win = ctk.CTkToplevel(self)
        win.title("Selecionar locatário")
        win.geometry("300x200")
        win.resizable(False, False)
        win.grab_set()

        nomes = [c.nome for c in clientes]
        opt = ctk.CTkOptionMenu(win, values=nomes)
        opt.pack(pady=20)

        def confirmar():
            nome = opt.get()
            cliente = self.imobiliaria.buscar_cliente(nome)
            prop.locatario = cliente
            prop.marcar_alugada()
            self.imobiliaria.atualizar_propriedades()
            self.atualizar_cards()
            win.destroy()

        ctk.CTkButton(win, text="Confirmar",
                    fg_color=self.colors["primary"],
                    command=confirmar).pack(pady=10)

import customtkinter as ctk
from src.models.cliente import Cliente

class TelaClientes(ctk.CTkFrame):
    def __init__(self, master, imobiliaria, colors):
        super().__init__(master, fg_color=colors["background"])
        self.imobiliaria = imobiliaria
        self.colors = colors

        self.pack(expand=True, fill="both")

        self._criar_header()
        self._criar_area_lista()
        self.atualizar_lista()

    def _criar_header(self):
        header = ctk.CTkFrame(self, fg_color=self.colors["background"])
        header.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            header,
            text="Clientes",
            font=("Segoe UI", 22, "bold"),
            text_color=self.colors["foreground"]
        ).pack(side="left")

        ctk.CTkButton(
            header,
            text="+ Novo Cliente",
            fg_color=self.colors["primary"],
            hover_color=self.colors["primary_hover"],
            command=self.abrir_modal_novo_cliente
        ).pack(side="right")

    def _criar_area_lista(self):
        self.scroll = ctk.CTkScrollableFrame(self, fg_color=self.colors["background"])
        self.scroll.pack(expand=True, fill="both", padx=10, pady=(0, 10))

    def atualizar_lista(self):
        for w in self.scroll.winfo_children():
            w.destroy()

        clientes = self.imobiliaria.listar_clientes()

        if not clientes:
            ctk.CTkLabel(
                self.scroll,
                text="Nenhum cliente cadastrado.",
                text_color=self.colors["foreground"]
            ).pack(pady=10, anchor="w")
            return

        for c in clientes:
            self._criar_card_cliente(c)

    def _criar_card_cliente(self, cliente):
        card = ctk.CTkFrame(
            self.scroll,
            fg_color=self.colors["card"],
            border_color=self.colors["border"],
            border_width=2,
            corner_radius=12
        )
        card.pack(fill="x", padx=10, pady=8)

        ctk.CTkLabel(
            card,
            text=cliente.nome,
            font=("Segoe UI", 16, "bold"),
            text_color=self.colors["foreground"]
        ).pack(anchor="w", padx=10, pady=(8, 0))

        ctk.CTkLabel(
            card,
            text=f"Telefone: {cliente.telefone} | E-mail: {cliente.email}",
            font=("Segoe UI", 11),
            text_color="#9AA0A6"
        ).pack(anchor="w", padx=10)

        # interesses
        if cliente.interesses:
            txt = f"Interesse: " + ", ".join([p.endereco for p in cliente.interesses])
        else:
            txt = "O cliente não possui interesses cadastrados."

        ctk.CTkLabel(
            card,
            text=txt,
            font=("Segoe UI", 11),
            text_color=self.colors["foreground"]
        ).pack(anchor="w", padx=10, pady=(4, 8))

        btn_frame = ctk.CTkFrame(card, fg_color="transparent")
        btn_frame.pack(fill="x", padx=10, pady=(0, 10))

        ctk.CTkButton(
            btn_frame,
            text="Alterar interesses",
            fg_color="#3b82f6",
            hover_color="#60a5fa",
            command=lambda c=cliente: self.abrir_modal_interesse(c)
        ).pack(side="left", expand=True, fill="x", padx=(0, 5))

        ctk.CTkButton(
            btn_frame,
            text="Editar",
            fg_color=self.colors["primary"],
            hover_color=self.colors["primary_hover"],
            command=lambda c=cliente: self.abrir_modal_editar(c)
        ).pack(side="left", expand=True, fill="x", padx=5)

        ctk.CTkButton(
            btn_frame,
            text="Remover",
            fg_color="#b91c1c",
            hover_color="#dc2626",
            command=lambda c=cliente: self.remover_cliente(c)
        ).pack(side="left", expand=True, fill="x", padx=(5, 0))

    def abrir_modal_editar(self, cliente):
        win = ctk.CTkToplevel(self)
        win.title(f"Editar Cliente - {cliente.nome}")
        win.geometry("400x320")
        win.resizable(False, False)
        win.grab_set()

        lbl_style = {"text_color": self.colors["foreground"], "font": ("Segoe UI", 12)}

        ctk.CTkLabel(win, text="Nome", **lbl_style).pack(anchor="w", padx=20, pady=(15, 0))
        entry_nome = ctk.CTkEntry(win, width=340)
        entry_nome.pack(padx=20)

        ctk.CTkLabel(win, text="Telefone", **lbl_style).pack(anchor="w", padx=20, pady=(10, 0))
        entry_tel = ctk.CTkEntry(win, width=340)
        entry_tel.pack(padx=20)

        ctk.CTkLabel(win, text="E-mail", **lbl_style).pack(anchor="w", padx=20, pady=(10, 0))
        entry_email = ctk.CTkEntry(win, width=340)
        entry_email.pack(padx=20)

        entry_nome.insert(0, cliente.nome)
        entry_tel.insert(0, cliente.telefone)
        entry_email.insert(0, cliente.email)

        msg_erro = ctk.CTkLabel(win, text="", text_color="#f97316")
        msg_erro.pack(pady=5)

        def salvar():
            try:
                novo_nome = entry_nome.get()
                novo_tel = entry_tel.get()
                novo_email = entry_email.get()

                # validações gerais 
                if not novo_nome.strip():
                    raise ValueError("O nome do cliente não pode ser vazio.")
                
                if not novo_email.strip():
                    raise ValueError("O e-mail do cliente não pode ser vazio.")
                
                if "@" not in novo_email:
                    raise ValueError("E-mail inválido.")
                
                if not novo_tel.strip():
                    raise ValueError("O telefone do cliente não pode ser vazio.")
                
                if len(novo_tel) < 8:
                    raise ValueError("Telefone muito curto.")
                
                if len(novo_tel) > 15:
                    raise ValueError("Telefone muito longo.")
                
                if len(novo_nome) < 3:
                    raise ValueError("Nome muito curto.")
                
                if len(novo_nome) > 50:
                    raise ValueError("Nome muito longo.")

                # captura de duplicidade
                for c in self.imobiliaria.listar_clientes():
                    if c is cliente:
                        continue
                    if c.nome == novo_nome:
                        raise ValueError("Já existe um cliente com esse nome.")
                    if c.email == novo_email:
                        raise ValueError("Já existe um cliente com esse e-mail.")
                    if c.telefone == novo_tel:
                        raise ValueError("Já existe um cliente com esse telefone.")

                # se ñ cair em nenhuma exception atualiza os dados
                cliente.nome = novo_nome
                cliente.telefone = novo_tel
                cliente.email = novo_email

                self.imobiliaria.atualizar_clientes()
                self.atualizar_lista()
                win.destroy()

            except ValueError as e:
                msg_erro.configure(text=str(e))
            except Exception:
                msg_erro.configure(text="Erro inesperado ao atualizar o cliente.")

        ctk.CTkButton(
            win,
            text="Salvar",
            fg_color=self.colors["primary"],
            hover_color=self.colors["primary_hover"],
            command=salvar
        ).pack(pady=20)

    def abrir_modal_novo_cliente(self):
        win = ctk.CTkToplevel(self)
        win.title("Cadastrar novo Cliente")
        win.geometry("400x320")
        win.resizable(False, False)
        win.grab_set()

        lbl_style = {"text_color": self.colors["foreground"], "font": ("Segoe UI", 12)}

        ctk.CTkLabel(win, text="Nome", **lbl_style).pack(anchor="w", padx=20, pady=(15, 0))
        entry_nome = ctk.CTkEntry(win, width=340)
        entry_nome.pack(padx=20)

        ctk.CTkLabel(win, text="Telefone", **lbl_style).pack(anchor="w", padx=20, pady=(10, 0))
        entry_tel = ctk.CTkEntry(win, width=340)
        entry_tel.pack(padx=20)

        ctk.CTkLabel(win, text="E-mail", **lbl_style).pack(anchor="w", padx=20, pady=(10, 0))
        entry_email = ctk.CTkEntry(win, width=340)
        entry_email.pack(padx=20)

        msg_erro = ctk.CTkLabel(win, text="", text_color="#f97316")
        msg_erro.pack(pady=5)

        def salvar():
            
            try:
                
                cliente = Cliente(entry_nome.get(), entry_tel.get(), entry_email.get())
                
                # erros de duplicidade
                
                if any(c.nome == cliente.nome for c in self.imobiliaria.listar_clientes()):
                    raise ValueError("Já existe um cliente com esse nome.")
                
                if any(c.email == cliente.email for c in self.imobiliaria.listar_clientes()):
                    raise ValueError("Já existe um cliente com esse e-mail.")
                
                if any(c.telefone == cliente.telefone for c in self.imobiliaria.listar_clientes()):
                    raise ValueError("Já existe um cliente com esse telefone.")
                
                # erros de validação geral
                
                if not cliente.nome.strip():
                    raise ValueError("O nome do cliente não pode ser vazio.")
                
                if not cliente.email.strip():
                    raise ValueError("O e-mail do cliente não pode ser vazio.")
                
                if not cliente.telefone.strip():
                    raise ValueError("O telefone do cliente não pode ser vazio.")
                
                if not cliente.email.strip() or "@" not in cliente.email:
                    raise ValueError("E-mail inválido.")
                
                if not cliente.telefone.strip():
                    raise ValueError("Telefone inválido.")
                
                if len(cliente.telefone) < 8:
                    raise ValueError("Telefone muito curto.")
                
                if len(cliente.telefone) > 15:
                    raise ValueError("Telefone muito longo.")
                
                if len(cliente.nome) < 3:
                    raise ValueError("Nome muito curto.")
                
                if len(cliente.nome) > 50:
                    raise ValueError("Nome muito longo.")
                
                self.imobiliaria.cadastrar_cliente(cliente)
                
                self.imobiliaria.atualizar_clientes()
                
                self.atualizar_lista()
                win.destroy()
                
            except ValueError as e:
                msg_erro.configure(text=str(e))
                
            except Exception as e:
                msg_erro.configure(text="Erro inesperado no sistema.")

        ctk.CTkButton(
            win,
            text="Salvar",
            fg_color=self.colors["primary"],
            hover_color=self.colors["primary_hover"],
            command=salvar
        ).pack(pady=20)

    def abrir_modal_interesse(self, cliente):
        props = self.imobiliaria.listar_propriedades()
        if not props:
            return

        win = ctk.CTkToplevel(self)
        win.title(f"Interesse do Cliente: {cliente.nome}")
        win.geometry("400x250")
        win.resizable(False, False)
        win.grab_set()

        ctk.CTkLabel(
            win,
            text="Selecione a propriedade de interesse:",
            text_color=self.colors["foreground"]
        ).pack(padx=20, pady=(20, 10))

        enderecos = [p.endereco for p in props]
        opt = ctk.CTkOptionMenu(win, values=enderecos)
        opt.pack(padx=20)

        def marcar():
            end = opt.get()
            prop = self.imobiliaria.buscar_propriedade(end)
            if prop:
                cliente.adicionar_interesse(prop)
                self.imobiliaria.atualizar_clientes()
                self.atualizar_lista()
            win.destroy()

        ctk.CTkButton(
            win,
            text="Confirmar",
            fg_color=self.colors["primary"],
            hover_color=self.colors["primary_hover"],
            command=marcar
        ).pack(pady=20)

    def remover_cliente(self, cliente):
        self.imobiliaria.remover_cliente(cliente.nome)
        self.atualizar_lista()

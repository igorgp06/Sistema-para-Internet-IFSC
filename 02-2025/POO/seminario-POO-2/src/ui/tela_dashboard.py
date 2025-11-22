import customtkinter as ctk

class TelaDashboard(ctk.CTkFrame):
    def __init__(self, master, imobiliaria, colors):
        super().__init__(master, fg_color=colors["background"])
        self.imobiliaria = imobiliaria
        self.colors = colors

        self.pack(expand=True, fill="both")

        self._criar_header()
        self._criar_cards()

    def _criar_header(self):
        header = ctk.CTkFrame(self, fg_color=self.colors["background"])
        header.pack(fill="x", padx=20, pady=(10, 0))

        ctk.CTkLabel(
            header,
            text="Visão geral do Sistema",
            font=("Segoe UI", 20, "bold"),
            text_color=self.colors["foreground"]
        ).pack(side="left")

        ctk.CTkLabel(
            header,
            text="Resumo das propriedades e clientes cadastrados",
            font=("Segoe UI", 12),
            text_color="#9AA0A6"
        ).pack(side="left", padx=(10, 0))

    def _criar_cards(self):
        props = self.imobiliaria.listar_propriedades()
        clientes = self.imobiliaria.listar_clientes()

        total = len(props)
        vendidas = len([p for p in props if p.status == "vendido"])
        alugadas = len([p for p in props if p.status == "alugado"])
        disponiveis = len([p for p in props if p.status == "disponível"])

        grid = ctk.CTkFrame(self, fg_color=self.colors["background"])
        grid.pack(expand=True, fill="both", padx=20, pady=20)

        # 4 colunas com mesmo tamanho
        for col in range(4):
            grid.grid_columnconfigure(col, weight=1, uniform="cards")

        # 2 linhas (linha 0 = 4 cards, linha 1 = 1 card full width)
        grid.grid_rowconfigure(0, weight=1)
        grid.grid_rowconfigure(1, weight=1)

        def card(titulo, valor, row, col, col_span=1, cor_valor=None):
            frame = ctk.CTkFrame(
                grid,
                fg_color=self.colors["card"],
                border_color=self.colors["border"],
                border_width=2,
                corner_radius=12
            )
            frame.grid(
                row=row,
                column=col,
                columnspan=col_span,
                padx=10,
                pady=10,
                sticky="nsew"  # ocupa toda a célula
            )

            ctk.CTkLabel(
                frame,
                text=titulo,
                font=("Segoe UI", 13),
                text_color="#9AA0A6"
            ).pack(anchor="w", padx=16, pady=(12, 0))

            ctk.CTkLabel(
                frame,
                text=str(valor),
                font=("Segoe UI", 24, "bold"),
                text_color=cor_valor or self.colors["foreground"]
            ).pack(anchor="w", padx=16, pady=(2, 12))

        # linha 0
        card("Total de propriedades", total,        0, 0)
        card("Disponíveis",            disponiveis, 0, 1, cor_valor="#22c55e")
        card("Vendidas",               vendidas,    0, 2, cor_valor="#f97316")
        card("Alugadas",               alugadas,    0, 3, cor_valor="#3b82f6")

        # linha 1: ocupa todas as colunas
        card("Clientes cadastrados", len(clientes), 1, 0, col_span=4)

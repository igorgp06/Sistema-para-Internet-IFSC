import customtkinter as ctk

class TelaDashboard(ctk.CTkFrame):
    def __init__(self, master, imobiliaria, colors):
        super().__init__(master, fg_color=colors["background"])
        self.imobiliaria = imobiliaria
        self.colors = colors

        self.pack(expand=True, fill="both")

        self._criar_cards()

    def _criar_cards(self):
        props = self.imobiliaria.listar_propriedades()
        clientes = self.imobiliaria.listar_clientes()

        total = len(props)
        vendidas = len([p for p in props if p.status == "vendido"])
        alugadas = len([p for p in props if p.status == "alugado"])
        disponiveis = len([p for p in props if p.status == "disponível"])

        grid = ctk.CTkFrame(self, fg_color=self.colors["background"])
        grid.pack(expand=True)

        def card(titulo, valor, row, col):
            frame = ctk.CTkFrame(
                grid,
                fg_color=self.colors["card"],
                border_color=self.colors["border"],
                border_width=2,
                corner_radius=12
            )
            frame.grid(row=row, column=col, padx=15, pady=15, ipadx=20, ipady=20) # TODO espaçamento quebrado, arrumar

            ctk.CTkLabel(
                frame,
                text=titulo,
                font=("Segoe UI", 14),
                text_color="#9AA0A6"
            ).pack()

            ctk.CTkLabel(
                frame,
                text=str(valor),
                font=("Segoe UI", 24, "bold"),
                text_color=self.colors["foreground"]
            ).pack()

        card("Total de propriedades", total, 0, 0)
        card("Disponíveis", disponiveis, 0, 1)
        card("Vendidas", vendidas, 0, 2)
        card("Alugadas", alugadas, 0, 3)
        card("Clientes cadastrados", len(clientes), 1, 0)

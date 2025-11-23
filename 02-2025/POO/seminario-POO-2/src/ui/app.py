import customtkinter as ctk

from src.models.imobiliaria import Imobiliaria
from src.ui.tela_dashboard import TelaDashboard
from src.ui.tela_propriedades import TelaPropriedades
from src.ui.tela_clientes import TelaClientes

COLORS = {
    "background": "#06090F",
    "foreground": "#E6EDF7",
    "card": "#0B111C",
    "primary": "#9C6BFF",
    "primary_hover": "#B189FF",
    "border": "#1E2838"
}

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # base
        ctk.set_appearance_mode("dark")

        self.title("Sistema Imobiliário - Igor Gonçalves")
        self.geometry("1000x600")
        self.resizable(False, False)

        # imobiliaria
        self.imobiliaria = Imobiliaria()

        # barra lateral
        self.sidebar = ctk.CTkFrame(
            self,
            width=260,
            fg_color=COLORS["card"],
        )
        self.sidebar.pack(side="left", fill="y")

        ctk.CTkLabel(
            self.sidebar,
            text="Sistema Imobiliário",
            font=("Segoe UI", 20, "bold"),
            text_color=COLORS["foreground"]
        ).pack(pady=30, padx=10)
        self.sidebar.pack_propagate(False)

        ctk.CTkButton(
            self.sidebar,
            text="Dashboard",
            fg_color=COLORS["primary"],
            hover_color=COLORS["primary_hover"],
            command=self.mostrar_dashboard
        ).pack(pady=10, padx=10 , fill="x")

        ctk.CTkButton(
            self.sidebar,
            text="Propriedades",
            fg_color=COLORS["primary"],
            hover_color=COLORS["primary_hover"],
            command=self.mostrar_propriedades
        ).pack(pady=10, padx=10 , fill="x")

        ctk.CTkButton(
            self.sidebar,
            text="Clientes",
            fg_color=COLORS["primary"],
            hover_color=COLORS["primary_hover"],
            command=self.mostrar_clientes
        ).pack(pady=10, padx=10 , fill="x")

        # area de conteudo
        self.frame_conteudo = ctk.CTkFrame(
            self,
            fg_color=COLORS["background"]
        )
        self.frame_conteudo.pack(side="right", expand=True, fill="both")

        self.mostrar_dashboard()

    def limpar_conteudo(self):
        for widget in self.frame_conteudo.winfo_children():
            widget.destroy()

    def mostrar_dashboard(self):
        self.limpar_conteudo()
        TelaDashboard(self.frame_conteudo, self.imobiliaria, COLORS)

    def mostrar_propriedades(self):
        self.limpar_conteudo()
        TelaPropriedades(self.frame_conteudo, self.imobiliaria, COLORS)

    def mostrar_clientes(self):
        self.limpar_conteudo()
        TelaClientes(self.frame_conteudo, self.imobiliaria, COLORS)

if __name__ == "__main__":
    app = App()
    app.mainloop()

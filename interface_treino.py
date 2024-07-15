import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from usuario import Usuario


class InterfaceTreino:
    def __init__(self, usuario):
        """
        Inicializa a interface gráfica da aplicação..

        Parâmetros:
        usuario (Usuario): Um objeto da classe Usuario que contém os métodos e dados do usuário.
        """
        self.usuario = usuario
        self.root = tk.Tk()
        self.root.geometry('700x900')
        self.root.title("Treino Personalizado")

        # Criação de um canvas com barra de rolagem
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame = ttk.Frame(self.canvas, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_window((0, 0), window=self.frame, anchor=tk.NW)

        # Título da aplicação
        self.label = ttk.Label(self.frame, text="Perguntas sobre o Treino", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.N)

        # Verifica se o treino já foi salvo e exibe ou faz perguntas ao usuário
        if self.usuario.verificar_treino_salvo():
            self.usuario.carregar_treino_salvo()
            self.exibir_treino()
        else:
            self.perguntas_dias_treino()
            self.pergunta_experiencia()
            self.pergunta_lesao_limitacao()

            # Botão para confirmar as respostas
            self.botao_confirmar = ttk.Button(self.frame, text="Confirmar", command=self.confirmar_respostas)
            self.botao_confirmar.grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=10)

        # Configurações para a barra de rolagem
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def perguntas_dias_treino(self):
        """
        Adiciona os checkboxes para selecionar os dias de treino.
        """
        ttk.Label(self.frame, text="Dias de Treino (selecione todos que aplicam):", anchor=tk.CENTER).grid(
            row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=5, sticky=tk.W)

        self.checkboxes_dias = []
        for dia in ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']:
            var = tk.IntVar()
            checkbox = ttk.Checkbutton(self.frame, text=dia, variable=var)
            checkbox.grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, sticky=tk.W)
            self.checkboxes_dias.append((dia, var))

    def pergunta_experiencia(self):
        """
        Adiciona os radiobuttons para selecionar o nível de experiência em musculação.
        """
        ttk.Label(self.frame, text="Experiência em Musculação:", anchor=tk.CENTER).grid(
            row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=5, sticky=tk.W)

        self.radio_experiencia = tk.StringVar()
        for nivel in [('Iniciante', '1'), ('Intermediário', '2'), ('Avançado', '3')]:
            ttk.Radiobutton(self.frame, text=nivel[0], variable=self.radio_experiencia, value=nivel[1]).grid(
                row=len(self.frame.grid_slaves()), column=0, columnspan=2, sticky=tk.W)

    def pergunta_lesao_limitacao(self):
        """
        Adiciona os radiobuttons para selecionar lesões ou limitações físicas.
        """
        ttk.Label(self.frame, text="Lesões ou Limitações Físicas:", anchor=tk.CENTER).grid(
            row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=5, sticky=tk.W)

        self.radio_lesao_limitacao = tk.StringVar()
        for opcao in ['Nenhuma', 'Ombro', 'Braços (incluindo cotovelos, punhos e mãos)',
                      'Pernas (incluindo quadril, joelhos, tornozelos e pés)']:
            ttk.Radiobutton(self.frame, text=opcao, variable=self.radio_lesao_limitacao, value=opcao).grid(
                row=len(self.frame.grid_slaves()), column=0, columnspan=2, sticky=tk.W)

    def confirmar_respostas(self):
        """
        Obtém as respostas do usuário, verifica a validade e salva os dados no objeto Usuario.
        """
        dias_selecionados = [dia for dia, var in self.checkboxes_dias if var.get() == 1]
        experiencia = {'texto': self.radio_experiencia.get(), 'numero': int(self.radio_experiencia.get())}
        lesao_limitacao = self.radio_lesao_limitacao.get()

        if not dias_selecionados:
            messagebox.showwarning("Erro", "Selecione pelo menos um dia de treino.")
            return

        if experiencia['texto'] not in ['1', '2', '3']:
            messagebox.showwarning("Erro", "Selecione um nível de experiência.")
            return

        if lesao_limitacao == '':
            messagebox.showwarning("Erro", "Selecione uma opção de lesão ou limitação física.")
            return

        self.usuario.receber_dias_treino(dias_selecionados)
        self.usuario.receber_experiencia(experiencia)
        self.usuario.receber_lesao_limitacao(lesao_limitacao)

        self.usuario.montar_treino()
        self.usuario.salvar_treinos_excel()
        self.exibir_treino()

    def exibir_treino(self):
        """
        Exibe o treino montado com base nas respostas do usuário.
        """
        for widget in self.frame.winfo_children():
            widget.destroy()

        ttk.Label(self.frame, text="\n*** Treino Montado ***\n", font=("Helvetica", 10)).grid(row=0, column=0,
                                                                                              columnspan=2, pady=10)

        fonte_treino = ("Helvetica", 9)
        for dia in self.usuario.treino_selecionado:
            ttk.Label(self.frame, text=f"Dia: {dia['dia']}", font=("Helvetica", 13, "bold")).grid(
                row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=5)
            for treino in dia['treino']:
                ttk.Label(self.frame, text=f"\nGrupo Muscular: {treino['grupo_muscular']}", font=fonte_treino).grid(
                    row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=3)
                for exercicio in treino['exercicios']:
                    ttk.Label(self.frame,
                              text=f"Exercício: {exercicio['exercicio']} - Séries: {exercicio['series']} - Repetições: {exercicio['repeticoes']}",
                              font=fonte_treino).grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=3)
                ttk.Separator(self.frame, orient='horizontal').grid(row=len(self.frame.grid_slaves()), column=0,
                                                                    columnspan=2, pady=5, sticky="ew")

        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):
        """
        Permite a rolagem vertical do canvas usando o mouse.
        """
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def exibir_interface(self):
        """
        Inicia o loop principal da interface Tkinter.
        """
        self.root.mainloop()

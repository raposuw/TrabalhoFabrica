import tkinter as tk
from tkinter import ttk, messagebox

class InterfaceTreino:
    def __init__(self, usuario):
        self.usuario = usuario
        self.root = tk.Tk()
        self.root.geometry('700x900')
        self.root.title("Treino Personalizado")

        # Cria um Canvas com Scrollbars
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame = ttk.Frame(self.canvas, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_window((0, 0), window=self.frame, anchor=tk.NW)

        self.label = ttk.Label(self.frame, text="Perguntas sobre o Treino", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.perguntas_dias_treino()
        self.pergunta_experiencia()
        self.pergunta_lesao_limitacao()

        self.botao_confirmar = ttk.Button(self.frame, text="Confirmar", command=self.confirmar_respostas)
        self.botao_confirmar.grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=10)

        # Configurações adicionais para o scroll
        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def perguntas_dias_treino(self):
        ttk.Label(self.frame, text="Dias de Treino (selecione todos que aplicam):").grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=5)

        self.checkboxes_dias = []
        for dia in ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']:
            var = tk.IntVar()
            checkbox = ttk.Checkbutton(self.frame, text=dia, variable=var)
            checkbox.grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, sticky=tk.W)
            self.checkboxes_dias.append((dia, var))

    def pergunta_experiencia(self):
        ttk.Label(self.frame, text="Experiência em Musculação:").grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=5)

        self.radio_experiencia = tk.StringVar()
        for nivel in [('Iniciante', '1'), ('Intermediário', '2'), ('Avançado', '3')]:
            ttk.Radiobutton(self.frame, text=nivel[0], variable=self.radio_experiencia, value=nivel[1]).grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, sticky=tk.W)

    def pergunta_lesao_limitacao(self):
        ttk.Label(self.frame, text="Lesões ou Limitações Físicas:").grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=5)

        self.radio_lesao_limitacao = tk.StringVar()
        for opcao in ['Nenhuma', 'Ombro', 'Braços (incluindo cotovelos, punhos e mãos)', 'Pernas (incluindo quadril, joelhos, tornozelos e pés)']:
            ttk.Radiobutton(self.frame, text=opcao, variable=self.radio_lesao_limitacao, value=opcao).grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, sticky=tk.W)

    def confirmar_respostas(self):
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
        self.exibir_treino()

    def exibir_treino(self):
        # Limpa o frame atual das perguntas
        for widget in self.frame.winfo_children():
            widget.destroy()

        ttk.Label(self.frame, text="\n*** Treino Montado ***\n", font=("Helvetica", 10)).grid(row=0, column=0, columnspan=2, pady=10)

        # Reduzindo o tamanho da fonte para os treinos
        fonte_treino = ("Helvetica", 9)
        for dia in self.usuario.treino_selecionado:
            ttk.Label(self.frame, text=f"Dia: {dia['dia']}", font=("Helvetica", 13, "bold")).grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=5)
            for treino in dia['treino']:
                ttk.Label(self.frame, text=f"\nGrupo Muscular: {treino['grupo_muscular']}", font=fonte_treino).grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=3)
                for exercicio in treino['exercicios']:
                    ttk.Label(self.frame, text=f"Exercício: {exercicio['exercicio']} - Séries: {exercicio['series']} - Repetições: {exercicio['repeticoes']}", font=fonte_treino).grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=3)
                ttk.Separator(self.frame, orient='horizontal').grid(row=len(self.frame.grid_slaves()), column=0, columnspan=2, pady=5, sticky="ew")

        # Atualiza a área de visualização no Canvas
        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def exibir_interface(self):
        self.root.mainloop()

if __name__ == "__main__":
    from cadastro import Usuario  # Importar a classe Usuario aqui

    usuario = Usuario()
    interface = InterfaceTreino(usuario)
    interface.exibir_interface()

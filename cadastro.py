from openpyxl import load_workbook
import os

class Usuario:
    def __init__(self):
        self.dias_treino = []
        self.experiencia = None
        self.lesao_limitacao = None
        self.treino_selecionado = []

    def perguntar_dias_treino(self):
        print("Quais dias da semana você planeja treinar? (Separe por vírgula)")
        print("( ) segunda")
        print("( ) terça")
        print("( ) quarta")
        print("( ) quinta")
        print("( ) sexta")
        print("( ) sábado")
        print("( ) domingo")
        dias_treino = input("Digite os dias de treino: ").strip().lower().split(", ")
        dias_validos = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
        for dia in dias_treino:
            if dia not in dias_validos:
                print(f"Dia inválido: {dia}. Por favor, escolha apenas dias válidos.")
                return self.perguntar_dias_treino()
        self.dias_treino = dias_treino

    def perguntar_experiencia_musculacao(self):
        print("Qual é o seu nível atual de experiência com musculação?")
        print("1. Iniciante (menos de 6 meses)")
        print("2. Intermediário (6 meses a 2 anos)")
        print("3. Avançado (mais de 2 anos)")
        opcao = input("Escolha uma opção pelo número correspondente: ").strip().lower()
        while opcao not in ['1', '2', '3']:
            print("Opção inválida. Escolha uma opção válida.")
            opcao = input("Escolha uma opção pelo número correspondente: ").strip().lower()

        opcoes = {
            '1': {"numero": 1, "resposta": "Iniciante (menos de 6 meses)"},
            '2': {"numero": 2, "resposta": "Intermediário (6 meses a 2 anos)"},
            '3': {"numero": 3, "resposta": "Avançado (mais de 2 anos)"}
        }
        self.experiencia = opcoes[opcao]

    def perguntar_lesao_limitacao(self):
        print("Você tem alguma lesão ou limitação física que devemos considerar ao montar seu treino?")
        print("1. Sim")
        print("2. Não")
        resposta = input("Escolha uma opção pelo número correspondente ou deixe em branco para não especificar: ").strip().lower()
        while resposta not in ['1', '2', '']:
            print("Opção inválida. Escolha uma opção válida.")
            resposta = input("Escolha uma opção pelo número correspondente ou deixe em branco para não especificar: ").strip().lower()

        if resposta == '1':
            print("Opções de lesão ou limitação física:")
            print("1. Ombros")
            print("2. Costas")
            print("3. Braços (incluindo cotovelos, punhos e mãos)")
            print("4. Pernas (incluindo quadril, joelhos, tornozelos e pés)")
            opcao = input("Escolha uma opção pelo número correspondente: ").strip().lower()
            while opcao not in ['1', '2', '3', '4']:
                print("Opção inválida. Escolha uma opção válida.")
                opcao = input("Escolha uma opção pelo número correspondente: ").strip().lower()

            opcoes = {
                '1': "Ombros",
                '2': "Costas",
                '3': "Braços (incluindo cotovelos, punhos e mãos)",
                '4': "Pernas (incluindo quadril, joelhos, tornozelos e pés)"
            }
            self.lesao_limitacao = {"numero": opcao, "resposta": opcoes[opcao]}
        else:
            self.lesao_limitacao = {"numero": resposta, "resposta": "Não"}

    def coletar_respostas(self):
        self.perguntar_dias_treino()
        self.perguntar_experiencia_musculacao()
        self.perguntar_lesao_limitacao()

    def carregar_treinos_excel(self):
        caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        arquivo_excel = os.path.join(caminho_downloads, 'planilha_treinos.xlsx')

        workbook = load_workbook(filename=arquivo_excel, read_only=True)
        sheet = workbook.active

        treinos = []

        for row in sheet.iter_rows(min_row=2, values_only=True):
            grupo_muscular, dificuldade, exercicio1, series1, repeticoes1, exercicio2, series2, repeticoes2, exercicio3, series3, repeticoes3, exercicio4, series4, repeticoes4 = row
            treinos.append({
                'grupo_muscular': grupo_muscular,
                'dificuldade': dificuldade,
                'exercicios': [
                    {'exercicio': exercicio1, 'series': series1, 'repeticoes': repeticoes1},
                    {'exercicio': exercicio2, 'series': series2, 'repeticoes': repeticoes2},
                    {'exercicio': exercicio3, 'series': series3, 'repeticoes': repeticoes3},
                    {'exercicio': exercicio4, 'series': series4, 'repeticoes': repeticoes4}
                ]
            })

        return treinos

    def selecionar_exercicios(self, grupo_muscular, dificuldade):
        treinos = self.carregar_treinos_excel()
        exercicios_selecionados = []

        for treino in treinos:
            if treino['grupo_muscular'].lower() == grupo_muscular.lower() and (str(treino['dificuldade']).lower() == dificuldade.lower() or (treino['dificuldade'] == 2 and dificuldade == '3')):
                exercicios_selecionados.extend(treino['exercicios'][:2])  # Seleciona os dois primeiros exercícios

        return exercicios_selecionados

    def montar_treino(self):
        treino_completo = []

        for dia in self.dias_treino:
            treino_dia = []

            for grupo_muscular in ['peito', 'ombro', 'bíceps', 'tríceps', 'antebraço', 'costas', 'quadríceps', 'posterior de coxa', 'glúteo']:
                exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']))
                if exercicios:
                    treino_dia.append({
                        'grupo_muscular': grupo_muscular.capitalize(),
                        'exercicios': exercicios
                    })

            if treino_dia:
                treino_completo.append({
                    'dia': dia.capitalize(),
                    'treino': treino_dia
                })
            else:
                print(f"Não há treino definido para {dia.capitalize()}.")

        self.treino_selecionado = treino_completo

    def imprimir_treino(self):
        for treino_dia in self.treino_selecionado:
            print(f"Dia de Treino: {treino_dia['dia']}")
            for grupo in treino_dia['treino']:
                print(f"Grupo Muscular: {grupo['grupo_muscular']}")
                for exercicio in grupo['exercicios']:
                    if exercicio['exercicio'] is not None:  # Verifica se há exercício definido
                        print(f"Exercício: {exercicio['exercicio']}, Séries: {exercicio['series']}, Repetições: {exercicio['repeticoes']}")
                print()  # Linha em branco entre os grupos musculares

# Exemplo de uso:
usuario = Usuario()
usuario.coletar_respostas()
usuario.montar_treino()
usuario.imprimir_treino()

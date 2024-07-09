from openpyxl import load_workbook, Workbook
import os

class Usuario:
    def __init__(self):
        self.dias_treino = []
        self.experiencia = None
        self.lesao_limitacao = None
        self.treino_selecionado = []

    def receber_dias_treino(self, dias_treino):
        self.dias_treino = dias_treino

    def receber_experiencia(self, experiencia):
        self.experiencia = experiencia

    def receber_lesao_limitacao(self, lesao_limitacao):
        self.lesao_limitacao = lesao_limitacao


    def carregar_treinos_excel(self):
        caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        arquivo_excel = os.path.join(caminho_downloads, 'planilha_treinos.xlsx')

        workbook = load_workbook(filename=arquivo_excel, read_only=True)
        sheet = workbook.active

        treinos = []

        for row in sheet.iter_rows(min_row=2, values_only=True):
            grupo_muscular, dificuldade, exercicio1, series1, repeticoes1, exercicio2, series2, repeticoes2, exercicio3, series3, repeticoes3, exercicio4, series4, repeticoes4 = row
            treinos.append({
                'grupo_muscular': grupo_muscular.lower(),
                'dificuldade': dificuldade,
                'exercicios': [
                    {'exercicio': exercicio1, 'series': series1, 'repeticoes': repeticoes1},
                    {'exercicio': exercicio2, 'series': series2, 'repeticoes': repeticoes2},
                    {'exercicio': exercicio3, 'series': series3, 'repeticoes': repeticoes3},
                    {'exercicio': exercicio4, 'series': series4, 'repeticoes': repeticoes4}
                ]
            })

        return treinos

    def selecionar_exercicios(self, grupo_muscular, dificuldade, grupos_selecionados, max_exercicios=3):
        treinos = self.carregar_treinos_excel()
        exercicios_selecionados = []

        for treino in treinos:
            if treino['grupo_muscular'] == grupo_muscular and (str(treino['dificuldade']).lower() == dificuldade.lower() or (treino['dificuldade'] == 2 and dificuldade == '3')):
                for exercicio in treino['exercicios']:
                    if exercicio['exercicio'] is not None and exercicio['exercicio'] not in grupos_selecionados:
                        exercicios_selecionados.append(exercicio)
                        grupos_selecionados.add(exercicio['exercicio'])

                if len(exercicios_selecionados) >= max_exercicios:
                    break

        return exercicios_selecionados[:max_exercicios]  # Limita aos primeiros exercícios

    def montar_treino(self):
        treino_completo = []
        if len(self.dias_treino) == 1:
            # Treino de um dia na semana
            treino_dia = []
            grupos_selecionados = set()
            for grupo_muscular in ['peito', 'ombro', 'tríceps', 'costas', 'antebraço', 'bíceps', 'quadríceps', 'posterior de coxa', 'glúteo']:
                exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']), grupos_selecionados, max_exercicios=2)
                if exercicios:
                    treino_dia.append({
                        'grupo_muscular': grupo_muscular.capitalize(),
                        'exercicios': exercicios
                    })
            if treino_dia:
                treino_completo.append({
                    'dia': self.dias_treino[0].capitalize(),
                    'treino': treino_dia
                })
            else:
                print(f"Não há treino definido para {self.dias_treino[0].capitalize()}.")

        elif len(self.dias_treino) == 2:
            # Treino separado em superiores e inferiores para dois dias na semana
            for i, dia in enumerate(self.dias_treino):
                treino_dia = []
                grupos_selecionados = set()
                if i == 0:  # Primeiro dia: Superiores
                    for grupo_muscular in ['peito', 'ombro', 'tríceps', 'costas', 'antebraço', 'bíceps']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']), grupos_selecionados, max_exercicios=3)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 1:  # Segundo dia: Inferiores
                    for grupo_muscular in ['quadríceps', 'posterior de coxa', 'glúteo']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']), grupos_selecionados, max_exercicios=3)
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

        elif len(self.dias_treino) == 3:
            # Treino dividido em três dias na semana
            for i, dia in enumerate(self.dias_treino):
                treino_dia = []
                grupos_selecionados = set()
                if i == 0:  # Primeiro dia: Peito, Ombro, Tríceps
                    for grupo_muscular in ['peito', 'ombro', 'tríceps']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']), grupos_selecionados, max_exercicios=3)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 1:  # Segundo dia: Costas, Antebraço, Bíceps
                    for grupo_muscular in ['costas', 'antebraço', 'bíceps']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']), grupos_selecionados, max_exercicios=3)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 2:  # Terceiro dia: Quadríceps, Posterior de coxa, Glúteo
                    for grupo_muscular in ['quadríceps', 'posterior de coxa', 'glúteo']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']), grupos_selecionados, max_exercicios=3)
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

        elif len(self.dias_treino) == 4:
            # Treino dividido em três dias na semana
            for i, dia in enumerate(self.dias_treino):
                treino_dia = []
                grupos_selecionados = set()
                if i == 0:  # Primeiro dia: Peito, Tríceps
                    for grupo_muscular in ['peito', 'ombro']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 1:  # Segundo dia: Costas, Antebraço,
                    for grupo_muscular in ['costas', 'antebraço']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 2:  # Terceiro dia: Quadríceps, Posterior de coxa, Glúteo
                    for grupo_muscular in ['quadríceps', 'posterior de coxa', 'glúteo']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 3:  # Quarto dia : Biceps e triceps
                    for grupo_muscular in ['bíceps', 'tríceps']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
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
        elif len(self.dias_treino) == 5:
            # Treino dividido em três dias na semana
            for i, dia in enumerate(self.dias_treino):
                treino_dia = []
                grupos_selecionados = set()
                if i == 0:  # Primeiro dia: Peito, Tríceps
                    for grupo_muscular in ['peito']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 1:  # Segundo dia: Costas, Antebraço,
                    for grupo_muscular in ['costas']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 2:  # Terceiro dia: Quadríceps, Posterior de coxa, Glúteo
                    for grupo_muscular in ['quadríceps', 'posterior de coxa', 'glúteo']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 3:  # Quarto dia : Biceps e triceps
                    for grupo_muscular in ['bíceps', 'tríceps']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 4:  # Quarto dia : Biceps e triceps
                    for grupo_muscular in ['ombro', 'antebraço']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
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
        elif len(self.dias_treino) == 6:
            # Treino dividido em três dias na semana
            for i, dia in enumerate(self.dias_treino):
                treino_dia = []
                grupos_selecionados = set()
                if i == 0:  # Primeiro dia: Peito, Tríceps
                    for grupo_muscular in ['peito']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 1:  # Segundo dia: Costas, Antebraço,
                    for grupo_muscular in ['costas']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 2:  # Terceiro dia: Quadríceps, Posterior de coxa, Glúteo
                    for grupo_muscular in ['quadríceps', 'posterior de coxa', 'glúteo']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 3:  # Quarto dia : Biceps e triceps
                    for grupo_muscular in ['bíceps']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 4:  # Quarto dia : Biceps e triceps
                    for grupo_muscular in ['tríceps']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 5:  # Quarto dia : Biceps e triceps
                    for grupo_muscular in ['ombro', 'antebraço']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
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
        elif len(self.dias_treino) == 7:
            # Treino dividido em três dias na semana
            for i, dia in enumerate(self.dias_treino):
                treino_dia = []
                grupos_selecionados = set()
                if i == 0:  # Primeiro dia: Peito, Tríceps
                    for grupo_muscular in ['peito']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 1:  # Segundo dia: Costas, Antebraço,
                    for grupo_muscular in ['costas']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 2:  # Terceiro dia: Quadríceps, Posterior de coxa, Glúteo
                    for grupo_muscular in ['quadríceps', 'posterior de coxa', 'glúteo']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 3:  # Quarto dia : Biceps e triceps
                    for grupo_muscular in ['bíceps']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 4:  # Quarto dia : Biceps e triceps
                    for grupo_muscular in ['tríceps']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 5:  # Quarto dia : Biceps e triceps
                    for grupo_muscular in ['ombro']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
                        if exercicios:
                            treino_dia.append({
                                'grupo_muscular': grupo_muscular.capitalize(),
                                'exercicios': exercicios
                            })
                elif i == 6:  # Quarto dia : Biceps e triceps
                    for grupo_muscular in ['ombro']:
                        exercicios = self.selecionar_exercicios(grupo_muscular, str(self.experiencia['numero']),
                                                                grupos_selecionados, max_exercicios=4)
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

    def salvar_treinos_excel(self):
        caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        arquivo_excel = os.path.join(caminho_downloads, 'treinos_usuario.xlsx')

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Treinos"

        # Escrever cabeçalhos
        sheet.append(['Dia de Treino', 'Grupo Muscular', 'Exercício', 'Séries', 'Repetições'])

        # Escrever dados dos treinos
        for treino_dia in self.treino_selecionado:
            for grupo in treino_dia['treino']:
                for exercicio in grupo['exercicios']:
                    sheet.append(
                        [treino_dia['dia'], grupo['grupo_muscular'], exercicio['exercicio'], exercicio['series'],
                         exercicio['repeticoes']])

        workbook.save(filename=arquivo_excel)
        print(f"Treinos salvos com sucesso em {arquivo_excel}")
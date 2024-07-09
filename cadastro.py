from semana import DiaDaSemana
from openpyxl import Workbook
import os
class Usuario:
    def __init__(self):
        self.objetivo = None
        self.dias_treino = []
        self.experiencia = None
        self.lesao_limitacao = None
        self.foco_corpo = None

    def perguntar_objetivo_musculacao(self):
        print("Qual é o seu principal objetivo com a musculação?")
        print("1. Ganho de massa muscular")
        print("2. Perda de gordura")
        print("3. Melhora da resistência física")
        print("4. Aumento da força")
        print("5. Manutenção da forma física")
        opcao = input("Escolha uma opção pelo número correspondente: ").strip().lower()
        while opcao not in ['1', '2', '3', '4', '5']:
            print("Opção inválida. Escolha uma opção válida.")
            opcao = input("Escolha uma opção pelo número correspondente: ").strip().lower()

        opcoes = {
            '1': "Ganho de massa muscular",
            '2': "Perda de gordura",
            '3': "Melhora da resistência física",
            '4': "Aumento da força",
            '5': "Manutenção da forma física"
        }
        self.objetivo = {"numero": opcao, "resposta": opcoes[opcao]}

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
            '1': "Iniciante (menos de 6 meses)",
            '2': "Intermediário (6 meses a 2 anos)",
            '3': "Avançado (mais de 2 anos)"
        }
        self.experiencia = {"numero": opcao, "resposta": opcoes[opcao]}

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

    def perguntar_foco_corpo(self):
        print("Qual área do corpo você gostaria de focar mais durante os treinos?")
        print("1. Pernas e glúteos")
        print("2. Peito e ombros")
        print("3. Costas e bíceps")
        print("4. Abdômen e core")
        print("5. Corpo inteiro")
        opcao = input("Escolha uma opção pelo número correspondente: ").strip().lower()
        while opcao not in ['1', '2', '3', '4', '5']:
            print("Opção inválida. Escolha uma opção válida.")
            opcao = input("Escolha uma opção pelo número correspondente: ").strip().lower()

        opcoes = {
            '1': "Pernas e glúteos",
            '2': "Peito e ombros",
            '3': "Costas e bíceps",
            '4': "Abdômen e core",
            '5': "Corpo inteiro"
        }
        self.foco_corpo = {"numero": opcao, "resposta": opcoes[opcao]}

    def coletar_respostas(self):
        self.perguntar_objetivo_musculacao()
        self.perguntar_dias_treino()
        self.perguntar_experiencia_musculacao()
        self.perguntar_lesao_limitacao()
        self.perguntar_foco_corpo()

    def mapear_dias_para_enum(self):
        dia_mapeamento = {
            "segunda": DiaDaSemana.SEGUNDA,
            "terça": DiaDaSemana.TERCA,
            "terca": DiaDaSemana.TERCA,
            "quarta": DiaDaSemana.QUARTA,
            "quinta": DiaDaSemana.QUINTA,
            "sexta": DiaDaSemana.SEXTA,
            "sábado": DiaDaSemana.SABADO,
            "sabado": DiaDaSemana.SABADO,
            "domingo": DiaDaSemana.DOMINGO
        }

        dias_treino_array = []

        for dia in self.dias_treino:
            dia_enum = dia_mapeamento.get(dia)
            if dia_enum:
                dias_treino_array.append({"codigo": dia_enum.value, "dia": dia_enum.name})

        return dias_treino_array

    def imprimir_respostas(self):
        print("\nRespostas coletadas:")
        print(f"1. Objetivo: {self.objetivo['resposta']} (Escolha {self.objetivo['numero']})")
        print(f"2. Dias de Treino: {', '.join(self.dias_treino)}")
        print(f"3. Experiência: {self.experiencia['resposta']} (Escolha {self.experiencia['numero']})")
        print(f"4. Lesão ou Limitação: {self.lesao_limitacao['resposta']} (Escolha {self.lesao_limitacao['numero']})")
        print(f"5. Foco do Corpo: {self.foco_corpo['resposta']} (Escolha {self.foco_corpo['numero']})")

    def salvar_respostas_excel(self):
        caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        nome_arquivo = "respostas_musculacao.xlsx"
        caminho_arquivo = os.path.join(caminho_downloads, nome_arquivo)

        if os.path.exists(caminho_arquivo):
            opcao = input(f"O arquivo '{nome_arquivo}' já existe. Deseja sobrescrever (s), renomear (r) ou cancelar (c)? ").strip().lower()
            if opcao == 'r':
                novo_nome_arquivo = input("Digite o novo nome do arquivo (com extensão .xlsx): ").strip()
                caminho_arquivo = os.path.join(caminho_downloads, novo_nome_arquivo)
            elif opcao == 'c':
                print("Operação cancelada.")
                return

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Respostas"

        sheet.append(["Pergunta", "Resposta", "Escolha"])
        sheet.append(["Objetivo", self.objetivo['resposta'], self.objetivo['numero']])
        sheet.append(["Dias de Treino", ', '.join(self.dias_treino), ""])
        sheet.append(["Experiência", self.experiencia['resposta'], self.experiencia['numero']])
        sheet.append(["Lesão ou Limitação", self.lesao_limitacao['resposta'], self.lesao_limitacao['numero']])
        sheet.append(["Foco do Corpo", self.foco_corpo['resposta'], self.foco_corpo['numero']])

        workbook.save(caminho_arquivo)
        print(f"Respostas salvas no arquivo: {caminho_arquivo}")
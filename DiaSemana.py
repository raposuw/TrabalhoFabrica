from enum import Enum

class DiaDaSemana(Enum):
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5
    SABADO = 6
    DOMINGO = 7

def perguntar_objetivo_musculacao():
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
    return {"numero": opcao, "resposta": opcoes[opcao]}

def perguntar_dias_treino():
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
            return perguntar_dias_treino()
    return dias_treino

def perguntar_experiencia_musculacao():
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
    return {"numero": opcao, "resposta": opcoes[opcao]}

def perguntar_lesao_limitacao():
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
        return {"numero": opcao, "resposta": opcoes[opcao]}
    else:
        return {"numero": resposta, "resposta": "Não"}

def perguntar_foco_corpo():
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
    return {"numero": opcao, "resposta": opcoes[opcao]}

def coletar_respostas():
    respostas = {}
    respostas['objetivo'] = perguntar_objetivo_musculacao()
    respostas['dias_treino'] = perguntar_dias_treino()
    respostas['experiencia'] = perguntar_experiencia_musculacao()
    respostas['lesao_limitacao'] = perguntar_lesao_limitacao()
    respostas['foco_corpo'] = perguntar_foco_corpo()
    return respostas

# Função para mapear os dias de treino para seus códigos
def mapear_dias_para_enum(dias_treino):
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

    for dia in dias_treino:
        dia_enum = dia_mapeamento.get(dia)
        if dia_enum:
            dias_treino_array.append({"codigo": dia_enum.value, "dia": dia_enum.name})

    return dias_treino_array

# Lista para armazenar todos os arrays de dias de treino inseridos
todos_dias_treino = []

# Coletar respostas do usuário
respostas = coletar_respostas()

# Mapear dias de treino para enums e adicionar à lista
dias_treino_array = mapear_dias_para_enum(respostas['dias_treino'])
todos_dias_treino.extend(dias_treino_array)

# Imprimir todas as respostas coletadas
print("\nRespostas coletadas:")
print(f"1. Objetivo: {respostas['objetivo']['resposta']} (Escolha {respostas['objetivo']['numero']})")
print(f"2. Dias de Treino: {', '.join(respostas['dias_treino'])}")
print(f"3. Experiência: {respostas['experiencia']['resposta']} (Escolha {respostas['experiencia']['numero']})")
print(f"4. Lesão ou Limitação: {respostas['lesao_limitacao']['resposta']} (Escolha {respostas['lesao_limitacao']['numero']})")
print(f"5. Foco do Corpo: {respostas['foco_corpo']['resposta']} (Escolha {respostas['foco_corpo']['numero']})")

# Imprimir todos os dias de treino inseridos
print("\nDias de treino inseridos:")
for dia in todos_dias_treino:
    print(f"Dia: {dia['dia']}, Código: {dia['codigo']}")

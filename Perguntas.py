from itertools import product

class Questionario:
    def __init__(self):
        self.perguntas = []
        self.respostas = {}

    def adicionar_pergunta(self, pergunta):
        if len(self.perguntas) < 10:
            self.perguntas.append(pergunta)
            print("Pergunta adicionada com sucesso!")
        else:
            print("Você já adicionou o número máximo de perguntas (10).")

    def exibir_pergunta(self, indice):
        if indice < len(self.perguntas):
            print(f"Pergunta {indice + 1}: {self.perguntas[indice]}")
            print("Opções de resposta:")
            print("1 - Resposta 1")
            print("2 - Resposta 2")
            print("3 - Resposta 3")
        else:
            print("Não há mais perguntas para exibir.")

    def armazenar_resposta(self, indice, resposta):
        if indice < len(self.perguntas):
            if resposta in ['1', '2', '3']:
                self.respostas[self.perguntas[indice]] = resposta
                print("Resposta armazenada com sucesso!")
            else:
                print("Por favor, escolha uma resposta válida (1, 2 ou 3).")
        else:
            print("Não é possível armazenar a resposta para esta pergunta.")


# Criando uma instância da classe Questionario
questionario = Questionario()

# Adicionando perguntas
questionario.adicionar_pergunta("Qual é a sua cor favorita?")
questionario.adicionar_pergunta("Qual é o seu animal favorito?")
questionario.adicionar_pergunta("Qual é a sua comida favorita?")

# Exibindo as perguntas e armazenando respostas
for i in range(len(questionario.perguntas)):
    questionario.exibir_pergunta(i)
    resposta = input("Digite o número correspondente à sua resposta (1, 2 ou 3): ")
    questionario.armazenar_resposta(i, resposta)

# Exibindo as perguntas e respostas armazenadas
print("\nPerguntas e respostas armazenadas:")
for pergunta, resposta in questionario.respostas.items():
    print(f"{pergunta}:")
    if resposta == '1':
        print("1 - Resposta 1")
    elif resposta == '2':
        print("2 - Resposta 2")
    elif resposta == '3':
        print("3 - Resposta 3")


class RespostasEspecificas:
    def __init__(self, respostas):
        self.respostas = respostas

    def obter_resposta_especifica(self):
        # Todas as possibilidades de ordem das respostas com mensagens correspondentes
        possibilidades_ordem = {
            ('1', '2', '3'): "Mensagem para a ordem 1-2-3",
            ('1', '3', '2'): "Mensagem para a ordem 1-3-2",
            ('2', '1', '3'): "Mensagem para a ordem 2-1-3",
            ('2', '3', '1'): "Mensagem para a ordem 2-3-1",
            ('3', '1', '2'): "Mensagem para a ordem 3-1-2",
            ('3', '2', '1'): "Mensagem para a ordem 3-2-1",
            ('')
        }

        # Verifica a ordem das respostas e retorna a mensagem correspondente
        for ordem, mensagem in possibilidades_ordem.items():
            if self.respostas == ordem:
                return mensagem

        return "Mensagem para outras ordens de resposta"

# Obtendo as respostas do questionário
respostas_questionario = list(questionario.respostas.values())

# Criando uma instância da classe RespostasEspecificas com as respostas do questionário
respostas_especificas = RespostasEspecificas(respostas_questionario)

# Obtendo e exibindo a mensagem específica com base nas respostas do questionário
mensagem_especifica = respostas_especificas.obter_resposta_especifica()
print("Mensagem específica com base nas respostas do questionário:", mensagem_especifica)


class semana(enum):
    
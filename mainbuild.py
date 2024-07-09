from cadastro import Usuario

# Uso do código:
usuario = Usuario()
usuario.coletar_respostas()
treinos = usuario.carregar_treinos_excel()
usuario.montar_treino(treinos)
usuario.imprimir_treino()

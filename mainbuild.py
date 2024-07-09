from cadastro import Usuario
from interface import InterfaceTreino


usuario = Usuario()
interface = InterfaceTreino(usuario)
interface.exibir_interface()
usuario.salvar_treinos_excel()
from class_pessoas import Pessoas
from class_endereco import Endereco
from class_cliente import Cliente
from class_funcionario import Funcionario
from class_item_pedido import ItemPedido
from class_pedido import Pedido
from class_produto import Produto
from class_mesa import Mesa
from class_nota_fiscal import NotaFiscal

from datetime import datetime

def menu_principal():  # MENU PRINCIPAL
    print('''
        MENU Principal:
        [1] - Cliente
        [2] - Funcionário
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

def cadastrar_cliente():
        nome = input("Nome do cliente: ")
        telefone = input("Telefone do cliente: ")
        cpf = input("CPF do cliente: ")
        email = input("Email do cliente: ")
        senha = input("Senha do cliente: ")

        novo_cliente = Cliente(nome, telefone, cpf, email, senha)
        lista_de_clientes.append(novo_cliente)

def cadastrar_funcionario():
    id = input("Digite o ID do funcionário: ")
    nome = input("Digite o nome do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")
    email = input("Digite o email do funcionário: ")
    senha = input("Digite a senha do funcionário: ")

    novo_funcionario = Funcionario.cadastrar_funcionario(id, nome, cpf, email, senha)
    print(f"Funcionário {novo_funcionario._id} cadastrado com sucesso!")

def remover_funcionario(cls, id):
        for funcionario in cls.funcionarios:
            if funcionario._id == id:
                cls.funcionarios.remove(funcionario)
                print(f"Funcionário {id} removido com sucesso!")
                break
        else:
            print(f"Funcionário {id} não encontrado.")

def cadastrar_produto(cls, codigo_produto, descricao, preco, validade):
        novo_produto = cls(codigo_produto, descricao, preco, validade)
        return novo_produto

def remover_produto(cls, codigo_produto):
        for produto in cls.produtos:
            if produto._codigo_produto == codigo_produto:
                cls.produtos.remove(produto)
                print(f"Produto {codigo_produto} removido com sucesso!")
                break
        else:
            print(f"Produto {codigo_produto} não encontrado.")

 def pesquisar_produto():
    codigo_produto = input("Digite o código do produto que deseja pesquisar: ")
    Produto.pesquisar_produto(codigo_produto)

# Função para cadastrar um pedido
def cadastrar_pedido():
    codigo_pedido = input("Digite o código do pedido: ")
    endereco_entrega = input("Digite o endereço de entrega: ")

    novo_pedido = Pedido(codigo_pedido, endereco_entrega)
    print(f"Pedido {novo_pedido._codigo_pedido} cadastrado com sucesso!")

# Função para editar um pedido
def editar_pedido():
    codigo_pedido = input("Digite o código do pedido que deseja editar: ")
    endereco_entrega = input("Digite o novo endereço de entrega: ")

    for pedido in Pedido.pedidos:
        if pedido._codigo_pedido == codigo_pedido:
            pedido.editar_pedido(endereco_entrega)
            break
    else:
        print(f"Pedido {codigo_pedido} não encontrado.")

# Função para concluir um pedido
def concluir_pedido():
    codigo_pedido = input("Digite o código do pedido que deseja concluir: ")

    for pedido in Pedido.pedidos:
        if pedido._codigo_pedido == codigo_pedido:
            pedido.concluir_pedido()
            break
    else:
        print(f"Pedido {codigo_pedido} não encontrado.")

# Função para excluir um pedido
def excluir_pedido():
    codigo_pedido = input("Digite o código do pedido que deseja excluir: ")

    for pedido in Pedido.pedidos:
        if pedido._codigo_pedido == codigo_pedido:
            pedido.excluir_pedido()
            break
    else:
        print(f"Pedido {codigo_pedido} não encontrado.")

def selecionar_endereco_entrega(self, enderecos):
        if not enderecos:
            print("Nenhum endereço cadastrado. Por favor, cadastre um novo endereço.")
            self.cadastrar_endereco()
        else:
            print("Endereços cadastrados:")
            for i, endereco in enumerate(enderecos):
                print(f"{i + 1}. CEP: {endereco._cep}, Rua: {endereco._rua}, Bairro: {endereco._bairro}, Cidade: {endereco._cidade}")

            escolha = input("Digite o número do endereço desejado ou 'N' para cadastrar um novo endereço: ")

            if escolha.lower() == 'n':
                self.cadastrar_endereco()
            else:
                try:
                    escolha_numero = int(escolha)
                    if 1 <= escolha_numero <= len(enderecos):
                        self.__endereco_entrega = enderecos[escolha_numero - 1]
                        print("Endereço selecionado com sucesso.")
                    else:
                        print("Opção inválida. Tente novamente.")
                except ValueError:
                    print("Opção inválida. Tente novamente.")

    def cadastrar_endereco(self):
        cep = input("Digite o CEP do novo endereço: ")
        rua = input("Digite a rua do novo endereço: ")
        numero = input("Digite o número do novo endereço: ")
        complemento = input("Digite o complemento do novo endereço: ")
        bairro = input("Digite o bairro do novo endereço: ")
        cidade = input("Digite a cidade do novo endereço: ")

        novo_endereco = Endereco(cep, rua, numero, complemento, bairro, cidade)
        self.__endereco_entrega = novo_endereco
        print("Novo endereço cadastrado e selecionado com sucesso.")

# Função para cadastrar uma nova mesa
def cadastrar_mesa():
    numero_da_mesa = input("Digite o número da mesa: ")

    # Verificar se a mesa com o número informado já existe
    for mesa in mesas:
        if mesa._numero_da_mesa == numero_da_mesa:
            print("Mesa já cadastrada.")
            return

    nova_mesa = Mesa(numero_da_mesa)
    mesas.append(nova_mesa)
    print(f"Mesa {nova_mesa._numero_da_mesa} cadastrada com sucesso!")

    
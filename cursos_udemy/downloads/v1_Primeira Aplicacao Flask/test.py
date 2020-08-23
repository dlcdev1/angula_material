import datetime
class Funcionario():
    aumento = 1.04
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        print({'nome': self.nome, 'salario': self.salario })

    def aplicar_aumento(self):
        self.salario *= self.aumento

    @classmethod
    def definir_novo_aumento(cls, novo_aumento):
        cls.aumento = novo_aumento

    @staticmethod
    def dia_util(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            print(False)
        print(True)

class Admin(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def atualizar_dados(self, nome):
        self.nome = nome
        return self.dados()

def soma_simplificada(*args):
    print(sum(args))
soma_simplificada(3, 4, 5, 6, 7, 8)

def metodo_kwargs(*args, **kwargs):
    print(args[3])
    print(kwargs.get('idade'))

metodo_kwargs(2, 3, 4, "david", nome="paulo", idade=43, torcedor="cruzeiro")



# fabio = Funcionario('Fabio', 7000)
# # fabio.dados()
# Funcionario.definir_novo_aumento(1.19)
# fabio.aplicar_aumento()
# fabio.dados()
# minha_data = datetime.datetime(2020, 5, 10)
# Funcionario.dia_util(minha_data)
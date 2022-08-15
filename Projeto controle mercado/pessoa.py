class Pessoa:
    def __init__(self, nome : str, idade: int, salario : float):
        self.nome = nome
        self.idade = idade
        self.salario = salario
    
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_salario(self):
        return self.salario
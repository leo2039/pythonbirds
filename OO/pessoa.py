

class Pessoa:
    def __init__(self, nome = None, idade=36):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'ola mundo'


if __name__ == '__main__':

    p = Pessoa('Leonardo')
    p.idade = 10
    print(p.nome)
    print(p.idade)
    p.nome = 'Patricia'

    print(p.nome)

    print(Pessoa.cumprimentar(p))
    print()
    print(p.cumprimentar())





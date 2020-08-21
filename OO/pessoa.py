

class Pessoa:
    def __init__(self,*filhos, nome = None, idade=36):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'ola mundo'


if __name__ == '__main__':

    leonardo = Pessoa(nome = 'Leonardo')
    vera = Pessoa(leonardo, nome = 'Vera')

    for filho in vera.filhos:
        print(filho.nome)
    print(vera.filhos)

    p = Pessoa



class Pessoa:
    # Método construtor
    def __init__(self, nome='George', sobrenome='Vieira', idade=26):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Jaide')
    print(p.nome)
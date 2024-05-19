class Pessoa():
    def __init__(self, nome, peso, idade):
        self.nome= nome
        self.peso= peso
        self.idade= idade
        self.acao_atual= None

    def comer (self):
        if self.acao_atual== None:
            self.acao_atual='comendo'
            print(f'{self.nome} está  comendo.')
        else:
            print(f'{self.nome} já está {self.acao_atual} não pode comer agora.')

    def parar_de_comer(self):
        if self.acao_atual=='comendo' :
            self.acao_atual= None
            print(f'{self.nome} parou de comer.')
        else:
            print(f'{self.nome} não está comendo agora.')

    def falando(self):
        if self.acao_atual== None:
            self.acao_atual='falando'
            print(f'{self.nome} está falando.')
        else:
            print(f'{self.nome} já está {self.acao_atual} não pode falar agora.')


    def parar_de_falar(self):
        if self.acao_atual == 'falando':
            self.acao_atual= None
            print(f'{self.nome} parou de falar')
        else:
            print(f'{self.nome}  não está falando agora.')

    def dormir (self):
        if self.acao_atual==None:
            self.acao_atual= 'dormindo'
            print(f'{self.nome} está dormindo.')
        else:
            print(f'{self.nome} já está {self.acao_atual} não pode dormir agora.')

    def parar_de_dormir(self):
        if self.acao_atual == 'dormindo':
            self.acao_atual= None
            print(f'{self.nome} parou de dormir')
        else:
            print(f'{self.nome}  não está dormindo agora.')




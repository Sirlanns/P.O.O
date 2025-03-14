#Atividade: Criando e interajindo com a classe cachorro
#-Requisitos da classe-
#--Nome:nome do cachorro.
#--Raça:raça do cachorro.
#--Comida:quantidade de comida disponivel.
#--Acordado(baolesma):indica se está acordado ou dormindo.
#--Feliz(baolesmo):indica se está feliz ou não.
#--Comer(quantidade):reduz a quantidade disponível e deixa o cachorro feliz.
#--Dormir():Altera o estado do cachorro para dormindo
#--Brincar():deixa o cachorro feliz
#--Latir():imprime uma mensagem indicando que o cachorro está latindo(se estiver acordado)

class Cachorro:
    def __init__(self, nome, raca, comida, energia, brincar, dormir):
        """Construtor da classe que inicializa os atributos do cachorro."""
        self.nome = nome  # Nome do cachorro
        self.raca = raca  # Raça do cachorro
        self.comida = comida  # Quantidade de comida disponível
        self.energia = energia
        self.brincar = brincar
        self.dormir = dormir
        self.acordado = True  # Indica se o cachorro está acordado
        self.feliz = False  # Indica se o cachorro está feliz

        def comer(self, quantidade):
            """Método para alimentar o cachorro."""
            if self.comida >= quantidade:
                self.comida -= quantidade  # Reduz a quantidade de comida disponível
                self.feliz = True  # O cachorro fica feliz após comer
                print(f"{self.nome} comeu {quantidade} porções de comida e está feliz!")
            else:
                print(f"{self.nome} não tem comida suficiente para comer!")

        def dormir(self):
            """Método para colocar o cachorro para dormir."""
            self.acordado = False  # Altera o estado para dormindo
            print(f"{self.nome} agora está dormindo.")

        def brincar(self):
            """Método para brincar com o cachorro."""
            if self.acordado and self.energia >= 20:
                self.feliz = True  # Cachorro fica feliz ao brincar
                print(f"{self.nome} brincou e está muito feliz!")
                self.energia - 20
            else:
                print(f"{self.nome} está dormindo/cansado e não pode brincar agora.")

        def latir(self):
            """Método para fazer o cachorro latir."""
            if self.acordado:
                print(f"{self.nome} está latindo! Au au!")
            else:
                print(f"{self.nome} está dormindo e não pode latir agora.")
        def energia(self):
            """atributo ligado as ações do cachorro"""
            self.energia = 100
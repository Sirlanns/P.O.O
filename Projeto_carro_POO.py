#Requisitos da classe:
#  Modelo: modelo do carro.
#  Ano: ano de fabricação.
#  Cor: cor do carro.
#  Combustível: quantidade de combustível disponível.
#  Ligado (booleano): indica se o carro está ligado ou desligado.
#  Velocidade: velocidade atual do carro.
#Métodos obrigatórios:
#  ligar(): liga o carro (se já não estiver ligado).
#  desligar(): desliga o carro e zera a velocidade.
#  acelerar(): aumenta a velocidade em 10 km/h e reduz 1 litro de combustível (se estiver ligado e houver combustível).
#  frear(): diminui a velocidade em 10 km/h (se o carro estiver ligado e em movimento).
#  abastecer(quantidade): adiciona a quantidade de combustível informada.
#  buzinar(): imprime uma mensagem indicando que o carro está buzinando.
#  status(): mostra as informações atuais do carro (modelo, ano, cor, se está ligado, velocidade e combustível).
class Carro:
    def __init__(self, modelo, ano, cor, combustivel):
        """Construtor da classe que inicializa os atributos do carro."""
        self.modelo = modelo  # Modelo do carro
        self.ano = ano  # Ano de fabricação
        self.cor = cor  # Cor do carro
        self.combustivel = combustivel  # Quantidade de combustível
        self.ligado = False  # Indica se o carro está ligado
        self.velocidade = 0  # Velocidade atual

    def ligar(self):
        """Liga o carro."""
        if not self.ligado:
            self.ligado = True
            print(f"{self.modelo} ligado.")
        else:
            print(f"{self.modelo} já está ligado.")

    def desligar(self):
        """Desliga o carro."""
        if self.ligado:
            self.ligado = False
            self.velocidade = 0  # Velocidade volta para zero ao desligar
            print(f"{self.modelo} desligado.")
        else:
            print(f"{self.modelo} já está desligado.")

    def acelerar(self):
        """Acelera o carro aumentando a velocidade."""
        if self.ligado:
            if self.combustivel > 0:
                self.velocidade += 10
                self.combustivel -= 1
                print(f"{self.modelo} acelerou. Velocidade: {self.velocidade} km/h. Combustível: {self.combustivel}L.")
            else:
                print("Sem combustível para acelerar.")
        else:
            print("O carro está desligado!")

    def frear(self):
        """Diminui a velocidade do carro."""
        if self.ligado and self.velocidade > 0:
            self.velocidade -= 10
            print(f"{self.modelo} freou. Velocidade atual: {self.velocidade} km/h.")
        else:
            print("O carro já está parado ou desligado.")

    def abastecer(self, quantidade):
        """Abastece o carro com a quantidade fornecida de combustível."""
        self.combustivel += quantidade
        print(f"{self.modelo} abastecido com {quantidade}L. Combustível atual: {self.combustivel}L.")

    def buzinar(self):
        """O carro buzina."""
        print("BEEEEEP!")

    def status(self):
        """Exibe o status atual do carro."""
        ligado_str = "ligado" if self.ligado else "desligado"
        print(f"Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, Estado: {ligado_str}, Velocidade: {self.velocidade} km/h, Combustível: {self.combustivel}L")

# Testes
meu_carro = Carro("Fusca", 1975, "Azul", 10)
meu_carro.status()
meu_carro.ligar()
meu_carro.acelerar()
meu_carro.frear()
meu_carro.buzinar()
meu_carro.abastecer(5)
meu_carro.status()
meu_carro.desligar()
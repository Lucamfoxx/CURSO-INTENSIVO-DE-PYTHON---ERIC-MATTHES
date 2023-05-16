class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    

    def get_descriptive_name(self):
        long_name = f"{str(self.year)}, {self.make}, {self.model}"
        return long_name.title()
    
    
    def read_odometer(self):
        print(f'O carro tem {self.odometer_reading} kilometros')
    
    
    def update_odometer(self, kilometros):
        if kilometros >= self.odometer_reading:
            self.odometer_reading = kilometros
        else:
            print('Voce não pode voltar o odemtro  ')

    
    def incrementa_odometro(self, km):
        self.odometer_reading += km


class Bateria():
    def __init__(self, bateria_tamanho=70):
        self.bateria_tamanho = bateria_tamanho

    def descriçao_bateria(self):
        print(f'Essa bateria tem {self.bateria_tamanho} de capacidade.')

    
    def get_range(self):
        if self.bateria_tamanho == 70:
            range = 240
        elif self.bateria_tamanho == 85:
            range = 270
        mensagem = f'O carro tem aproximadamente {range}km na sua capacidade total'
        print(mensagem)


class Carro_eletrico(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.bateria = Bateria()

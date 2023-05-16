from car import Car, Carro_eletrico
print('-=' * 30)
meu_carro = Car('Ferrari', '250 gt', 1986)
print(meu_carro.get_descriptive_name())
print('-=' * 30)
meu_carro.odometer_reading = 23
meu_carro.read_odometer()
print('-=' * 30)

meu_carro2 = Carro_eletrico('tesla','model S','2016')
print('-=' * 30)
print(meu_carro2.get_descriptive_name())
meu_carro2.bateria.descriçao_bateria()
meu_carro2.bateria.get_range()
print('-=' * 30)
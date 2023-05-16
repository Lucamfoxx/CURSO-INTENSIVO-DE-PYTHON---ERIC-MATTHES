from car import Carro_eletrico

meu_carro = Carro_eletrico('tesla','model S','2016')

print(meu_carro.get_descriptive_name())
meu_carro.bateria.descriçao_bateria()
meu_carro.bateria.get_range()
#Joao Gustavo Mota Ramos, Murilo Henrique de Souza Silva, Yago Roberto Gomes Morais
try:
    celsius = float(input("Digite a temperatura em Celsius: "))

    
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15


    print(f"\nTemperatura em Celsius: {celsius:.2f} °C")
    print(f"Convertida para Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Convertida para Kelvin: {kelvin:.2f} K")
except ValueError:
    print("Por favor, insira um valor numérico válido.")
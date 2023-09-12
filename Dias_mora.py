import funcimora

path = "Base_Datos/Dias_mora_2023.csv"
Mora = {}

# CAPTURA DE FECHAS POR EMPRESA
companies = funcimora.read_csv(path)

for key, value in companies.items():
    funcimora.dates(value)
    # days = funcimora.dates(value)
    # Mora[key] = days
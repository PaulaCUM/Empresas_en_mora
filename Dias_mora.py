import funcimora

# path = "Base_Datos/Dias_mora_2023.csv"
# path2 = "Base_Datos/Dias de mora por empresa.csv"

path,path2,fechaInicial,fechaFinal,Mora = funcimora.init_data()

# CAPTURA DE FECHAS POR EMPRESA
companies = funcimora.read_csv(path,fechaInicial,fechaFinal)

for key, value in companies.items():
    # funcimora.dates(value)
    days = funcimora.dates(value)
    Mora[key] = days
# Generar CSV de salida con los datos calculados
funcimora.write_csv(Mora,path2)

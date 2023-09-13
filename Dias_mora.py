import funcimora
#!/usr/bin/env python

path,path2,fechaInicial,fechaFinal,Mora = funcimora.init_data()

# CAPTURA DE FECHAS POR EMPRESA
companies = funcimora.read_csv(path,fechaInicial,fechaFinal)

for key, value in companies.items():
    # funcimora.dates(value)
    days = funcimora.dates(value)
    Mora[key] = days
# Generar CSV de salida con los datos calculados
funcimora.write_csv(Mora,path2)

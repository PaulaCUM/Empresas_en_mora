import csv
from datetime import datetime

# IMPORTAR CSV
def read_csv(path):
    with open(path,'r') as csvfile:
        data = csv.reader(csvfile, delimiter=';')
        companies = {}
        values = []
        key = ""
        DateFormat = '%d/%m/%y'
        next(data)

        for row in data:
            if row[0] != '':
                if key != row[0]:
                    # Obtener nombres de las empresas
                    key = row[0]      
                    values = []                                   
                # Obtener valores de cada empresa
                values.append([datetime.strptime(row[2], DateFormat), datetime.strptime(row[3], DateFormat)])
                # Crear diccionario con las empresas y sus valores
                companies[key] = values
    print('Se cargaron correctamente las siguientes empresas:')
    i = 0
    for key, value in companies.items():
        i += 1
        message =  "{}. {}: con {} fechas por analizar".format(i, key, len(value))
        print(message)
    return companies

# ANALIZAR RANGOS DE FECHAS DE INICIO Y FINAL POR EMPRESA
def dates(companyDates):
    Tfmax = companyDates[0][0]
    C = 0
    for date in companyDates:
        if Tfmax >= date[0]:
            if Tfmax < date[1]:
                C = 0
                NumM = date[1].month - Tfmax.month
                Ti = Tfmax
                Tf = date[1]
        elif Tfmax < date[1]:
            C = 1
            NumM = date[1].month - date[0].month
            Ti = date[0]
            Tf = date[1]
        # Ejecutar funcion que cuenta la cantidad de dias dentro del rango
        days = count_days(NumM, Ti, Tf)
        Tfmax = Tf
    return days

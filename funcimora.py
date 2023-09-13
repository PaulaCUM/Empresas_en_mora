import csv
from datetime import datetime, timedelta
from calendar import monthrange
import calendar

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
    Tfmax = companyDates[0][0] - timedelta(days=1)
    C = 0
    days = [0] * 12
    for date in companyDates:
        if Tfmax >= date[0]:
            if Tfmax < date[1]:
                C = 0
                NumM = date[1].month - Tfmax.month
                Ti = Tfmax
                Tf = date[1]
            else:
                continue
        elif Tfmax < date[1]:
            C = 1
            NumM = date[1].month - date[0].month
            Ti = date[0]
            Tf = date[1]
        else:
            print('Error en la data. Recuerde ordenar las fechas de menor a mayor para la fecha de inicio')
            continue
        # Ejecutar funcion que cuenta la cantidad de dias dentro del rango
        days = count_days(NumM, Ti, Tf, C, days)
        if Tf > Tfmax:
            Tfmax = Tf
    return days

# CALCULAR LA CANTIDAD DE DIAS DENTRO DE UN RANGO DEFINIDO DE FECHAS
def count_days(NumM,Ti,Tf,C,days):
    Di = Ti.day
    Mi = Ti.month
    Yi = Ti.year
    Df = Tf.day
    Mf = Tf.month
    Yf = Tf.year

    # Cambio de mes
    if NumM >= 1:
        for it in range(NumM):
            days[Mi + it - 1] = monthrange(Yi, (Mi + it))[1] - Di + C + days[Mi + it - 1]
            Di = 0
            C = 0
        days[Mf - 1] = Df + days[Mf - 1]
    # En el mismo mes
    else:
        days[Mf - 1] = Df - Di + C + days[Mf - 1]
    return days

# CREAR ARCHIVO CSV DE SALIDA PARA MOSTRAR LOS RESULTADOS
def write_csv(Mora,path):   
    # Encabezado tabla 
    header = {
        'Company': list(calendar.month_name[month+1] for month in range(12))
    }

    # Nombre archivo resultante
    csvFile = path

    # Escribir en el archivo CSV
    with open(csvFile, 'w', newline='') as file:
        writer = csv.writer(file)
        
        FirstHeader, valores = dicc_to_list(header)

        fieldnames = FirstHeader + valores
        writer.writerow(fieldnames)

        # Escribir los datos
        for key, values in Mora.items(): 
            row = [key] + values     
            writer.writerow(row)   

# Convertir valor del diccionario en listas para el CSV
def dicc_to_list(dicc):
    Col1 = list(dicc.keys())
    FirstCol = [Col1[0]]
    values = list(dicc.values())
    valores = values[0]
    return FirstCol, valores
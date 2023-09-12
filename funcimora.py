import csv

# IMPORTAR CSV
def read_csv(path):
    with open(path,'r') as csvfile:
        data = csv.reader(csvfile, delimiter=';')
        companies = {}
        values = []
        key = ""
        next(data)

        for row in data:
            if row[0] != '':
                if key != row[0]:
                    # Obtener nombres de las empresas
                    key = row[0]      
                    values = []          
                    values.append([row[2], row[3]])           
                else:
                    # Obtener valores de cada empresa
                    values.append([row[2], row[3]])
                # Crear diccionario con las empresas y sus valores
                companies[key] = values
    print('Se cargaron correctamente las siguientes empresas:')
    i = 0
    for key, value in companies.items():
        i += 1
        message =  "{}. {}: con {} fechas por analizar".format(i, key, len(value))
        print(message)


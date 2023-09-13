import funcimora

# path = "Base_Datos/Dias_mora_2023.csv"
# path2 = "Base_Datos/Dias de mora por empresa.csv"
def init_data():
    print('///---' * 15)
    path = str(input("Ingrese la direccion del archivo CSV a evaluar.\nRecuerde ingresar la direccion completa, incluyendo el nombre del archivo con su extension.\nPor ejemplo: Base_Datos/Dias_mora_2023.csv\nIngrese la direccion del archivo = "))
    print('///---' * 15)
    path2 = str(input("Ingrese la direccion donde desea generar el CSV de salida y el nombre del archivo con extension .csv\nPor ejemplo: Base_Datos/Dias de mora por empresa.csv\nIngrese la direccion del archivo = "))
    print('///---' * 15)
    fechaInicial = int(input("Ingrese el número de columna correspondiente a la fecha INICIAL de la mora.\nRecuerde iniciar el conteo de columnas en 0 de izquierda a derecha.\nEvite ingresar un numero negativo o un texto: "))
    print('///---' * 15)
    fechaFinal = int(input("Ingrese el número de columna correspondiente a la fecha FINAL de la mora.\nRecuerde iniciar el conteo de columnas en 0 de izquierda a derecha.\nEvite ingresar un numero negativo o un texto: "))
    print('///---' * 15)
    Mora = {}

    return path,path2,fechaInicial,fechaFinal,Mora

path,path2,fechaInicial,fechaFinal,Mora = init_data()

# CAPTURA DE FECHAS POR EMPRESA
companies = funcimora.read_csv(path,fechaInicial,fechaFinal)

for key, value in companies.items():
    # funcimora.dates(value)
    days = funcimora.dates(value)
    Mora[key] = days
# Generar CSV de salida con los datos calculados
funcimora.write_csv(Mora,path2)

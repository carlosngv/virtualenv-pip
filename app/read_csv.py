import csv

"""
  Por cada fila leída del CSV la uniremos con el encabezado utilizando
  la función "zip".

  Está función une los elementos en orden y en tuplas. Es decir, une los primeros elementos
  en ambas tuplas, los segundos y así sucesivamente.

  Esto nos facilita posteriormente a almacenar la fila y encabezado actual en un diccionario.

  El resultado es una lista de diccionarios, cada diccionario tiene la información de un país.



"""

def read_csv(path):
  with open(path, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      # Unimos la fila header con la fila actual de contenido
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data


if __name__ == '__main__':
  data = read_csv('./data.csv')
  print(data[0])

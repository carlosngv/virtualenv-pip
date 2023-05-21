import utils
import charts
import read_csv

def run():
  # La data es una lista de diccionarios.
  # Cada diccionario tiene la información de su respectivo país
  data = read_csv.read_csv('./data.csv')
  country = input('Type country: ')

  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]

    keys, values = utils.get_population(country)
    charts.generate_bar_chart(keys, values)



if __name__ == '__main__':
  run()

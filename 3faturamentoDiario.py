import json

with open('dados.json', 'r+') as data_json:
  data = data_json.read()

def mediaFaturamento(data):
  media = 0
  n_valores = 0
  for dia in data:
    if dia['valor'] != 0.0:
      media += dia['valor']
      n_valores += 1
  
  return media/n_valores

def minimo(data):
  value_min = 9999999
  dia = 0
  if data:
    for i in range(len(data)):
      if data[i]['valor'] < value_min and data[i]['valor'] != 0.0:
        dia = i
        value_min = data[i]['valor']
    return value_min, dia
  else:
    return -1

def maximo(data):
  value_max = 0.0
  dia = 0
  if data:
    for i in range(len(data)):
      if data[i]['valor'] > value_max:
        dia = i
        value_max = data[i]['valor']
    return value_max, dia
  else:
    return -1
  
dic_json = json.loads(data)
media = mediaFaturamento(dic_json)

good_days = 0
for i in dic_json:
  if i['valor'] > media:
    good_days += 1

valor_minimo, dia_min = minimo(dic_json)
valor_maximo, dia_max = maximo(dic_json)

print("%.4f do dia %d do mês" % (valor_minimo, dic_json[dia_min]['dia']))
print("%.4f do dia %d do mês" % (valor_maximo, dic_json[dia_max]['dia']))
print(good_days, "dias de faturamento maior que a média")
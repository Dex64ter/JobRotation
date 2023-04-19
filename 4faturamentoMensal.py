faturamento_Estados = {
  "SP": 67836.43,
  "RJ": 36678.66,
  "MG": 29229.88,
  "ES": 27165.48,
  "Outros": 19849.53
}

def porcentFat(dictionary):
  valor_total = sum(dictionary.values())
  for k, v in dictionary.items():
    porcent = (v/valor_total)*100
    print(k, "-",round(porcent,2),"%")

porcentFat(faturamento_Estados)
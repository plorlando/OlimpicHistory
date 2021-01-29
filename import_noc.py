# procedimento para leitura do csv e importação da base noc_regions.csv.

import psycopg2
import csv
# conexão com o banco de dado POSTGREE
con = psycopg2.connect(host='ec2-54-172-17-119.compute-1.amazonaws.com', database='da4641m5jji053',
user='vslyjabiirjdzs', password='aaabea3a16ed663a10148ef2e31066286730a24716f7a09f789b66d34cb388ab', port=5432)
cursor = con.cursor()

with open('noc_regions.csv', 'rt') as file:
    csv_reader = csv.reader(file)

    next(csv_reader)  # ignora a linha com cabeçalhos das colunas

    contador = 1
    for line in csv_reader:
        # mapeamento dos campos em variáveis
        noc = line[0]
        region = line[1]
        notes = line[2]

        # insert no banco de dados
        try:
            cursor.execute(f"INSERT INTO olimpic_noc (noc, region, notes) VALUES ('{noc}', '{region}', '{notes}')")
            con.commit()
            print(str(contador) + ", " + noc +  ", " + region + ", " + notes + ", SUCESSO")
        except Exception as e:
            print(str(contador) + ", " + noc + ", " + region + ", " + notes + ", " + str(e))

        contador += 1
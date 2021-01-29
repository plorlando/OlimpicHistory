# procedimento para leitura do csv e importação da base athlete_events.csv.
# devido às verificações necessárias de ForeignKey, a importação ficou bem lenta, mas funcional

import psycopg2
import csv
# conexão com o banco de dado POSTGREE
con = psycopg2.connect(host='ec2-54-172-17-119.compute-1.amazonaws.com', database='da4641m5jji053',
user='vslyjabiirjdzs', password='aaabea3a16ed663a10148ef2e31066286730a24716f7a09f789b66d34cb388ab', port=5432)
cursor = con.cursor()


with open('athlete_events.csv', 'rt') as file:
    csv_reader = csv.reader(file)

    next(csv_reader)  # ignora a linha com cabeçalhos das colunas


    # cursor.execute("DELETE FROM olimpic_athlete_events")
    # con.commit()

    contador = 1
    for line in csv_reader:
        # mapeamento dos campos em variáveis, e tratamento dos dados
        id = line[0]
        name = line[1].replace("'", "")
        sex = line[2]
        age = str(line[3]).replace('NA', '0')
        height = str(line[4]).replace('NA', '0')
        weight = line[5].replace('NA', '0')
        team = line[6].replace("'", "")
        n = line[7]
        noc = cursor.execute(f"SELECT noc from olimpic_noc where noc = '{n}'")
        find_noc = cursor.fetchone()

        # precisa verificar se achou o valor de noc no banco
        if find_noc:
            noc = find_noc[0]
        else:
           noc = 'NNA'

        games = line[8]
        year = line[9]
        season = line[10].replace("'", "")
        city = line[11].replace("'", "")
        sport = line[12].replace("'", "")
        event = line[13].replace("'", "")
        medal = line[14]

        # insert no banco de dados
        try:
            cursor.execute(f"INSERT INTO olimpic_athlete_events (id_athlete, name, sex, age, height, weight, team, games, year, season, "
                            f"city, sport, event, medal, noc_id) VALUES ({id}, '{name}', '{sex}', {age}, {height}, {weight}, "
                             f"'{team}', '{games}', {year}, '{season}', '{city}', '{sport}', '{event}', '{medal}', '{noc}')")
            con.commit()
            print(str(contador) + ", " + id + ", " + name + ", " + noc + ", SUCESSO")

        except Exception as e:
            print(str(contador) + ", " + id + ", " + name + ", " + noc + ", " + str(e))

        contador += 1
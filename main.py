import psycopg2

username = 'postgres'
password = 'A_m0N66'
database = 'beer_DB'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT TRIM(beer_name), info_abv
FROM beers, info
WHERE beers.info_id = info.info_id
AND info_abv IS NOT NULL
ORDER BY info_abv DESC
'''
query_2 = '''
SELECT TRIM(place_country), COUNT(*)
FROM beers, place
WHERE beers.place_id = place.place_id
GROUP BY place_country
'''
query_3 = '''
SELECT TRIM(place_country), SUM(info_abv) / COUNT(*)
FROM place, info, beers
WHERE beers.info_id = info.info_id 
AND beers.place_id = place.place_id
AND info_abv IS NOT NULL
GROUP BY place_country
'''

def max_len_x(x):
    max_len = 0
    for i in range(len(x)):
        if len(x[i]) > max_len:
            max_len = len(x[i])
    return max_len

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur1 = conn.cursor()
    cur1.execute(query_1)
    b_name = []
    i_abv = []

    for row in cur1:
        b_name.append(row[0])
        i_abv.append(row[1])

    max_len_name = max_len_x(b_name)   # максимальна довжина імені (потрібно для красивого вивода)
    print('Статистика за міцністю пива')
    for i in range(len(b_name)):
        print(b_name[i], ' ' * (max_len_name - len(b_name[i])), '| ', i_abv[i])
    print('\n')


    cur2 = conn.cursor()
    cur2.execute(query_2)
    p_country = []
    count = []

    for row in cur2:
        p_country.append(row[0])
        count.append(row[1])

    max_len_country = max_len_x(p_country)
    print('Кількість різних пив у кожній країні')
    for i in range(len(p_country)):
        print(p_country[i], ' ' * (max_len_country - len(p_country[i])), '| ', count[i])
    print('\n')


    cur3 = conn.cursor()
    cur3.execute(query_3)
    p_country = []
    average = []

    for row in cur3:
        p_country.append(row[0])
        average.append(row[1])

    max_len_country = max_len_x(p_country)
    print('Cередня міцність пива в кожній країні')
    for i in range(len(p_country)):
        print(p_country[i], ' ' * (max_len_country - len(p_country[i])), '| ', average[i])

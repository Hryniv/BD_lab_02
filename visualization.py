import psycopg2
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with conn:
    cur = conn.cursor()

    cur.execute(query_1)
    b_name = []
    i_abv = []

    for row in cur:
        b_name.append(row[0])
        i_abv.append(row[1])

    fig, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    bar_ax.set_title('Статистика за міцністю пива')
    bar = bar_ax.bar(b_name, i_abv)
    bar_ax.set_xticks(range(len(b_name)))
    bar_ax.set_xticklabels(b_name, rotation=0)
    bar_ax.yaxis.set_major_locator(ticker.MultipleLocator(1))


    cur.execute(query_2)
    p_country = []
    count = []

    for row in cur:
        p_country.append(row[0])
        count.append(row[1])

    pie_ax.pie(count, labels=p_country, autopct='%1.1f%%')
    pie_ax.set_title('Кількість різних пив у кожній країні')

    cur.execute(query_3)
    p_country = []
    average = []

    for row in cur:
        p_country.append(row[0])
        average.append(row[1])

    graph_ax.plot(p_country, average, marker='o')
    graph_ax.set_title('Середня міцність пива в кожній країні')
    graph_ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

plt.show()

-- Cтатистика за міцністю пива (info_abv)
SELECT beer_name, info_abv
FROM beers, info
WHERE beers.info_id = info.info_id
AND info_abv IS NOT NULL
ORDER BY info_abv DESC

-- Кількість різних пив у кожній країні
SELECT place_country, COUNT(*)
FROM beers, place
WHERE beers.place_id = place.place_id
GROUP BY place_country

-- Cередня міцність пива в кожній країні
SELECT place_country, SUM(info_abv) / COUNT(*)
FROM place, info, beers
WHERE beers.info_id = info.info_id 
AND beers.place_id = place.place_id
AND info_abv IS NOT NULL
GROUP BY place_country


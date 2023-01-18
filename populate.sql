-- ------------------------
-- Populate Place table
-- ------------------------
INSERT INTO Place(place_id, place_country, place_state)
VALUES(0, 'US', 'TX');
INSERT INTO Place(place_id, place_country, place_state)
VALUES(1, 'US', 'LA');
INSERT INTO Place(place_id, place_country, place_state)
VALUES(2, 'BE', NULL);
INSERT INTO Place(place_id, place_country, place_state)
VALUES(3, 'GB', 'GB2');
INSERT INTO Place(place_id, place_country, place_state)
VALUES(4, 'CA', 'ON');


-- ------------------------
-- Populate Info table
-- ------------------------
INSERT INTO Info(info_id, info_style, info_availability, info_abv, info_notes)
VALUES(0, 'American IPA', 'Year-round', NULL, 'No notes at this time.');
INSERT INTO Info(info_id, info_style, info_availability, info_abv, info_notes)
VALUES(1, 'Vienna Lager', 'Year-round', 4.5, 'Amber is a Munich style lager brewed with crystal malt and Perle hops. It has a smooth, malty, sligh...');
INSERT INTO Info(info_id, info_style, info_availability, info_abv, info_notes)
VALUES(2, 'English Brown Ale', 'Summer', 5.4, 'No notes at this time.');
INSERT INTO Info(info_id, info_style, info_availability, info_abv, info_notes)
VALUES(3, 'Belgian Dubbel', 'Year-round', 7, NULL);
INSERT INTO Info(info_id, info_style, info_availability, info_abv, info_notes)
VALUES(4, 'Scottish Ale', 'Winter', NULL, 'No notes at this time.');


-- ------------------------
-- Populate Beers table
-- ------------------------
INSERT INTO Beers(beer_id, beer_name, place_id, info_id)
VALUES(0, 'Widmer Hefeweizen', 0, 0);
INSERT INTO Beers(beer_id, beer_name, place_id, info_id)
VALUES(1, 'Sommerbräu', 0, 1);
INSERT INTO Beers(beer_id, beer_name, place_id, info_id)
VALUES(2, 'Mackeson Triple XXX Stout', 1, 0);
INSERT INTO Beers(beer_id, beer_name, place_id, info_id)
VALUES(3, 'Old Izaak', 1, 2);
INSERT INTO Beers(beer_id, beer_name, place_id, info_id)
VALUES(4, 'Cactus Queen IPA', 1, 4);
INSERT INTO Beers(beer_id, beer_name, place_id, info_id)
VALUES(5, 'Amber', 2, 3);
INSERT INTO Beers(beer_id, beer_name, place_id, info_id)
VALUES(6, 'Turbodog', 3, 3);
INSERT INTO Beers(beer_id, beer_name, place_id, info_id)
VALUES(7, 'Purple Haze', 4, 4);
INSERT INTO Beers(beer_id, beer_name, place_id, info_id)
VALUES(8, 'Wheat', 4, 2);
INSERT INTO Beers(beer_id, beer_name, place_id, info_id)
VALUES(9, 'Golden', 4, 1);


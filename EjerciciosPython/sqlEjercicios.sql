--Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.

select * from city where population > 100000 and countrycode = 'USA'

--Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
select name from city where population > 120000 and countrycode = 'USA'



--Consulte una lista de nombres de CIUDADes de STATION para las ciudades que tienen un número de identificación par. Imprima los resultados en cualquier orden, pero excluya los duplicados de la respuesta.
--La tabla STATION se describe de la siguiente manera:

--mod saca "par"

select distinct city from station where mod(id,2)=0 order by id


--Find the difference between the total number of CITY entries in the table
-- and the number of distinct CITY entries in the table.

SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION


--Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

select distinct city from station where left(city,1) in('a','e','i','o','u')


--Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

--Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

select sum(city.population) from country join city on country.code = city.countrycode where country.continent = 'Asia'


--Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

--Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

select city.name from city join country on  CITY.CountryCode = COUNTRY.Code where continent = 'africa'


--Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.

--Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

select COUNTRY.Continent, floor(avg(CITY.Population)) from country join city on CITY.CountryCode = COUNTRY.Code group by country.continent; 

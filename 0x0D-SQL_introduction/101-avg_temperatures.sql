-- Import in hbtn_0c_0 database this table dump: download Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending) --
Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
mysql -u root -p hbtn_0c_0;
source temperatures.sql;
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
/*
(Hard) 262. Trips and Users
The Trips table holds all taxi trips. Each trip has a unique Id, while Client_Id and Driver_Id are both foreign keys to the Users_Id at the Users table. 
Status is an ENUM type of (‘completed’, ‘cancelled_by_driver’, ‘cancelled_by_client’).

+----+-----------+-----------+---------+--------------------+----------+
| Id | Client_Id | Driver_Id | City_Id |        Status      |Request_at|
+----+-----------+-----------+---------+--------------------+----------+
| 1  |     1     |    10     |    1    |     completed      |2013-10-01|
| 2  |     2     |    11     |    1    | cancelled_by_driver|2013-10-01|
| 3  |     3     |    12     |    6    |     completed      |2013-10-01|
| 4  |     4     |    13     |    6    | cancelled_by_client|2013-10-01|
| 5  |     1     |    10     |    1    |     completed      |2013-10-02|
| 6  |     2     |    11     |    6    |     completed      |2013-10-02|
| 7  |     3     |    12     |    6    |     completed      |2013-10-02|
| 8  |     2     |    12     |    12   |     completed      |2013-10-03|
| 9  |     3     |    10     |    12   |     completed      |2013-10-03| 
| 10 |     4     |    13     |    12   | cancelled_by_driver|2013-10-03|
+----+-----------+-----------+---------+--------------------+----------+
The Users table holds all users. Each user has an unique Users_Id, and Role is an ENUM type of (‘client’, ‘driver’, ‘partner’).

+----------+--------+--------+
| Users_Id | Banned |  Role  |
+----------+--------+--------+
|    1     |   No   | client |
|    2     |   Yes  | client |
|    3     |   No   | client |
|    4     |   No   | client |
|    10    |   No   | driver |
|    11    |   No   | driver |
|    12    |   No   | driver |
|    13    |   No   | driver |
+----------+--------+--------+
Write a SQL query to find the cancellation rate of requests made by unbanned clients between Oct 1, 2013 and Oct 3, 2013. 
For the above tables, your SQL query should return the following rows with the cancellation rate being rounded to two decimal places.

+------------+-------------------+
|     Day    | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 |       0.33        |
| 2013-10-02 |       0.00        |
| 2013-10-03 |       0.50        |
+------------+-------------------+


*/

-----------  MySQL ATTEMPT: ACCEPTED --------------
SELECT D.Request_at AS Day, COALESCE(ROUND(Cancels*1.0 / Total, 2),0) AS `Cancellation Rate` 
FROM 
(
	SELECT Request_at, COUNT(Client_Id) AS Total
	FROM Trips T JOIN Users U ON (

		T.Client_Id = U.Users_Id
	)
	WHERE Banned LIKE "No" 
	GROUP BY Request_at
) AS D 
LEFT JOIN 
(
	SELECT Request_at, COUNT(Client_Id) AS Cancels
	FROM Trips T JOIN Users U ON (

		T.Client_Id = U.Users_Id
	)
	WHERE Banned LIKE "No" AND Status NOT LIKE "completed"
	GROUP BY Request_at
) AS C ON (
	C.Request_at = D.Request_at
)
WHERE D.Request_at BETWEEN "2013-10-01" AND "2013-10-03"
ORDER BY D.Request_at


-----------  MySQL ANSWER: ACCEPTED --------------
SELECT 
t.Request_at Day, 
ROUND(SUM(CASE WHEN t.Status = 'completed' THEN 0 ELSE 1 END) / COUNT(*), 2) Rate			-- IMPORTANT: conditional processing
FROM Trips t
INNER JOIN Users u 
ON t.Client_Id = u.Users_Id AND u.Banned = 'No'
WHERE t.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.Request_at
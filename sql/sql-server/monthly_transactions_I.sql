/*

LC-1193
Medium

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

The query result format is in the following example:

Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+

Result table:
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+

*/


CREATE TABLE Transactions
    ([id] int, [country] varchar(2), [state] varchar(8), [amount] int, [trans_date] datetime)
;
    
INSERT INTO Transactions
    ([id], [country], [state], [amount], [trans_date])
VALUES
    (121, 'US', 'approved', 1000, '2018-12-18 00:00:00'),
    (122, 'US', 'declined', 2000, '2018-12-19 00:00:00'),
    (123, 'US', 'approved', 2000, '2019-01-01 00:00:00'),
    (124, 'DE', 'approved', 2000, '2019-01-07 00:00:00')
;



SELECT
  country
  , FORMAT(trans_date, 'yyyy-MM') AS month
  , COUNT([id]) AS trans_count
  , SUM(
    CASE 
      WHEN state LIKE 'approved' THEN 1
      ELSE 0
    END
  ) AS approved_count
  , SUM(amount) AS total_amount
  , SUM(
    CASE 
      WHEN state LIKE 'approved' THEN amount
      ELSE 0
    END
  ) AS approved_amount
 FROM
   Transactions
 GROUP BY
   country, FORMAT(trans_date, 'yyyy-MM')
 ORDER BY
   FORMAT(trans_date, 'yyyy-MM')
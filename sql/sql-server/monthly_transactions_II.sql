/*

LC-1205

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| id             | int     |
| country        | varchar |
| state          | enum    |
| amount         | int     |
| trans_date     | date    |
+----------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| trans_id       | int     |
| charge_date    | date    |
+----------------+---------+
Chargebacks contains basic information regarding incoming chargebacks from some transactions placed in Transactions table.
trans_id is a foreign key to the id column of Transactions table.
Each chargeback corresponds to a transaction made previously even if they were not approved.


Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 101  | US      | approved | 1000   | 2019-05-18 |
| 102  | US      | declined | 2000   | 2019-05-19 |
| 103  | US      | approved | 3000   | 2019-06-10 |
| 104  | US      | approved | 4000   | 2019-06-13 |
| 105  | US      | approved | 5000   | 2019-06-15 |
+------+---------+----------+--------+------------+

Chargebacks table:
+------------+------------+
| trans_id   | trans_date |
+------------+------------+
| 102        | 2019-05-29 |
| 101        | 2019-06-30 |
| 105        | 2019-09-18 |
+------------+------------+

Result table:
+----------+---------+----------------+-----------------+-------------------+--------------------+
| month    | country | approved_count | approved_amount | chargeback_count  | chargeback_amount  |
+----------+---------+----------------+-----------------+-------------------+--------------------+
| 2019-05  | US      | 1              | 1000            | 1                 | 2000               |
| 2019-06  | US      | 3              | 12000           | 1                 | 1000               |
| 2019-09  | US      | 0              | 0               | 1                 | 5000               |
+----------+---------+----------------+-----------------+-------------------+--------------------+

*/


WITH TransactionPrepared AS (
  SELECT
    t.*
    , (
      CASE 
        WHEN c.trans_id IS NULL THEN 0
        ELSE 1
      END
    ) AS chargeback
  FROM
    Transactions t LEFT JOIN Chargebacks c ON (
      t.trans_id = c.trans_id
    )
)
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
  , SUM(
    CASE 
      WHEN state LIKE 'approved' THEN amount
      ELSE 0
    END
  ) AS approved_amount
  , SUM(chargeback) AS chargeback_count
  , SUM(
    CASE 
      WHEN chargeback = 1 THEN amount
      ELSE 0
    END
  ) AS chargeback_amount
FROM
  TransactionPrepared
GROUP BY
  country, FORMAT(trans_date, 'yyyy-MM')
ORDER BY
  country, FORMAT(trans_date, 'yyyy-MM')
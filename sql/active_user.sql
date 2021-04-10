--Question 94
-- Table Accounts:

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | name          | varchar |
-- +---------------+---------+
-- the id is the primary key for this table.
-- This table contains the account id and the user name of each account.
 

-- Table Logins:

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | login_date    | date    |
-- +---------------+---------+
-- There is no primary key for this table, it may contain duplicates.
-- This table contains the account id of the user who logged in and the login date. A user may log in multiple times in the day.
 

-- Write an SQL query to find the id and the name of active users.

-- Active users are those who logged in to their accounts for 5 or more consecutive days.

-- Return the result table ordered by the id.

-- The query result format is in the following example:

-- Accounts table:
-- +----+----------+
-- | id | name     |
-- +----+----------+
-- | 1  | Winston  |
-- | 7  | Jonathan |
-- +----+----------+

-- Logins table:
-- +----+------------+
-- | id | login_date |
-- +----+------------+
-- | 7  | 2020-05-30 |
-- | 1  | 2020-05-30 |
-- | 7  | 2020-05-31 |
-- | 7  | 2020-06-01 |
-- | 7  | 2020-06-02 |
-- | 7  | 2020-06-02 |
-- | 7  | 2020-06-03 |
-- | 1  | 2020-06-07 |
-- | 7  | 2020-06-10 |
-- +----+------------+

-- Result table:
-- +----+----------+
-- | id | name     |
-- +----+----------+
-- | 7  | Jonathan |
-- +----+----------+
-- User Winston with id = 1 logged in 2 times only in 2 different days, so, Winston is not an active user.
-- User Jonathan with id = 7 logged in 7 times in 6 different days, five of them were consecutive days, so, Jonathan is an active user.

-- Solution 1 with self-join 
WITH daily_logins AS (
    SELECT 
      id 
      ,login_date
      ,1 AS daily_logins
    FROM 
      Logins
    GROUP BY 
      id, login_date
), login_counts AS (
  SELECT 
      c.id
      ,c.login_date 
      ,SUM(p.daily_logins) AS logins_past_5_days
  FROM daily_logins AS c INNER JOIN daily_logins AS p ON (
        c.id = p.id AND 
        DATEDIFF(DAY, p.login_date, c.login_date) BETWEEN 0 AND 4
  )
  GROUP BY
      c.id, c.login_date
)
SELECT *
FROM
    login_counts
ORDER BY id, login_date

-- Solution 2 with Window Function
WITH Login_Days AS (
  SELECT 
    DISTINCT *
  FROM
    Logins
), Login_History AS (
  SELECT 
    id, 
    login_date,
    LAG(login_date, 4) OVER (PARTITION BY id ORDER BY login_date ASC) AS login_date_lag4
  FROM
    Login_Days
)
SELECT *
FROM
    Login_History
WHERE 
    DATEDIFF(DAY, login_date_lag4, login_date) = 4
ORDER BY id, login_date
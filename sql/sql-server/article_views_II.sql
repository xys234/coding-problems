/*


Leetcode 1149
Medium

Linkedin phone interview question

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key for this table, it may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.


Write an SQL query to find all the people who viewed more than one article on the same date, sorted in ascending order by their id.

Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 3          | 4         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+

Result table:
+------+
| id   |
+------+
| 5    |
| 6    |
+------+

*/

-- Not all groupby columns need to be in the select list

SELECT viewer_id
FROM views
GROUP BY viewer_id, view_date
HAVING COUNT(DISTINCT article_id) > 1
ORDER BY viewer_id


/* 

pandas solution

df.groupby(['viewer_id', 'view_date'])['author_id'].unique()

*/


-- Follow up
-- How many members viewed more than one article on 2019-08-01?
-- SQL datetime functions

SELECT viewer_id
FROM Views
WHERE CONVERT(DATE, view_date) = CAST('2019-08-01' AS DATE) 
GROUP BY viewer_id
HAVING COUNT(DISTINCT article_id) > 1

/* Pandas solution 

-- df.loc[df.view_date == '2018-08-01'].groupby('viewer_id', as_index=False)['article_id'].nunique().shape[0]

*/

-- How many article authors have never viewed their own article?
SELECT COUNT(author_id)
FROM Views
WHERE author_id NOT IN (
    SELECT DISTINCT author_id 
    FROM Views
    WHERE author_id == viewer_id
)

/*

Pandas solution

df.loc[~df.author_id.isin(df.loc[df.author_id == df.viewer_id, 'author_id'].unique())]

*/
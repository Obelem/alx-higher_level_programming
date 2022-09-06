-- lists the number of records with the same score in the table second_table 
-- of the database hbtn_0c_0 in your MySQL server.
-- It displays
-- 	1. The score
-- 	2. The number of records for this score with the label number
-- List is sorted in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC 

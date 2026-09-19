-- ============================================================
-- GOOGLE PLAY STORE SQL ANALYSIS
-- ============================================================
-- Database: google_playstore.db
-- Table: apps
-- Purpose: Practice SQL and perform basic business analysis
-- ============================================================


-- ============================================================
-- 1. BASIC DATA EXPLORATION
-- ============================================================

-- 1.1 View application data
SELECT "App Name", Category, Rating
FROM apps
LIMIT 10;


-- 1.2 Count total number of applications
SELECT COUNT(*) AS Total_Apps
FROM apps;


-- 1.3 View all unique categories
SELECT DISTINCT Category
FROM apps
ORDER BY Category;


-- ============================================================
-- 2. FILTERING WITH WHERE
-- ============================================================

-- 2.1 Find Racing applications
SELECT "App Name", Category, Rating
FROM apps
WHERE Category = 'Racing';


-- 2.2 Find Racing applications rated above 4.5
SELECT "App Name", Category, Rating
FROM apps
WHERE Category = 'Racing'
AND Rating > 4.5;


-- ============================================================
-- 3. SORTING WITH ORDER BY
-- ============================================================

-- 3.1 Highest-rated Racing applications
SELECT "App Name", Category, Rating
FROM apps
WHERE Category = 'Racing'
ORDER BY Rating DESC;


-- 3.2 Lowest-rated Racing applications
SELECT "App Name", Category, Rating
FROM apps
WHERE Category = 'Racing'
ORDER BY Rating ASC;


-- ============================================================
-- 4. LIMIT
-- ============================================================

-- 4.1 Top 5 highest-rated applications
SELECT "App Name", Category, Rating
FROM apps
ORDER BY Rating DESC
LIMIT 5;


-- ============================================================
-- 5. AGGREGATE FUNCTIONS
-- ============================================================

-- 5.1 Count Racing applications
SELECT COUNT(*) AS Racing_App_Count
FROM apps
WHERE Category = 'Racing';


-- 5.2 Average rating of Racing applications
SELECT ROUND(AVG(Rating), 2) AS Average_Racing_Rating
FROM apps
WHERE Category = 'Racing';


-- 5.3 Total installs for Racing applications
SELECT SUM("Installs") AS Total_Racing_Installs
FROM apps
WHERE Category = 'Racing';


-- 5.4 Highest Racing application rating
SELECT MAX(Rating) AS Highest_Racing_Rating
FROM apps
WHERE Category = 'Racing';


-- 5.5 Lowest Racing application rating
SELECT MIN(Rating) AS Lowest_Racing_Rating
FROM apps
WHERE Category = 'Racing';


-- ============================================================
-- 6. GROUP BY
-- ============================================================

-- 6.1 Number of applications in each category
SELECT Category, COUNT(*) AS App_Count
FROM apps
GROUP BY Category
ORDER BY COUNT(*) DESC;


-- 6.2 Average rating for each category
SELECT Category,
       ROUND(AVG(Rating), 2) AS Average_Rating
FROM apps
GROUP BY Category
ORDER BY AVG(Rating) DESC;


-- ============================================================
-- 7. GROUP BY + ORDER BY + LIMIT
-- ============================================================

-- 7.1 Top 5 categories by number of applications
SELECT Category, COUNT(*) AS App_Count
FROM apps
GROUP BY Category
ORDER BY COUNT(*) DESC
LIMIT 5;


-- 7.2 Top 5 categories by average rating
SELECT Category,
       ROUND(AVG(Rating), 2) AS Average_Rating
FROM apps
GROUP BY Category
ORDER BY AVG(Rating) DESC
LIMIT 5;


-- ============================================================
-- 8. HAVING
-- ============================================================

-- 8.1 Categories containing more than 100 applications
SELECT Category, COUNT(*) AS App_Count
FROM apps
GROUP BY Category
HAVING COUNT(*) > 100;


-- 8.2 Top 5 categories with more than 100 applications
SELECT Category, COUNT(*) AS App_Count
FROM apps
GROUP BY Category
HAVING COUNT(*) > 100
ORDER BY COUNT(*) DESC
LIMIT 5;


-- ============================================================
-- 9. BUSINESS ANALYSIS QUESTIONS
-- ============================================================

-- Question 1:
-- Which categories contain the most applications?

SELECT Category, COUNT(*) AS App_Count
FROM apps
GROUP BY Category
ORDER BY App_Count DESC
LIMIT 5;


-- Question 2:
-- Which categories have the highest average ratings?

SELECT Category,
       ROUND(AVG(Rating), 2) AS Average_Rating
FROM apps
GROUP BY Category
ORDER BY Average_Rating DESC
LIMIT 5;


-- Question 3:
-- Which Racing applications have ratings above 4.5?

SELECT "App Name", Rating
FROM apps
WHERE Category = 'Racing'
AND Rating > 4.5
ORDER BY Rating DESC;


-- Question 4:
-- How many applications are in each category?

SELECT Category, COUNT(*) AS App_Count
FROM apps
GROUP BY Category
ORDER BY App_Count DESC;


-- Question 5:
-- Which categories have more than 100 applications?

SELECT Category, COUNT(*) AS App_Count
FROM apps
GROUP BY Category
HAVING COUNT(*) > 100
ORDER BY App_Count DESC;


-- Question 6:
-- What is the overall average application rating?

SELECT ROUND(AVG(Rating), 2) AS Overall_Average_Rating
FROM apps;


-- Question 7:
-- What is the highest application rating?

SELECT MAX(Rating) AS Highest_Rating
FROM apps;


-- Question 8:
-- What is the lowest application rating?

SELECT MIN(Rating) AS Lowest_Rating
FROM apps;


-- ============================================================
-- END OF SQL PROJECT
-- ============================================================
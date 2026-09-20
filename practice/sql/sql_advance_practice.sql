-- ============================================================
-- SQL ADVANCED PRACTICE
-- Database: google_playstore.db
-- Table: apps
-- ============================================================


-- ============================================================
-- 1. CASE STATEMENT
-- ============================================================

-- Classify apps based on their rating

SELECT
    "App Name",
    Category,
    Rating,
    CASE
        WHEN Rating >= 4.5 THEN 'Excellent'
        WHEN Rating >= 4.0 THEN 'Good'
        WHEN Rating >= 3.0 THEN 'Average'
        ELSE 'Poor'
    END AS Rating_Category
FROM apps;
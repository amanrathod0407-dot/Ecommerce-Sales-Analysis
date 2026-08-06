-- ============================================
-- 02_basic_queries.sql
-- E-Commerce Sales Analysis
-- Basic SQL Queries
-- ============================================

USE ecommerce_sales;

-- 1. View all records
SELECT * FROM superstore;

-- 2. View first 10 records
SELECT * FROM superstore
LIMIT 10;

-- 3. View specific columns
SELECT Customer_Name, Sales
FROM superstore;

-- 4. Find Technology category products
SELECT *
FROM superstore
WHERE Category = 'Technology';

-- 5. Find Furniture category products
SELECT *
FROM superstore
WHERE Category = 'Furniture';

-- 6. Orders with Sales greater than 1000
SELECT *
FROM superstore
WHERE Sales > 1000;

-- 7. Orders with Profit less than 0
SELECT *
FROM superstore
WHERE Profit < 0;

-- 8. Orders from California
SELECT *
FROM superstore
WHERE State = 'California';

-- 9. Sort Sales (Highest First)
SELECT Product_Name, Sales
FROM superstore
ORDER BY Sales DESC;

-- 10. Sort Profit (Highest First)
SELECT Product_Name, Profit
FROM superstore
ORDER BY Profit DESC;

-- 11. Lowest Profit
SELECT Product_Name, Profit
FROM superstore
ORDER BY Profit ASC
LIMIT 10;

-- 12. Highest Discount
SELECT Product_Name, Discount
FROM superstore
ORDER BY Discount DESC;

-- 13. Distinct Categories
SELECT DISTINCT Category
FROM superstore;

-- 14. Distinct Regions
SELECT DISTINCT Region
FROM superstore;

-- 15. Distinct Segments
SELECT DISTINCT Segment
FROM superstore;

-- 16. Orders with Quantity >= 5
SELECT *
FROM superstore
WHERE Quantity >= 5;

-- 17. Sales between 500 and 1000
SELECT *
FROM superstore
WHERE Sales BETWEEN 500 AND 1000;

-- 18. Customers whose name starts with A
SELECT *
FROM superstore
WHERE Customer_Name LIKE 'A%';

-- 19. Products containing Chair
SELECT *
FROM superstore
WHERE Product_Name LIKE '%Chair%';

-- 20. Count Total Orders
SELECT COUNT(*) AS Total_Orders
FROM superstore;
-- ============================================
-- 04_advanced_queries.sql
-- Advanced SQL
-- ============================================

USE ecommerce_sales;

-- 1. Sales Status using CASE
SELECT Product_Name,
       Sales,
       CASE
           WHEN Sales >= 1000 THEN 'High'
           WHEN Sales >= 500 THEN 'Medium'
           ELSE 'Low'
       END AS Sales_Level
FROM superstore;

-- 2. Profit Status
SELECT Product_Name,
       Profit,
       CASE
           WHEN Profit > 0 THEN 'Profit'
           ELSE 'Loss'
       END AS Profit_Status
FROM superstore;

-- 3. Rank Products by Sales
SELECT Product_Name,
       Sales,
       RANK() OVER(ORDER BY Sales DESC) AS Sales_Rank
FROM superstore;

-- 4. Dense Rank Products
SELECT Product_Name,
       Sales,
       DENSE_RANK() OVER(ORDER BY Sales DESC) AS Dense_Rank
FROM superstore;

-- 5. Row Number
SELECT Product_Name,
       Sales,
       ROW_NUMBER() OVER(ORDER BY Sales DESC) AS Row_Num
FROM superstore;

-- 6. Running Total of Sales
SELECT Order_Date,
       Sales,
       SUM(Sales) OVER(ORDER BY Order_Date) AS Running_Total
FROM superstore;

-- 7. Average Sales by Category
SELECT Product_Name,
       Category,
       Sales,
       AVG(Sales) OVER(PARTITION BY Category) AS Avg_Category_Sales
FROM superstore;

-- 8. Maximum Sales by Category
SELECT Product_Name,
       Category,
       MAX(Sales) OVER(PARTITION BY Category) AS Max_Sales
FROM superstore;

-- 9. Minimum Sales by Category
SELECT Product_Name,
       Category,
       MIN(Sales) OVER(PARTITION BY Category) AS Min_Sales
FROM superstore;

-- 10. Total Sales by Region
SELECT Product_Name,
       Region,
       SUM(Sales) OVER(PARTITION BY Region) AS Region_Sales
FROM superstore;

-- 11. Products above Average Sales
SELECT Product_Name,
       Sales
FROM superstore
WHERE Sales >
(
SELECT AVG(Sales)
FROM superstore
);

-- 12. Customers above Average Profit
SELECT Customer_Name,
       Profit
FROM superstore
WHERE Profit >
(
SELECT AVG(Profit)
FROM superstore
);

-- 13. Top 5 Sales
SELECT *
FROM superstore
ORDER BY Sales DESC
LIMIT 5;

-- 14. Top 5 Profit
SELECT *
FROM superstore
ORDER BY Profit DESC
LIMIT 5;

-- 15. Bottom 5 Profit
SELECT *
FROM superstore
ORDER BY Profit ASC
LIMIT 5;

-- 16. Count Orders by Category
SELECT Category,
       COUNT(*) AS Orders
FROM superstore
GROUP BY Category;

-- 17. Total Sales by Customer
SELECT Customer_Name,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Customer_Name
ORDER BY Total_Sales DESC;

-- 18. Total Profit by Customer
SELECT Customer_Name,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Customer_Name
ORDER BY Total_Profit DESC;

-- 19. Top 10 Products by Sales
SELECT Product_Name,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- 20. Top 10 Products by Profit
SELECT Product_Name,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Product_Name
ORDER BY Total_Profit DESC
LIMIT 10;
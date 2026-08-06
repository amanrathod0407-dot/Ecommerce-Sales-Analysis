USE ecommerce_sales;

-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM superstore;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM superstore;

-- Average Sales
SELECT AVG(Sales) AS Average_Sales
FROM superstore;

-- Sales by Category
SELECT Category,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category;

-- Profit by Category
SELECT Category,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category;





USE ecommerce_sales;

-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM superstore;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM superstore;

-- Average Sales
SELECT AVG(Sales) AS Average_Sales
FROM superstore;

-- Maximum Sale
SELECT MAX(Sales) AS Highest_Sale
FROM superstore;

-- Minimum Sale
SELECT MIN(Sales) AS Lowest_Sale
FROM superstore;


-- Sales by Category
SELECT
    Category,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Profit by Category
SELECT
    Category,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC;
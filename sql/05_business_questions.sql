-- =============================================
-- 05_business_questions.sql
-- E-Commerce Sales Analysis
-- Business Questions
-- =============================================

USE ecommerce_sales;

-- 1. Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM superstore;

-- 2. Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM superstore;

-- 3. Total Orders
SELECT COUNT(*) AS Total_Orders
FROM superstore;

-- 4. Total Customers
SELECT COUNT(DISTINCT Customer_ID) AS Total_Customers
FROM superstore;

-- 5. Highest Sales Category
SELECT Category,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC
LIMIT 1;

-- 6. Highest Profit Category
SELECT Category,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC
LIMIT 1;

-- 7. Region with Highest Sales
SELECT Region,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC
LIMIT 1;

-- 8. Region with Highest Profit
SELECT Region,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Region
ORDER BY Total_Profit DESC
LIMIT 1;

-- 9. State with Highest Sales
SELECT State,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY State
ORDER BY Total_Sales DESC
LIMIT 1;

-- 10. State with Highest Profit
SELECT State,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY State
ORDER BY Total_Profit DESC
LIMIT 1;

-- 11. Top 10 Customers by Sales
SELECT Customer_Name,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- 12. Top 10 Customers by Profit
SELECT Customer_Name,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Customer_Name
ORDER BY Total_Profit DESC
LIMIT 10;

-- 13. Bottom 10 Customers by Profit
SELECT Customer_Name,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Customer_Name
ORDER BY Total_Profit ASC
LIMIT 10;

-- 14. Top 10 Products by Sales
SELECT Product_Name,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- 15. Top 10 Products by Profit
SELECT Product_Name,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Product_Name
ORDER BY Total_Profit DESC
LIMIT 10;

-- 16. Products Making Loss
SELECT Product_Name,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Product_Name
HAVING SUM(Profit) < 0
ORDER BY Total_Profit;

-- 17. Category-wise Average Discount
SELECT Category,
       AVG(Discount) AS Avg_Discount
FROM superstore
GROUP BY Category;

-- 18. Ship Mode Performance
SELECT Ship_Mode,
       SUM(Sales) AS Total_Sales,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Ship_Mode;

-- 19. Segment-wise Sales
SELECT Segment,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Segment
ORDER BY Total_Sales DESC;

-- 20. Segment-wise Profit
SELECT Segment,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Segment
ORDER BY Total_Profit DESC;

-- 21. Monthly Sales Trend
SELECT DATE_FORMAT(STR_TO_DATE(Order_Date,'%Y-%m-%d'),'%Y-%m') AS Month,
       SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Month
ORDER BY Month;

-- 22. Monthly Profit Trend
SELECT DATE_FORMAT(STR_TO_DATE(Order_Date,'%Y-%m-%d'),'%Y-%m') AS Month,
       SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Month
ORDER BY Month;

-- 23. Average Order Value
SELECT AVG(Sales) AS Average_Order_Value
FROM superstore;

-- 24. Most Ordered Category
SELECT Category,
       SUM(Quantity) AS Total_Quantity
FROM superstore
GROUP BY Category
ORDER BY Total_Quantity DESC
LIMIT 1;

-- 25. Overall Business Summary
SELECT
    COUNT(*) AS Total_Orders,
    COUNT(DISTINCT Customer_ID) AS Total_Customers,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    AVG(Discount) AS Average_Discount
FROM superstore;
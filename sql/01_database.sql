CREATE DATABASE ecommerce_sales;
USE ecommerce_sales;

SHOW DATABASES;


USE ecommerce_sales;

SELECT DATABASE();

CREATE TABLE superstore (

    Row_ID INT,
    Order_ID VARCHAR(30),
    Order_Date VARCHAR(30),
    Ship_Date VARCHAR(30),
    Ship_Mode VARCHAR(50),
    Customer_ID VARCHAR(30),
    Customer_Name VARCHAR(100),
    Segment VARCHAR(50),
    Country VARCHAR(50),
    City VARCHAR(100),
    State VARCHAR(100),
    Postal_Code INT,
    Region VARCHAR(50),
    Product_ID VARCHAR(50),
    Category VARCHAR(50),
    Sub_Category VARCHAR(50),
    Product_Name VARCHAR(255),
    Sales DECIMAL(10,2),
    Quantity INT,
    Discount DECIMAL(5,2),
    Profit DECIMAL(10,2)

);

SHOW TABLES;

DESCRIBE superstore;



SELECT COUNT(*) AS Total_Rows
FROM superstore;

SELECT *
FROM superstore
LIMIT 10;
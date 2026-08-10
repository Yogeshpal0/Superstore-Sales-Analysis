
-- Database Setup

CREATE DATABASE superstore_db;
USE superstore_db;

CREATE TABLE superstore (
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(50),
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    country VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    region VARCHAR(20),
    product_id VARCHAR(50),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(255),
    sales DECIMAL(10,2),
    quantity INT,
    discount DECIMAL(5,2),
    profit DECIMAL(10,2),
    year INT,
    month VARCHAR(20),
    quarter VARCHAR(10),
    delivery_days INT
);

-- Import Data

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/clean_superstore.csv'
INTO TABLE superstore
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
order_id,@order_date,@ship_date,ship_mode,customer_id,customer_name,
segment,country,city,state,postal_code,region,product_id,category,
sub_category,product_name,sales,quantity,discount,profit,
year,month,quarter,delivery_days
)
SET
order_date = STR_TO_DATE(@order_date,'%d-%m-%Y'),
ship_date = STR_TO_DATE(@ship_date,'%d-%m-%Y');

-- KPIs

SELECT COUNT(DISTINCT order_id) AS total_orders FROM superstore;
SELECT COUNT(DISTINCT customer_id) AS total_customers FROM superstore;
SELECT ROUND(SUM(sales),2) AS total_sales FROM superstore;
SELECT ROUND(SUM(profit),2) AS total_profit FROM superstore;

-- Category Analysis

SELECT category, ROUND(SUM(sales),2) AS total_sales
FROM superstore GROUP BY category ORDER BY total_sales DESC;

SELECT category, ROUND(SUM(profit),2) AS total_profit
FROM superstore GROUP BY category ORDER BY total_profit DESC;

-- Sub Category Analysis

SELECT sub_category, ROUND(SUM(sales),2) AS total_sales
FROM superstore GROUP BY sub_category ORDER BY total_sales DESC;

SELECT sub_category, ROUND(SUM(profit),2) AS total_profit
FROM superstore GROUP BY sub_category ORDER BY total_profit DESC;

-- Monthly Analysis

SELECT month, ROUND(SUM(sales),2) AS total_sales
FROM superstore GROUP BY month ORDER BY total_sales DESC;

SELECT month,
ROUND(SUM(sales),2) AS total_sales,
ROUND(SUM(profit),2) AS total_profit,
ROUND((SUM(profit)/SUM(sales))*100,2) AS profit_margin
FROM superstore
GROUP BY month;

-- Customer Analysis

SELECT customer_name,
ROUND(SUM(sales),2) AS total_sales
FROM superstore
GROUP BY customer_name
ORDER BY total_sales DESC;

SELECT customer_name,
ROUND(SUM(profit),2) AS total_profit
FROM superstore
GROUP BY customer_name
ORDER BY total_profit DESC
LIMIT 10;

-- Region Analysis

SELECT region, ROUND(SUM(sales),2) AS total_sales
FROM superstore GROUP BY region ORDER BY total_sales DESC;

SELECT region, ROUND(SUM(profit),2) AS total_profit
FROM superstore GROUP BY region ORDER BY total_profit DESC;

-- State Analysis

SELECT state, ROUND(SUM(sales),2) AS total_sales
FROM superstore
GROUP BY state
ORDER BY total_sales DESC
LIMIT 10;

-- Segment Analysis

SELECT segment, ROUND(SUM(sales),2) AS total_sales
FROM superstore GROUP BY segment;

SELECT segment, ROUND(SUM(profit),2) AS total_profit
FROM superstore GROUP BY segment;

-- Window Functions

SELECT
    category,
    customer_name,
    ROUND(SUM(sales),2) AS total_sales,
    ROW_NUMBER() OVER(
        PARTITION BY category
        ORDER BY SUM(sales) DESC
    ) AS rn
FROM superstore
GROUP BY category, customer_name;

SELECT
    customer_name,
    ROUND(SUM(sales),2) AS total_sales,
    DENSE_RANK() OVER(
        ORDER BY SUM(sales) DESC
    ) AS customer_rank
FROM superstore
GROUP BY customer_name;

-- CTE + DENSE_RANK

WITH customer_rank AS
(
    SELECT
        category,
        customer_name,
        ROUND(SUM(sales),2) AS total_sales,
        DENSE_RANK() OVER(
            PARTITION BY category
            ORDER BY SUM(sales) DESC
        ) AS customer_rank
    FROM superstore
    GROUP BY category, customer_name
)
SELECT *
FROM customer_rank
WHERE customer_rank <= 3;

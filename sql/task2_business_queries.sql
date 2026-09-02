SELECT
    Category,
    ROUND(SUM(Total_Sales), 2) AS Total_Revenue
FROM sales_data
GROUP BY Category
ORDER BY Total_Revenue DESC;

SELECT
    City,
    ROUND(SUM(Total_Sales), 2) AS Total_Revenue
FROM sales_data
GROUP BY City
ORDER BY Total_Revenue DESC
LIMIT 10;

SELECT
    Order_Year,
    Order_Month,
    ROUND(SUM(Total_Sales), 2) AS Monthly_Revenue
FROM sales_data
GROUP BY Order_Year, Order_Month
ORDER BY Order_Year, Order_Month;

SELECT
    Age_Group,
    ROUND(SUM(Total_Sales), 2) AS Total_Revenue
FROM sales_data
GROUP BY Age_Group
ORDER BY Total_Revenue DESC;

SELECT
    Category,
    ROUND(AVG(Total_Sales), 2) AS Average_Order_Value
FROM sales_data
GROUP BY Category
ORDER BY Average_Order_Value DESC;

SELECT
    Product,
    ROUND(SUM(Total_Sales), 2) AS Total_Revenue
FROM sales_data
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 5;

SELECT
    Age_Group,
    Gender,
    ROUND(AVG(Total_Sales), 2) AS Average_Transaction_Value,
    COUNT(*) AS Number_Of_Orders
FROM sales_data
GROUP BY Age_Group, Gender
ORDER BY Average_Transaction_Value DESC;


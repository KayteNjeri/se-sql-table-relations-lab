# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql(""" SELECT firstName, jobTitle 
    FROM employees 
    JOIN offices USING(officeCode) 
    WHERE city = 'Boston';
""", conn)
print(df_boston)

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql("""SELECT offices.officeCode, offices.city FROM offices LEFT JOIN employees USING(officeCode) GROUP BY 1 HAVING COUNT(employeeNumber) = 0;""", conn)
print(df_zero_emp)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql("""
    SELECT 
        employees.firstName, 
        employees.lastName, 
        offices.city, 
        offices.state
    FROM employees
    LEFT JOIN offices USING(officeCode)
    ORDER BY employees.firstName ASC, employees.lastName ASC;
""", conn)
print(df_employee)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql("""
    SELECT 
        contactFirstName, 
        contactLastName, 
        phone, 
        salesRepEmployeeNumber
    FROM customers
    LEFT JOIN orders USING(customerNumber)
    WHERE orders.orderNumber IS NULL
    ORDER BY contactLastName ASC;
""", conn)
print(df_contacts)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql("""
    SELECT 
        customers.contactFirstName, 
        customers.contactLastName, 
        payments.paymentDate, 
        payments.amount
    FROM customers
    JOIN payments USING(customerNumber)
    ORDER BY CAST(payments.amount AS DECIMAL(10,2)) DESC;
""", conn)
print(df_payment)

# STEP 6
# Replace None with your code
df_credit =  pd.read_sql("""
    SELECT 
        employees.employeeNumber, 
        employees.firstName, 
        employees.lastName, 
        COUNT(customers.customerNumber) AS num_customers
    FROM employees
    JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber
    GROUP BY employees.employeeNumber, employees.firstName, employees.lastName
    HAVING AVG(customers.creditLimit) > 90000
    ORDER BY num_customers DESC;
""", conn)
print(df_credit)

# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql("""
    SELECT 
        products.productName, 
        COUNT(DISTINCT orderdetails.orderNumber) AS numorders, 
        SUM(orderdetails.quantityOrdered) AS totalunits
    FROM products
    JOIN orderdetails USING(productCode)
    GROUP BY products.productCode, products.productName
    ORDER BY totalunits DESC;
""", conn)
print(df_product_sold)

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql("""
    SELECT 
        products.productName, 
        products.productCode, 
        COUNT(DISTINCT orders.customerNumber) AS numpurchasers
    FROM products
    JOIN orderdetails USING(productCode)
    JOIN orders USING(orderNumber)
    GROUP BY products.productCode, products.productName
    ORDER BY numpurchasers DESC;
""", conn)
print(df_total_customers)

# STEP 9
# Replace None with your code
df_customers = pd.read_sql("""
    SELECT 
        offices.officeCode, 
        offices.city, 
        COUNT(customers.customerNumber) AS n_customers
    FROM offices
    JOIN employees USING(officeCode)
    JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber
    GROUP BY offices.officeCode, offices.city;
""", conn)
print(df_customers)

# STEP 10
# Replace None with your code


df_under_20 = pd.read_sql("""
    SELECT
    DISTINCT employeeNumber,
    officeCode,
    o.city,
    firstName,
    lastName
FROM employees AS e
JOIN offices AS o
    USING(officeCode)
JOIN customers AS c
    ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders
    USING(customerNumber)
JOIN orderdetails
    USING(orderNumber)
WHERE productCode IN (
    SELECT productCode
    FROM products
    JOIN orderdetails
        USING(productCode)
    JOIN orders
        USING(orderNumber)
    GROUP BY productCode
    HAVING COUNT(DISTINCT customerNumber) < 20
) ORDER BY lastName ASC;""", conn)
print(df_under_20)

conn.close()
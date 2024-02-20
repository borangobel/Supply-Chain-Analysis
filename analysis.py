import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import datetime as dt

# Establish a connection to the SQL Server database
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-5MSEV36C;DATABASE=AdventureWorks2019;Trusted_Connection=yes;')

# Query the data from SQL Server
sql_query = "SELECT * FROM SupplyChainAnalysis;"
data = pd.read_sql(sql_query, conn)


# Data Type editing
data['OrderDate'] = pd.to_datetime(data['OrderDate'])
data['ShipDate'] = pd.to_datetime(data['ShipDate'])

# print(data.info())

# Question 1 : Which vendor has the highest total sales amount?

# select VendorID, SUM(TotalAmount) as TotalAmountSum
# from dbo.SupplyChainAnalysis
# group by VendorID
# order by SUM(TotalAmount) desc;

# select * from SupplyChainAnalysis;




# Question 2 : What is the average order quantity for each product?

# --2
# select ProductID,ProductName, avg(OrderQty) AS AvgOrderQty
# from SupplyChainAnalysis
# group by ProductID,ProductName
# order by AvgOrderQty desc;

# Question 3 : What is the total sales amount for each year?

def year_sales() :
    order_year = data['OrderDate'].dt.year
    total_sales_year = data.groupby(order_year)['TotalAmount'].sum()

    print(total_sales_year.head(15))

# Question 4 : Which product has the highest total sales amount?
    
def highest_sales_product():
    grouped = data.groupby('ProductName')
    total_sales_product = grouped['TotalAmount'].sum()

    top_products = total_sales_product.head(10).sort_values(ascending = False)

    plt.figure(figsize=(10,6))
    plt.bar(top_products.index,top_products.values)
    plt.xticks(rotation = 90)
    plt.grid(True)
    plt.show()

highest_sales_product()

# Question 5 : How many orders were shipped late? 
def late_shipments():
    
    data['EstimatedShipDate'] = data['OrderDate'] + pd.Timedelta(days=9)

    late_ship = data[data['ShipDate'] > data['EstimatedShipDate']]
    no_late_ship = len(late_ship)

    late_ship_percent = (no_late_ship *100)/len(data['OrderDate'])

    print("Number of orders shipped late:", no_late_ship)
    print("Percentage of late shipment : ", late_ship_percent)


# Question 6 : What is the average unit price for each vendor?
    
def avg_unitprice ():

    avg_prc = data.groupby('VendorName')['UnitPrice'].mean().sort_values(ascending=False).head(10)
    # print(avg_prc.head(10).sort_values(ascending=False))

    plt.figure(figsize=(10,6))
    plt.bar(avg_prc.index,avg_prc.values,color = 'skyblue')
    plt.xlabel('Vendor Names')
    plt.ylabel('Average Unit Prices')
    plt.grid(True)
    plt.xticks(rotation= 90)
    plt.show()

# Question 7 : What is the total sales amount for each vendor?

def vendor_total_sales():
    total_sales = data.groupby('VendorName')['OrderQty'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(14,7))
    plt.barh(total_sales.index,total_sales.values, color = 'blue')
    plt.title("TOP 10 Vendor Sales Amount")
    plt.grid(True)
    plt.yticks(rotation = 45)
    plt.show()


# Question 8 : What is the distribution of order quantities?
    
def distribution_orderqty():
    order_quantity_stats = data['OrderQty'].describe()

    # Visualize the Distribution
    plt.figure(figsize=(10, 6))
    plt.hist(data['OrderQty'], bins=30, color='skyblue', edgecolor='black')  # Increase the number of bins to 30
    plt.title('Distribution of Order Quantities')
    plt.xlabel('Order Quantity')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Print Descriptive Statistics
    print("Descriptive Statistics for Order Quantities:")
    print(order_quantity_stats)


print(data.head())

# Question 9 : Which product category has the highest total sales amount?

# select ProductCategory,sum(TotalAmount) as TotalSalesAmount
# from SupplyChainAnalysis
# where ProductCategory <> 'Uncategorized'
# group by ProductCategory
# ORDER BY TotalSalesAmount DESC;

# Question 10 : How many unique products were ordered?

def unique_product():
    n_unique = data['ProductName'].nunique()
    print(n_unique)

data.to_csv('SupplyChainAnalysis.csv', index=False)
# Close the connection
conn.close()

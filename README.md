# Supply-Chain-Analysis

Overview
This project focuses on analyzing supply chain data from the AdventureWorks2019 database to gain insights into various aspects of the supply chain process. The analysis includes tasks such as supplier performance evaluation, inventory management analysis, demand forecasting, and procurement analysis.

Dataset
The dataset used for this analysis is sourced from the AdventureWorks2019 database, which provides comprehensive information on purchase orders, vendors, products, and sales transactions. The dataset contains the following key columns:

PurchaseOrderID: Unique identifier for each purchase order.
OrderDate: Date when the purchase order was placed.
ShipDate: Date when the purchase order was shipped.
VendorID: Unique identifier for each vendor.
VendorName: Name of the vendor.
ProductID: Unique identifier for each product.
ProductName: Name of the product.
ProductCategory: Category of the product.
ProductSubcategory: Subcategory of the product.
OrderQty: Quantity of the product ordered.
UnitPrice: Unit price of the product.
TotalAmount: Total amount for the purchase order.


Tasks
The analysis encompasses the following tasks:

Which vendor has the highest total sales amount?
What is the average order quantity for each product?
What is the total sales amount for each year?
Which product has the highest total sales amount?
How many orders were shipped late?
What is the average unit price for each vendor?
What is the total sales amount for each vendor?
What is the distribution of order quantities?
Which product category has the highest total sales amount?
How many unique products were ordered?


Tools and Technologies
SQL: Used for querying and extracting data from the AdventureWorks2019 database.
Python: Utilized libraries such as pandas for data manipulation and analysis.
Tableau: Used for data visualization and creating interactive dashboards to present the analysis results.
Files Included
data_analysis.sql: SQL queries used for data extraction and preparation from the AdventureWorks2019 database.
data_analysis.py: Python script for performing data analysis tasks using pandas.
supply_chain_analysis_tasks.sql: SQL queries for solving some of the analysis tasks.
supply_chain_analysis.twb: Tableau workbook containing visualizations and dashboards for presenting the analysis results.
README.md: This README file providing an overview of the project and instructions for running the analysis.


How to Run the Analysis
Ensure that you have access to the AdventureWorks2019 database.
Execute the SQL queries in SupplyChainAnalysis.Create%Insert.sql to extract and prepare the data for analysis.
Run the Python script analysis.py to perform data analysis tasks using pandas.
Execute the SQL queries in supplychainanalysis_tasks.sql to solve some of the analysis tasks.
Open the Tableau workbook supply_chain_analysis.twb to visualize the analysis results and explore interactive dashboards.


Conclusion
The supply chain analysis project aims to provide valuable insights into supply chain operations, vendor performance, inventory management, and procurement strategies. By leveraging data analytics techniques and visualization tools, stakeholders can make informed decisions to optimize supply chain processes, improve efficiency, and drive business growth.

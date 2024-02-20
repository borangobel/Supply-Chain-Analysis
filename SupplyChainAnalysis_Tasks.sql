--Question 1 : Which vendor has the highest total sales amount?

select VendorID, SUM(TotalAmount) as TotalAmountSum
from dbo.SupplyChainAnalysis
group by VendorID
order by SUM(TotalAmount) desc;

select * from SupplyChainAnalysis;

--Question 2 : What is the average order quantity for each product?

select ProductID,ProductName, avg(OrderQty) AS AvgOrderQty
from SupplyChainAnalysis
group by ProductID,ProductName
order by AvgOrderQty desc;

--Question 9 : Which product category has the highest total sales amount?

select ProductCategory,sum(TotalAmount) as TotalSalesAmount
from SupplyChainAnalysis
where ProductCategory <> 'Uncategorized'
group by ProductCategory
ORDER BY TotalSalesAmount DESC;
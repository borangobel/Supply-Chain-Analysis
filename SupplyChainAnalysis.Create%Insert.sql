--Creating Table
CREATE TABLE SupplyChainAnalysis (
    PurchaseOrderID INT,
    OrderDate DATE,
    ShipDate DATE,
    BusinessEntityID INT,
    VendorName NVARCHAR(255),
    ProductID INT,
    ProductName NVARCHAR(255),
    OrderQty INT,
    UnitPrice DECIMAL(18, 2),
    TotalAmount DECIMAL(18, 2)
);

--Inserting data
INSERT INTO SupplyChainAnalysis (PurchaseOrderID, OrderDate, ShipDate, BusinessEntityID, VendorName, ProductID, ProductName, OrderQty, UnitPrice, TotalAmount)
SELECT 
    po.PurchaseOrderID,
    po.OrderDate,
    po.ShipDate,
    v.BusinessEntityID,
    v.Name AS VendorName,
    pod.ProductID,
    p.Name AS ProductName,
    pod.OrderQty,
    pod.UnitPrice,
    pod.OrderQty * pod.UnitPrice AS TotalAmount
FROM 
    Purchasing.PurchaseOrderHeader po
INNER JOIN 
    Purchasing.PurchaseOrderDetail pod ON po.PurchaseOrderID = pod.PurchaseOrderID
INNER JOIN 
    Production.Product p ON pod.ProductID = p.ProductID
INNER JOIN 
    Purchasing.Vendor v ON po.VendorID = v.BusinessEntityID;

--Adding Collumn
ALTER TABLE SupplyChainAnalysis
ADD ProductCategory NVARCHAR(255),
    ProductSubcategory NVARCHAR(255);

--Inserting Data to the Collumn
UPDATE SupplyChainAnalysis
SET 
    ProductCategory = pc.Name,
    ProductSubcategory = ps.Name
FROM 
    SupplyChainAnalysis sca
INNER JOIN 
    Production.Product p ON sca.ProductID = p.ProductID
INNER JOIN 
    Production.ProductSubcategory ps ON p.ProductSubcategoryID = ps.ProductSubcategoryID
INNER JOIN 
    Production.ProductCategory pc ON ps.ProductCategoryID = pc.ProductCategoryID;

--Changing the null values 
	UPDATE SupplyChainAnalysis
SET 
    ProductCategory = COALESCE(ProductCategory, 'Uncategorized'),
    ProductSubcategory = COALESCE(ProductSubcategory, 'Not Specified');



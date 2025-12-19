-- Insert data into bronze schema tables

-- Insert data into brand_info table
BULK INSERT bronze.brand_info
FROM 'C:\Users\ASUS\Downloads\reporting\brand data\brand_table.csv'
WITH (
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
);

-- Insert data into host_info table
BULK INSERT bronze.host_info
FROM 'C:\Users\ASUS\Downloads\reporting\host data\host_table.csv'
WITH (
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
);

-- Insert data into shopee_livestreaming table
BULK INSERT bronze.shopee_livestreaming
FROM 'C:\Users\ASUS\Downloads\reporting\result\shopee_ready_to_db.csv'
WITH (
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
);

-- Insert data into tiktok_livestreaming table
BULK INSERT bronze.tiktok_livestreaming
FROM 'C:\Users\ASUS\Downloads\reporting\result\tiktok_ready_to_db.csv'
WITH (
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
);

-- CHECK
SELECT * FROM bronze.brand_info
SELECT * FROM bronze.host_info
SELECT * FROM bronze.shopee_livestreaming
SELECT * FROM bronze.tiktok_livestreaming

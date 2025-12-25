-- Insert data into bronze schema tables
USE BuzzliveWarehouse;
GO
CREATE PROCEDURE bronze.load_info AS
BEGIN
	-- Insert data into brand_info table
	TRUNCATE TABLE bronze.brand_info;
	BULK INSERT bronze.brand_info
	FROM 'C:\Users\ASUS\Downloads\reporting\brand data\brand_table.csv'
	WITH (
		FIRSTROW = 2,
		FIELDTERMINATOR = ',',
		TABLOCK
	);

	-- Insert data into host_info table
	TRUNCATE TABLE bronze.host_info;
	BULK INSERT bronze.host_info
	FROM 'C:\Users\ASUS\Downloads\reporting\host data\host_table.csv'
	WITH (
		FIRSTROW = 2,
		FIELDTERMINATOR = ',',
		TABLOCK
	);
END;

GO

CREATE PROCEDURE bronze.load_shopee AS
BEGIN
	-- Insert data into shopee_livestreaming table
	--TRUNCATE TABLE bronze.shopee_livestreaming;
	BULK INSERT bronze.shopee_livestreaming
	FROM 'C:\Users\ASUS\Downloads\reporting\result\ready_to_db_shopee.csv'
	WITH (
		FIRSTROW = 2,
		FIELDTERMINATOR = ',',
		TABLOCK,
		CODEPAGE = 'ACP'
	);
END;

GO
 
CREATE PROCEDURE bronze.load_tiktok AS
BEGIN
	-- Insert data into tiktok_livestreaming table
	--TRUNCATE TABLE bronze.tiktok_livestreaming;
	BULK INSERT bronze.tiktok_livestreaming
	FROM 'C:\Users\ASUS\Downloads\reporting\result\ready_to_db_tiktok.csv'
	WITH (
		FIRSTROW = 2,
		FIELDTERMINATOR = ',',
		TABLOCK
	);
END;

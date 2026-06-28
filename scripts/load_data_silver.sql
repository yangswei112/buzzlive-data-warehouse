-- Insert data into silver table
USE BuzzliveWarehouse;
GO

DROP PROCEDURE silver.load_info;
GO
CREATE PROCEDURE silver.load_info AS
BEGIN
	-- Insert data into brand_table
	TRUNCATE TABLE silver.brand_info;
	INSERT INTO silver.brand_info (
		brand_id,
		brand_category,
		brand_name,
		platform,
		business_category)

	SELECT
	brand_id,
	brand_category,
	brand_name,
	platform,
	business_category
	FROM bronze.brand_info;

	-- Insert data into host_table
	TRUNCATE TABLE silver.host_info;
	INSERT INTO silver.host_info (
		host_id,
		host_name,
		host_birthdate)

	SELECT
		host_id,
		host_name,
		host_birthdate
	FROM bronze.host_info;
END;

GO

DROP PROCEDURE silver.load_shopee;
GO
CREATE PROCEDURE silver.load_shopee AS
BEGIN
	-- Insert data into shopee_livestreaming table
	--TRUNCATE TABLE bronze.shopee_livestreaming;
	BULK INSERT silver.shopee_livestreaming
	FROM 'data/result/ready_to_db_shopee_silver.csv'
	WITH (
		FIRSTROW = 2,
		FIELDTERMINATOR = ',',
		TABLOCK,
		CODEPAGE = 'ACP'
	);
END;

GO

DROP PROCEDURE silver.load_tiktok;
GO 
CREATE PROCEDURE silver.load_tiktok AS
BEGIN
	-- Insert data into tiktok_livestreaming table
	--TRUNCATE TABLE bronze.tiktok_livestreaming;
	BULK INSERT silver.tiktok_livestreaming
	FROM 'data/result/ready_to_db_tiktok.csv'
	WITH (
		FIRSTROW = 2,
		FIELDTERMINATOR = ',',
		TABLOCK
	);
END;
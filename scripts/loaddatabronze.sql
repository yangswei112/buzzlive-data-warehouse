-- Insert data into bronze schema tables

-- Insert data into brand_info table
BULK INSERT bronze.brand_info
FROM 'C:\Users\ASUS\Downloads\reporting\brand data\brand_table.csv'
WITH (
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
);

-- Insert data into shopee_livestreaming table
BULK INSERT bronze.shopee_livestreaming
FROM 'C:\Users\ASUS\Downloads\reporting\shopee seller center\supermarket_shopee_live.csv'
WITH (
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
);

BULK INSERT bronze.shopee_livestreaming
FROM 'C:\Users\ASUS\Downloads\reporting\shopee seller center\ortus_shopee.csv'
WITH (
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
);

-- Insert data into tiktok_livestreaming table
BULK INSERT bronze.tiktok_livestreaming
FROM 'C:\Users\ASUS\Downloads\reporting\tiktok seller center\ortus_tiktok_live_nov.csv'
WITH (
	FIRSTROW = 2,
	FIELDTERMINATOR = ',',
	TABLOCK
);


-- Check data
SELECT * FROM bronze.brand_info;
SELECT * FROM bronze.shopee_livestreaming;

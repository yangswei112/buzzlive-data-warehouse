-- Create table in bronze schema
USE BuzzliveWarehouse;
-- Create brand table
IF OBJECT_ID ('bronze.brand_info', 'U') IS NOT NULL
	DROP TABLE bronze.brand_info;
CREATE TABLE bronze.brand_info (
	brand_id NVARCHAR(50),
	brand_name NVARCHAR(50),
	platform NVARCHAR(50),
	category NVARCHAR(50)
);

-- Create host table
IF OBJECT_ID ('bronze.host_info', 'U') IS NOT NULL
	DROP TABLE bronze.host_info;
CREATE TABLE bronze.host_info (
	host_id NVARCHAR(50),
	host_name NVARCHAR(50),
	host_birthdate NVARCHAR(50)
);

-- Create shopee livestreaming table
IF OBJECT_ID ('bronze.shopee_livestreaming', 'U') IS NOT NULL
	DROP TABLE bronze.shopee_livestreaming;
CREATE TABLE bronze.shopee_livestreaming(
	DataPeriod NVARCHAR(50),
	UserId NVARCHAR(50),
	No INT,
	LivestreamName NVARCHAR(100),
	StartTime NVARCHAR(50),
	Duration NVARCHAR(50),
	EngagedViewers NVARCHAR(50),
	Comments NVARCHAR(50),
	ATC NVARCHAR(50),
	AvgViewingDuration NVARCHAR(50),
	Viewers NVARCHAR(50),
	Orders_PlacedOrder NVARCHAR(50),
	Orders_ConfirmedOrder NVARCHAR(50),
	ItemsSold_PlacedOrder NVARCHAR(50),
	ItemsSold_ConfirmedOrder NVARCHAR(50),
	Sales_PlacedOrder NVARCHAR(50),
	Sales_ConfirmedOrder NVARCHAR(50),
	live_host_id NVARCHAR(50), 
	live_start DATETIME2(0), 
	live_start_date DATE, 
	live_viewers INT
);

-- Create tiktok livestreaming table
IF OBJECT_ID ('bronze.tiktok_livestreaming', 'U') IS NOT NULL
	DROP TABLE bronze.tiktok_livestreaming;
CREATE TABLE bronze.tiktok_livestreaming(
	CreatorId NVARCHAR(50), 
	LivestreamCreator NVARCHAR(100),
	StartTime NVARCHAR(50), 
	Duration NVARCHAR(50), 
	live_direct_gmv FLOAT,
	OrdersPaidFor INT, 
	ItemsSold INT, 
	Customers INT, 
	live_avg_price FLOAT, 
	CTOR NVARCHAR(50),
	live_gross_revenue FLOAT, 
	Viewers INT, 
	Views INT, 
	AvgViewDuration FLOAT, 
	Comments INT,
	Shares INT, 
	Likes INT, 
	NewFollowers INT, 
	ProductImpressions INT,
	ProductClicks INT, 
	CTR NVARCHAR(50), 
	live_start_date DATE, 
	live_start_time TIME(0),
	live_duration FLOAT, 
	live_ctor FLOAT, 
	live_ctr FLOAT,
	Studio NVARCHAR(20)
);

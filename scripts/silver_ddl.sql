-- Create table in silver schema

-- Create brand table
IF OBJECT_ID ('silver.brand_info', 'U') IS NOT NULL
	DROP TABLE silver.brand_info;
CREATE TABLE silver.brand_info (
	brand_id NVARCHAR(50),
	brand_name NVARCHAR(50),
	platform NVARCHAR(50)
);

-- Create host table
IF OBJECT_ID ('silver.host_info', 'U') IS NOT NULL
	DROP TABLE silver.host_info;
CREATE TABLE silver.host_info (
	host_id NVARCHAR(50),
	host_name NVARCHAR(50),
	host_birthdate NVARCHAR(50)
);

-- Create shopee livestreaming table
IF OBJECT_ID ('silver.shopee_livestreaming', 'U') IS NOT NULL
	DROP TABLE silver.shopee_livestreaming;
CREATE TABLE silver.shopee_livestreaming(
	UserId INT,
	LivestreamName NVARCHAR(50),
	live_host_id NVARCHAR(50), 
	live_start DATETIME2, 
	live_start_date DATE, 
	live_start_time TIME,
	live_duration FLOAT, 
	live_engaged_viewers INT, 
	live_comments INT, 
	live_atc INT,
	live_viewers INT, 
	live_placed_orders INT, 
	live_confirmed_orders INT,
	live_placed_items_sold INT, 
	live_confirmed_items_sold INT,
	live_avg_viewing_duration FLOAT,
	live_placed_sales FLOAT,
	live_confirmed_sales FLOAT
);

-- Create tiktok livestreaming table
IF OBJECT_ID ('silver.tiktok_livestreaming', 'U') IS NOT NULL
	DROP TABLE silver.tiktok_livestreaming;
CREATE TABLE silver.tiktok_livestreaming(
	CreatorId NVARCHAR(50), 
	LivestreamCreator NVARCHAR(50), 
	live_direct_gmv FLOAT,
	OrdersPaidFor INT, 
	ItemsSold INT, 
	Customers INT, 
	live_avg_price FLOAT, 
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
	live_start_date DATE, 
	live_start_time TIME,
	live_duration FLOAT, 
	live_ctor FLOAT, 
	live_ctr FLOAT
);

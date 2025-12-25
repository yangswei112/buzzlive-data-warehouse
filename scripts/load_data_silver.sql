-- Insert data into silver table
USE BuzzliveWarehouse;
GO
CREATE PROCEDURE silver.load_info AS
BEGIN
	-- Insert data into brand_table
	TRUNCATE TABLE silver.brand_info;
	INSERT INTO silver.brand_info (
		brand_id,
		brand_name,
		platform)

	SELECT
	brand_id,
	brand_name,
	platform
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

CREATE PROCEDURE silver.load_shopee AS
BEGIN
	-- INSERT INTO SHOPEE_LIVESTREAMING
	TRUNCATE TABLE silver.shopee_livestreaming;
	INSERT INTO silver.shopee_livestreaming (
		UserId,
		LivestreamName,
		live_host_id, 
		live_start, 
		live_start_date, 
		live_start_time,
		live_duration, 
		live_engaged_viewers, 
		live_comments, 
		live_atc,
		live_viewers, 
		live_placed_orders, 
		live_confirmed_orders,
		live_placed_items_sold, 
		live_confirmed_items_sold,
		live_avg_viewing_duration,
		live_placed_sales,
		live_confirmed_sales
	)
	SELECT
		UserId,
		LivestreamName,
		live_host_id, 
		live_start, 
		live_start_date, 
		live_start_time,
		live_duration, 
		live_engaged_viewers, 
		live_comments, 
		live_atc,
		live_viewers, 
		live_placed_orders, 
		live_confirmed_orders,
		live_placed_items_sold, 
		live_confirmed_items_sold,
		live_avg_viewing_duration,
		live_placed_sales,
		live_confirmed_sales

	FROM bronze.shopee_livestreaming;
END;

GO

CREATE PROCEDURE silver.load_tiktok AS
BEGIN
	-- INSERT INTO TIKTOK_LIVESTREAMING
	TRUNCATE TABLE silver.tiktok_livestreaming;
	INSERT INTO silver.tiktok_livestreaming (
		CreatorId, 
		LivestreamCreator, 
		live_direct_gmv,
		OrdersPaidFor, 
		ItemsSold, 
		Customers, 
		live_avg_price, 
		live_gross_revenue, 
		Viewers, 
		Views, 
		AvgViewDuration, 
		Comments,
		Shares, 
		Likes, 
		NewFollowers, 
		ProductImpressions,
		ProductClicks,  
		live_start_date, 
		live_start_time,
		live_duration, 
		live_ctor, 
		live_ctr
	)
	SELECT
	CreatorId, 
		LivestreamCreator, 
		live_direct_gmv,
		OrdersPaidFor, 
		ItemsSold, 
		Customers, 
		live_avg_price, 
		live_gross_revenue, 
		Viewers, 
		Views, 
		AvgViewDuration, 
		Comments,
		Shares, 
		Likes, 
		NewFollowers, 
		ProductImpressions,
		ProductClicks,  
		live_start_date, 
		live_start_time,
		live_duration, 
		live_ctor, 
		live_ctr
	FROM bronze.tiktok_livestreaming;
END;

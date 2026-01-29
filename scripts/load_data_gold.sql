USE BuzzliveWarehouse;

-- CREATE VIEWS FOR WEEKLY REPORTING
CREATE VIEW gold.WeeklyShopeeLive AS
SELECT
sl.Studio,
bi.brand_name AS Brand,
sl.live_start_date AS Date,
sl.live_start_time As StartLive,
DATEADD(hour, ROUND(sl.live_duration/60,0), sl.live_start_time) AS EndLive,
CONVERT(VARCHAR(5), sl.live_start_time, 108) + ' ' + '-' + ' ' + CONVERT(VARCHAR(5), DATEADD(hour, ROUND(sl.live_duration/60,0), sl.live_start_time), 108) AS TimeLive,
ROUND(sl.live_duration/60,2) AS HourDuration,
sl.live_confirmed_sales AS Sales,
sl.live_confirmed_orders AS Orders,
sl.live_confirmed_items_sold AS ItemsSold,
sl.live_viewers AS Viewers,
sl.live_avg_viewing_duration AS StayDuration,
bi.platform as Platform,
hi.host_name AS Host
FROM silver.shopee_livestreaming sl
LEFT JOIN silver.brand_info bi
ON sl.UserId = bi.brand_id
LEFT JOIN silver.host_info hi
ON sl.live_host_id = hi.host_id;

CREATE VIEW gold.WeeklyTiktokLive AS
SELECT
tl.Studio AS Studio,
bi.brand_name AS Brand,
tl.live_start_date AS Date,
tl.live_start_time As StartLive,
DATEADD(hour, ROUND(tl.live_duration/60,0), tl.live_start_time) AS EndLive,
CONVERT(VARCHAR(5), tl.live_start_time, 108) + ' ' + '-' + ' ' + CONVERT(VARCHAR(5), DATEADD(hour, ROUND(tl.live_duration/60,0), tl.live_start_time), 108) AS TimeLive,
ROUND(tl.live_duration/60,2) AS HourDuration,
tl.live_direct_gmv AS Sales,
tl.OrdersPaidFor AS Orders,
tl.ItemsSold AS ItemsSold,
tl.Viewers AS Viewers,
tl.AvgViewDuration AS StayDuration,
bi.platform as Platform
FROM silver.tiktok_livestreaming tl
LEFT JOIN silver.brand_info bi
ON tl.CreatorId = bi.brand_id;

-- FOR HR
CREATE VIEW gold.ShopeeRawDataForHR AS
SELECT sl.LivestreamName, sl.StartTime, sl.Duration, sl.live_start_date, bi.brand_name, bi.platform 
FROM bronze.shopee_livestreaming sl
LEFT JOIN bronze.brand_info bi
ON sl.UserId = bi.brand_id;

CREATE VIEW gold.TiktokRawDataForHR AS
SELECT tl.LivestreamCreator, tl.StartTime, tl.Duration, tl.live_start_date, bi.brand_name, bi.platform 
FROM bronze.tiktok_livestreaming tl
LEFT JOIN bronze.brand_info bi
ON tl.CreatorId = bi.brand_id;

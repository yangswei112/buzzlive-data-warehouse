USE BuzzliveWarehouse;

-- LOAD NEW DATA
EXEC bronze.load_info;
EXEC bronze.load_tiktok;
EXEC bronze.load_shopee;
EXEC silver.load_info;
EXEC silver.load_tiktok;
EXEC silver.load_shopee;

-- FOR HR
SELECT * FROM gold.ShopeeRawDataForHR
WHERE live_start_date BETWEEN '2026-01-12' AND '2026-01-18';
SELECT * FROM gold.TiktokRawDataForHR
WHERE live_start_date BETWEEN '2026-01-12' AND '2026-01-18';

-- FOR SHOPEE WEEKLY REPORT
SELECT * FROM gold.WeeklyShopeeLive
WHERE Date BETWEEN '2025-12-25' AND '2025-12-31'
AND Studio = 'Klaten'
AND Brand = 'HOTTO'
ORDER BY Brand, Date, StartLive ASC;

-- FOR TIKTOK WEEKLY REPORT
SELECT * FROM gold.WeeklyTiktokLive
--WHERE bi.brand_name = 'Ortuseight'
WHERE Date BETWEEN '2026-01-12' AND '2026-01-18'
AND Studio = 'Klaten'
ORDER BY Brand, Date, StartLive ASC;
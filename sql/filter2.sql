USE BuzzliveWarehouse;

GO

-- TIKTOK LIVE
DROP PROCEDURE silver.filter_brand_tiktok2;
GO
CREATE PROCEDURE silver.filter_brand_tiktok2
-- SET PARAMETER
    @start_date DATE,
    @end_date DATE
AS
BEGIN
    SET NOCOUNT ON;
    PRINT 'FILTER TIKTOK LIVE STARTED'

    DECLARE @local_start DATE = @start_date;
    DECLARE @local_end DATE = @end_date;

    UPDATE t
    SET t.Studio = 'Klaten'
    FROM silver.tiktok_livestreaming t
    INNER JOIN silver.brand_info b
        ON t.CreatorId = b.brand_id
       AND b.platform = 'Tiktok'
    WHERE t.live_start_date BETWEEN @local_start AND @local_end;

    PRINT 'ALL TIKTOK BRANDS FILTERED';
END;

GO

-- SHOPEE LIVE
DROP PROCEDURE silver.filter_brand_shopee2;
GO
CREATE PROCEDURE silver.filter_brand_shopee2
-- SET PARAMETER
    @start_date DATE,
    @end_date DATE
AS
BEGIN
    SET NOCOUNT ON;
    PRINT 'FILTER SHOPEE LIVE STARTED'

    DECLARE @local_start DATE = @start_date;
    DECLARE @local_end DATE = @end_date;

    UPDATE s
    SET s.Studio = 'Klaten'
    FROM silver.shopee_livestreaming s
    INNER JOIN silver.brand_info b
        ON s.UserId = b.brand_id
       AND b.platform = 'Shopee'
    WHERE s.live_start_date BETWEEN @local_start AND @local_end;

    PRINT 'ALL SHOPEE BRANDS FILTERED';
END;
USE BuzzliveWarehouse;

GO

-- TIKTOK LIVE
DROP PROCEDURE silver.filter_brand_tiktok;
GO
CREATE PROCEDURE silver.filter_brand_tiktok
-- SET PARAMETER
    @start_date VARCHAR(10),
    @end_date VARCHAR(10)
AS
BEGIN
    SET NOCOUNT ON;
    PRINT 'FILTER TIKTOK LIVE STARTED'
    -- DELTOMED
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Deltomed' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'DELTOMED FILTERED'

    -- -- TATARUMA
    -- UPDATE silver.tiktok_livestreaming
    -- SET Studio = CASE 
    --     WHEN live_start_time BETWEEN '18:00:00' AND '22:59:00' THEN 'Klaten'
    --     ELSE 'Client' 
    -- END
    -- WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Tataruma' AND platform='Tiktok')
    -- AND live_start_date BETWEEN @start_date AND @end_date
    -- PRINT 'TATARUMA FILTERED'

    -- Ortuseight
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Ortuseight' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'ORTUSEIGHT FILTERED'

    -- Bloomlab
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Bloomlab' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'BLOOMLAB FILTERED'

    -- Beeme
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Beeme' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'BEEME FILTERED'

    -- Ona Indonesia
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Ona Indonesia' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'ONA INDONESIA FILTERED'

    -- Medikon
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Medikon' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'MEDIKON FILTERED'

    -- Samyang
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Samyang' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'SAMYANG FILTERED'

    -- Herbana
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Herbana' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'HERBANA FILTERED'

    -- Herbamojo
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Herbamojo' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'HERBAMOJO FILTERED'

END;

GO

-- SHOPEE LIVE
DROP PROCEDURE silver.filter_brand_shopee;
GO
CREATE PROCEDURE silver.filter_brand_shopee
-- SET PARAMETER
    @start_date VARCHAR(10),
    @end_date VARCHAR(10)
AS
BEGIN
    SET NOCOUNT ON;
    PRINT 'FILTER SHOPEE LIVE STARTED'
    -- DELTOMED
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Deltomed' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'DELTOMED FILTERED'

    -- -- TATARUMA
    -- UPDATE silver.shopee_livestreaming
    -- SET Studio = 'Klaten'
    -- WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Tataruma' AND platform='Shopee')
    -- AND live_start_date BETWEEN @start_date AND @end_date
    -- PRINT 'TATARUMA FILTERED'

    -- Ortuseight
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Ortuseight' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'ORTUSEIGHT FILTERED'

    -- Samyang
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Samyang' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'SAMYANG FILTERED'

    -- Heavenly Yogurt
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Heavenly Yogurt' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'HEAVENLY YOGURT FILTERED'

     -- Beeme
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Beeme' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'BEEME FILTERED'

     -- Ona Indonesia
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Ona Indonesia' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'ONA INDONESIA FILTERED'

    -- Herbana
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Herbana' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'HERBANA FILTERED'

    -- Herbamojo
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Herbamojo' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'HERBAMOJO FILTERED'

    -- reniafrianishop
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='reniafrianishop' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'RENIAFRIANISHOP FILTERED'

    -- URBANX
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='URBANX' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'URBANX FILTERED'

    -- IRISHLAB
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='IRISHLAB' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'IRISHLAB FILTERED'

    -- BASEUS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='BASEUS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'BASEUS FILTERED'

    -- KANBAI
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='KANBAI' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'KANBAI FILTERED'
END;
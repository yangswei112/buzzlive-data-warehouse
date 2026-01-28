USE BuzzliveWarehouse;

GO

-- TIKTOK LIVE
CREATE PROCEDURE silver.filter_brand_tiktok
-- SET PARAMETER
    @start_date VARCHAR(10),
    @end_date VARCHAR(10)
AS
BEGIN
    -- DELTOMED
    UPDATE silver.tiktok_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '10:00:00' AND '17:59:00' THEN 'Client'
        ELSE 'Klaten' 
    END
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Deltomed' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- TATARUMA
    UPDATE silver.tiktok_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '18:00:00' AND '22:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Tataruma' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- Ortuseight
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Ortuseight' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- Bloomlab
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Bloomlab' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- Beeme
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Beeme' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date

END;

GO

-- SHOPEE LIVE
CREATE PROCEDURE silver.filter_brand_shopee
-- SET PARAMETER
    @start_date VARCHAR(10),
    @end_date VARCHAR(10)
AS
BEGIN
    -- DELTOMED
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '10:00:00' AND '11:59:00' THEN 'Client'
        WHEN live_start_time BETWEEN '14:00:00' AND '15:59:00' THEN 'Client'
        ELSE 'Klaten' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Deltomed' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- TATARUMA
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '18:00:00' AND '21:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Tataruma' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- Ortuseight
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Ortuseight' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- Samyang
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Samyang Food Indonesia' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- Heavenly Yogurt
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Heavenly Yogurt' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- Juwara Pedas
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '11:00:00' AND '14:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Juwara Pedas' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- JIJONE
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='JIJONE' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- SEOLMI
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '07:00:00' AND '08:59:00' THEN 'Klaten'
        WHEN live_start_time BETWEEN '17:00:00' AND '18:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='SEOLMI' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- HOTTO
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '14:00:00' AND '17:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='HOTTO' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

     -- Beeme
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Beeme' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- reniafrianishop
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '06:00:00' AND '09:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='reniafrianishop' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- DPALTERS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='DPALTERS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- HASTI COLLECTIONS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='HASTI COLLECTIONS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- ANEBLESS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='ANEBLESS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- ADEBAH
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        --WHEN live_start_time < '16:00:00' THEN 'Klaten'
        WHEN live_start_time BETWEEN '06:00:00' AND '09:59:00' THEN 'Klaten'
        --WHEN live_start_time BETWEEN '14:00:00' AND '15:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='ADEBAH' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- URBANX
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='URBANX' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- ARMOURS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='ARMOURS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- IRISHLAB
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='IRISHLAB' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- KENZ17
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='KENZ17' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- CELCIUS OS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='CELCIUS OS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- QUEENSLAND OS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='QUEENSLAND OS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- MISSISSIPPI OS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='MISSISSIPPI OS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- MOMOCABAG
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='MOMOCABAG' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- ECHABUTIK
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='ECHABUTIK' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- SENSATIA BOTANICA
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='SENSATIA BOTANICA' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- chinlili108
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time < '10:00:00' THEN 'Klaten'
        --WHEN live_start_time BETWEEN '15:00:00' AND '16:59:00' THEN 'Klaten'
        --WHEN live_start_time BETWEEN '14:00:00' AND '15:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='chinlili108' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- tuah_slimbags
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '10:00:00' AND '13:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='tuah_slimbags')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- TOKOBIG
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time > '08:00:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='TOKOBIG')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- SONIX
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '20:00:00' AND '21:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='SONIX' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- LIVCHI
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '10:00:00' AND '11:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='LIVCHI' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- Abadi Logam
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Abadi Logam' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- DEMODE088
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='DEMODE088' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- ENESIS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='ENESIS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

    -- JUNICASE.ID
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='JUNICASE.ID' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date

END;
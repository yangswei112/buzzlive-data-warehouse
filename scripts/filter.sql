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
    PRINT 'FILTER TIKTOK LIVE STARTED'
    -- DELTOMED
    UPDATE silver.tiktok_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '07:00:00' AND '09:59:00' THEN 'Klaten'
        WHEN live_start_time BETWEEN '19:00:00' AND '22:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Deltomed' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'DELTOMED FILTERED'

    -- TATARUMA
    UPDATE silver.tiktok_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '18:00:00' AND '22:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Tataruma' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'TATARUMA FILTERED'

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
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '09:00:00' AND '17:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Medikon' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'MEDIKON FILTERED'

     -- Wund+
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Wund+' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'WUND+ FILTERED'

     -- Samyang
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Samyang' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'SAMYANG FILTERED'

     -- Everbest
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Everbest' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'EVERBEST FILTERED'

     -- Paffle
    UPDATE silver.tiktok_livestreaming
    SET Studio = 'Klaten'
    WHERE CreatorId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Paffle' AND platform='Tiktok')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'PAFFLE FILTERED'

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
    PRINT 'FILTER SHOPEE LIVE STARTED'
    -- DELTOMED
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '07:00:00' AND '09:59:00' THEN 'Klaten'
        WHEN live_start_time BETWEEN '12:00:00' AND '13:59:00' THEN 'Klaten'
        WHEN live_start_time BETWEEN '17:00:00' AND '22:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Deltomed' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'DELTOMED FILTERED'

    -- TATARUMA
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Tataruma' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'TATARUMA FILTERED'

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

    -- Juwara Pedas
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '11:00:00' AND '14:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Juwara Pedas' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'JUWARA PEDAS FILTERED'

    -- JIJONE
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='JIJONE' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'JIJONE FILTERED'

    -- SEOLMI
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '07:00:00' AND '08:59:00' THEN 'Klaten'
        WHEN live_start_time BETWEEN '17:00:00' AND '18:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='SEOLMI' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'SEOLMI FILTERED'

    -- HOTTO
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '14:00:00' AND '17:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='HOTTO' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'HOTTO FILTERED'

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

     -- Wund+
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Wund+' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'WUND+ FILTERED'

     -- PAFLE
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Pafle' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'PAFLE FILTERED'

    -- reniafrianishop
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='reniafrianishop' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'RENIAFRIANISHOP FILTERED'

    -- DPALTERS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='DPALTERS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'DPALTERS FILTERED'

    -- HASTI COLLECTIONS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='HASTI COLLECTIONS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'HASTI COLLECTIONS FILTERED'

    -- ANEBLESS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='ANEBLESS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'ANEBLESS FILTERED'

    -- ADEBAH
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        --WHEN live_start_time < '16:00:00' THEN 'Klaten'
        WHEN live_start_time BETWEEN '07:00:00' AND '13:59:00' THEN 'Klaten'
        --WHEN live_start_time BETWEEN '14:00:00' AND '15:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='ADEBAH' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'ADEBAH FILTERED'

    -- URBANX
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='URBANX' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'URBANX FILTERED'

    -- ARMOURS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='ARMOURS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'ARMOURS FILTERED'

    -- IRISHLAB
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='IRISHLAB' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'IRISHLAB FILTERED'

    -- KENZ17
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='KENZ17' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'KENZ17 FILTERED'

    -- CELCIUS OS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='CELCIUS OS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'CELCIUS OS FILTERED'

    -- QUEENSLAND OS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='QUEENSLAND OS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'QUEENSLAND OS FILTERED'

    -- MISSISSIPPI OS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='MISSISSIPPI OS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'MISSISSIPPI OS FILTERED'

    -- MOMOCABAG
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='MOMOCABAG' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'MOMOCABAG FILTERED'

    -- ECHABUTIK
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='ECHABUTIK' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'ECHABUTIK FILTERED'

    -- SENSATIA BOTANICA
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '10:00:00' AND '11:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='SENSATIA BOTANICA' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'SENSATIA BOTANICA FILTERED'

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
    PRINT 'CHINLILI108 FILTERED'

    -- tuah_slimbags
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '10:00:00' AND '13:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='tuah_slimbags')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'TUAH_SLIMBAGS FILTERED'

    -- TOKOBIG
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '18:00:00' AND '21:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='TOKOBIG')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'TOKOBIG FILTERED'

    -- SONIX
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '18:00:00' AND '19:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='SONIX' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'SONIX FILTERED'

    -- LIVCHI
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '10:00:00' AND '11:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='LIVCHI' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'LIVCHI FILTERED'

    -- Abadi Logam
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '20:00:00' AND '23:59:00' THEN 'Client'
        ELSE 'Klaten' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='Abadi Logam' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'ABADI LOGAM FILTERED'

    -- DEMODE088
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='DEMODE088' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'DEMODE088 FILTERED'

    -- ENESIS
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='ENESIS' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'ENESIS FILTERED'

    -- JUNICASE.ID
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='JUNICASE.ID' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'JUNICASE.ID FILTERED'

    -- VILEO
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='VILEOHANDICRAFT' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'VILEO FILTERED';

    -- WESTBRONCO
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='WESTBRONCO' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'WESTBRONCO FILTERED'

    -- SMITHMENSUPLAY
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='SMITHMENSUPPLY' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'SMITHMENSUPLAY FILTERED'

    -- MITRA10BAHANBANGUNAN
    UPDATE silver.shopee_livestreaming
    SET Studio = CASE 
        WHEN live_start_time BETWEEN '14:00:00' AND '19:59:00' THEN 'Klaten'
        ELSE 'Client' 
    END
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='MITRA10BAHANBANGUNAN' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'MITRA10BAHANBANGUNAN FILTERED'

    -- AOMIOFFICIAL
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='AOMIOFFICIAL' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'AOMIOFFICIAL FILTERED'

    -- LEARNING RESOURCES
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='LEARNING RESOURCES' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'LEARNING RESOURCES FILTERED'

    -- WELLENPRINT
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='WELLENPRINT' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'WELLENPRINT FILTERED'

    -- VIDYA OUTLET
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='VIDYA OUTLET' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'VIDYA OUTLET FILTERED'

    -- COROLLA.FASHION.ID
    UPDATE silver.shopee_livestreaming
    SET Studio ='Client'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='COROLLA.FASHION.ID' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'COROLLA.FASHION.ID FILTERED'

    -- ALKES
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='ALKES' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'ALKES FILTERED'

    -- BELLAGIO
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='BELLAGIO' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'BELLAGIO FILTERED'

    -- XITAO
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='XITAO' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'XITAO FILTERED'

    -- OOUWA
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='OOUWA' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'OOUWA FILTERED'

    -- SENSWELL
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='SENSWELL' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'SENSWELL FILTERED'

    -- HIRAKIYA
    UPDATE silver.shopee_livestreaming
    SET Studio = 'Klaten'
    WHERE UserId = (SELECT brand_id FROM silver.brand_info WHERE brand_name='HIRAKIYA' AND platform='Shopee')
    AND live_start_date BETWEEN @start_date AND @end_date
    PRINT 'HIRAKIYA FILTERED'
END;
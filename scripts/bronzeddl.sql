-- Create table in bronze schema

-- Create brand table
IF OBJECT_ID ('bronze.brand_info', 'U') IS NOT NULL
	DROP TABLE bronze.brand_info;
CREATE TABLE bronze.brand_info (
	brand_id NVARCHAR(50),
	brand_name NVARCHAR(50),
	platform NVARCHAR(50)
);

-- Create shopee livestreaming table
IF OBJECT_ID ('bronze.shopee_livestreaming', 'U') IS NOT NULL
	DROP TABLE bronze.shopee_livestreaming;
CREATE TABLE bronze.shopee_livestreaming(
	DataPeriod NVARCHAR(50),
	UserId INT,
	No INT,
	LivestreamName NVARCHAR(50),
	StartTime NVARCHAR(50),
	Duration NVARCHAR(50),
	EngagedViewers NVARCHAR(50),
	Comments NVARCHAR(50),
	ATC NVARCHAR(50),
	AvgViewingDuration NVARCHAR(50),
	Viewers NVARCHAR(50),
	OrdersPlacedOrder NVARCHAR(50),
	OrdersConfirmedOrder NVARCHAR(50),
	ItemsSoldPlacedOrder NVARCHAR(50),
	ItemsSoldConfirmedOrder NVARCHAR(50),
	SalesPlacedOrder NVARCHAR(50),
	SalesConfirmedOrder NVARCHAR(50)
);

-- Create tiktok livestreaming table
IF OBJECT_ID ('bronze.tiktok_livestreaming', 'U') IS NOT NULL
	DROP TABLE bronze.tiktok_livestreaming;
CREATE TABLE bronze.tiktok_livestreaming(
	IDKreator INT,
	Kreator NVARCHAR(50),
	Namapanggilan NVARCHAR(50),
	WaktuLive DATETIME,
	Durasi NVARCHAR(50),
	NilaibarangdaganganbrutoLIVERp INT,
	Produkyangditambahkan INT,
	ProdukTerjual INT,
	PesananSKUyangdibuat INT,
	PesananSKULIVE INT,
	ProdukyangterjualdariLIVE INT,
	Pembeli INT,
	HargaRataRataRp INT,
	RasiopesananperklikLIVE NVARCHAR(50),
	GMVyangdidapatdariLIVERp INT,
	Penonton INT,
	LiveStreamDilihat INT,
	DurasimenontonratarataSiaranLIVE INT,
	Komentar INT,
	LiveDibagikan INT,
	SukapadaLIVE INT,
	PengikutbaruVideokreator INT,
	ProdukDilihat INT,
	KlikProduk INT,
	CTR NVARCHAR(50)
);

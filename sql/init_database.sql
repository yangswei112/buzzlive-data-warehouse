
USE master;
GO
-- Drop and recreate Database 'BuzzliveWarehouse'
IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'BuzzliveWarehouse')
BEGIN
  ALTER DATABASE BuzzliveWarehouse SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
  DROP DATABASE BuzzliveWarehouse
END;
GO
  
-- Create Database 'BuzzliveWarehouse'
CREATE DATABASE BuzzliveWarehouse;
GO
  
USE BuzzliveWarehouse;
GO

-- Create Schema
CREATE SCHEMA bronze;
GO
CREATE SCHEMA silver;
GO
CREATE SCHEMA gold;

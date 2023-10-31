## HW 1 Install & Setup - ELT
## Create Python VENV 
    ##python3 -m venv env; 
    ##env/scripts/activate;
    ##python -m pip install -r requirements.txt;

##Windows PowerShell Install & S3 Download
    ##Copyright (C) Microsoft Corporation. All rights reserved.
    ##Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

## AWSCLI Download 
    ##PS C:\Users\KaiES> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
    ##PS C:\Users\KaiES> aws --version
    ##aws-cli/2.13.30 Python/3.11.6 Windows/10 exe/AMD64 prompt/off
    ##PS C:\Users\KaiES> aws configure
    ##AWS Access Key ID [None]: AKIA2CI5DHS4DG2ZAHUM
    ##AWS Secret Access Key [None]: [Added]
    ##Default region name [None]: us-east-1
    ##Default output format [None]: json
    ##PS C:\Users\KaiES> aws help

    #PS C:\Users\KaiES> aws s3 sync s3://cmu-95797-23m2 Downloads

    #PS C:\Users\KaiES>  aws s3 sync s3://cmu-95797-23m2 Downloads
    #warning: Skipping file C:\Users\KaiES\Downloads\~$be7ce31f-5a1e-4eb3-b2ef-b206bd9fcd6c.xlsx. File/Directory is not readable.
    ##download: s3://cmu-95797-23m2/data/nyct2010_15b/nyct2010.shp.xml to Downloads\data\nyct2010_15b\nyct2010.shp.xml
    ##download: s3://cmu-95797-23m2/data/nyct2010_15b/nyct2010.prj to Downloads\data\nyct2010_15b\nyct2010.prj
    ##download: s3://cmu-95797-23m2/data/central_park_weather.csv to Downloads\data\central_park_weather.csv
    ##download: s3://cmu-95797-23m2/data/nyct2010_15b/nyct2010.dbf to Downloads\data\nyct2010_15b\nyct2010.dbf
    ##download: s3://cmu-95797-23m2/data/nyct2010_15b/nyct2010.shp to Downloads\data\nyct2010_15b\nyct2010.shp
    ##download: s3://cmu-95797-23m2/data/nyct2010_15b/nyct2010.shx to Downloads\data\nyct2010_15b\nyct2010.shx
    ##download: s3://cmu-95797-23m2/data/taxi/green_tripdata.parquet to Downloads\data\taxi\green_tripdata.parquet
    ##download: s3://cmu-95797-23m2/data/taxi_zones/taxi_zones.dbf to Downloads\data\taxi_zones\taxi_zones.dbf
    ##download: s3://cmu-95797-23m2/data/taxi_zones/taxi_zones.prj to Downloads\data\taxi_zones\taxi_zones.prj
    ##download: s3://cmu-95797-23m2/data/taxi/fhv_tripdata.parquet to Downloads\data\taxi\fhv_tripdata.parquet
    ##download: s3://cmu-95797-23m2/data/taxi_zones/taxi_zones.sbx to Downloads\data\taxi_zones\taxi_zones.sbx
    ##download: s3://cmu-95797-23m2/data/taxi_zones/taxi_zones.sbn to Downloads\data\taxi_zones\taxi_zones.sbn
    ##download: s3://cmu-95797-23m2/data/taxi_zones/taxi_zones.shp.xml to Downloads\data\taxi_zones\taxi_zones.shp.xml
    ##download: s3://cmu-95797-23m2/data/citibike-tripdata.csv.gz to Downloads\data\citibike-tripdata.csv.gz
    ##download: s3://cmu-95797-23m2/data/taxi_zones/taxi_zones.shx to Downloads\data\taxi_zones\taxi_zones.shx
    ##download: s3://cmu-95797-23m2/index.html to Downloads\index.html
    ##download: s3://cmu-95797-23m2/data/taxi_zones/taxi_zones.shp to Downloads\data\taxi_zones\taxi_zones.shp
    ##download: s3://cmu-95797-23m2/data/taxi/yellow_tripdata.parquet to Downloads\data\taxi\yellow_tripdata.parquet
    ##download: s3://cmu-95797-23m2/data/taxi/fhvhv_tripdata.parquet to Downloads\data\taxi\fhvhv_tripdata.parquet
 ## Code Adapted from https://robust-dinosaur-2ef.notion.site/DuckDB-Tutorial-Getting-started-for-beginners-b80bf0de8d6142d6979e78e59ffbbefe



import duckdb 

##Import S3 Data 
##Individual Files

##CSV Files - Code Adapted from https://duckdb.org/docs/data/multiple_files/overview.html
SELECT * FROM read_csv_auto('C:\Users\KaiES\Downloads\data\fhv_bases.csv');
SELECT *SELECT * FROM read_csv_auto('C:\Users\KaiES\Downloads\data\central_park_weather.csv');

## Compressed GZip Files - Code Adapted from https://duckdb.org/docs/data/overview.html
SELECT * FROM read_csv_auto('C:\Users\KaiES\Downloads\data\citibike-tripdata.csv.gz');

##  Parquet Files - Code Adapted from https://duckdb.org/docs/data/overview.html
SELECT * FROM read_parquet('C:\Users\KaiES\Downloads\data\taxi\green_tripdata.parquet');
SELECT * FROM read_parquet('C:\Users\KaiES\Downloads\data\taxi\fhv_tripdata.parquet');
SELECT * FROM read_parquet('C:\Users\KaiES\Downloads\data\taxi\fhvhv_tripdata.parquet');
SELECT * FROM read_parquet('C:\Users\KaiES\Downloads\data\taxi\yellow_tripdata.parquet');

## Count Rows _ Code Addapted from CHatGBT
SELECT COUNT(*) FROM 'C:\Users\KaiES\Downloads\data\fhv_bases.csv';
SELECT COUNT(*) FROM 'C:\Users\KaiES\Downloads\data\central_park_weather.csv';
SELECT COUNT(*) FROM 'C:\Users\KaiES\Downloads\data\citibike-tripdata.csv.gz';
SELECT COUNT(*) FROM 'C:\Users\KaiES\Downloads\data\taxi\green_tripdata.parquet';
SELECT COUNT(*) FROM 'C:\Users\KaiES\Downloads\data\taxi\fhv_tripdata.parquet';
SELECT COUNT(*) FROM 'C:\Users\KaiES\Downloads\data\taxi\fhvhv_tripdata.parquet';
SELECT COUNT(*) FROM 'C:\Users\KaiES\Downloads\data\taxi\yellow_tripdata.parquet';


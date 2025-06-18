# F1 Racing Analytics Project

**Author:** Ida Bagus Gede Purwa Manik Adiputra

## Overview

This project is a comprehensive Formula 1 racing data analytics platform built on Azure Databricks. It demonstrates end-to-end data engineering and analytics workflows, from raw data ingestion to business intelligence reporting using F1 racing data from the Ergast API.

## Architecture

The project follows a medallion architecture pattern:
- **Bronze Layer (Raw):** Raw data ingestion from various file formats
- **Silver Layer (Processed):** Cleaned and transformed data
- **Gold Layer (Presentation):** Business-ready aggregated data

## Technologies Used

- **Azure Databricks** - Primary data processing platform
- **PySpark** - Data processing and transformation
- **Delta Lake** - Data storage format for ACID transactions
- **Azure Data Lake Storage (ADLS)** - Cloud storage
- **SQL** - Data querying and analysis
- **Power BI** - Business intelligence and visualization
- **Azure Pipelines** - Workflow orchestration

## Project Structure

```
F1/
├── analysis/                    # SQL analysis queries
│   ├── find_dominant_drivers.sql
│   ├── find_dominant_teams.sql
│   ├── viz_dominant_drivers.sql
│   └── viz_dominant_teams.sql
├── demo/                        # Learning and demonstration notebooks
│   ├── aggregation_demo.py
│   ├── delta_lake_demo.py
│   ├── filter_demo.py
│   ├── join_demo.py
│   └── sql_*.sql
├── includes/                    # Common utilities and configurations
│   ├── common_functions.py
│   └── configuration.py
├── ingestion/                   # Data ingestion notebooks
│   ├── ingest_circuits_file.py
│   ├── ingest_constructors_file.py
│   ├── ingest_drivers_file.py
│   ├── ingest_lap_times_file.py
│   ├── ingest_pit_stops_file.py
│   ├── ingest_qualifying_file.py
│   ├── ingest_races_file.py
│   ├── ingest_results_file.py
│   └── ingest_all_files.py
├── raw/                         # Raw data table definitions
│   └── create_raw_tables.sql
├── setup/                       # Azure configuration notebooks
│   ├── access_adls_access_keys.py
│   ├── access_adls_cluster_scoped.py
│   ├── access_adls_sas_token.py
│   └── access_adls_service_principal.py
├── transformation/              # Data transformation notebooks
│   ├── calculated_race_results.py
│   ├── constructor_standings.py
│   ├── driver_standings.py
│   └── race_results.py
└── utils/                       # Utility functions
    └── prepare_for_incremental_load.sql
Pipelines/
└── f1_ingestion.yaml           # Azure Databricks workflow
raw data/                       # Source data files
├── circuits.csv
├── constructors.json
├── drivers.json
├── pit_stops.json
├── races.csv
├── results.json
├── lap_times/
│   ├── lap_times_split_1.csv
│   ├── lap_times_split_2.csv
│   ├── lap_times_split_3.csv
│   ├── lap_times_split_4.csv
│   └── lap_times_split_5.csv
└── qualifying/
    ├── qualifying_split_1.json
    └── qualifying_split_2.json
Reports/
└── F1 Dashboard.pbix           # Power BI dashboard
```

## Features

### Data Ingestion
- **Multi-format Support:** Handles CSV, JSON, and multi-line JSON files
- **Schema Enforcement:** Predefined schemas for data quality
- **Incremental Loading:** Delta Lake merge operations for efficient updates
- **Error Handling:** Robust error handling and data validation

### Data Processing
- **Column Standardization:** Consistent naming conventions (snake_case)
- **Data Enrichment:** Addition of metadata columns (ingestion_date, data_source, file_date)
- **Deduplication:** Removes duplicate records based on business keys
- **Data Quality:** Drops unwanted columns and validates data integrity

### Analytics & Transformations
- **Race Results:** Comprehensive race outcome analysis
- **Driver Standings:** Season-by-season driver performance metrics
- **Constructor Standings:** Team performance and championship standings
- **Dominant Analysis:** Identification of dominant drivers and teams across seasons

### Key Data Entities

1. **Circuits** - F1 racing circuits information
2. **Constructors** - Racing teams/manufacturers
3. **Drivers** - Driver profiles and details
4. **Races** - Race events and schedules
5. **Results** - Race outcomes and positions
6. **Qualifying** - Qualifying session results
7. **Pit Stops** - Pit stop timing data
8. **Lap Times** - Individual lap performance data

## Setup Instructions

### Prerequisites
- Azure Databricks workspace
- Azure Data Lake Storage account
- Power BI (optional, for reporting)

### Configuration
1. Set up Azure Data Lake Storage access using one of the authentication methods in `F1/setup/`
2. Configure the workspace secrets for secure access
3. Update the configuration file with your storage paths

### Deployment
1. Import all notebooks into your Databricks workspace
2. Run the setup notebooks to configure data lake access
3. Execute the ingestion pipeline using `F1/ingestion/ingest_all_files.py`
4. Run transformation notebooks to create presentation layer data

## Usage

### Manual Execution
Run notebooks in the following order:
1. Setup and configuration
2. Raw table creation (`F1/raw/create_raw_tables.sql`)
3. Data ingestion (`F1/ingestion/ingest_all_files.py`)
4. Data transformation (`F1/transformation/`)
5. Analysis queries (`F1/analysis/`)

### Automated Execution
Use the Azure Databricks pipeline defined in `Pipelines/f1_ingestion.yaml` for automated workflow execution.

## Key Functions

### Common Functions (`F1/includes/common_functions.py`)
- `add_ingestion_date` - Adds timestamp for data lineage
- `rearrange_partition_column` - Optimizes data partitioning
- `overwrite_partition` - Efficient partition updates
- `df_column_to_list` - Column value extraction

## Data Sources

The project uses Formula 1 data from the Ergast Developer API, including:
- Historical race data
- Driver and constructor information
- Circuit details
- Race results and standings
- Timing data (lap times, pit stops, qualifying)

## Business Intelligence

The project includes a Power BI dashboard (`Reports/F1 Dashboard.pbix`) that provides:
- Race results visualization
- Driver and constructor performance trends
- Historical championship analysis
- Circuit-specific analytics

## Contributing

1. Follow the established naming conventions
2. Ensure all notebooks include proper documentation
3. Test data transformations with sample datasets
4. Update this README when adding new features

## License

This project is for educational and demonstration purposes.

---

*This project demonstrates modern data engineering practices using Azure cloud services and showcases the power of Databricks for large-scale data processing and analytics.*

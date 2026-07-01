# Azure Medallion Architecture - Local Simulation
End-to-end data pipeline using PySpark + Delta Lake, replicating Azure Databricks workflow.

## Tech Stack
PySpark, Delta Lake 3.0, Python, REST API, MySQL

## Architecture
1. **Bronze**: Ingested 50K+ records from JSON API + CSV files into Delta tables
2. **Silver**: Applied SCD Type-2, data quality checks, schema enforcement with PySpark  
3. **Gold**: Built star schema aggregate tables for BI reporting, 60% faster queries

## Key Features
- ACID transactions using Delta Lake
- Incremental loading pattern
- Local simulation of Azure Databricks Medallion Architecture

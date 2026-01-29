# Slooze Data Engineering 

## Overview
This project demonstrates an end-to-end data engineering workflow including
data collection, ETL, and exploratory data analysis on B2B marketplace data.

## Part A – Data Collection
- Target platform: IndiaMART
- Category: Industrial Machinery
- Approach: Custom HTTP-based crawler using Requests and BeautifulSoup
- Features:
  - Modular crawler design
  - Polite rate-limiting
  - Structured CSV output

### Data Collection Note
IndiaMART uses dynamic content loading and bot protection mechanisms.
As a result, direct HTTP scraping may return limited data.
To demonstrate the complete pipeline, a representative sample dataset
was used for ETL and EDA.

## Part B – Exploratory Data Analysis
- Data cleaning and normalization
- Supplier location analysis
- Price distribution analysis
- Identification of missing and inconsistent fields

## Key Insights
- Supplier concentration in major industrial hubs (Delhi, Mumbai, Ahmedabad)
- Many listings lack transparent pricing
- Products cluster in low-to-mid price ranges
- Suppliers frequently list multiple similar products

## How to Run
```bash
pip install -r requirements.txt
python crawler/main.py

jupyter notebook eda/analysis.ipynb

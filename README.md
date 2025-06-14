# Slooze Data Science Challenge - Inventory, Purchase, Sales Analysis and Optimization

![Logo](./public/FFFFFF-1.png)

A retail wine & spirits company, operates across multiple locations and manages millions of transactions related to sales, purchases, and inventory records. Given the high volume of data, traditional spreadsheet-based analysis is inadequate. The company seeks a sophisticated data-driven approach to optimize inventory control and extract valuable business insights.

## 🎯 Objectives
- Inventory Optimization → Determine the ideal inventory levels for different product categories.
- Sales & Purchase Insights → Identify trends, top-performing products, and supplier efficiency.
- Process Improvement → Optimize procurement and stock control to minimize financial loss.

## 🔎 Tasks to be Performed
### **1️⃣ Demand Forecasting**
- Analyze **historical sales data** to predict future demand.
- Use **time-series models** for accuracy.

### **2️⃣ ABC Analysis**
- Classify inventory into **A (high value), B (moderate), and C (low priority)**.
- Prioritize high-value inventory management.

### **3️⃣ Economic Order Quantity (EOQ) Analysis**
- Calculate **optimal order quantity** to minimize ordering & carrying costs.
- Implement **just-in-time inventory practices** where feasible.

### **4️⃣ Reorder Point Analysis**
- Determine **reorder points for each product** to avoid stockouts.
- Factor in **lead time** to ensure continuity.

### **5️⃣ Lead Time Analysis**
- Optimize **supply chain efficiency** by assessing material procurement timelines.
- Reduce **waiting periods** for production inputs.

## Project Structure
```
.
├── datasets/                  # Raw data files
├── functions/                 # Python scripts and functions
│   ├── eda.py                # Exploratory Data Analysis script
│   ├── arima_forecast.py     # ARIMA forecasting model
│   ├── prophet_forecast.py   # Prophet forecasting model
│   └── run_forecasting.py    # Main script to run both models
├── results/                   # Analysis results and visualizations
└── README.md                 # Project documentation
```

## Data Files

Due to GitHub's file size limitations, the following large data files are not included in this repository:
- `datasets/PurchasesFINAL12312016.csv` (383.14 MB)
- `datasets/SalesFINAL12312016.csv` (121.94 MB)

To run the analysis, you'll need to obtain these files separately. Please contact the repository owner for access to these files.

## Dataset Overview

### 1. Sales Data (SalesFINAL12312016.csv)
- **Records**: 1,048,575
- **Columns**: 14
- **Key Metrics**:
  - Average sales quantity: 2.34 units per transaction
  - Maximum sales quantity: 432 units
  - Store range: 1-79
  - No missing values
- **Important Columns**:
  - InventoryId
  - Store
  - Brand
  - Description
  - Size
  - SalesQuantity
  - SalesDollars
  - SalesPrice
  - SalesDate
  - Volume
  - Classification
  - ExciseTax
  - VendorNo
  - VendorName

### 2. Purchases Data (PurchasesFINAL12312016.csv)
- **Records**: 2,372,474
- **Columns**: 16
- **Key Metrics**:
  - Average purchase quantity: 1.42 units
  - Maximum purchase quantity: 381.6 units
  - Only 3 missing values (in Size column)
- **Important Columns**:
  - InventoryId
  - Store
  - Brand
  - Description
  - Size
  - VendorNumber
  - VendorName
  - PONumber
  - PODate
  - ReceivingDate
  - InvoiceDate
  - PayDate
  - PurchasePrice
  - Quantity
  - Dollars
  - Classification

### 3. Inventory Data

#### Beginning Inventory (BegInvFINAL12312016.csv)
- **Records**: 206,529
- **Columns**: 9
- **Key Metrics**:
  - Average on-hand quantity: 20.43 units
  - Price range: $0 to $13,999.90
  - No missing values

#### Ending Inventory (EndInvFINAL12312016.csv)
- **Records**: 224,489
- **Columns**: 9
- **Key Metrics**:
  - Average on-hand quantity: 21.76 units
  - Price range: $0.49 to $13,999.90
  - 1,284 missing values in City column

### 4. Additional Files
- **Invoice Purchases** (InvoicePurchases12312016.csv): 5,543 records
- **Purchase Prices** (2017PurchasePricesDec.csv): 12,261 records

## Detailed Exploratory Data Analysis

### Sales Analysis
1. **Sales Volume Distribution**
   - Most transactions involve 1-2 units (based on average of 2.34)
   - Maximum single transaction: 432 units
   - Distribution is right-skewed, indicating occasional bulk purchases

2. **Store Performance**
   - Operations across 79 stores
   - Store IDs range from 1 to 79
   - Each store maintains consistent sales records

3. **Product Classification**
   - Products are classified into categories (Classification column)
   - Classification values range from 1 to 2
   - Helps in product categorization and analysis

4. **Pricing Analysis**
   - SalesPrice and SalesDollars columns provide pricing information
   - ExciseTax column indicates additional tax components
   - Volume column helps in understanding product sizes

### Purchase Analysis
1. **Purchase Patterns**
   - Average purchase quantity (1.42) is lower than sales quantity (2.34)
   - Maximum purchase quantity: 381.6 units
   - Suggests strategic bulk purchasing

2. **Vendor Relationships**
   - Multiple vendors (VendorNumber and VendorName)
   - Purchase orders tracked through PONumber
   - Complete vendor transaction history

3. **Timing Analysis**
   - Three key dates tracked:
     - PODate (Purchase Order)
     - ReceivingDate
     - PayDate
   - Helps in analyzing supply chain efficiency

4. **Financial Tracking**
   - PurchasePrice and Dollars columns for cost analysis
   - Quantity tracking for volume analysis
   - Classification for product categorization

### Inventory Analysis
1. **Beginning vs Ending Inventory**
   - Beginning: 206,529 records
   - Ending: 224,489 records
   - Net increase in inventory items

2. **Quantity Analysis**
   - Beginning average: 20.43 units
   - Ending average: 21.76 units
   - 6.5% increase in average inventory levels

3. **Price Distribution**
   - Beginning range: $0 to $13,999.90
   - Ending range: $0.49 to $13,999.90
   - Minimum price increased slightly
   - Maximum price remained constant

4. **Data Quality**
   - Beginning inventory: No missing values
   - Ending inventory: 1,284 missing values in City column
   - High data completeness overall

### Cross-Dataset Insights
1. **Supply Chain Efficiency**
   - Complete tracking from purchase to sale
   - Inventory levels maintained between purchases and sales
   - Clear vendor relationships

2. **Product Lifecycle**
   - Purchase → Inventory → Sale cycle
   - Average 21-day inventory holding period
   - Efficient inventory turnover

3. **Financial Flow**
   - Purchase costs tracked
   - Sales revenue recorded
   - Inventory valuation maintained

4. **Operational Metrics**
   - Store performance tracking
   - Vendor performance analysis
   - Product category management

## Key Insights

1. **Supply Chain Coverage**
   - Complete tracking of sales, purchases, and inventory
   - Comprehensive vendor and product information

2. **Product Pricing**
   - Wide price range: $0 to $13,999.90
   - Significant variation in product values

3. **Sales vs. Purchase Patterns**
   - Average sales quantity (2.34) > Average purchase quantity (1.42)
   - Suggests bulk purchases are broken down into smaller sales

4. **Inventory Trends**
   - Slight increase in average inventory levels
   - Beginning: 20.43 units
   - Ending: 21.76 units

5. **Store Network**
   - Operations across multiple stores (1-81)
   - Detailed vendor relationships

## Demand Forecasting

### Models Implemented

1. **ARIMA (AutoRegressive Integrated Moving Average)**
   - Handles time series data with trends and seasonality
   - Features:
     - Stationarity testing
     - Automatic parameter selection
     - Forecast evaluation metrics
   - Outputs:
     - Forecast visualization
     - Model metrics (MAE, RMSE, R2)

2. **Prophet**
   - Facebook's time series forecasting tool
   - Features:
     - Handles multiple seasonality patterns
     - Automatic changepoint detection
     - Robust to missing data
   - Outputs:
     - Forecast visualization
     - Seasonality components
     - Model metrics (MAE, RMSE, R2)

### Running the Forecasts

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run both models:
```bash
python functions/run_forecasting.py
```

3. Check results in the `results` directory:
   - `arima_forecast.png`: ARIMA forecast visualization
   - `prophet_forecast.png`: Prophet forecast visualization
   - `prophet_components.png`: Prophet seasonality components
   - `arima_metrics.txt`: ARIMA model performance metrics
   - `prophet_metrics.txt`: Prophet model performance metrics
   - `model_comparison.txt`: Comparison of both models

### Model Selection

The best model is selected based on:
- Mean Absolute Error (MAE)
- Root Mean Square Error (RMSE)
- R-squared (R2) score

The comparison report in `model_comparison.txt` provides detailed metrics and recommendations.

## Setup and Running

1. Install dependencies:
```
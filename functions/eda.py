import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn')
sns.set_palette("husl")

def load_data():
    """Load all CSV files from the datasets folder"""
    print("Loading datasets...")
    
    # Load Sales data
    sales_df = pd.read_csv('datasets/SalesFINAL12312016.csv')
    print("\nSales Data Shape:", sales_df.shape)
    
    # Load Purchases data
    purchases_df = pd.read_csv('datasets/PurchasesFINAL12312016.csv')
    print("Purchases Data Shape:", purchases_df.shape)
    
    # Load Inventory data
    beg_inv_df = pd.read_csv('datasets/BegInvFINAL12312016.csv')
    end_inv_df = pd.read_csv('datasets/EndInvFINAL12312016.csv')
    print("Beginning Inventory Shape:", beg_inv_df.shape)
    print("Ending Inventory Shape:", end_inv_df.shape)
    
    # Load Invoice Purchases data
    invoice_purchases_df = pd.read_csv('datasets/InvoicePurchases12312016.csv')
    print("Invoice Purchases Shape:", invoice_purchases_df.shape)
    
    # Load Purchase Prices data
    purchase_prices_df = pd.read_csv('datasets/2017PurchasePricesDec.csv')
    print("Purchase Prices Shape:", purchase_prices_df.shape)
    
    return sales_df, purchases_df, beg_inv_df, end_inv_df, invoice_purchases_df, purchase_prices_df

def analyze_sales(sales_df):
    """Analyze sales data"""
    print("\n=== Sales Analysis ===")
    
    # Basic statistics
    print("\nBasic Statistics:")
    print(sales_df.describe())
    
    # Check for missing values
    print("\nMissing Values:")
    print(sales_df.isnull().sum())
    
    # Display column information
    print("\nColumn Information:")
    print(sales_df.info())

def analyze_purchases(purchases_df):
    """Analyze purchases data"""
    print("\n=== Purchases Analysis ===")
    
    # Basic statistics
    print("\nBasic Statistics:")
    print(purchases_df.describe())
    
    # Check for missing values
    print("\nMissing Values:")
    print(purchases_df.isnull().sum())
    
    # Display column information
    print("\nColumn Information:")
    print(purchases_df.info())

def analyze_inventory(beg_inv_df, end_inv_df):
    """Analyze inventory data"""
    print("\n=== Inventory Analysis ===")
    
    # Basic statistics for beginning inventory
    print("\nBeginning Inventory Statistics:")
    print(beg_inv_df.describe())
    
    # Basic statistics for ending inventory
    print("\nEnding Inventory Statistics:")
    print(end_inv_df.describe())
    
    # Check for missing values
    print("\nMissing Values in Beginning Inventory:")
    print(beg_inv_df.isnull().sum())
    print("\nMissing Values in Ending Inventory:")
    print(end_inv_df.isnull().sum())

def main():
    # Load all datasets
    sales_df, purchases_df, beg_inv_df, end_inv_df, invoice_purchases_df, purchase_prices_df = load_data()
    
    # Perform analysis on each dataset
    analyze_sales(sales_df)
    analyze_purchases(purchases_df)
    analyze_inventory(beg_inv_df, end_inv_df)

if __name__ == "__main__":
    main() 
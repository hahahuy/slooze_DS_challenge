import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def prepare_sales_data(sales_df):
    """
    Prepare sales data for time series analysis
    """
    # Convert SalesDate to datetime
    sales_df['SalesDate'] = pd.to_datetime(sales_df['SalesDate'])
    
    # Aggregate daily sales
    daily_sales = sales_df.groupby('SalesDate')['SalesQuantity'].sum().reset_index()
    daily_sales.set_index('SalesDate', inplace=True)
    
    return daily_sales

def check_stationarity(timeseries):
    """
    Check stationarity of time series using Augmented Dickey-Fuller test
    """
    result = adfuller(timeseries)
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical values:', result[4])
    
    return result[1] < 0.05  # Return True if stationary

def train_arima_model(data, order=(1,1,1)):
    """
    Train ARIMA model
    """
    model = ARIMA(data, order=order)
    model_fit = model.fit()
    return model_fit

def forecast_arima(model, steps=30):
    """
    Generate forecast using ARIMA model
    """
    forecast = model.forecast(steps=steps)
    return forecast

def plot_forecast(historical_data, forecast, title="ARIMA Forecast"):
    """
    Plot historical data and forecast
    """
    plt.figure(figsize=(12, 6))
    plt.plot(historical_data.index, historical_data.values, label='Historical')
    plt.plot(pd.date_range(start=historical_data.index[-1], periods=len(forecast)+1, freq='D')[1:],
             forecast, label='Forecast', color='red')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Sales Quantity')
    plt.legend()
    plt.grid(True)
    
    # Save plot
    plt.savefig('results/arima_forecast.png')
    plt.close()

def evaluate_forecast(actual, predicted):
    """
    Evaluate forecast accuracy using common metrics
    """
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    r2 = r2_score(actual, predicted)
    
    return {
        'MAE': mae,
        'RMSE': rmse,
        'R2': r2
    }

def main():
    # Load sales data
    sales_df = pd.read_csv('datasets/SalesFINAL12312016.csv')
    
    # Prepare data
    daily_sales = prepare_sales_data(sales_df)
    
    # Check stationarity
    is_stationary = check_stationarity(daily_sales['SalesQuantity'])
    print(f"\nIs the time series stationary? {is_stationary}")
    
    # Split data into train and test
    train_size = int(len(daily_sales) * 0.8)
    train_data = daily_sales[:train_size]
    test_data = daily_sales[train_size:]
    
    # Train ARIMA model
    model = train_arima_model(train_data['SalesQuantity'])
    
    # Generate forecast
    forecast = forecast_arima(model, steps=len(test_data))
    
    # Plot results
    plot_forecast(daily_sales['SalesQuantity'], forecast)
    
    # Evaluate model
    metrics = evaluate_forecast(test_data['SalesQuantity'], forecast)
    print("\nForecast Evaluation Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")
    
    # Save metrics to file
    with open('results/arima_metrics.txt', 'w') as f:
        f.write("ARIMA Model Evaluation Metrics:\n")
        for metric, value in metrics.items():
            f.write(f"{metric}: {value:.4f}\n")

if __name__ == "__main__":
    main() 
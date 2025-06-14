import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def prepare_sales_data(sales_df):
    """
    Prepare sales data for Prophet analysis
    """
    # Convert SalesDate to datetime
    sales_df['SalesDate'] = pd.to_datetime(sales_df['SalesDate'])
    
    # Aggregate daily sales
    daily_sales = sales_df.groupby('SalesDate')['SalesQuantity'].sum().reset_index()
    
    # Rename columns for Prophet
    daily_sales.columns = ['ds', 'y']
    
    return daily_sales

def train_prophet_model(data, seasonality_mode='multiplicative'):
    """
    Train Prophet model
    """
    model = Prophet(
        seasonality_mode=seasonality_mode,
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=True
    )
    
    # Add additional regressors if needed
    # model.add_regressor('additional_feature')
    
    model.fit(data)
    return model

def generate_forecast(model, periods=30):
    """
    Generate forecast using Prophet model
    """
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

def plot_prophet_forecast(model, forecast, title="Prophet Forecast"):
    """
    Plot Prophet forecast components
    """
    # Plot the forecast
    fig1 = model.plot(forecast)
    plt.title(title)
    plt.savefig('results/prophet_forecast.png')
    plt.close()
    
    # Plot the components
    fig2 = model.plot_components(forecast)
    plt.savefig('results/prophet_components.png')
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
    
    # Split data into train and test
    train_size = int(len(daily_sales) * 0.8)
    train_data = daily_sales[:train_size]
    test_data = daily_sales[train_size:]
    
    # Train Prophet model
    model = train_prophet_model(train_data)
    
    # Generate forecast
    forecast = generate_forecast(model, periods=len(test_data))
    
    # Plot results
    plot_prophet_forecast(model, forecast)
    
    # Evaluate model
    metrics = evaluate_forecast(
        test_data['y'],
        forecast['yhat'][-len(test_data):]
    )
    
    print("\nForecast Evaluation Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")
    
    # Save metrics to file
    with open('results/prophet_metrics.txt', 'w') as f:
        f.write("Prophet Model Evaluation Metrics:\n")
        for metric, value in metrics.items():
            f.write(f"{metric}: {value:.4f}\n")
        
        # Add seasonality information
        f.write("\nSeasonality Analysis:\n")
        f.write(f"Weekly Seasonality: {model.weekly_seasonality}\n")
        f.write(f"Yearly Seasonality: {model.yearly_seasonality}\n")
        f.write(f"Daily Seasonality: {model.daily_seasonality}\n")

if __name__ == "__main__":
    main() 
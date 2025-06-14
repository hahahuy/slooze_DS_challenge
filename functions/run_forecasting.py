import os
import pandas as pd
import matplotlib.pyplot as plt
from arima_forecast import main as run_arima
from prophet_forecast import main as run_prophet

def create_results_directory():
    """Create results directory if it doesn't exist"""
    if not os.path.exists('results'):
        os.makedirs('results')

def compare_models():
    """Compare ARIMA and Prophet model results"""
    # Read metrics from both models
    with open('results/arima_metrics.txt', 'r') as f:
        arima_metrics = f.read()
    
    with open('results/prophet_metrics.txt', 'r') as f:
        prophet_metrics = f.read()
    
    # Create comparison report
    with open('results/model_comparison.txt', 'w') as f:
        f.write("Model Comparison Report\n")
        f.write("=====================\n\n")
        f.write("ARIMA Model Metrics:\n")
        f.write(arima_metrics)
        f.write("\nProphet Model Metrics:\n")
        f.write(prophet_metrics)
        f.write("\nRecommendation:\n")
        f.write("Based on the metrics, the model with lower MAE and RMSE, ")
        f.write("and higher R2 score is recommended for forecasting.\n")

def main():
    # Create results directory
    create_results_directory()
    
    print("Running ARIMA model...")
    run_arima()
    
    print("\nRunning Prophet model...")
    run_prophet()
    
    print("\nComparing models...")
    compare_models()
    
    print("\nAnalysis complete! Check the results directory for outputs.")

if __name__ == "__main__":
    main() 
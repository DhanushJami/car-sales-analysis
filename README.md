# Car Sales Analysis

## Project Description
This project analyzes a dataset of car sales. The dataset contains information about various car models, including attributes such as price, sales, engine size, horsepower, and fuel efficiency. The analysis includes data cleaning, basic statistical calculations, and visualizations.

## Files in the Repository

- **analysis.py**: Python script that performs the analysis on the dataset.
  - Reads the data from the CSV file.
  - Cleans the data (removes duplicates, fills missing values).
  - Computes basic statistics such as the mean, mode, and sum.
  - Creates visualizations such as histograms, scatter plots, and pie charts.

- **dataset.csv**: Dataset containing the car sales data with columns such as `Price_in_thousands`, `sales`, `Engine_size`, `Horsepower`, and `Fuel_efficiency`.

## Requirements
This project requires the following Python libraries:
- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations.
- **matplotlib**: For data visualization.

You can install the required libraries by running the following command:
```bash
pip install pandas numpy matplotlib
python analysis.py

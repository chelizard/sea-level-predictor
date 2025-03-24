import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create the figure and axis
    plt.figure(figsize=(10, 6))
    
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Get the slope and intercept of the line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create future predictions through 2050
    future_years = pd.Series(range(df['Year'].min(), 2051))
    plt.plot(future_years, slope * future_years + intercept, 'r', label='1880-2050 trend line')

    # Create second line of best fit for the years 2000 to 2050
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    future_years_recent = pd.Series(range(2000, 2051))
    plt.plot(future_years_recent, slope_recent * future_years_recent + intercept_recent, 'g', label='2000-2050 trend line')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Add legend
    plt.legend(loc='upper left')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

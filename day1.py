# Step 1: Import Libraries and Load Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the traffic dataset
traffic_df = pd.read_excel(r"C:\Users\Bhanupratap singh\OneDrive\Desktop\India_Traffic_Congestion_Data.csv")

# Step 2: Convert Date column to datetime
traffic_df["Date"] = pd.to_datetime(traffic_df["Date"])

# Display initial info
print(traffic_df.info())
print(traffic_df.head())


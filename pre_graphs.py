import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt

# clean traffic data location and opening 
cleantrafficdata = pd.read_csv('cleaned_traffic_accidents.csv')

# set size for all graphs
plt.rcParams["figure.figsize"] = (10, 5)

# creates a graph for all OHE data 
def creat_graph(prefix, title):
    category_columns = [col for col in cleantrafficdata.columns if col.startswith(prefix)]
    category_counts = cleantrafficdata[category_columns].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(12, 5))
    category_counts.plot(kind="bar")
    plt.title(f"Accident Count by {title}")
    plt.xlabel(title)
    plt.ylabel("Count")
    plt.xticks(rotation=90, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

# 
creat_graph("weather_condition_", "Weather Condition")
creat_graph("lighting_condition_", "Lighting Condition")
creat_graph("roadway_surface_cond_", "Roadway Surface Condition")
creat_graph("prim_contributory_cause_", "Primary Contributory Cause")
creat_graph("traffic_control_device_", "Traffic Control Device")

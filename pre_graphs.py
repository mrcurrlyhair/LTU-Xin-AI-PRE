import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt

# clean traffic data location and opening 
cleantrafficdata = pd.read_csv('cleaned_traffic_accidents.csv')

# set size for all graphs
plt.rcParams["figure.figsize"] = (10, 5)

def create_ohegraph(prefix, title):
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

    
# funtion to create graph for non ohe data
def create_graph(column, title):
    plt.figure(figsize=(8, 5))
    plt.hist(cleantrafficdata[column], bins=20, edgecolor="black")
    plt.title(f"Distribution of {title}")
    plt.xlabel(title)
    plt.ylabel("Frequency")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

# fatal vs non fatal graph 
def create_fatgraph():
    plt.figure(figsize=(6, 5))
    cleantrafficdata["injuries_fatal"].value_counts().sort_index().plot(kind="bar", color=["blue", "red"])
    plt.title("Fatal vs. Non-Fatal Accidents")
    plt.xlabel("Fatality")
    plt.ylabel("Count")
    plt.xticks([0, 1], ["No Fatalities", "At Least 1 Fatality"], rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

# user selection 
print("\nChoose which graphs you want to see (enter numbers separated by commas):")
print("1 - Weather Condition")
print("2 - Lighting Condition")
print("3 - Roadway Surface Condition")
print("4 - Primary Contributory Cause")
print("5 - Traffic Control Device")
print("6 - Cars Involved")
print("7 - Injuries Total")
print("8 - Crash Hour")
print("9 - Crash Day of Week")
print("10 - Fatal vs. Non-Fatal Accidents")

# get user input
selected_graphs = input("Please enter an option ").split(",")

# convert input to integers
selected_graphs = [int(num.strip()) for num in selected_graphs if num.strip().isdigit()]

# generate selected graphs
if 1 in selected_graphs:
    create_ohegraph("weather_condition_", "Weather Condition")
if 2 in selected_graphs:
    create_ohegraph("lighting_condition_", "Lighting Condition")
if 3 in selected_graphs:
    create_ohegraph("roadway_surface_cond_", "Roadway Surface Condition")
if 4 in selected_graphs:
    create_ohegraph("prim_contributory_cause_", "Primary Contributory Cause")
if 5 in selected_graphs:
    create_ohegraph("traffic_control_device_", "Traffic Control Device")
if 6 in selected_graphs:
    create_graph("cars_involved", "Cars Involved")
if 7 in selected_graphs:
    create_graph("injuries_total", "Injuries Total")
if 8 in selected_graphs:
    create_graph("crash_hour", "Crash Hour")
if 9 in selected_graphs:
    create_graph("crash_day_of_week", "Crash Day of Week")
if 10 in selected_graphs:
    create_fatgraph()


# using function, creates a graph for OHE data
# create_ohegraph("weather_condition_", "Weather Condition")
# create_ohegraph("lighting_condition_", "Lighting Condition")
# create_ohegraph("roadway_surface_cond_", "Roadway Surface Condition")
# create_ohegraph("prim_contributory_cause_", "Primary Contributory Cause")
# create_ohegraph("traffic_control_device_", "Traffic Control Device")

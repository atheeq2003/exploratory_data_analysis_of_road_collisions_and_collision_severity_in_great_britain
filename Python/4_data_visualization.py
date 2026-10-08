#!/usr/bin/env python
# coding: utf-8

# # Data Visualization
# 
# This notebook contains the charts, heatmaps, plots, and geographic visualizations for Q1–Q10.
# 

# ### Q1. What is the distribution of collision severity in Great Britain?

# In[47]:


# Visualize the overall distribution of collision severity.
plt.figure(figsize=(8, 5))

bars = plt.bar(
    severity_counts.index,
    severity_counts.values
)

plt.title("Distribution of Collision Severity in Great Britain")
plt.xlabel("Collision Severity")
plt.ylabel("Number of Collisions")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height):,}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()


# # Q2. Which speed limits are associated with more severe collisions?

# In[50]:


speed_severity_percent = pd.crosstab(
    cleaned_df["speed_limit"],
    cleaned_df["collision_severity_label"],
    normalize="index"
) * 100

speed_severity_percent = speed_severity_percent[
    ["Slight", "Serious", "Fatal"]
]

ax = speed_severity_percent.plot(
    kind="bar",
    stacked=True,
    figsize=(10, 6)
)

plt.title("Collision Severity Distribution by Speed Limit")
plt.xlabel("Speed Limit (mph)")
plt.ylabel("Percentage of Collisions (%)")
plt.xticks(rotation=0)
plt.legend(title="Collision Severity")

plt.tight_layout()
plt.show()


# In[52]:


# Plot the Serious-or-Fatal collision rate across speed limits.
plt.figure(figsize=(9, 5))

plt.plot(
    severe_rate.index,
    severe_rate["Serious_or_Fatal"],
    marker="o"
)

plt.title("Serious or Fatal Collision Rate by Speed Limit")
plt.xlabel("Speed Limit (mph)")
plt.ylabel("Serious + Fatal Collisions (%)")
plt.xticks(severe_rate.index)

plt.tight_layout()
plt.show()


# ## Q3. How do weather and road surface conditions relate to collision severity?
# 

# In[57]:


# Compare severity distributions across weather conditions.
weather_severity_percent.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 6)
)

plt.title("Collision Severity Distribution by Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Percentage of Collisions (%)")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Collision Severity")

plt.tight_layout()
plt.show()


# In[58]:


# Compare severity distributions across road-surface conditions.
surface_severity_percent.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 6)
)

plt.title("Collision Severity Distribution by Road Surface Condition")
plt.xlabel("Road Surface Condition")
plt.ylabel("Percentage of Collisions (%)")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Collision Severity")

plt.tight_layout()
plt.show()


# In[61]:


# Rank weather conditions by their Serious-or-Fatal collision rate.
plt.figure(figsize=(11, 6))

weather_severe_rate.sort_values().plot(
    kind="barh"
)

plt.title("Serious or Fatal Collision Rate by Weather Condition")
plt.xlabel("Serious + Fatal Collisions (%)")
plt.ylabel("Weather Condition")

plt.tight_layout()
plt.show()


# In[62]:


# Rank road-surface conditions by their Serious-or-Fatal collision rate.
plt.figure(figsize=(10, 6))

surface_severe_rate.sort_values().plot(
    kind="barh"
)

plt.title("Serious or Fatal Collision Rate by Road Surface Condition")
plt.xlabel("Serious + Fatal Collisions (%)")
plt.ylabel("Road Surface Condition")

plt.tight_layout()
plt.show()


# ## Q4. Does collision severity vary between urban and rural areas?
# 

# In[67]:


# Compare severity distributions between urban and rural areas.
urban_rural_percent.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 6)
)

plt.title("Collision Severity Distribution by Urban/Rural Area")
plt.xlabel("Area Type")
plt.ylabel("Percentage of Collisions (%)")
plt.xticks(rotation=0)
plt.legend(title="Collision Severity")

plt.tight_layout()
plt.show()


# In[68]:


# Compare Serious-or-Fatal rates between urban and rural areas.
plt.figure(figsize=(8, 5))

urban_rural_severe_rate.plot(kind="bar")

plt.title("Serious or Fatal Collision Rate by Area Type")
plt.xlabel("Area Type")
plt.ylabel("Serious + Fatal Collisions (%)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ## Q5. Which road types and junction conditions experience more collisions?

# In[73]:


# Visualize the number of collisions across road types.
plt.figure(figsize=(10, 6))

road_type_counts.sort_values().plot(kind="barh")

plt.title("Number of Collisions by Road Type")
plt.xlabel("Number of Collisions")
plt.ylabel("Road Type")

plt.tight_layout()
plt.show()


# In[74]:


# Calculate the combined Serious + Fatal rate for each road type.
road_type_severe_rate = (
    road_type_severity_percent["Serious"] +
    road_type_severity_percent["Fatal"]
)

plt.figure(figsize=(10, 6))

road_type_severe_rate.sort_values().plot(kind="barh")

plt.title("Serious or Fatal Collision Rate by Road Type")
plt.xlabel("Serious + Fatal Collisions (%)")
plt.ylabel("Road Type")

plt.tight_layout()
plt.show()


# In[78]:


# Visualize the severity distribution across junction conditions.
junction_severity_percent.plot(
    kind="bar",
    stacked=True,
    figsize=(13, 7)
)

plt.title("Collision Severity Distribution by Junction Condition")
plt.xlabel("Junction Condition")
plt.ylabel("Percentage of Collisions (%)")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Collision Severity")

plt.tight_layout()
plt.show()


# In[79]:


# Visualize the number of collisions across junction conditions.
plt.figure(figsize=(12, 7))

junction_counts.sort_values().plot(
    kind="barh"
)

plt.title("Number of Collisions by Junction Condition")
plt.xlabel("Number of Collisions")
plt.ylabel("Junction Condition")

plt.tight_layout()
plt.show()


# In[80]:


# Calculate the combined Serious + Fatal rate for each junction condition.
junction_severe_rate = (
    junction_severity_percent["Serious"] +
    junction_severity_percent["Fatal"]
)

plt.figure(figsize=(12, 7))

junction_severe_rate.sort_values().plot(
    kind="barh"
)

plt.title("Serious or Fatal Collision Rate by Junction Condition")
plt.xlabel("Serious + Fatal Collisions (%)")
plt.ylabel("Junction Condition")

plt.tight_layout()
plt.show()


# ## Q6. How does the number of vehicles involved relate to severity?
# 

# In[91]:


# Visualize severity distribution across the grouped vehicle categories.
vehicle_group_severity.plot(
    kind="bar",
    stacked=True,
    figsize=(10, 6)
)

plt.title("Collision Severity Distribution by Number of Vehicles")
plt.xlabel("Number of Vehicles")
plt.ylabel("Percentage of Collisions (%)")
plt.xticks(rotation=0)
plt.legend(title="Collision Severity")

plt.tight_layout()
plt.show()


# In[92]:


# Recalculate the Serious + Fatal rate for the grouped vehicle categories.
vehicle_group_severe_rate = (
    vehicle_group_severity["Serious"] +
    vehicle_group_severity["Fatal"]
)

plt.figure(figsize=(9, 5))

vehicle_group_severe_rate.plot(
    kind="bar"
)

plt.title("Serious or Fatal Collision Rate by Number of Vehicles")
plt.xlabel("Number of Vehicles")
plt.ylabel("Serious + Fatal Collisions (%)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ## Q7. At what times and days do collisions occur most frequently?
# 

# In[97]:


# Plot the number of collisions by hour to identify peak periods.
plt.figure(figsize=(12, 6))

hour_counts.plot(
    kind="line",
    marker="o"
)

plt.title("Number of Collisions by Hour of Day")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Collisions")
plt.xticks(range(24))
plt.grid(True)

plt.tight_layout()
plt.show()


# In[98]:


# Create a day-by-time-period collision frequency table for the heatmap.
day_time_counts = pd.crosstab(
    cleaned_df["day_of_week_label"],
    cleaned_df["time_period"]
)

day_time_counts = day_time_counts.reindex(
    index=day_order,
    columns=time_period_order
)

print(day_time_counts)


# In[99]:


# Visualize collision concentration by day of week and time period.
plt.figure(figsize=(10, 7))

sns.heatmap(
    day_time_counts,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("Collision Frequency by Day and Time Period")
plt.xlabel("Time Period")
plt.ylabel("Day of Week")

plt.tight_layout()
plt.show()


# ## Q8. Is there a relationship between number of casualties and collision severity?
# 

# In[102]:


# Compare casualty distributions across collision severity categories.
plt.figure(figsize=(10, 6))

sns.boxplot(
    data=cleaned_df,
    x="collision_severity_label",
    y="number_of_casualties"
)

plt.title("Number of Casualties by Collision Severity")
plt.xlabel("Collision Severity")
plt.ylabel("Number of Casualties")

plt.tight_layout()
plt.show()


# In[103]:


# Use the 99th percentile to reduce the influence of extreme casualty outliers in the boxplot.
upper_limit = cleaned_df["number_of_casualties"].quantile(0.99)

casualty_plot_df = cleaned_df[
    cleaned_df["number_of_casualties"] <= upper_limit
]

print("99th percentile:", upper_limit)


# In[104]:


# Plot casualty distributions after limiting extreme values for clearer comparison.
plt.figure(figsize=(10, 6))

sns.boxplot(
    data=casualty_plot_df,
    x="collision_severity_label",
    y="number_of_casualties"
)

plt.title("Number of Casualties by Collision Severity (99th Percentile)")
plt.xlabel("Collision Severity")
plt.ylabel("Number of Casualties")

plt.tight_layout()
plt.show()


# In[106]:


# Visualize average casualties by collision severity.
plt.figure(figsize=(8, 5))

mean_casualties.plot(kind="bar")

plt.title("Average Number of Casualties by Collision Severity")
plt.xlabel("Collision Severity")
plt.ylabel("Average Number of Casualties")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ## Q9. Which locations/areas have higher collision concentrations?
# 

# In[110]:


# Recalculate collision counts using the readable local-authority names.
area_counts = (
    cleaned_df["local_authority_name"]
    .value_counts()
)

top_10_areas = area_counts.head(10).sort_values()

plt.figure(figsize=(10, 6))

top_10_areas.plot(kind="barh")

plt.title("Top 10 Local Authority Areas by Number of Collisions")
plt.xlabel("Number of Collisions")
plt.ylabel("Local Authority Area")

plt.tight_layout()
plt.show()


# In[113]:


# Visualize the geographic concentration of collisions using longitude and latitude.
import seaborn as sns

plt.figure(figsize=(12, 8))

sns.histplot(
    data=cleaned_df,
    x="longitude",
    y="latitude",
    bins=60,
    cbar=True
)

plt.title("Collision Density Across Great Britain")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()
plt.show()


# In[115]:


# Visualize the geographic concentration of Serious-or-Fatal collisions.
plt.figure(figsize=(12, 8))

sns.histplot(
    data=serious_fatal_df,
    x="longitude",
    y="latitude",
    bins=60,
    cbar=True
)

plt.title("Serious and Fatal Collision Density Across Great Britain")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()
plt.show()


# ## Q10. Which combinations of road, environmental, traffic, and temporal conditions are frequently observed in serious and fatal collisions?
# 

# In[122]:


# Visualize the most frequent condition combinations

plot_q10 = top_q10.sort_values(
    "serious_fatal_collisions",
    ascending=True
)

plt.figure(figsize=(14, 9))

plt.barh(
    plot_q10["condition_combination"],
    plot_q10["serious_fatal_collisions"]
)

plt.xlabel("Number of Serious/Fatal Collisions")
plt.ylabel("Condition Combination")
plt.title(
    "Most Frequently Observed Condition Combinations "
    "in Serious and Fatal Collisions"
)

plt.tight_layout()
plt.show()


# In[125]:


plt.figure(figsize=(10, 6))

vehicle_group_frequency.sort_index().plot(
    kind="bar"
)

plt.title(
    "Number of Vehicles Involved in Serious and Fatal Collisions"
)
plt.xlabel("Number of Vehicles")
plt.ylabel("Number of Serious/Fatal Collisions")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# In[127]:


# Create a day × time-period heatmap

temporal_heatmap = pd.crosstab(
    serious_fatal_df["day_of_week_label"],
    serious_fatal_df["time_period"]
)

temporal_heatmap = temporal_heatmap.reindex(
    index=[
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ],
    columns=[
        "Morning",
        "Afternoon",
        "Evening",
        "Night"
    ]
)

plt.figure(figsize=(10, 6))

sns.heatmap(
    temporal_heatmap,
    annot=True,
    fmt="d"
)

plt.title(
    "Serious and Fatal Collisions by Day and Time Period"
)

plt.xlabel("Time Period")
plt.ylabel("Day of Week")

plt.tight_layout()
plt.show()


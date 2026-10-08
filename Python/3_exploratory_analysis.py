#!/usr/bin/env python
# coding: utf-8

# # Exploratory Analysis
# 
# This notebook contains the statistical analysis, distributions, groupby calculations, percentages, relationships, and findings for Q1–Q10.
# 

# ### Q1. What is the distribution of collision severity in Great Britain?

# In[46]:


# Calculate the number of collisions in each severity category and order them by frequency.
severity_counts = (
    cleaned_df["collision_severity_label"]
    .value_counts()
)

severity_percent = (
    severity_counts / severity_counts.sum()
) * 100

severity_summary = pd.DataFrame({
    "Collision Severity": severity_counts.index,
    "Number of Collisions": severity_counts.values,
    "Percentage": severity_percent.values.round(2)
})

print(severity_summary)


# # Q2. Which speed limits are associated with more severe collisions?

# In[48]:


# Create a severity frequency table for each speed-limit category.
speed_severity = pd.crosstab(
    cleaned_df["speed_limit"],
    cleaned_df["collision_severity_label"]
)

print(speed_severity)


# In[49]:


# Convert the speed-limit severity counts into percentages within each speed limit.
speed_severity_percent = pd.crosstab(
    cleaned_df["speed_limit"],
    cleaned_df["collision_severity_label"],
    normalize="index"
) * 100

print(speed_severity_percent.round(2))


# In[51]:


# Calculate the combined Serious + Fatal percentage for each speed limit.
severe_rate = speed_severity_percent.copy()

severe_rate["Serious_or_Fatal"] = (
    severe_rate["Serious"] +
    severe_rate["Fatal"]
)

print(
    severe_rate[["Serious_or_Fatal"]].round(2)
)


# ## Q3. How do weather and road surface conditions relate to collision severity?
# 

# In[53]:


# Create a severity frequency table for each weather condition.
weather_severity = pd.crosstab(
    cleaned_df["weather_conditions_label"],
    cleaned_df["collision_severity_label"]
)

print(weather_severity)


# In[54]:


# Convert weather-condition severity counts into percentages within each weather category.
weather_severity_percent = pd.crosstab(
    cleaned_df["weather_conditions_label"],
    cleaned_df["collision_severity_label"],
    normalize="index"
) * 100

weather_severity_percent = weather_severity_percent[
    ["Slight", "Serious", "Fatal"]
]

print(weather_severity_percent.round(2))


# In[55]:


# Create a severity frequency table for each road-surface condition.
surface_severity = pd.crosstab(
    cleaned_df["road_surface_conditions_label"],
    cleaned_df["collision_severity_label"]
)

print(surface_severity)


# In[56]:


# Convert road-surface severity counts into percentages within each surface category.
surface_severity_percent = pd.crosstab(
    cleaned_df["road_surface_conditions_label"],
    cleaned_df["collision_severity_label"],
    normalize="index"
) * 100

surface_severity_percent = surface_severity_percent[
    ["Slight", "Serious", "Fatal"]
]

print(surface_severity_percent.round(2))


# In[59]:


# Calculate the Serious + Fatal rate for each weather condition.
weather_severe_rate = (
    weather_severity_percent["Serious"] +
    weather_severity_percent["Fatal"]
)

print(
    weather_severe_rate
    .sort_values(ascending=False)
    .round(2)
)


# In[60]:


# Calculate the Serious + Fatal rate for each road-surface condition.
surface_severe_rate = (
    surface_severity_percent["Serious"] +
    surface_severity_percent["Fatal"]
)

print(
    surface_severe_rate
    .sort_values(ascending=False)
    .round(2)
)


# ## Q4. Does collision severity vary between urban and rural areas?
# 

# In[63]:


# Count collisions by urban/rural classification and severity.
urban_rural_counts = pd.crosstab(
    cleaned_df["urban_or_rural_area_label"],
    cleaned_df["collision_severity_label"]
)

print(urban_rural_counts)


# In[64]:


urban_rural_df = cleaned_df[
    cleaned_df["urban_or_rural_area_label"].isin(["Urban", "Rural"])
].copy()

print(urban_rural_df["urban_or_rural_area_label"].value_counts())


# In[65]:


# Calculate severity percentages within each urban/rural category.
urban_rural_percent = pd.crosstab(
    urban_rural_df["urban_or_rural_area_label"],
    urban_rural_df["collision_severity_label"],
    normalize="index"
) * 100

urban_rural_percent = urban_rural_percent[
    ["Slight", "Serious", "Fatal"]
]

print(urban_rural_percent.round(2))


# In[66]:


# Calculate the combined Serious + Fatal rate for urban and rural areas.
urban_rural_severe_rate = (
    urban_rural_percent["Serious"] +
    urban_rural_percent["Fatal"]
)

print(urban_rural_severe_rate.round(2))


# ## Q5. Which road types and junction conditions experience more collisions?

# In[69]:


# Calculate road-type collision counts and severity distributions.
road_type_counts = cleaned_df["road_type_label"].value_counts()

road_type_severity = pd.crosstab(
    cleaned_df["road_type_label"],
    cleaned_df["collision_severity_label"]
)

road_type_severity_percent = pd.crosstab(
    cleaned_df["road_type_label"],
    cleaned_df["collision_severity_label"],
    normalize="index"
) * 100

road_type_severity_percent = road_type_severity_percent[["Slight", "Serious", "Fatal"]]

print("Road type collision counts:")
print(road_type_counts)
print("\nRoad type severity percentages:")
print(road_type_severity_percent.round(2))


# In[70]:


# Count the total number of collisions for each road type.
road_type_counts


# In[71]:


# Create a severity frequency table for each road type.
road_type_severity


# In[72]:


# Convert road-type severity counts into percentages within each road type.
road_type_severity_percent


# In[75]:


# Count collisions by junction condition.
junction_counts = (
    cleaned_df["junction_detail_label"]
    .value_counts()
)

print(junction_counts)


# In[76]:


# Create a severity frequency table for each junction condition.
junction_severity = pd.crosstab(
    cleaned_df["junction_detail_label"],
    cleaned_df["collision_severity_label"]
)

print(junction_severity)


# In[77]:


# Convert junction severity counts into percentages within each junction category.
junction_severity_percent = pd.crosstab(
    cleaned_df["junction_detail_label"],
    cleaned_df["collision_severity_label"],
    normalize="index"
) * 100

junction_severity_percent = junction_severity_percent[
    ["Slight", "Serious", "Fatal"]
]

print(junction_severity_percent.round(2))


# ## Q6. How does the number of vehicles involved relate to severity?
# 

# In[81]:


# Count collisions by number of vehicles involved.
vehicle_counts = (
    cleaned_df["number_of_vehicles"]
    .value_counts()
    .sort_index()
)

print(vehicle_counts)


# In[82]:


# Create a severity frequency table for each vehicle count.
vehicle_severity = pd.crosstab(
    cleaned_df["number_of_vehicles"],
    cleaned_df["collision_severity_label"]
)

print(vehicle_severity)


# In[83]:


# Convert vehicle-count severity counts into percentages within each vehicle-count category.
vehicle_severity_percent = pd.crosstab(
    cleaned_df["number_of_vehicles"],
    cleaned_df["collision_severity_label"],
    normalize="index"
) * 100

vehicle_severity_percent = vehicle_severity_percent[
    ["Slight", "Serious", "Fatal"]
]

print(vehicle_severity_percent.round(2))


# In[84]:


# Calculate the combined Serious + Fatal rate for each vehicle-count category.
vehicle_severe_rate = (
    vehicle_severity_percent["Serious"] +
    vehicle_severity_percent["Fatal"]
)

print(
    vehicle_severe_rate.round(2)
)


# In[85]:


# Group high vehicle counts together so sparse categories can be compared more reliably.
cleaned_df["vehicle_group"] = np.where(
    cleaned_df["number_of_vehicles"] >= 5,
    "5+ vehicles",
    cleaned_df["number_of_vehicles"].astype(str)
)


# In[86]:


print(
    cleaned_df["vehicle_group"].value_counts()
)


# In[87]:


# Create a severity frequency table for the grouped vehicle categories.
vehicle_group_severity = pd.crosstab(
    cleaned_df["vehicle_group"],
    cleaned_df["collision_severity_label"],
    normalize="index"
) * 100

vehicle_group_severity = vehicle_group_severity[
    ["Slight", "Serious", "Fatal"]
]

print(vehicle_group_severity.round(2))


# In[88]:


# Calculate the combined Serious + Fatal rate for each grouped vehicle category.
vehicle_group_severe_rate = (
    vehicle_group_severity["Serious"] +
    vehicle_group_severity["Fatal"]
)

print(
    vehicle_group_severe_rate.round(2)
)


# In[89]:


print(
    cleaned_df["vehicle_group"].value_counts()
)


# In[90]:


print(
    vehicle_group_severity.round(2)
)


# ## Q7. At what times and days do collisions occur most frequently?
# 

# In[93]:


# Define the logical weekday order for consistent plotting.
day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

day_counts = (
    cleaned_df["day_of_week_label"]
    .value_counts()
    .reindex(day_order)
)

print(day_counts)


# In[94]:


# Define the logical time-period order for consistent plotting.
time_period_order = [
    "Morning",
    "Afternoon",
    "Evening",
    "Night"
]

time_period_counts = (
    cleaned_df["time_period"]
    .value_counts()
    .reindex(time_period_order)
)

print(time_period_counts)


# In[95]:


# Count collisions for each hour of the day.
hour_counts = (
    cleaned_df["hour"]
    .value_counts()
    .sort_index()
)

print(hour_counts)


# In[96]:


peak_hour = hour_counts.idxmax()
peak_hour_count = hour_counts.max()

print("Peak hour:", peak_hour)
print("Number of collisions:", peak_hour_count)


# In[100]:


# Identify the day and time period with the highest collision count.
peak_day_time = day_time_counts.stack().idxmax()
peak_count = day_time_counts.stack().max()

print("Peak day and time period:", peak_day_time)
print("Number of collisions:", peak_count)


# ## Q8. Is there a relationship between number of casualties and collision severity?
# 

# In[101]:


# Calculate descriptive statistics for casualties within each severity category.
casualty_stats = cleaned_df.groupby(
    "collision_severity_label"
)["number_of_casualties"].agg(
    ["count", "mean", "median", "min", "max", "std"]
)

print(casualty_stats)


# In[105]:


# Calculate the average number of casualties for each collision severity.
mean_casualties = (
    cleaned_df.groupby("collision_severity_label")[
        "number_of_casualties"
    ].mean()
    .reindex(["Slight", "Serious", "Fatal"])
)

print(mean_casualties)


# ## Q9. Which locations/areas have higher collision concentrations?
# 

# In[107]:


# Count collisions for each local authority district.
area_counts = (
    cleaned_df["local_authority_ons_district"]
    .value_counts()
)

print(area_counts.head(15))


# In[108]:


# Map selected local-authority district codes to readable names.
area_name_mapping = {
    "E08000025": "Birmingham",
    "E08000035": "Leeds",
    "E06000065": "North Yorkshire",
    "E09000033": "Westminster",
    "E06000054": "Wiltshire",
    "E08000032": "Bradford",
    "E09000030": "Tower Hamlets",
    "E09000022": "Lambeth",
    "E09000008": "Croydon",
    "E09000028": "Southwark",
    "E06000052": "Cornwall",
    "E09000010": "Enfield",
    "E06000066": "Somerset",
    "E08000012": "Liverpool",
    "E08000039": "Sheffield"
}


# In[109]:


# Add readable local-authority names for easier interpretation of the analysis.
cleaned_df["local_authority_name"] = (
    cleaned_df["local_authority_ons_district"]
    .map(area_name_mapping)
    .fillna(cleaned_df["local_authority_ons_district"])
)


# In[111]:


print(area_counts.head(10))


# In[112]:


print(cleaned_df[["latitude", "longitude"]].isnull().sum())


# In[114]:


# Filter the dataset to Serious and Fatal collisions for geographic comparison.
serious_fatal_df = cleaned_df[
    cleaned_df["collision_severity_label"].isin(["Serious", "Fatal"])
].copy()


# ## Q10. Which combinations of road, environmental, traffic, and temporal conditions are frequently observed in serious and fatal collisions?
# 

# In[116]:


# Filter the dataset to Serious and Fatal collisions only

serious_fatal_df = cleaned_df[
    cleaned_df["collision_severity_label"].isin(["Serious", "Fatal"])
].copy()

print("Total Serious/Fatal collisions:", len(serious_fatal_df))

print("\nSeverity distribution:")
print(
    serious_fatal_df["collision_severity_label"]
    .value_counts()
)


# In[117]:


# Create combinations of road, environmental, traffic and temporal conditions

q10_combinations = (
    serious_fatal_df
    .groupby([
        "road_type_label",
        "junction_detail_label",
        "weather_conditions_label",
        "road_surface_conditions_label",
        "speed_limit",
        "time_period"
    ])
    .size()
    .reset_index(name="serious_fatal_collisions")
)

# Sort by frequency
q10_combinations = q10_combinations.sort_values(
    "serious_fatal_collisions",
    ascending=False
)

q10_combinations.head(20)


# In[118]:


# Keep only combinations that occur at least 20 times
# among Serious/Fatal collisions

q10_frequent = q10_combinations[
    q10_combinations["serious_fatal_collisions"] >= 20
].copy()

print(
    "Number of frequent combinations:",
    len(q10_frequent)
)

q10_frequent.head(20)


# In[119]:


# Top 15 most frequently observed combinations

top_q10 = q10_frequent.head(15).copy()

print(
    top_q10[
        [
            "road_type_label",
            "junction_detail_label",
            "weather_conditions_label",
            "road_surface_conditions_label",
            "speed_limit",
            "time_period",
            "serious_fatal_collisions"
        ]
    ].to_string(index=False)
)


# In[120]:


# Calculate the percentage of all Serious/Fatal collisions
# represented by each condition combination

total_serious_fatal = len(serious_fatal_df)

top_q10["percentage_of_serious_fatal"] = (
    top_q10["serious_fatal_collisions"]
    / total_serious_fatal
    * 100
)

top_q10[
    [
        "road_type_label",
        "junction_detail_label",
        "weather_conditions_label",
        "road_surface_conditions_label",
        "speed_limit",
        "time_period",
        "serious_fatal_collisions",
        "percentage_of_serious_fatal"
    ]
]


# In[121]:


# Create a readable label for each condition combination

top_q10["condition_combination"] = (
    top_q10["road_type_label"].astype(str)
    + " | "
    + top_q10["junction_detail_label"].astype(str)
    + " | "
    + top_q10["weather_conditions_label"].astype(str)
    + " | "
    + top_q10["road_surface_conditions_label"].astype(str)
    + " | "
    + top_q10["speed_limit"].astype(str)
    + " mph | "
    + top_q10["time_period"].astype(str)
)

top_q10[
    [
        "condition_combination",
        "serious_fatal_collisions",
        "percentage_of_serious_fatal"
    ]
]


# In[123]:


# Analyze number of vehicles involved in Serious/Fatal collisions

vehicle_frequency = (
    serious_fatal_df["number_of_vehicles"]
    .value_counts()
    .sort_index()
)

print(vehicle_frequency)


# In[124]:


# Group rare high vehicle counts into 5+ vehicles

serious_fatal_df["vehicle_group"] = np.where(
    serious_fatal_df["number_of_vehicles"] >= 5,
    "5+ vehicles",
    serious_fatal_df["number_of_vehicles"].astype(str)
)

vehicle_group_frequency = (
    serious_fatal_df["vehicle_group"]
    .value_counts()
)

print(vehicle_group_frequency)


# In[126]:


# Identify the most frequent day and time-period combinations
# among Serious/Fatal collisions

temporal_frequency = (
    serious_fatal_df
    .groupby([
        "day_of_week_label",
        "time_period"
    ])
    .size()
    .reset_index(
        name="serious_fatal_collisions"
    )
    .sort_values(
        "serious_fatal_collisions",
        ascending=False
    )
)

print(
    temporal_frequency.head(10).to_string(index=False)
)


# In[128]:


# Perform a final quality check before saving the cleaned dataset.
print("===== FINAL DATASET CHECK =====")

print("Shape:", cleaned_df.shape)

print("\nMissing values:")
print(cleaned_df.isnull().sum()[cleaned_df.isnull().sum() > 0])

print("\nDuplicate rows:", cleaned_df.duplicated().sum())

print("\nTarget distribution:")
print(cleaned_df["collision_severity_label"].value_counts())

print("\nData types:")
print(cleaned_df.dtypes)


# In[130]:


# Save the final cleaned dataset so it can be reused without modifying the raw data.
cleaned_df.to_csv(
    "Great_Britain_Road_Collisions_2025_Cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully.")


# # Overall EDA Findings
# 
# 1. Slight collisions dominate the dataset, representing approximately 73.8% of all collisions.
# 2. 60 mph roads show the highest proportion of serious/fatal collisions.
# 3. Rural collisions have a higher serious/fatal proportion than urban collisions.
# 4. Single carriageways account for the largest number of collisions.
# 5. Friday is the busiest collision day, while 17:00 is the peak collision hour.
# 6. Fatal collisions have the highest average number of casualties.
# 7. Birmingham has the highest number of recorded collisions among local authority areas.
# 8. Higher-risk combinations are concentrated around higher speed limits, rural environments, and certain weather/surface conditions.
# 9. Weather and road-surface categories with very small sample sizes should be interpreted cautiously.
# 10. Collision severity and casualty count have an inherent relationship in the dataset and should not be interpreted as an independent causal relationship.

# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning
# 
# This notebook contains the cleaning steps of the raw dataset.
# 

# In[11]:


# Finding Missing Values

missing_values = cleaned_df.isnull().sum()
missing_values


# In[12]:


# Finding Duplicate Rows

duplicated_count = cleaned_df.duplicated().sum()
duplicated_count


# In[13]:


# Finding Unique Values and Sorting them by index

print("Collision Severity:")
print(cleaned_df["collision_severity"].value_counts().sort_index())

print("\nSpeed Limit:")
print(cleaned_df["speed_limit"].value_counts().sort_index())

print("\nUrban/Rural:")
print(cleaned_df["urban_or_rural_area"].value_counts().sort_index())

print("\nRoad Type:")
print(cleaned_df["road_type"].value_counts().sort_index())

print("\nWeather:")
print(cleaned_df["weather_conditions"].value_counts().sort_index())

print("\nRoad Surface:")
print(cleaned_df["road_surface_conditions"].value_counts().sort_index())


# In[14]:


print("Date examples:")
print(cleaned_df["date"].head())

print("\nTime examples:")
print(cleaned_df["time"].head())


# In[15]:


# Labelling Categorical Data

severity_labels = {
    1: "Fatal",
    2: "Serious",
    3: "Slight"
}

day_labels = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

road_type_labels = {
    1: "Roundabout",
    2: "One way street",
    3: "Dual carriageway",
    6: "Single carriageway",
    7: "Slip road",
    9: "Unknown"
}

urban_rural_labels = {
    -1: "Data missing or out of range",
    1: "Urban",
    2: "Rural",
    3: "Unallocated"
}


# In[16]:


cleaned_df["collision_severity_label"] = cleaned_df["collision_severity"].map(severity_labels)

cleaned_df["day_of_week_label"] = cleaned_df["day_of_week"].map(day_labels)

cleaned_df["road_type_label"] = cleaned_df["road_type"].map(road_type_labels)

cleaned_df["urban_or_rural_area_label"] = cleaned_df["urban_or_rural_area"].map(urban_rural_labels)


# In[17]:


print(cleaned_df[[
    "collision_severity",
    "collision_severity_label"
]].drop_duplicates().sort_values("collision_severity"))


# In[18]:


print(cleaned_df[[
    "day_of_week",
    "day_of_week_label"
]].drop_duplicates().sort_values("day_of_week"))


# In[19]:


print(cleaned_df[[
    "road_type",
    "road_type_label"
]].drop_duplicates().sort_values("road_type"))


# In[20]:


print(cleaned_df[[
    "urban_or_rural_area",
    "urban_or_rural_area_label"
]].drop_duplicates().sort_values("urban_or_rural_area"))


# In[21]:


junction_labels = {
    -1: "Data missing or out of range",
     0: "Not at or within 20 metres of junction",
    13: "T or staggered junction",
    16: "Crossroads",
    17: "Junction with more than four arms (not roundabout)",
    18: "Using private drive or entrance",
    19: "Unknown (self-reported)",
    99: "Other junction"
}

weather_labels = {
    1: "Fine no high winds",
    2: "Raining no high winds",
    3: "Snowing no high winds",
    4: "Fine + high winds",
    5: "Raining + high winds",
    6: "Snowing + high winds",
    7: "Fog or mist",
    8: "Other",
    9: "Unknown"
}

road_surface_labels = {
    -1: "Data missing or out of range",
     1: "Dry",
     2: "Wet or damp",
     3: "Snow",
     4: "Frost or ice",
     5: "Flood over 3cm deep",
     9: "Unknown"
}

light_labels = {
    -1: "Data missing or out of range",
     1: "Daylight",
     4: "Darkness - lights lit",
     5: "Darkness - lights unlit",
     6: "Darkness - no lighting",
     7: "Darkness - lighting unknown"
}


# In[22]:


cleaned_df["junction_detail_label"] = cleaned_df["junction_detail"].map(junction_labels)

cleaned_df["weather_conditions_label"] = cleaned_df["weather_conditions"].map(weather_labels)

cleaned_df["road_surface_conditions_label"] = cleaned_df["road_surface_conditions"].map(road_surface_labels)

cleaned_df["light_conditions_label"] = cleaned_df["light_conditions"].map(light_labels)


# In[23]:


label_columns = [
    "collision_severity_label",
    "day_of_week_label",
    "road_type_label",
    "urban_or_rural_area_label",
    "junction_detail_label",
    "weather_conditions_label",
    "road_surface_conditions_label",
    "light_conditions_label"
]

for column in label_columns:
    print(f"\n")
    print(cleaned_df[column].value_counts(dropna=False))


# In[24]:


missing_location = cleaned_df[
    cleaned_df[[
        "longitude",
        "latitude",
        "location_easting_osgr",
        "location_northing_osgr"
    ]].isnull().any(axis=1)
]

print(missing_location)


# In[25]:


print("Number of records with missing location:",
      len(missing_location))


# In[26]:


missing_summary = cleaned_df.isnull().sum()

missing_summary = missing_summary[missing_summary > 0]

print(missing_summary)


# In[27]:


location_columns = [
    "location_easting_osgr",
    "location_northing_osgr",
    "longitude",
    "latitude"
]

for col in location_columns:
    cleaned_df[col] = cleaned_df.groupby("police_force")[col].transform(
        lambda x: x.fillna(x.median())
    )


# In[28]:


location_columns = [
    "location_easting_osgr",
    "location_northing_osgr",
    "longitude",
    "latitude"
]

for col in location_columns:
    cleaned_df[col] = cleaned_df.groupby("police_force")[col].transform(
        lambda x: x.fillna(x.median())
    )


# In[29]:


print(cleaned_df[location_columns].isnull().sum())


# In[30]:


# Converting date and time to pandas datetime format

cleaned_df["date_datetime"] = pd.to_datetime(
    cleaned_df["date"],
    format="%d/%m/%Y"
)


# In[31]:


cleaned_df.isnull().sum()


# In[32]:


print(cleaned_df[["date", "date_datetime"]].head())


# In[33]:


print("Invalid dates:",cleaned_df["date_datetime"].isna().sum())


# In[34]:


cleaned_df["month"] = cleaned_df["date_datetime"].dt.month


# In[35]:


cleaned_df["month_name"] = cleaned_df["date_datetime"].dt.month_name()


# In[36]:


cleaned_df["hour"] = cleaned_df["time"].str.split(":").str[0].astype(int)


# In[37]:


print(cleaned_df[["time", "hour"]].head(10))


# In[38]:


conditions = [
    cleaned_df["hour"].between(0, 5),
    cleaned_df["hour"].between(6, 11),
    cleaned_df["hour"].between(12, 17),
    cleaned_df["hour"].between(18, 23)
]

choices = [
    "Night",
    "Morning",
    "Afternoon",
    "Evening"
]

cleaned_df["time_period"] = np.select(
    conditions,
    choices,
    default="Unknown"
)


# In[39]:


print(cleaned_df["time_period"].value_counts())


# In[40]:


print("Date range:",
      cleaned_df["date_datetime"].min(),
      "to",
      cleaned_df["date_datetime"].max())

print("\nTime period:")
print(cleaned_df["time_period"].value_counts())

print("\nHour range:",
      cleaned_df["hour"].min(),
      "to",
      cleaned_df["hour"].max())


# In[41]:


missing_summary = cleaned_df.isnull().sum()

print("Columns with missing values:")
print(missing_summary[missing_summary > 0])


# In[42]:


print("Duplicate rows:", cleaned_df.duplicated().sum())


# In[43]:


print("\nDerived columns:")
print(
    cleaned_df[
        [
            "date_datetime",
            "month",
            "month_name",
            "hour",
            "time_period"
        ]
    ].head()
)


# In[44]:


print("\nFinal dataset shape:", cleaned_df.shape)


# In[45]:


print(
    cleaned_df[
        ["collision_severity", "collision_severity_label"]
    ].value_counts()
)


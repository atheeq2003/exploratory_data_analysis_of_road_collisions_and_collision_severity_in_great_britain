# Exploratory Data Analysis of Road Collisions and Collision Severity in Great Britain

## Project Overview

This project performs exploratory data analysis on the **2025 Great
Britain road collision dataset** to identify patterns in collision
occurrence and collision severity. The analysis focuses on factors such
as speed limits, weather, road surface conditions, urban or rural areas,
road types, junction conditions, number of vehicles, time and day,
casualties, geographical location, and combinations of conditions
associated with serious and fatal collisions.

## Industry

**Road Safety / Transportation**

## Problem Statement

Road collisions vary considerably in terms of their severity and the
conditions under which they occur. Understanding the factors associated
with serious and fatal collisions can help identify important patterns
in road safety data.

This project aims to explore the 2025 Great Britain road collision
dataset and examine relationships between collision severity and factors
such as speed limits, weather, road surface conditions, road types,
junction conditions, urban or rural areas, number of vehicles, time of
occurrence, casualties, and geographical location.

## Proposed Analysis

The project uses Python-based exploratory data analysis to answer the
following ten questions:

1. **What is the distribution of collision severity in Great Britain?**
2. **Which speed limits are associated with more severe collisions?**
3. **How do weather and road surface conditions relate to collision
   severity?**
4. **Does collision severity vary between urban and rural areas?**
5. **Which road types and junction conditions experience more
   collisions?**
6. **How does the number of vehicles involved relate to severity?**
7. **At what times and days do collisions occur most frequently?**
8. **Is there a relationship between number of casualties and collision
   severity?**
9. **Which locations/areas have higher collision concentrations?**
10. **What combination of conditions appears frequently in serious or
    fatal collisions?**

## Dataset

**Dataset Name:** 2025 Great Britain Road Collision Dataset

**Dataset Source:** Not specified in the provided project information.

The dataset contains road collision records used to analyse collision
severity and related road, environmental, temporal, casualty, vehicle,
and geographical factors.

## Tools & Technologies

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn

## Project Workflow

```text
Industry Selection
        ↓
Problem Identification
        ↓
Dataset Collection
        ↓
Data Cleaning
        ↓
Data Transformation
        ↓
Data Analysis
        ↓
Data Visualization
        ↓
Insights
        ↓
Recommendations
```

## Project Structure

```text
Data-Analysis-Python-Project/
│
├── README.md
│
├── Dataset/
│   ├── raw_dataset.csv
│   └── cleaned_dataset.csv
│
├── Notebook/
│   └── Data_Analysis_EDA.ipynb
│
├── Python/
│   ├── data_loading.ipynb
│   ├── data_cleaning.ipynb
│   ├── exploratory_analysis.ipynb
│   └── data_visualization.ipynb
│
├── Visualizations/
│   ├── Q1_collision_severity_distribution/
│   ├── Q2_speed_limit_and_severity/
│   ├── Q3_weather_and_road_surface/
│   ├── Q4_urban_rural_and_severity/
│   ├── Q5_road_types_and_junctions/
│   ├── Q6_vehicles_and_severity/
│   ├── Q7_time_and_day_patterns/
│   ├── Q8_casualties_and_severity/
│   ├── Q9_geographic_collision_concentration/
│   └── Q10_serious_fatal_condition_combinations/
│
└── Documentation/
    └── Project_Report.pdf
```

## Data Preparation

The analysis includes data cleaning and transformation before performing
exploratory analysis.

The final cleaned dataset contains:

- **101,525 rows**
- **60 columns**
- **0 missing values**
- **0 duplicate rows**

The collision severity distribution in the cleaned dataset is:

  Collision Severity     Number of Collisions   Percentage

---

  Slight                               74,881       73.76%
  Serious                              25,191       24.81%
  Fatal                                 1,453        1.43%

The project also retains the original coded categorical columns and
creates separate labelled columns for interpretation.

## Data Analysis & Visualization

### Distribution Analysis

- Collision severity distribution across Great Britain.
- Distribution of collision severity across speed limits.
- Distribution of collision severity across weather conditions.
- Distribution of collision severity across road surface conditions.
- Distribution of collision severity across urban and rural areas.
- Distribution of collision severity across junction conditions.
- Distribution of collision severity across the number of vehicles
  involved.

### Category-wise Analysis

- Road type collision counts.
- Junction condition collision counts.
- Local authority collision counts.
- Collision severity across road types and junction conditions.
- Collision severity across urban and rural areas.

### Comparison Analysis

- Speed limits and collision severity.
- Weather conditions and collision severity.
- Road surface conditions and collision severity.
- Urban and rural collision severity.
- Road types and collision severity.
- Junction conditions and collision severity.
- Number of vehicles and collision severity.

### Time-based Analysis

- Collision frequency by hour of the day.
- Collision frequency by day of the week.
- Collision frequency by time period.
- Day and time-period collision patterns.

### Relationship Analysis

- Number of casualties and collision severity.
- Number of vehicles involved and collision severity.
- Speed limit and serious/fatal collision rate.
- Environmental and road conditions associated with serious/fatal
  collisions.

### Geographic Analysis

- Top local authority areas by number of collisions.
- Geographic distribution of collisions across Great Britain.
- Geographic distribution of serious and fatal collisions.

### Condition Combination Analysis

The project analyses combinations of:

- Speed limit
- Weather conditions
- Road surface conditions
- Urban/rural area

A serious/fatal indicator is also used to examine combinations of
conditions that occur frequently in serious and fatal collisions.

## Key Insights

### Collision Severity

- **Slight collisions** represent the majority of recorded collisions
  at **73.76%**.
- **Serious collisions** account for **24.81%**.
- **Fatal collisions** account for **1.43%**.

### Speed Limit

The serious/fatal collision rate generally increases across the
lower-to-higher speed-limit categories, with the **60 mph category
showing a 36.38% serious/fatal rate** in the analysed data.

### Urban and Rural Areas

Rural collisions show a higher proportion of serious and fatal outcomes
than urban collisions:

- **Rural:** 30.88% serious/fatal
- **Urban:** 23.87% serious/fatal

### Number of Vehicles

The analysis shows that collisions involving a single vehicle have a
higher serious/fatal proportion than collisions involving two vehicles
in the analysed dataset.

### Time and Day

- **Friday** has the highest number of recorded collisions among the
  days of the week.
- **Afternoon** has the highest number of collisions among the defined
  time periods.
- **17:00** is the peak hour, with **8,877 collisions**.

### Casualties

The average number of casualties increases with collision severity:

  Collision Severity     Average Casualties

---

  Slight                             1.2245
  Serious                            1.3422
  Fatal                              1.6366

### Geographic Concentration

The analysis identifies local authority areas with higher collision
counts. The highest recorded collision counts among the analysed local
authorities include Birmingham, Leeds, North Yorkshire, Westminster,
Wiltshire, Bradford, Tower Hamlets, Lambeth, Croydon, and Southwark.

Collision count should not be interpreted as collision risk because the
analysis does not normalize the counts by factors such as population,
traffic volume, or road length.

### Serious/Fatal Condition Combinations

Among the analysed combinations with at least 100 collisions, the
highest observed combination was:

**60 mph + Fine no high winds + Dry + Rural**

This combination contained **8,004 collisions**, of which **3,098 were
serious/fatal**, giving a serious/fatal rate of approximately
**38.71%**.

## Recommendations

Based on the findings from this analysis:

1. **Give particular attention to rural road safety**, as rural
   collisions show a higher serious/fatal proportion than urban
   collisions.
2. **Prioritize road-safety analysis for higher-speed roads**,
   particularly the 60 mph category, where the analysed serious/fatal
   rate is comparatively high.
3. **Consider time-based safety planning**, particularly around periods
   with high collision frequency such as Friday and the afternoon
   period.
4. **Use casualty and severity patterns when assessing collision
   impact**, since average casualties increase with collision severity.
5. **Investigate combinations of road, environmental, and area
   conditions**, especially combinations showing comparatively high
   serious/fatal rates.
6. **Use geographic collision concentrations to identify areas for
   further investigation**, while avoiding interpretation of raw
   collision counts as risk without appropriate normalization.

## Visualization Screenshots

The project contains **27 visualizations across the 10 analysis
questions**. The visualization files are organized by question inside
the `Visualizations/` directory.

### Q1 --- Distribution of Collision Severity in Great Britain

![Distribution of Collision Severity in Great
Britain](Visualizations/Q1_collision_severity_distribution/Distribution_of_Collision_Severity_in_Great_Britain.png)

### Q2 --- Collision Severity Distribution by Speed Limit

![Collision Severity Distribution by Speed
Limit](Visualizations/Q2_speed_limit_and_severity/Collision_Severity_Distribution_by_Speed_Limit.png)

### Q2 --- Serious or Fatal Collision Rate by Speed Limit

![Serious or Fatal Collision Rate by Speed
Limit](Visualizations/Q2_speed_limit_and_severity/Serious_or_Fatal_Collision_Rate_by_Speed_Limit.png)

### Q3 --- Collision Severity Distribution by Weather Condition

![Collision Severity Distribution by Weather
Condition](Visualizations/Q3_weather_and_road_surface/Collision_Severity_Distribution_by_Weather_Condition.png)

### Q3 --- Collision Severity Distribution by Road Surface Condition

![Collision Severity Distribution by Road Surface
Condition](Visualizations/Q3_weather_and_road_surface/Collision_Severity_Distribution_by_Road_Surface_Condition.png)

### Q3 --- Serious or Fatal Collision Rate by Weather Condition

![Serious or Fatal Collision Rate by Weather
Condition](Visualizations/Q3_weather_and_road_surface/Serious_or_Fatal_Collision_Rate_by_Weather_Condition.png)

### Q3 --- Serious or Fatal Collision Rate by Road Surface Condition

![Serious or Fatal Collision Rate by Road Surface
Condition](Visualizations/Q3_weather_and_road_surface/Serious_or_Fatal_Collision_Rate_by_Road_Surface_Condition.png)

### Q4 --- Collision Severity Distribution by Urban/Rural Area

![Collision Severity Distribution by Urban Rural
Area](Visualizations/Q4_urban_rural_and_severity/Collision_Severity_Distribution_by_Urban_Rural_Area.png)

### Q4 --- Serious or Fatal Collision Rate by Area Type

![Serious or Fatal Collision Rate by Area
Type](Visualizations/Q4_urban_rural_and_severity/Serious_or_Fatal_Collision_Rate_by_Area_Type.png)

### Q5 --- Number of Collisions by Road Type

![Number of Collisions by Road
Type](Visualizations/Q5_road_types_and_junctions/Number_of_Collisions_by_Road_Type.png)

### Q5 --- Serious or Fatal Collision Rate by Road Type

![Serious or Fatal Collision Rate by Road
Type](Visualizations/Q5_road_types_and_junctions/Serious_or_Fatal_Collision_Rate_by_Road_Type.png)

### Q5 --- Collision Severity Distribution by Junction Condition

![Collision Severity Distribution by Junction
Condition](Visualizations/Q5_road_types_and_junctions/Collision_Severity_Distribution_by_Junction_Condition.png)

### Q5 --- Number of Collisions by Junction Condition

![Number of Collisions by Junction
Condition](Visualizations/Q5_road_types_and_junctions/Number_of_Collisions_by_Junction_Condition.png)

### Q5 --- Serious or Fatal Collision Rate by Junction Condition

![Serious or Fatal Collision Rate by Junction
Condition](Visualizations/Q5_road_types_and_junctions/Serious_or_Fatal_Collision_Rate_by_Junction_Condition.png)

### Q6 --- Collision Severity Distribution by Number of Vehicles

![Collision Severity Distribution by Number of
Vehicles](Visualizations/Q6_vehicles_and_severity/Collision_Severity_Distribution_by_Number_of_Vehicles.png)

### Q6 --- Serious or Fatal Collision Rate by Number of Vehicles

![Serious or Fatal Collision Rate by Number of
Vehicles](Visualizations/Q6_vehicles_and_severity/Serious_or_Fatal_Collision_Rate_by_Number_of_Vehicles.png)

### Q7 --- Number of Collisions by Hour of Day

![Number of Collisions by Hour of
Day](Visualizations/Q7_time_and_day_patterns/Number_of_Collisions_by_Hour_of_Day.png)

### Q7 --- Collision Frequency by Day and Time Period

![Collision Frequency by Day and Time
Period](Visualizations/Q7_time_and_day_patterns/Collision_Frequency_by_Day_and_Time_Period.png)

### Q8 --- Number of Casualties by Collision Severity

![Number of Casualties by Collision
Severity](Visualizations/Q8_casualties_and_severity/Number_of_Casualties_by_Collision_Severity.png)

### Q8 --- Number of Casualties by Collision Severity --- 99th Percentile

![Number of Casualties by Collision Severity 99th
Percentile](Visualizations/Q8_casualties_and_severity/Number_of_Casualties_by_Collision_Severity_99th_Percentile.png)

### Q8 --- Average Number of Casualties by Collision Severity

![Average Number of Casualties by Collision
Severity](Visualizations/Q8_casualties_and_severity/Average_Number_of_Casualties_by_Collision_Severity.png)

### Q9 --- Top 10 Local Authority Areas by Number of Collisions

![Top 10 Local Authority Areas by Number of
Collisions](Visualizations/Q9_geographic_collision_concentration/Top_10_Local_Authority_Areas_by_Number_of_Collisions.png)

### Q9 --- Collision Density Across Great Britain

![Collision Density Across Great
Britain](Visualizations/Q9_geographic_collision_concentration/Collision_Density_Across_Great_Britain.png)

### Q9 --- Serious and Fatal Collision Density Across Great Britain

![Serious and Fatal Collision Density Across Great
Britain](Visualizations/Q9_geographic_collision_concentration/Serious_and_Fatal_Collision_Density_Across_Great_Britain.png)

### Q10 --- Most Frequently Observed Condition Combinations

![Most Frequently Observed Condition
Combinations](Visualizations/Q10_serious_fatal_condition_combinations/Most_Frequently_Observed_Condition_Combinations.png)

### Q10 --- Number of Vehicles Involved in Serious and Fatal Collisions

![Number of Vehicles Involved in Serious and Fatal
Collisions](Visualizations/Q10_serious_fatal_condition_combinations/Number_of_Vehicles_Involved_in_Serious_and_Fatal_Collisions.png)

### Q10 --- Serious and Fatal Collisions by Day and Time Period

![Serious and Fatal Collisions by Day and Time
Period](Visualizations/Q10_serious_fatal_condition_combinations/Serious_and_Fatal_Collisions_by_Day_and_Time_Period.png)

## Author

- **Name:** Atheequr Rahaman B
- **Student ID:** AF05311605
- **Organization:** Anudip Foundation
- **Course:** AIML
- **Batch Code:** ANP-D7444

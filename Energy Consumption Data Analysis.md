📊 Energy Consumption Data Analysis



This project performs a complete Exploratory Data Analysis (EDA) on the Energy Consumption Dataset, including data cleaning, outlier detection, summary statistics, and initial visualizations.

The dataset contains timestamped building energy-related metrics such as temperature, humidity, occupancy, HVAC usage, renewable energy generation, and total energy consumption.



**output:**



RangeIndex: 1000 entries, 0 to 999

Data columns (total 11 columns):

&nbsp;#   Column             Non-Null Count  Dtype  

---  ------             --------------  -----  

&nbsp;0   Timestamp          1000 non-null   object 

&nbsp;1   Temperature        1000 non-null   float64

&nbsp;2   Humidity           1000 non-null   float64

&nbsp;3   SquareFootage      1000 non-null   float64

&nbsp;4   Occupancy          1000 non-null   int64  

&nbsp;5   HVACUsage          1000 non-null   object 

&nbsp;6   LightingUsage      1000 non-null   object 

&nbsp;7   RenewableEnergy    1000 non-null   float64

&nbsp;8   DayOfWeek          1000 non-null   object 

&nbsp;9   Holiday            1000 non-null   object 

&nbsp;10  EnergyConsumption  1000 non-null   float64

dtypes: float64(5), int64(1), object(5)

memory usage: 86.1+ KB







{'null\_values': Timestamp            0

&nbsp;Temperature          0

&nbsp;Humidity             0

&nbsp;SquareFootage        0

&nbsp;Occupancy            0

&nbsp;HVACUsage            0

&nbsp;LightingUsage        0

&nbsp;RenewableEnergy      0

&nbsp;DayOfWeek            0

&nbsp;Holiday              0

&nbsp;EnergyConsumption    0

&nbsp;dtype: int64,

&nbsp;'duplicate\_count': 0,

&nbsp;'outlier\_rows': 1,

&nbsp;'summary\_stats':        Temperature     Humidity  SquareFootage    Occupancy  RenewableEnergy  \\

&nbsp;count  1000.000000  1000.000000    1000.000000  1000.000000      1000.000000   

&nbsp;mean     24.982026    45.395412    1500.052488     4.581000        15.132813   

&nbsp;std       2.836850     8.518905     288.418873     2.865598         8.745917   

&nbsp;min      20.007565    30.015975    1000.512661     0.000000         0.006642   

&nbsp;25%      22.645070    38.297722    1247.108548     2.000000         7.628385   

&nbsp;50%      24.751637    45.972116    1507.967426     5.000000        15.072296   

&nbsp;75%      27.418174    52.420066    1740.340165     7.000000        22.884064   

&nbsp;max      29.998671    59.969085    1999.982252     9.000000        29.965327   

&nbsp;

&nbsp;       EnergyConsumption  

&nbsp;count        1000.000000  

&nbsp;mean           77.055873  

&nbsp;std             8.144112  

&nbsp;min            53.263278  

&nbsp;25%            71.544690  

&nbsp;50%            76.943696  

&nbsp;75%            82.921742  

&nbsp;max            99.201120  }


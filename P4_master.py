import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

####### Input data: #########
reference_temperature = 21.1
reference_frequency = 1

data_iterations = 1000


####### Extracting data: ########
df = pd.read_excel(r'/Users/joakimbonde/Desktop/Pavement mech./Projects/P4_data.xlsx', sheet_name='data')

#Extracting data columns:
df_temp = df['Test Temperature [°C]']
temp = df_temp.unique()
df_freq = df['Frequency [Hz]']

#Normalizing dynamic moduls and phase angle:
df['Dynamic Modulus [MPa]'] = df['Dynamic Modulus [MPa]'] / df[(df['Test Temperature [°C]'] == reference_temperature) & (df['Frequency [Hz]'] == reference_frequency)]['Dynamic Modulus [MPa]'].values[0]
df['Phase Angle [Deg.]'] = df['Phase Angle [Deg.]'] / df[(df['Test Temperature [°C]'] == reference_temperature) & (df['Frequency [Hz]'] == reference_frequency)]['Phase Angle [Deg.]'].values[0]

#Misc:
data_dict = {}

# Creating vector dictionary 
for idx in range(len(temp)):
    v_name = f"T_{temp[idx]}"
    frequency = df[(df['Test Temperature [°C]'] == temp[idx])]['Frequency [Hz]'].values
    modulus = df[(df['Test Temperature [°C]'] == temp[idx])]['Dynamic Modulus [MPa]'].values
    data_dict[v_name] = [frequency, modulus]

 
for idx in range(len(temp)):

    ref_name = f"T_{reference_temperature}"
    ref_array = data_dict[ref_name]

    if temp[idx] != reference_temperature:
        v_name = f"T_{temp[idx]}"
        array = data_dict[v_name]


        print("hej")





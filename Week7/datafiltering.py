import os
import pandas as pd
folder_path = "C:/Users/adity/OneDrive/Desktop/Sixth Semester/CE6018 Seismic Data Analytics/Program/Week7/ReqResampleData"

# Get all files in the folder
files = os.listdir(folder_path)
print(files)

# Filter out directories
files = [file for file in files if os.path.isfile(
    os.path.join(folder_path, file))]

# Now 'files' contains a list of all the files in the folder
print(files)
for file in files:
    filepath = folder_path+"/"+file
    dataframe= pd.read_csv(filepath)
    dataframe.drop(dataframe[(dataframe['T0.010S'] == -999)].index, inplace=True)
    print(dataframe.shape)
    dataframe.to_csv(filepath)

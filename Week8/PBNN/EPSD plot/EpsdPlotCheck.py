# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

folder_path="C:/Users/adity/OneDrive/Desktop/Sixth Semester/CE6018 Seismic Data Analytics/Program/Week8/PBNN/EPSD plot/EPSD_Data/"
# Load the data
freqEnv_actual = pd.read_csv(folder_path+'FreqEnv/Actuals_epoch1000.csv')
freqEnv_prediction = pd.read_csv(folder_path+'FreqEnv/Predictions_epoch1000.csv')


timeEnv_actual = pd.read_csv(folder_path+'TimeEnv/Actuals_epoch1000.csv')
timeEnv_prediction = pd.read_csv(folder_path+'TimeEnv/Predictions_epoch1000.csv')
# print(freqEnv_actual.shape)
# print(freqEnv_prediction.shape)
# print(timeEnv_actual.shape)
# print(timeEnv_prediction.shape)

# %%
#taking only the common RSN in both the actual and predicted data
RSN_FreqEnv_actual= list( freqEnv_actual["RSN"])
RSN_TimeEnv_actual= list( timeEnv_actual["RSN"])

#Taking the common RSN in both the actual and predicted data
common_RSN = list(set(RSN_FreqEnv_actual).intersection(set(RSN_TimeEnv_actual)))

freqEnv_actual = freqEnv_actual[freqEnv_actual["RSN"].isin(common_RSN)]
freqEnv_prediction = freqEnv_prediction[freqEnv_prediction["RSN"].isin(common_RSN)]
timeEnv_actual = timeEnv_actual[timeEnv_actual["RSN"].isin(common_RSN)]
timeEnv_prediction = timeEnv_prediction[timeEnv_prediction["RSN"].isin(common_RSN)]


# %%
#shorting the data based on RSN
freqEnv_actual = freqEnv_actual.sort_values(by=['RSN'])
freqEnv_prediction = freqEnv_prediction.sort_values(by=['RSN'])
timeEnv_actual = timeEnv_actual.sort_values(by=['RSN'])
timeEnv_prediction = timeEnv_prediction.sort_values(by=['RSN'])



#setting the RSN as index
freqEnv_actual = freqEnv_actual.set_index('RSN')
freqEnv_prediction = freqEnv_prediction.set_index('RSN')
timeEnv_actual = timeEnv_actual.set_index('RSN')
timeEnv_prediction = timeEnv_prediction.set_index('RSN')





# %%
Total_RSN=list(freqEnv_actual.index)

req_no=20
row_no = Total_RSN[:req_no]

actual_matrix=[]
prediction_matrix=[]
residuals_matrix=[]
for i in range(req_no):
    freqEnv_actual_row = freqEnv_actual.loc[row_no[i]][9:]
    freqEnv_actual_row = freqEnv_actual_row.apply(lambda x: 10**x)
    freqEnv_prediction_row = freqEnv_prediction.loc[row_no[i]][9:]
    freqEnv_prediction_row = freqEnv_prediction_row.apply(lambda x: 10**x)
    timeEnv_actual_row = timeEnv_actual.loc[row_no[i]][9:]
    timeEnv_actual_row = timeEnv_actual_row.apply(lambda x: 10**x)
    timeEnv_prediction_row = timeEnv_prediction.loc[row_no[i]][9:]
    timeEnv_prediction_row = timeEnv_prediction_row.apply(lambda x: 10**x)
    actual = np.outer(timeEnv_actual_row,freqEnv_actual_row)
    prediction = np.outer(timeEnv_prediction_row,freqEnv_prediction_row)
    actual_matrix.append(actual)
    prediction_matrix.append(prediction)
    residuals_matrix.append(prediction - actual)



# %%



for i in range(req_no):
    #Plotting the actual matrix in 3d and keeping the plots side by side


    fig, (ax1, ax2,ax3) = plt.subplots(1, 3, figsize=(15, 6), subplot_kw={'projection': '3d'})

    x1 = np.arange(actual_matrix[i].shape[0])
    y1 = np.arange(actual_matrix[i].shape[1])
    Y1, X1 = np.meshgrid(y1, x1)  # Changed the order of inputs
    ax1.plot_surface(X1, Y1, actual_matrix[i], cmap='jet')
    ax1.view_init(elev=18, azim=68)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Frequency')
    ax1.set_zlabel('Amplitude')
    ax1.set_title(f'Actual Matrix for RSN {row_no[i]}')

    x2 = np.arange(prediction_matrix[i].shape[0])
    y2 = np.arange(prediction_matrix[i].shape[1])
    Y2, X2 = np.meshgrid(y2, x2)  # Changed the order of inputs
    ax2.plot_surface(X2, Y2, prediction_matrix[i], cmap='jet')
    ax2.view_init(elev=18, azim=68)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Frequency')
    ax2.set_zlabel('Amplitude')
    ax2.set_title( f'Predicted Matrix for RSN {row_no[i]}')


    x3 = np.arange(residuals_matrix[i].shape[0])
    y3 = np.arange(residuals_matrix[i].shape[1])
    Y3, X3 = np.meshgrid(y3, x3)  # Changed the order of inputs
    ax3.plot_surface(X3, Y3, residuals_matrix[i], cmap='jet')
    ax3.view_init(elev=-164, azim=-76)
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Frequency')
    ax3.set_zlabel('Amplitude')
    ax3.set_title(f'Residuals Matrix for RSN {row_no[i]}')

    plt.tight_layout() # Adjust the subplots to give some space
    plt.show()



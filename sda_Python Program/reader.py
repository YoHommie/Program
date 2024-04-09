from scipy.io import loadmat

file_path = r"C:/Users/adity/OneDrive/Desktop/Sixth Semester/CE6018 Seismic Data Analytics/Program/sda_Python Program/RSN1_X.mat"
data = loadmat(file_path)


# data= loadmat("RSN1_X")

print(len(data["resampledSignal"][0]))
import pandas as pd
import numpy as np

def Testing1(X, thresh):
    labels = []
    m = 0
    for i in range(X.shape[0]):
        indexes = np.nonzero(X[i])
        Avg_P = np.mean(X[i][indexes])
        if Avg_P > float(thresh):

            m += 1
            labels.append(1)
        else:
            labels.append(0)

    return [m] + labels

Data  = pd.read_csv("level_1_input/level_1_4.csv", skiprows=2, header=None)
Data = np.array(Data)
T = int(pd.read_csv("level_1_input/level_1_4.csv", on_bad_lines="skip").iloc[0])
Result = Testing1(Data, T)
pd.DataFrame(Result).to_csv("level_1_output/level_1_4.csv", index=False, header=False)

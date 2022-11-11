import os
import pandas as pd
from sklearn.preprocessing import StandardScaler


def structure_data():
    with open("data/value_target.csv", "w") as f:
        f.write("")

    with open("data/value_target.csv", "a") as f:
        header = "target"
        for i in range(1, 1001):
            header = header + ",value_" + str(i)
        f.write(header + "\n")

    # iter over every file from a folder
    for filename in os.listdir("data/standards_warm/"):
        # open file
        df_standards_warm = pd.read_csv("data/standards_warm/" + filename)
        # get the number which appears at the end between _...csv
        number = filename.split("_")[-1].split(".")[0]
        # get the values from the column value
        values = df_standards_warm["Value"]
        # create a new file with the name data_max/file
        with open("data/value_target.csv", "a") as f:
            # write the number which appears at the end between _...csv in a row of data/data_max/file
            f.write(number)
            # write a comma
            f.write(",")
            # write the values from the column value in a row of data/data_max/file
            f.write(",".join(str(x) for x in values))
            # write a new line
            f.write("\n")

    # iter over every file from a folder
    for filename in os.listdir("data/warm_standards_hamilton"):
        # open file
        df_standards_warm = pd.read_csv("data/warm_standards_hamilton/" + filename)
        # get the number which appears at the end between _...csv
        number = filename.split("_")[-1].split(".")[0]
        # get the values from the column value
        values = df_standards_warm["Value"]
        # create a new file with the name data_max/file
        with open("data/value_target.csv", "a") as f:
            # write the number which appears at the end between _...csv in a row of data/data_max/file
            f.write(number)
            # write a comma
            f.write(",")
            # write the values from the column value in a row of data/data_max/file
            f.write(",".join(str(x) for x in values))
            # write a new line
            f.write("\n")


def get_data_unscaled():
    df_value_target = pd.read_csv("data/value_target.csv")
    test = df_value_target.tail(8)
    train = df_value_target.drop(df_value_target.tail(8).index)
    test_x = test.drop("target", axis=1)
    test_y = test["target"]
    train_x = train.drop("target", axis=1)
    train_y = train["target"]
    return train_x, test_x, train_y, test_y


def get_data_scaled():
    train_x, test_x, train_y, test_y = get_data_unscaled()    
    test_x = pd.DataFrame(test_x)
    test_y = pd.DataFrame(test_y)
    train_x = pd.DataFrame(train_x)
    train_y = pd.DataFrame(train_y)
    object= StandardScaler()    
    train_x_scale = object.fit_transform(train_x)
    train_y_scale = object.fit_transform(train_y)
    test_x_scale = object.fit_transform(test_x)
    test_y_scale = object.fit_transform(test_y)
    return train_x_scale, test_x_scale, train_y_scale, test_y_scale

if __name__ == "__main__":
    '''structure_data()
    train_x, test_x, train_y, test_y = get_data_unscaled()
    train_x, test_x, train_y, test_y = get_data_scaled()
    get_data_scaled()'''
    get_data_scaled()

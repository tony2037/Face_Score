import glob
import cv2
import numpy as np
import json


def load_data(x_path="./dataset/x/", y_path="./dataset/y/"):
    X_Train = None
    X_Test = None
    y_Train = None
    y_Test = None
    x_size = (256,256,3)

    x_list = glob.glob(x_path + "*.jpg")
    y_list = glob.glob(y_path + "*.json")
    assert len(x_list) == len(y_list)

    X_Train = np.zeros((len(x_list), x_size[0], x_size[1], x_size[2]))
    y_Train = []
    
    for i in range(0, len(x_list)):
        img = cv2.imread(x_list[i])
        img = cv2.resize(img, (x_size[0],x_size[1]), interpolation=cv2.INTER_LINEAR)
        assert img.shape == x_size
        X_Train[i] = img
        
    assert X_Train.shape == (len(x_list), 256, 256, 3)

    for i in range(0 , len(y_list)):
        with open(y_list[i],"r") as f:
            data = json.load(f)
            y_Train.append([data["score"]])

    y_Train = np.array(y_Train)
    #y_Train = np.reshape(y_Train,[y_Train.shape[0]])


    return (X_Train, y_Train), (X_Test, y_Test)


if __name__ == "__main__":
    load_data(x_path="./dataset/x/", y_path="./dataset/y/")

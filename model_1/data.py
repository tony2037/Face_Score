import glob


def load_data(x_path="",y_path=""):
    X_Train = None
    X_Test = None
    y_Train = None
    y_Test = None

    x_list = glob.glob(x_path + "*.jpg")
    print x_list
    return (X_Train, y_Train), (X_Test, y_Test)


if __name__ == "__main__":
    load_data(x_path="../dataset/x/")
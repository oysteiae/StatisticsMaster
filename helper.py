from os import listdir as _listdir, getcwd, mkdir, path
from os.path import isfile as _isfile,join as  _join, abspath, splitext

def sort_func(s):
   sort_string = s.split('/')[-1].rstrip()
   return sort_string


def load_files(data_file_location):
    data = []

    startswith = None
    endswith = None
    contains = None
    contains_not = None

    for path in data_file_location:
        gg = [(_join(path, f) if path != "." else f) for f in _listdir(path) if
              _isfile(_join(path, f)) and (startswith == None or f.startswith(startswith)) and (
              endswith == None or f.endswith(endswith)) and (contains == None or contains in f) and (
              contains_not == None or (not (contains_not in f)))]
        data.append(gg)

    combined_list = []
    # Sort the lists:
    for i in range(len(data)):
        elem = sorted(data[i])
        combined_list = combined_list + elem

    combined_list = strip_files_of_doubles(combined_list)
    combined_list = sorted(combined_list, key=sort_func)
    return combined_list

def strip_files_of_doubles(files):
    new_files = []
    for file in files:
        split = file.split('.')
        if (split[-1] != "img" and split[-1] != "mat"):
            new_files.append(file)

    return new_files

def compute_scores(pred, label):
    assert pred.shape == label.shape, "Shape mismatch between prediction and label when calculating scores"
    shape = pred.shape
    TP = 0.0
    TN = 0.0
    FP = 0.0
    FN = 0.0

    for i in range(0, shape[0]):
        if (i % 25 == 0):
            print("Comleted", float(i) / float(shape[0]) * 100, "%")
        for j in range(0, shape[1]):
            for k in range(0, shape[2]):
                if (pred[i][j][k] == 1 and label[i][j][k] >= 1):
                    TP += 1
                elif (pred[i][j][k] == 1 and label[i][j][k] == 0):
                    FP += 1
                elif (pred[i][j][k] == 0 and label[i][j][k] >= 1):
                    FN += 1
                elif (pred[i][j][k] == 0 and label[i][j][k] == 0):
                    TN += 1


    print(TP)
    print(TN)
    print(FP)
    print(FN)

    if ((2 * TP + FP + FN) == 0):
        dice_coefficient = 1.0
    else:
        dice_coefficient = float((2 * TP)) / float((2 * TP + FP + FN))
    if ((TP + FN) == 0):
        sensitivity = 1.0
    else:
        sensitivity = float(TP) / float((TP + FN))
    if ((TN + FP) == 0):
        specificity = 1.0
    else:
        specificity = float(TN) / float((TN + FP))

    return dice_coefficient, sensitivity, specificity
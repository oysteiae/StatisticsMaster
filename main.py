import os
from os import listdir as _listdir, getcwd, mkdir, path
from os.path import isfile as _isfile,join as  _join, abspath, splitext
import numpy as np
import nibabel as nib
import argparse

# Taken from https://github.com/GUR9000/Deep_MRI_brain_extraction
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

    return combined_list

def compute_scores(pred, label):
    assert pred.shape == label.shape, "Shape mismatch between prediction and label when calculating scores"
    print(label.shape)
    print(pred.shape)
    shape = pred.shape
    TP = 0
    TN = 0
    FP = 0
    FN = 0

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

    if ((2 * TP + FP + FN) == 0):
        dice_coefficient = 1.0
    else:
        dice_coefficient = (2 * TP) / (2 * TP + FP + FN)
    if ((TP + FN) == 0):
        sensitivity = 1.0
    else:
        sensitivity = TP / (TP + FN)
    if ((TN + FP) == 0):
        specificity = 1.0
    else:
        specificity = TN / (TN + FP)

    return dice_coefficient, sensitivity, specificity

def compute_dice_sen_spe_deep_medic(save_name, path_to_deep_medic_predictions, label_names_file):
    score_file = open(save_name + "_scores.tsv", 'w')
    score_file.write("name\tdcs\tsen\tspe\n")

    deep_medic_predictions = load_files(path_to_deep_medic_predictions)
    deep_medic_brain_masks = []

    for file in deep_medic_predictions:
        a = file.split('_')
        if(a[-1] == "Segm.nii.gz"):
            deep_medic_brain_masks.append(file)

    deep_medic_brain_masks = sorted(deep_medic_brain_masks)
    label_names = open(label_names_file, 'r')
    i = 0
    for name in label_names:
        name = name.rstrip()
        print("Label:", name)
        print("Prediction:", deep_medic_brain_masks[i])
        pred = nib.load(deep_medic_brain_masks[i])
        label = nib.load(name)

        dsc, sen, spe = compute_scores(pred.get_data(), label.get_data())
        score_file.write(name + "\t" + str(dsc) + "\t" + str(sen) + "\t" + str(spe) + "\n")
        i += 1

def main():
    parser = argparse.ArgumentParser(description='Evaluating deepmedic')
    parser.add_argument('--savename', dest='save_name', required=True, type=str, help='Path to the corresponding labels')
    parser.add_argument('--predictions', dest='predictions', required=True, type=str, nargs='+', help='Path to the data')
    parser.add_argument('--labelfilenames', dest='label_file_names', required=True, type=str, help='Path to the corresponding labels')
    args = parser.parse_args()

    compute_dice_sen_spe_deep_medic(args.save_name, args.predictions, args.label_file_names)

main()
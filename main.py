import os
from os import listdir as _listdir, getcwd, mkdir, path
from os.path import isfile as _isfile,join as  _join, abspath, splitext
import numpy as np
import nibabel as nib
import argparse
from compute_scores import compute_scores

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

def sort_func(s):
   sort_string = s.split('/')[-1]
   return sort_string

def compute_dice_sen_spe_deep_medic(save_name, path_to_deep_medic_predictions, label_names_file):
    score_file = open(save_name + "_scores.tsv", 'w')
    score_file.write("name\tdcs\tsen\tspe\n")

    deep_medic_predictions = load_files(path_to_deep_medic_predictions)
    deep_medic_brain_masks = []

    for file in deep_medic_predictions:
        a = file.split('_')
        if(a[-1] == "Segm.nii.gz"):
            deep_medic_brain_masks.append(file)

    deep_medic_brain_masks = sorted(deep_medic_brain_masks, key=sort_func)
    label_names = open(label_names_file, 'r')
    
    label_names_list = []
    for name in label_names:
        label_names_list.append(name)

    label_names_list = sorted(label_names_list, key=sort_func)
    
    i = 0
    for name in label_names_list:
        name = name.rstrip()
        print("Label:", name)
        print("Prediction:", deep_medic_brain_masks[i])
        pred = nib.load(deep_medic_brain_masks[i]).get_data()
        label = nib.load(name).get_data()
        pred = (pred > 0).astype('int16')
        label = (label > 0).astype('int16')
        dsc, sen, spe = compute_scores(pred, label)
        print(dsc)
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

from helper import load_files
import numpy as np
from os.path import basename
import pickle
import locale



def sort_func(s):
   sort_string = s.split('/')[-1].rstrip()
   return sort_string

def reverse_engineer(experimentDirectory, data_directory):
    train_channels_location = experimentDirectory + "/train/trainChannels_t1c.cfg"
    validation_channels_location = experimentDirectory + "/train/validation/validationChannels_t1c.cfg"
    test_channels_location = experimentDirectory + "/test/testChannels_t1c.cfg"

    train_channels = []
    validation_channels = []
    test_channels = []
    locale.setlocale(locale.LC_ALL, "C")
    with open(train_channels_location) as f:
        lines = f.read().splitlines()
        for l in lines:
            train_channels.append(l)
    with open(validation_channels_location) as f:
        lines = f.read().splitlines()
        for l in lines:
            validation_channels.append(l)
    with open(test_channels_location) as f:
        lines = f.read().splitlines()
        for l in lines:
            test_channels.append(l)

    data_base = np.asarray(load_files(data_directory))

    train_channels = [d.replace('_processed', '') for d in train_channels]
    validation_channels = [d.replace('_processed', '') for d in validation_channels]
    test_channels = [d.replace('_processed', '') for d in test_channels]

    train_channels = sorted(train_channels)
    validation_channels = sorted(validation_channels)
    test_channels = sorted(test_channels)

    data = np.asarray([basename(d) for d in data_base])
    train_channels = [basename(d) for d in train_channels]
    validation_channels = [basename(d) for d in validation_channels]
    test_channels = [basename(d) for d in test_channels]

    data = np.asarray([d.split('.')[0] for d in data])
    train_channels = [d.split('.')[0] for d in train_channels]
    validation_channels = [d.split('.')[0] for d in validation_channels]
    test_channels = [d.split('.')[0] for d in test_channels]

    training_indices = []
    validation_indices = []
    testing_indices = []

    for i in range(0, len(data)):
        if(data[i] in train_channels):
            training_indices.append(i)

        elif(data[i] in validation_channels):
            validation_indices.append(i)

        elif(data[i] in test_channels):
            testing_indices.append(i)

    for line in data_base[testing_indices]:
        print(line)

    print()

    for line in test_channels:
        print(line)

    # experiment_directory = "D:\\Master\\ExperimentIndices\\"
    # save_name = "AllDataNotResampled"
    # with open(experiment_directory + save_name + "\\training_indices" + save_name + ".txt", "wb") as tr:
    #     pickle.dump(training_indices, tr)
    # with open(experiment_directory + save_name +  "\\validation_indices" + save_name + ".txt", "wb") as va:
    #     pickle.dump(validation_indices, va)
    # with open(experiment_directory + save_name + "\\testing_indices" + save_name + ".txt", "wb") as te:
    #     pickle.dump(testing_indices, te)

    print(len(validation_indices + testing_indices + training_indices))

reverse_engineer("D:/deepmedic/examples/configFiles/configAllDataNotResampled", ["D:\\MRISCANS\\StOlavsResampled\\data\\", "D:\\MRISCANS\\OASIS\\data\\", "D:\\MRISCANS\\LBPA40Resampled\\data\\"])
# reverse_engineer("D:/deepmedic/examples/configFiles/configStOlavs", ["D:\\MRISCANS\\StOlavsResampled\\data\\"])
# D:\\MRISCANS\\NormalizedStOlavsResampled\\data\\ D:\\MRISCANS\\NormalizedOASIS\\data\\ D:\\MRISCANS\\NormalizedLBPA40Resampled\\data\\
# reverse_engineer("D:/deepmedic/examples/configFiles/configAllDataNotResampled", ["D:\\MRISCANS\\NormalizedStOlavsResampled\\data\\", "D:\\MRISCANS\\NormalizedOASIS\\data\\", "D:\\MRISCANS\\NormalizedLBPA40Resampled\\data\\"])
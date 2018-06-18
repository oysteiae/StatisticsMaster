import matplotlib.pyplot as plt
import numpy as np
import csv

def read_scores(path_to_file, index):
    scores = []

    with open(path_to_file, 'r') as log:
        log = csv.reader(log, delimiter='\t')
        first = True

        for row in log:
            if(first):
                first = False
                continue
            scores.append(float(row[index]))

    return scores

def box_plot(path_to_scores_cnn, path_to_scores_unet, path_to_scores_deepmedic, index):
    bottom = 0.7
    top = 1.0

    cnn_scores = read_scores(path_to_scores_cnn, index)
    unet_scores = read_scores(path_to_scores_unet, index)
    deepmedic_scores = read_scores(path_to_scores_deepmedic, index)

    data_to_plot = [cnn_scores, unet_scores, deepmedic_scores]

    fig = plt.figure(1, figsize=(9, 6))
    # Create an axes instance
    ax = fig.add_subplot(111)
    # Create the boxplot
    bp = ax.boxplot(data_to_plot)

    architectures = ["CNN", "U-Net", "DeepMedic"]
    ax.set_ylim(bottom, top)
    ax.set_xticklabels(architectures,
                        rotation=45, fontsize=8)
    plt.show()

box_plot( "D:\\Master\\DefinitiveFinalExperiments\\CNNAllDataNotResampled\\testing_indices_CNNAllDataNotResampled_scores.tsv", "D:\\Master\\DefinitiveFinalExperiments\\UnetFinalDataNotResampled\\testing_indices_UnetFinalDataNotResampled_scores.tsv", "D:\\Master\\deepmedicexperiments\\DeepMedicAllDataNotResampled_scores.tsv", 1)
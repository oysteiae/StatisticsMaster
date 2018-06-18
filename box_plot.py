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
    ax.set_ylabel("Dice score", fontsize=12)
    ax.set_xlabel("Architecture", fontsize=12)

    architectures = ["CNN", "U-Net", "DeepMedic"]
    ax.set_ylim(bottom, top)
    ax.set_xticklabels(architectures,
                        rotation=45, fontsize=15)

    plt.gcf().subplots_adjust(bottom=0.21)
    plt.show()
    fig.savefig("C:\\Users\\oyste\\Documents\\Master\\graphs\\BoxPlotAll.png")

box_plot("C:\\Users\\oyste\\Documents\\Master\\ExperimentsFinal\\CNNAllFinal\\testing_indices_CNNAllFinal_scores.tsv", "C:\\Users\\oyste\\Documents\\Master\\ExperimentsFinal\\UnetAllFinal\\testing_indices_UnetAllFinal_scores.tsv", "C:\\Users\\oyste\\Documents\\Master\\deepmedicExperiments\\scores\\DeepMedicAll_scores.tsv", 1)
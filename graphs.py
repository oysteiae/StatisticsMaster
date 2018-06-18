import csv
import numpy as np
import matplotlib.pyplot as plt

# experiment_5_x, experiment_5_y = get_y_and_x_lists('C:\\Users\\oyste\\Documents\\Visual Studio 2015\\Projects\\SkullStripping\\BrainSegmentationStOlavs\\SkullStripping\\both_datasets_crossvalidation_logs1.tsv', 'C:\\Users\\oyste\\Documents\\Visual Studio 2015\\Projects\\SkullStripping\\BrainSegmentationStOlavs\\SkullStripping\\both_datasets_crossvalidation_logs2.tsv', 5)
def get_y_and_x_lists(logs1, logs2, index):
    x_1 = []
    y_1 = []
    time_1 = []
    n = 500
    with open(logs1, 'rb') as tsvin1, open(logs2, 'rb') as tsvin2:
        tsvin1 = csv.reader(tsvin1, delimiter='\t')
        tsvin2 = csv.reader(tsvin2, delimiter='\t')

        i = 0
        average_per_n_epoch = 0
        for row in tsvin1:
            if(i != 0):
                average_per_n_epoch += float(row[index])
                if i % n == 0:
                    y_1.append(average_per_n_epoch/n)
                    x_1.append(float(row[0]))
                    time_1.append(float(row[3]))
                    average_per_n_epoch = 0
            i+=1

        x_2 = []
        y_2 = []
        time_2 = []
        i = 0
        average_per_n_epoch = 0
        for row in tsvin2:
            if(i != 0):
                average_per_n_epoch += float(row[index])
                if i % n == 0:
                    y_2.append(average_per_n_epoch/n)
                    x_2.append(float(row[0]))
                    time_2.append(float(row[3]))
                    average_per_n_epoch = 0
            i+=1

    y = [(x + y)/2 for x, y in zip(y_1, y_2)]
    # Lazy way of getting the x list that matches the y list
    x = [i for i, j in zip(x_1, x_2)]
    print ((time_1[-1] - time_1[0]) + (time_2[-1] - time_2[0])) / 2

    return x, y

def graph_accuracy(file_name, index):
    x = []
    y = []
    log_avg_point_per = 500
    accumulated_y = 0

    with open(file_name, 'r') as log:
        log = csv.reader(log, delimiter='\t')
        first = True

        for row in log:
            if(first):
                first = False
                continue
            accumulated_y += float(row[index])
            if(int(row[0]) % log_avg_point_per == 0):
                x.append(int(row[0]))
                y.append(accumulated_y / log_avg_point_per)
                accumulated_y = 0

    return x, y


def get_time_and_epochs(file_name):
    epoch = []
    time = []
    time_per_epoch = []
    with open(file_name, 'r') as log:
        log = csv.reader(log, delimiter='\t')
        first = True
        i = 0
        for row in log:
            if(first):
                first = False
                continue
            epoch.append(int(row[0]))
            time.append(float(row[3]))
            if(i > 1):
                time_per_epoch.append(time[-1] - time[-2])
            i += 1

    print("%.5f" % (sum(time_per_epoch)/len(time_per_epoch)))

    return epoch, time

def graph_loss_and_val_loss(logs_file_location):
    x, y = graph_accuracy(logs_file_location, 2)
    val_x, val_y = graph_accuracy(logs_file_location, 4)

    plt.plot(x, y)
    plt.plot(val_x, val_y)

    plt.legend(['Loss', 'Validation loss'])

    plt.show()

def graph_acc_and_val_acc(logs_file_location):
    x, y = graph_accuracy(logs_file_location, 1)
    val_x, val_y = graph_accuracy(logs_file_location, 5)

    plt.plot(x, y)
    plt.plot(val_x, val_y)

    plt.legend(['Accuracy', 'Validation accuracy'])
    plt.show()

def graph_time_and_epochs(file_name):
    epoch = []
    time = []
    time_per_epoch = []
    with open(file_name, 'r') as log:
        log = csv.reader(log, delimiter='\t')
        first = True
        i = 0
        for row in log:
            if(first):
                first = False
                continue
            epoch.append(int(row[0]))
            time.append(float(row[3]))
            if(i > 1):
                time_per_epoch.append(time[-1] - time[-2])
            i += 1

    print("%.5f" % (sum(time_per_epoch)/len(time_per_epoch)))

    return epoch, time

>>>>>>> bbfcee33e2f3b46d9bf93bb4990f5afd5699d1c9
# graph_accuracy("D:\\Master\\Experiments\\UnetBiggerPatch\\UnetBiggerPatch_logs.tsv", 1)
def show_graph_accuracy():
    # graph_acc_and_val_acc("D:\\Master\\DefinitiveFinalExperiments\\UnetOnlyOASIS32Final\\UnetOnlyOASIS32Final_logs.tsv")
    graph_time_and_epochs("D:\\Master\\AllExperiments\\CNNTest1GPUs\\CNNTest1GPUs_logs.tsv")
    # graph_acc_and_val_acc("D:\\Master\\DefinitiveFinalExperiments\\UnetFinalLBPA40\\UnetFinalLBPA40_logs.tsv")
    # graph_acc_and_val_acc("D:\\Master\\DefinitiveFinalExperiments\\UnetOnlyOASIS64Final\\UnetOnlyOASIS64Final_logs.tsv")
    # graph_acc_and_val_acc("D:\\Master\\DefinitiveFinalExperiments\\UnetOnlyOASIS32Final\\UnetOnlyOASIS32Final_logs.tsv")
    # graph_acc_and_val_acc("D:\\Master\\DefinitiveFinalExperiments\\UnetOnlyOASIS64Final\\UnetOnlyOASIS64Final_logs.tsv")
    # graph_acc_and_val_acc("D:\\Master\\DefinitiveFinalExperiments\\UnetOnlyStOlavsFinal\\UnetOnlyStOlavsFinal_logs.tsv")
    # graph_loss_and_val_loss("D:\\Master\\DefinitiveFinalExperiments\\UnetOnlyOASIS32Final\\UnetOnlyOASIS32Final_logs.tsv")
    # graph_loss_and_val_loss("D:\\Master\\DefinitiveFinalExperiments\\UnetFinalLBPA40\\UnetFinalLBPA40_logs.tsv")
    #
    # graph_acc_and_val_acc("D:\\Master\\DefinitiveFinalExperiments\\UnetFinalDataNotResampled\\UnetFinalDataNotResampled_logs.tsv")
    # graph_loss_and_val_loss("D:\\Master\\DefinitiveFinalExperiments\\Unet40FromAll\\Unet40FromAll_logs.tsv")
    # graph_acc_and_val_acc("D:\\Master\\DefinitiveFinalExperiments\\UnetSmallerPatchStOlavsLBPA40\\UnetSmallerPatchStOlavsLBPA40_logs.tsv")
    # graph_acc_and_val_acc("D:\\Master\\DefinitiveFinalExperiments\\UnetSmallerPatchStOlavsOASIS\\UnetSmallerPatchStOlavsOASIS_logs.tsv")

    # graph_accuracy("D:\\Master\\Experiments\\UnetLITS\\UnetLITS_logs.tsv", 2)
    # graph_accuracy("D:\\Master\\Experiments\\CNNLITS\\CNNLITS_logs.tsv", 2)
    # graph_loss_and_val_loss("C:\\Users\\oyste\\Documents\\Master\\AllExperimentsEpic\\Experiments\\CNNAll\\CNNAll_logs.tsv")
    # graph_loss_and_val_loss("C:\\Users\\oyste\\Documents\\Master\\AllExperimentsEpic\\Experiments\\UnetAll\\UnetAll_logs.tsv")

    graph_acc_and_val_acc("C:\\Users\\oyste\\Documents\\Master\\FinalExperiments\\UnetAllFinal\\UnetAllFinal_logs.tsv")

    # plt.xlim((0,60000))
    # plt.ylim((0,7000))

    # plt.title("CNN 16 batches")
    # plt.ylabel("Time")
    # plt.xlabel("Update step")
    #
    # plt.plot(x_1, y_1)
    # plt.plot(x_2, y_2)
    # plt.plot(x_3, y_3)
    # plt.plot(x_4, y_4)
    #
    # plt.legend(['1 Tesla P100', '2 Tesla P100', 'Titan X'], loc='lower right')
    #
    # plt.show()



show_graph_accuracy()
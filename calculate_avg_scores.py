import numpy as np
import csv

def find_average_dcs(filename):
    with open(filename, 'r') as tsvin: #, open('new.csv', 'wb') as csvout:
        tsvin = csv.reader(tsvin, delimiter='\t')
        i = 0
        dcs_list = []
        sen_list = []
        spe_list = []
        num = 0
        for row in tsvin:
            if(i != 0):
                num += 1
                dcs_list.append(float(row[1]))
                sen_list.append(float(row[2]))
                spe_list.append(float(row[3]))
            i += 1
        print(i)
        print(num)
        average_dcs = sum(dcs_list)/len(dcs_list)
        average_sen = sum(sen_list)/len(sen_list)
        average_spe = sum(spe_list)/len(spe_list)

        print("Dice $" + "%.5f" % average_dcs + " \\pm " +  "%.5f" % np.std(dcs_list) + "$")
        print("Sen $" + "%.5f" % average_sen + " \\pm " +  "%.5f" % np.std(sen_list) + "$")
        print("spe $" + "%.5f" % average_spe + " \\pm " +  "%.5f" % np.std(spe_list) + "$")

find_average_dcs("C:\\Users\\oyste\\Documents\\Master\\deepmedicExperiments\\DeepMedicLITS.tsv")
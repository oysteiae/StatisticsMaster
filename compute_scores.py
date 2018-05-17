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
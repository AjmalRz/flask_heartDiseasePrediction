import math
from tkinter import Tk, Label, Entry

import numpy as np

from collections import Counter




class CKNN:

    def __init__(self):
        self.accurate_predictions = 0
        self.total_predictions = 0
        self.accuracy = 0.0
        ##########

        lines=[]
        training_data=np.loadtxt("static/heart_dataset.txt",dtype=str,delimiter=" ")




        self.training_set= { '0':[],'1':[],'2':[],'3':[],'4':[]}

        #Split data into training and test for cross validation
        #training_data = lbls[: len(lbls)]
        test_data = []#[-int(test_size * len(dataset)):]

        #Insert data into the training set
        cnt=0

        for record in training_data:
            print(record)

            if record[0]!='':
                lis=[]
                lis.append(int(record[0]))
                lis.append(int(record[1]))
                lis.append(int(record[2]))
                lis.append(int(record[3]))
                lis.append(int(record[4]))
                lis.append(int(record[5]))
                lis.append(int(record[6]))
                lis.append(int(record[7]))
                lis.append(int(record[8]))
                lis.append(int(record[9]))
                lis.append(int(record[10]))
                lis.append(int(record[11]))
                lis.append(int(record[12]))


            # st=lines[cnt][0]
            # cnt+=1
            #
            # print(st)
                self.training_set[record[13]].append( lis)

    #########

    def predict(self,  to_predict, k = 1):


        distributions = []
        for group in self.training_set:
            i=0
            # print(group,'group')
            for features in self.training_set[group]:

                euclidean_distance = np.linalg.norm(np.array(features)- np.array(to_predict))

                distributions.append([euclidean_distance, group])

        # print(distributions)
        results = [i[1] for i in sorted(distributions)[:k]]
        result = Counter(results).most_common(1)[0][0]
        # print("rs",results,self.training_set.keys())
        confidence = Counter(results).most_common(1)[0][1]/k

        return result, confidence



def prep(data):



    feat=data
    knn = CKNN()
    res=knn.predict(feat)


    return res[0]

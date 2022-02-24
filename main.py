
import pandas as pd
import math
import numpy as np
import os


class HRVDatum:
    munix_epoch = 0
    mbbi = 0

    def __init__(self, epoch, bbi):
        self.munix_epoch = int(epoch)
        self.mbbi = int(bbi)

    def __str__(self):
        return 'Unix Epoch: ' + str(self.munix_epoch) + ', Beat-to-Beat Interval: ' + str(self.mbbi)


# arguments: a list of HRVDatum objects
# returns: the standard deviation of the bbis from the input list
def stddev(HRVs):
    average = 0
    for i in HRVs:
        average += i.mbbi
    average /= len(HRVs)
    std = 0
    for i in HRVs:
        std += ((i.mbbi - average) ** 2)
    return math.sqrt(std / len(HRVs))


# arguments: a list of HRVDatum objects
# returns: the root mean square of successive differences of the bbis from the input list
def rmssd(HRVs):
    prev = HRVs[0].mbbi
    sqdiff = 0
    for i in range(1, len(HRVs)):
        sqdiff += (HRVs[i].mbbi - prev) ** 2
        prev = HRVs[i].mbbi
    return np.log(math.sqrt(sqdiff / len(HRVs)))


if __name__ == '__main__':
    directory = os.fsencode('source/')
    for file in os.listdir(directory):  # read each file in the source directory
        ifile = os.fsdecode(file)
        ofile = 'results/' + ifile[:10] + '_results.csv'
        df = pd.read_csv('source/' + ifile)
        data = []
        five_minute_interval = []
        epoch = 0
        d = {'standard deviation': [], 'rmssd': []}

        for index, row in df.iterrows():
            tempdata = HRVDatum(row['unix_epoch_in_miliseconds'], row['bbi'])
            five_minute_interval.append(tempdata)
            if epoch == 0:
                epoch = tempdata.munix_epoch
            elif tempdata.munix_epoch - epoch >= 300000:  # five_minute_interval now contains 5 minutes of data
                data.append(five_minute_interval[:])
                epoch = 0
                five_minute_interval.clear()
        data.append(five_minute_interval)   # the last interval will almost certainly be < 5 minutes

        for i in data:
            d['standard deviation'].append(stddev(i))
            d['rmssd'].append(rmssd(i))
        df = pd.DataFrame(data=d)
        df.to_csv(ofile)

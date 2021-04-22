import sys, os, re
import json
import numpy as np
import math


def main():
    # existed = open("existed.txt", "r")
    # exist_list = existed.read().split(',')
    path1 = '../../scratch.1/covidtweets_before_july/covidtweets_1/'
    path2 = 'covid_before_july/'
    files = os.listdir(path1)
    print(len(files))
    for file in files:
        # if file not in exist_list:
        file_name, file_extension = os.path.splitext(file)
        records = []
        if file_extension == '.json':
            print("Start: " + file)
            for line in open(path1 + file, 'r'):
                try:
                    records.append(json.loads(line))
                except:
                    continue

            count = len(records)
            sample_ratio = 0.01
            sample_count = math.ceil(count * sample_ratio)

            sample_indexes = np.random.choice(
              count,
              sample_count
            )
            # sample_indexes = np.random.randint(0, count, sample_count)

            sample_records = []
            for sample_index in sample_indexes:
                sample_record = records[sample_index]
                sample_records.append(sample_record)

            assert len(sample_records) == sample_count

            with open(path2 + file, "w") as f2:
                for record in sample_records:
                    f2.write(json.dumps(record) + "\n")
        else:
            continue

        print("Finished: " + str(file))
        print("Sampled {} records from {} original records.".format(
          sample_count,
          count
        ))



if __name__ == '__main__':
    main()


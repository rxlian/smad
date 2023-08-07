import pandas as pd
import tqdm as tqdm
import json

def main():
    df = pd.read_csv('mri_conversion.csv', low_memory=False)
    variables = list(df.columns)[1:]
    cnt = 0
    for var in variables:
        f = open('code_book.txt', 'a')
        print(f"\n{var}", file=f)
        keys = list(df[var].value_counts().keys())
        values = [i for i in range(1, len(keys)+1)]
        mapping = dict(zip(keys, values))
        df[var] = df[var].map(mapping)
        with open('code_book.txt', 'a') as file:
            file.write(json.dumps(mapping))
    df = df.fillna(999)
    df.to_csv('all_mri_conversion_numeric.csv', index=False)

if __name__ == '__main__':
    main()

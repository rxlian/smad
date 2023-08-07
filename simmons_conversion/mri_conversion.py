import pandas as pd
from tqdm import tqdm
import numpy as np

def main():
    code = pd.read_csv('code.csv')
    respondent = pd.read_csv('respondent.csv')
    responses = pd.read_csv('responses.csv')

    super_vars = list(code['Super'].value_counts().keys())
    newdf = pd.DataFrame(data={'Resp': [i for i in range(1, len(respondent)+1)]})
    for var in tqdm(super_vars):
        category_vars = list(code[code['Super']==var]['Category'].value_counts().keys())
        for categ in category_vars:
            name = str(var) + str(categ)
            sub_code = code[(code['Super']==str(var))&(code['Category']==str(categ))]
            group = sub_code.groupby(['QID', 'DID'])['Detail1'].first().reset_index()
            merge = responses.merge(group, on=['QID', 'DID'], how='inner')
            merge_res = respondent.merge(merge[['Resp', 'Detail1']], on='Resp', how='left')
            merge_res = merge_res.rename(columns={'Detail1': name})
            merge_res2 = merge_res.groupby('Resp')[name].first().reset_index()
            newdf[name] = merge_res2[name].tolist()
    newdf.to_csv('mri_conversion.csv', index=False)

if __name__=='__main__':
    main()

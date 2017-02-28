
# coding: utf-8

# In[185]:

import pandas as pd


# In[186]:

xls_file = pd.ExcelFile('data/tom/ExampleSNPTable.xlsx') 
df = xls_file.parse("Sheet1", header=None)

# get genes
gene_df = pd.DataFrame(df.iloc[0:1,:])
gene_df = gene_df.to_dict('records')
gene_df = gene_df[0]
# print(gene_df)

# get rs
rs_df = pd.DataFrame(df.iloc[1:2,:])
rs_df = rs_df.to_dict('records')
rs_df = rs_df[0]
# print(rs_df)

# get samples
samples_df = pd.DataFrame(df.iloc[2:,:])


# In[189]:

def refactor_sample_record(x):
    sample_dict = dict(name=x[0])
    characteristics = list()
    
    for i in range(1, len(x)):
        characteristics.append(dict(gene=gene_df[i],rs=rs_df[i],snp=x[i]))
    
    sample_dict['characteristics'] = characteristics
    return sample_dict


# In[197]:

v = samples_df.apply(lambda row: refactor_sample_record(row), axis=1)
v = list(v)
v
# print(type(v))


# In[106]:

# view the excel file's sheet names
xls_file.sheet_names


# In[107]:

# load the xls file's Sheet1 as a dataframe
df = xls_file.parse('Sheet1')
# list(df)
# get columns
df.head(4)
# gene_names = df.columns.values.tolist()
# df.columns.values.tolist()


# In[ ]:




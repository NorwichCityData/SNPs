import pandas as pd

xls_file = pd.ExcelFile('data/tom/ExampleSNPTable.xlsx') # point this to the spreadsheet on your local
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



def refactor_sample_record(x):
    sample_dict = dict(name=x[0])
    characteristics = list()
    
    for i in range(1, len(x)):
        characteristics.append(dict(gene=gene_df[i],rs=rs_df[i],snp=x[i]))
    
    sample_dict['characteristics'] = characteristics
    return sample_dict

v = samples_df.apply(lambda row: refactor_sample_record(row), axis=1)
v = list(v)


'''
# output should be in the form...
[{'characteristics': [{'gene': 'ADIPOQ', 'rs': 'rs17300539', 'snp': 'GG'},
   {'gene': 'ANKK1', 'rs': 'rs1800497', 'snp': 'TT'},
   {'gene': 'FTO', 'rs': 'rs11076022', 'snp': 'GG'},
   {'gene': 'FTO', 'rs': 'rs1121980', 'snp': 'CC'},
   {'gene': 'FTO', 'rs': 'rs12446047', 'snp': 'CT'},
   {'gene': 'FTO', 'rs': 'rs12921970', 'snp': 'CC'},
   {'gene': 'FTO', 'rs': 'rs1421085', 'snp': 'TT'},
   {'gene': 'FTO', 'rs': 'rs3751812', 'snp': 'GG'},
   {'gene': 'FTO', 'rs': 'rs7199716', 'snp': 'CC'},
   {'gene': 'FTO', 'rs': 'rs8049933', 'snp': 'CC'},
   {'gene': 'FTO', 'rs': 'rs8050136', 'snp': 'AC'},
   {'gene': 'FTO', 'rs': 'rs9936768', 'snp': 'CC'},
   {'gene': 'FTO', 'rs': 'rs9939609', 'snp': 'AA'},
   {'gene': 'LEPR', 'rs': 'rs2025804', 'snp': 'CT'},
   {'gene': 'LEPR', 'rs': 'rs8179183', 'snp': 'GG'},
   {'gene': 'LIPC', 'rs': 'rs1800588', 'snp': 'TT'},
   {'gene': 'LPL', 'rs': 'rs328', 'snp': 'CC'},
   {'gene': 'MC4R', 'rs': 'rs17782313', 'snp': 'TT'},
   {'gene': 'PPARD', 'rs': 'rs2016520', 'snp': 'AA'},
   {'gene': 'SLC2A2', 'rs': 'rs5400', 'snp': 'TT'},
   {'gene': 'TAS2R38', 'rs': 'rs1726866', 'snp': 'CC'}],
  'name': 'Sample_1'},
'''
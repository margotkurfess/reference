### General ###

# sort by one column
df.sort_values('col')

# sort by multiple colummns
df.sort(['col1','col2'], ascending=[1, 0])

# drop duplicates in a df
df = df.drop_duplicates()

# list unique values of a column in a df
df.col.unique()

# reset index of a df
df = df.reset_index()

# keep and order columns in a df
df = df[['col1','col2','col3',...]]

# get data types of the objects in a df
df.dtypes

# cast column as type
df['column'] = df.column.astype('int')

# rename columns
df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})

### Pandas ###

import pandas as pd

# read csv file
df = pd.read_csv('filename.csv')

# to_datetime
df['date'] = pd.to_datetime(df['date'])

### Datetime ###

from datetime import datetime, date, time

# convert to different type of date format
df['session_month'] = df['session_date'].datetime.strftime('%Y-%m')


### Seaborn ###

import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline

# as bar chart
casper_palette = vis.generate_casper_palette('dark')
sns.set(style="ticks", palette=casper_palette)
g = sns.factorplot(x="session_month", y="unioned_sessions", hue="data_source", data=df,
                   aspect=4,
                   ci=None,
                   kind="bar",
                   estimator=sum)
g.ax.set_title("Title", fontsize=20) # set title
g.set_axis_labels("x_label", "y_label") # set labels
g.set_xticklabels(rotation=45); # rotate x axis labels


### S3 ###

s3_csv = s3.df_to_s3(summary,'filename.csv')
print s3_csv # print the s3 path to this file

df = pd.read_csv(s3_csv, index_col=0) # read in the s3 file
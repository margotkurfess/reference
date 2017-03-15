# Python

This documentation is to keep track of useful commands and resources for Python.

## General resources

- [Python for Data Analysis (book)](http://shop.oreilly.com/product/0636920023784.do) - I use this book regularly as reference for all things data analysis-related
- [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/) - Kenneth Reitz rocks and his guides for using Python for projects has been amazingly helpful. In addition to the docs, I also really recommend [the book version](http://shop.oreilly.com/product/0636920042921.do)
- [Python Reference Guide](https://www.python.org/dev/peps/pep-0008/) - Style guide for Python

## Useful commands by library

- [General](https://github.com/margotkurfess/reference/blob/master/python.md#general)
- [Datetime](https://github.com/margotkurfess/reference/blob/master/python.md#datetime)
- [Pandas](https://github.com/margotkurfess/reference/blob/master/python.md#pandas)
- [NumPy](https://github.com/margotkurfess/reference/blob/master/python.md#numpy)
- [Seaborn](https://github.com/margotkurfess/reference/blob/master/python.md#seaborn)

### General

-	sort by one column
	```python
	df.sort_values('col')
	```

-	sort by multiple colummns
	```python
	df.sort(['col1','col2'], ascending=[1, 0])
	```

-	drop duplicates in a df
	```python
	df = df.drop_duplicates()
	```

-	list unique values of a column in a df	
	```python
	df.col.unique()
	```

-	reset index of a df
	```python
	df = df.reset_index()
	```

-	keep and order columns in a df
	```python
	df = df[['col1','col2','col3',...]]
	```

-	get data types of the objects in a df
	```python
	df.dtypes
	```

-	cast column as type
	```python
	df['column'] = df.column.astype('type')
	```

-	rename columns
	```python
	df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})
	```

### Datetime

-	import library
	```python
	from datetime import datetime, date, time
	```

-	convert to different type of date format
	```python
	month = date.strftime('%Y-%m')
	```

	```python
	df['date'] = df['date'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d'))
	```

### Pandas

-	import library
	```python
	import pandas as pd
	```

-	read in a csv file
	```python
	df = pd.read_csv('filename.csv')
	```

-	convert object to datetime
	```python
	df['date'] = pd.to_datetime(df['date'])
	```

### NumPy
_to be added_

### Seaborn

-	import library
	```python
	import matplotlib
	from matplotlib import pyplot as plt
	import seaborn as sns
	%matplotlib inline
	```

-	bar chart
	```python
	casper_palette = vis.generate_casper_palette('dark')
	sns.set(style="ticks", palette=casper_palette)
	g = sns.factorplot(x="x_values", y="y_values", hue="data_source", data=df,
	                   aspect=4,
	                   ci=None,
	                   kind="bar",
	                   estimator=sum)
	g.ax.set_title("Title", fontsize=20) # set title
	g.set_axis_labels("x_label", "y_label") # set labels
	g.set_xticklabels(rotation=45); # rotate x axis labels
	```

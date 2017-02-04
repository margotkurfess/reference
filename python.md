# Python

This documentation is to keep track of 


## General resources

-	[Python Reference Guide](https://www.python.org/dev/peps/pep-0008/)
-	[PyCharm](https://www.jetbrains.com/pycharm/)

## Useful commands by library

-	General
- 	Pandas
- 	Seaborn
- 	Datetime

### General

-	sort by one column
	```python
	df.sort_values('col')```

-	sort by multiple colummns
	```python
	df.sort(['col1','col2'], ascending=[1, 0])```

-	drop duplicates in a df
	```python
	df = df.drop_duplicates()```

-	list unique values of a column in a df	
	```python
	df.col.unique()```

-	reset index of a df
	```python
	df = df.reset_index()```

-	keep and order columns in a df
	```python
	df = df[['col1','col2','col3',...]]```

-	get data types of the objects in a df
	```python
	df.dtypes```

-	cast column as type
	```python
	df['column'] = df.column.astype('type')```

-	rename columns
	```python
	df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})```
## Pandas notes

This is a tutorial I gave for the strategy consultants and developers in our company. The aim is to encourage them to use python(pandas) in their daily work of analytics, instead of Excel.

### Import file

First of all, import pandas module

```
import pandas as pd
```

Import example excel file

```
df = pd.read_excel("job_examples.xlsx")
```

Import specific excel sheet(jobs)

```
df = pd.read_excel("job_examples.xlsx", sheet_name="jobs")
```

Use a column(job_id) as an index

```
df = pd.read_excel("job_examples.xlsx", sheet_name="jobs", index_col="job_id")
```


### Overview

Gives a summary of dataframe

```
df.info()
```

Summary statistics of dataframe

```
df.describe()
```

Datatypes of the dataframe

```
df.dtypes
```

Get the name of all columns

```
df.columns
```

Dimensions of dataframe

```
df.shape
```



### Select

Head or Tail - display first/final 5 rows

```
df.head()
df.tail()
```

Select a column

```
df['location']
df.loc[:,['location']]
df.iloc[:,[3]] 							# 4th column
```

Select some columns

```
df[['job_title','location','company_name']]
df.loc[:, ['job_title','location','company_name']]
df.iloc[:, [3, 4, 5]] 					# 3, 4, 5th column
```

Select some rows

```
df.loc[22779711:22779706]
df.loc[[22779711, 22465415, 22779706]]	# job id as index

df.iloc[10:20]
df.iloc[[1,3,5]]
```

Select some rows and columns

```
df.loc[[22779711, 22465415, 22779706], ['job_title','location','company_name']]
df.iloc[10:20, [3, 4, 5]]		
```

Filter categorical data

```
df[df['country_code'] == 'DE']
df[df['country_code'].isin(['DE', 'GB'])]	# multiple filter
df[~df['country_code'] == 'DE']				# negative filter
```

Filter numerical data

```
df[df['job_id']>1000]
df[(df['job_id']>1000) & (df['job_id']<10000)]
```

Filter string data

```
df[df['location'].str.contains("Essen")]
```

Sort value

```
df.sort_values("language_id")
```



### Statistic summary

Shape of dataframe

```
df.shape					# #row, #column
df.size						# #cells
df.count()
```

Sum

```
df.sum(axis = 0)			# sum column
df.sum(axis = 1)			# sum row
```

Mean, max, min

```
df.mean()
df.max()
df.min()
```

Unique

```
df['language_id'].unique()
```

Groupby

```
df.groupby('language_id').mean()
df.groupby('language_id').max()
df.groupby('language_id').min()
```


### Lambda function

It is a very flexible way to manipulate data in a specific column.

The following two examples are the same, the query with lambda function may look very long, but you can define any function as you like.

```
df[df['language_id']>1]
df[df['language_id'].apply(lambda x: x > 1)]
```

A more complex example

```
## find long job titles
df[df.apply(lambda x : len(x['job_title'].split(" "))>10,axis=1)]
```


**References**

[1] https://github.com/ank0409/Ditching-Excel-for-Python  
[2] https://mode.com/python-tutorial/pandas-groupby-and-python-lambda-functions/

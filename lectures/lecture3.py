"""Series"""
import pandas as pd

index = [
   ...,
   ...,
 ]

data = [
   ...,
   ...,
 ]

ser = pd.Series(data=data, index=index)

"""Dataframes"""
import pandas as pd

index = [
   ...,
   ...,
   ]

data_1 = [
   ...,
   ...,
   ]

data_2 = [
   ...,
   ...,
   ]

ser_1 = pd.Series(data=data_1, index=index)
ser_2 = pd.Series(data=data_2, index=index)

df = pd.DataFrame({'name1': ser_1, 'name2': ser_2})

"""Sort Series or Data Frame"""
sorted_ser = df.sort_index()






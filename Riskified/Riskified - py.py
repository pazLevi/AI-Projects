# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lEuKch_p2SSe3GrPBNE9s1dBl5QeuQOl

# Paz Levi - Riskified
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the Excel file 
df = pd.read_excel('new_dataset_(4)_(1)_(1).xlsx')
df.head(5)

#Check the column types
df.info()

"""## Q1 - Set all values below the 90% threshold as 'decline' (in the rest of the questions I continued with the original table)"""

df_cp = df.copy()
df_cp.loc[df['classification_score']<0.90,'order_status'] = 'decline'

df_cp['order_status'].value_counts().plot(kind='bar'),
plt.title("Count orders per order_source")
plt.show()

"""## Q2 - Plot the model scores distribution"""

plt.xlim(min(df['classification_score']),1)

sns.kdeplot(df['classification_score'])
plt.title("Distribution of the predictions of the model")

plt.show()

"""## Q3

**Given**:

CHB's / Total_revenue = 0.5 (50%)

I calculated the percentage of total revenue in relation to the sum of all orders

I summed up all the chargebacks that exist in the data to find the total revenue
"""

CHB = sum(df[df['order_status'] =='chargeback']['price'])
TR = CHB * 2 
fee = TR/sum(df['price']) * 100
print(f"The fee is { fee} %")

"""## Q4"""

plt.title("Ratio between of the order status in relation to whether the transaction is digital or not")
sns.countplot(x=df['order_status'],hue=df['digital_product'])
plt.show()

plt.title("Ratio between of prediction of the model in relation to whether the transaction is digital or not")
sns.countplot(x=df['digital_product'],hue=df['classification_score']> 0.9)
plt.show()

sns.countplot(x=df['digital_product'],hue=df['order_source'])
plt.title("Column Order Counting Whether the order is digital or not - is divided by the order source")
plt.show()

"""**Use one label encoding to make all columns numeric (I removed the zip because I did not find use for this column)**"""

df_new = df.copy()
print('The columns I made them one label encoding to make them numeric:\n')
for i in df.drop('billing_zip',axis=1).columns[2:]:
  if df[i].dtype == 'object' or  df[i].dtype =='bool':
    print(i)
    df_new=pd.concat([df_new,pd.get_dummies(df[[i]])],axis=1).drop(i,axis=1)

df_new.head(4)

abs(df_new.corrwith(df['digital_product'])).sort_values(ascending=False).plot(kind='bar')
plt.title("Calculate the correlation between the features in the table with digital_product column")
plt.show()

sns.displot(df['shipping_name_length'])
plt.title("The distribution of the length of the shipping name")
plt.show()

"""**Distribution of the length of the shipping name to all tangible orders**"""

plt.title('Count according to the length of the shipping name for all tangible orders')

df[df['digital_product']==False]['shipping_name_length'].value_counts().plot(kind='bar')
plt.show()

plt.title('Count according to the length of the shipping name for all digital orders')
df[df['digital_product']==True]['shipping_name_length'].value_counts().plot(kind='bar')
plt.show()

df['price'].plot(kind='kde',xlim=(0))
plt.title("Price distribution")
plt.show()

as_fig = sns.FacetGrid(df,hue='digital_product',aspect=5)

as_fig.map(sns.kdeplot,'price',shade=True)

# oldest = df['price'].max()

as_fig.set(xlim=(0,3000))

as_fig.add_legend()
plt.show()

"""**Conclusions (Question 4):**


 - As I presented in the graphs, between the digital column and some of the columns there is a high correlation (ratio) to the columns: length of the shipment name, and the price.

 - It can be seen that the price of tangible orders is low compared to the digital.

 - The length of the shipping name in digital orders is usually 0 while in tangible orders it is scattered



"""

from autoviz.AutoViz_Class import AutoViz_Class

AV = AutoViz_Class()
dft = AV.AutoViz("", depVar='order_status', dfte=df[2:], verbose=1)

"""##  Free exploration:

 - Is a relationship between price and the prediction of the model.
At high prices the result of the prediction is high (fit)

- It can be seen that orders that the model has given a low prediction have a high chance of chargeback

- The higher the price, the higher the chance that the model will classify the order as "approval"

- The chargeback order price is significantly lower in price


"""
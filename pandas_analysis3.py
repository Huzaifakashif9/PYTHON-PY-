# STEP 1: LOAD DATA
# STEP 2: FIRST LOOK (BASIC UNDERSTANDING)
# STEP 3: DATA TYPES FIX KARNA
# STEP 4: MISSING VALUES ANALYSIS (VERY IMPORTANT)




import pandas as pd
# 'Sales Person', 'Country', 'Product', 'Date', 'Amount',
    #    'Boxes Shipped']
df=pd.read_csv('Chocolate_Sales.csv')
print(df)

print(df.head())
print(df.tail())
print(df.sample(5))
print(df.shape)
print(df.columns)
print(df.info())

print(df.dtypes)
#amount ka dollar hatana aur comma hatana
df['Amount']=(df['Amount'].str.replace(r'[$,]','',regex=True).astype(float))
print(df.dtypes)

print(df['Amount'])

#date to date ke object me convert krna
df['Date']=pd.to_datetime(df['Date'],dayfirst=True)
print(df.dtypes)
print(df['Date'])

print(df.isnull().sum())

df['Sale']=df['Amount']*0.10
print(df)

df['Year']=df['Date'].dt.year
df['Month']=df['Date'].dt.month
df['Month_name']=df['Date'].dt.month_name()

print(df.columns)

kk=df[(df['Country']=='India')&(df['Amount']>5000)]
print(kk)




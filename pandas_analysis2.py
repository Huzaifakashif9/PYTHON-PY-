import pandas as pd
df=pd.read_csv('data.csv')
# Index(['Duration', 'Date', 'Pulse', 'Maxpulse', 'Calories']
print(df)

print(df.head())

print(df.columns)

print(df.info())

print(df.isnull().sum())

print(df['Calories'].value_counts())

print(df['Duration'].value_counts())

print(df['Pulse'].value_counts())

print(df['Maxpulse'].value_counts())

df['Fees']=df['Calories']*10
print(df)

print(df['Calories'].isnull().sum())

print(df['Fees'].isnull().sum())

df['Calories']=df['Calories'].fillna("Missing")
print(df)

df['Fees']=df['Fees'].fillna(df['Fees'].mean())
print(df)

k=df['Fees'].sum()
print(k)

print(df['Fees'].mean())
#highest fees
k=df[df['Fees']>df['Fees'].mean()]
print(k)

low_fees=df[df['Fees']<df['Fees'].mean()]
print(low_fees)

def spend_level(amount):
  if amount < 50:
    return 'Low'
  elif amount < 150:
    return 'Medium'
  else:
    return 'High'
# create a new feature called 'Spend Level', apply above function on Purchase Amount column
df['Spend Level'] = df['Purchase Amount (USD)'].apply(spend_level)

def age_group(age):
  if age < 25:
    return 'Young'
  elif age < 40:
    return 'Adult'
  else:
    return 'Senior'
df['Age Group'] = df['Age'].apply(age_group)

df[['Age', 'Age Group']]
import pandas as pd
df=pd.DataFrame([1,2,3])
print(df)

data={
"name":["ali","ayan","shariq","huzaifa"],
"Marks": [85, 60, 90,55],
"Age": [20, 21, 19,45],
"course":["adse","stc","hdse","abc"],
"school":["kps","aps","roots","beacon"]
}
df=pd.DataFrame(data)
# print(df)

print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.rename(columns={'course':'tuition'}))
p=df.info()
print(p)
print(df.describe())

df.to_csv('hello.csv',index=False)

k=pd.read_csv('hello.csv')
print(k)

print(k[['name']])

kk=k.loc[k.name=='ali']
print(kk)

pk=k.loc[(k.name=='huzaifa')&(k.Age>=20)]
print(pk)

l=k.loc[0:3]
print(l)

j=k.iloc[0:3]
print(j)

h=k.iloc[1]
print(h)

gg=k[k['Age']>20]
print(gg)

s=k[(k['Age']>20)&(k["Marks"]>=60)]
print(s)

d=k.query("Age>18 and Marks>=60")
print(d)

k['Team']=['ceo','manager','tl','freshie']
print(k)

k['bonus']=k['Marks']*2
print(k)

k.loc[0,'Marks']=90
print(k)

gfd=k.drop(k[k.name=='huzaifa'].index)
print(gfd)

jjj=k.drop('bonus',axis=1)
print(jjj)

nm=k.drop(['bonus','Age'],axis=1)
print(nm)

llm=k.sort_values('Age',ascending=True)
print(llm)

llmk=k.sort_values('Age',ascending=False)
print(llmk)


b=k['Age'].value_counts()
print(b)

# jh=k[k['Marks'==90].value_counts()]
# print(jh)

c=k.groupby('Age')['Marks'].sum()
print(c)

cv=k.groupby('Age').agg({'Marks':'mean','name':'count'})
print(cv)
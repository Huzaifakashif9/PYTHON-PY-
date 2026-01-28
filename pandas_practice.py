import pandas as pd
df=pd.read_csv('huzaifa.csv')
print(df)

print(df.head(2))

print(df.info())

print(df.shape)

print(df.describe())

print(df.isnull().sum())  

#2 department 1 age and 3 salary mising

df['Department']=df['Department'].fillna("MISSING")
print(df)

df['Age']=df['Age'].fillna(df['Age'].mean())
print(df)

df['Salary']=df['Salary'].fillna(df['Age'].median())
print(df)

print(df.isnull().sum())

#sab duplicate remove hogaya


#department mai account aur accounts
#  clash kr rha hai isko rename krna hai

df['Department']=df['Department'].replace({
    "Account":"Accounts"
})
print(df)

df=df.drop_duplicates()
print(df)

#High salary employees (> 100k)
highest =df[df['Salary']>100000]
print(highest)

#it depart employes

IT=df[df['Department']=='IT']
print(IT)

#SALARY 100 SE UPAR AUR AGE 30 SE UPAR

doub=df[(df['Salary']>100000) & (df['Age']>30)]
print(doub)

#designation -officere other not okay

desig=df.where(df["Designation"]=="Officer",other='notokay')
print(desig)

#adding column of bonus *by 20% by the salary

df['Bonus']=df['Salary']*0.2
print(df)

#salary only 100000
sal=df[df['Salary']==100000]
print(sal)

#----------:Business / HR Analytics Questions:-----------

#average salary by department

avg_salary=df.groupby("Department")["Salary"].mean()
print(avg_salary)

#average age by designation

avg_age=df.groupby("Designation")["Age"].mean()
print(avg_age)

#Highest paid designation
high=df.groupby("Designation")["Salary"].mean().sort_values(ascending=False)
print(high)

#Employee count by department
kk=df['Department'].value_counts()
print(kk)

#Age vs Salary insight
j=df.groupby("Age")["Salary"].mean()
print(j)

#Top 5 highest paid employees
sortt=df.sort_values("Salary",ascending=False).head(5)
print(sortt)

#Which department has the highest average salary?

avg=df.groupby('Department')['Salary'].mean().sort_values(ascending=False)
print(avg)

#2️⃣ Which designation is overpaid compared to department average?

dep_avg=df.groupby('Department')['Salary'].transform("mean")
df[df["Salary"] > dep_avg][["Emp_ID","Designation","Department","Salary"]]


#3️⃣ Which department has the youngest workforce?

young=df.groupby('Department')['Age'].mean().sort_values()
print(young)

#4️⃣ Which department spends the most on salary (total cost)?

most=df.groupby('Department')['Salary'].sum().sort_values(ascending=False)
print(most)

#5️⃣ Which designation has the highest salary variation (std)?
std=df.groupby('Designation')['Salary'].std().sort_values(ascending=False)
print(std)

#:-----Advanced Filtering & Logic:----


#Employees who are: Age < 30.... Salary > department average
depp=df.groupby('Department')['Salary'].transform("mean")
ag=df[(df['Age']<30) & (df['Salary']>depp)]
print(ag)


# 7️⃣ Departments where:
# Average salary > overall company average
jj=df['Salary'].mean()
kk=df.groupby('Department')['Salary'].mean()[lambda x: x >jj]
print(kk)

#-------------:Feature Engineering (Real DS Work):------------

# 🔟 Create a column:
# Salary_Rank within each department

df['Salary_Rank']=df.groupby("Department")['Salary'].rank(ascending=False)
print(df)

# 1️⃣1️⃣ Create:

# Experience_Level (Age based: Junior / Mid / Senior)
df["Experience_Level"]=pd.cut(df["Age"],bins=[20,30,40,60],labels=["Junior","Mid","Senior"])
print


# 1️⃣4️⃣ Does designation matter more than department for salary?
df.groupby("Designation")["Salary"].mean()
df.groupby("Department")["Salary"].mean()

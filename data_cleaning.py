import pandas as pd

df_gender = pd.read_csv("BDD/gender_submission.csv", encoding = "utf-8")
print(df_gender)
df_test = pd.read_csv("BDD/test.csv", encoding = "utf-8")
df_test = df_test.set_index('PassengerId')
print(df_test)
df_train = pd.read_csv("BDD/train.csv", encoding = "utf-8")
df_train = df_train.set_index('PassengerId')
print(df_train)


df_train['Age'].fillna(df_train['Age'].median(), inplace=True)
df_train.describe()

df_train[df_train['Survived']==1]['Sex'].value_counts()
df_train[df_train['Survived']==0]['Sex'].value_counts()

survived_sex = df_train[df_train['Survived']==1]['Sex'].value_counts()
dead_sex = df_train[df_train['Survived']==0]['Sex'].value_counts()
df_s = pd.DataFrame([survived_sex,dead_sex])
df_s.index = ['Survived','Dead']
df_s.plot(kind='bar',stacked=True, figsize=(15,8))
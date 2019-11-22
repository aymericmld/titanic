import pandas as pd

df_gender = pd.read_csv("BDD/gender_submission.csv", encoding = "utf-8")
print(df_gender)
df_test = pd.read_csv("BDD/test.csv", encoding = "utf-8")
df_test = df_test.set_index('PassengerId')
print(df_test)
df_train = pd.read_csv("BDD/train.csv", encoding = "utf-8")
df_train = df_train.set_index('PassengerId')
print(df_train)


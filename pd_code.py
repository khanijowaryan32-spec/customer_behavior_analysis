import pandas as pd 

df = pd.read_csv("customer_shopping_behavior.csv")

print(df.info())
print(df.describe(include="all"))
print(df.isna().sum())

df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(lambda x : x.fillna(x.median()))


df.columns = df.columns.str.replace(" " , "_").str.lower()
print(df.columns)

df.rename(columns={"purchase_amount_(usd)" : "purchase_amount"} , inplace=True)
print(df["purchase_amount"].head(5))

labels = ["Young Adult" , "Adult" , "Middle-aged" , "Senior"]
df["age_group"] = pd.qcut(df["age"] , q=4 , labels=labels)
print(df["age_group"])

print(df.frequency_of_purchases.unique())

frequency = {
            'Fortnightly' : 14 , 
            'Weekly' : 7 , 
            'Annually' : 365  , 
            'Quarterly' : 90 , 
            'Bi-Weekly' : 14 , 
            'Monthly' : 30 , 
            'Every 3 Months' : 90
            }
df["purchase_frequency_days"] = df["frequency_of_purchases"].map(frequency)

print((df['discount_applied'] == df['promo_code_used']).all())

df.drop(columns='promo_code_used' , inplace=True)
print(df.columns)

df.to_csv("customer_data.csv" , index= False)
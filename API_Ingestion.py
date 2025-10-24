import requests
import pandas as pd
import os

response = requests.get("https://randomuser.me/api/?results=10&inc=login,name,email,registered,location")
users = response.json()["results"] # "results" is the Json object that the API says it has all the user info.
df = pd.json_normalize(users)

main_cols = df[["login.uuid","name.first", "name.last", 
                "email","registered.date", "registered.age", 
                "location.country", "location.street.name"]]

csv_file = "random_users.csv"

# If the file exists, load and append without duplicates
if os.path.exists(csv_file):
    df_existing = pd.read_csv(csv_file)
    df_final = pd.concat([df_existing, main_cols], ignore_index=True)
else:
    df_final = main_cols

# Save result back to CSV (overwrite file)
df_final.to_csv(csv_file, index=False)




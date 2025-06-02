import pandas as pd
df = pd.read_csv(r"C:\Users\badgu\OneDrive\Desktop\Movies and shows Dataset\netflix_titles.csv")
print("✅ Dataset loaded. First 5 rows:")
print(df.head())

print("\n📊 Dataset info:")
print(df.info())

print("\n🔍 Missing values per column:")
print(df.isnull().sum())

df = df.drop_duplicates()
print(f"\n✅ After removing duplicates: {df.shape}")

df = df.dropna()
print(f"\n🧹 After dropping rows with missing values: {df.shape}")

df['rating'] = df['rating'].str.lower().str.strip()
df['type'] = df['type'].str.lower().str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

df.to_csv("cleaned_netflix_titles.csv", index=False)
print("\n✅ Data cleaning complete. File saved as 'cleaned_netflix_titles.csv'")

for col in ['country', 'director', 'cast']:
    df[col] = df[col].astype(str).str.strip().str.lower()

df['release_year'] = df['release_year'].astype(int)
df['duration'] = df['duration'].astype(str)

df.to_csv("final_cleaned_netflix_titles.csv", index=False)
print("\n✅ Final cleaning complete. File saved as 'final_cleaned_netflix_titles.csv'")

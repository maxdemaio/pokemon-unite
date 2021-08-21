import json
import numpy as np, pandas as pd

# URL for JSON: https://unite-db.com/stats.json
# Convert to CSV: df.to_csv("uniteAggregate.csv", encoding='utf-8', index=False)

# Load data using Python JSON module
with open('data.json','r') as f:
    data = json.loads(f.read())

# Normalizing data
df = pd.json_normalize(data, record_path=["level"], meta=["name"])

# Create level column
df.insert(loc=0, column="lvl",
    value=np.tile([i for i in range(1,16)], 22))

print(df)

# Group data by level
grouped = df.groupby(["lvl"])

# Analyze by level
for i in range(1, 16):
    grouped.get_group(i).to_csv(
        "uniteCSVs/uniteLevel{}.csv".format(i), encoding='utf-8', index=False)



    
    

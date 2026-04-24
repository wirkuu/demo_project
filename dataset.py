import pandas as pd

data = {
    "name": ["John Doe", "Jane Smith", "Alice Johnson"],
    "age": [30, 25, 28],
    "city": ["New York", "Los Angeles", "Chicago"],
}
df = pd.DataFrame(data)

df

df.replace("John Doe", "Jonathan Doe", inplace=True)

df.head(2)
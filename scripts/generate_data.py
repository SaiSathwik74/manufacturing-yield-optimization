import numpy as np
import pandas as pd

np.random.seed(42)
rows = 250_000

df = pd.DataFrame({
    "temperature": np.random.normal(700, 25, rows),
    "pressure": np.random.normal(30, 5, rows),
    "machine_speed": np.random.normal(120, 15, rows),
    "material_quality": np.random.uniform(0.7, 1.0, rows),
    "downtime_minutes": np.random.exponential(10, rows)
})

df["yield_percent"] = (
    85
    + 0.02 * (df["temperature"] - 700)
    - 0.15 * df["downtime_minutes"]
    + 5 * (df["material_quality"] - 0.85)
    + np.random.normal(0, 2, rows)
)

df.to_csv("data/raw/manufacturing_data.csv", index=False)
print("Synthetic dataset generated.")

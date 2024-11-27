import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(0)

# Create four numeric columns with 50 rows each
data = {
    "numeric_col1": np.random.rand(50),
    "numeric_col2": np.random.rand(50) * 100,
    "numeric_col3": np.random.randint(1, 100, size=50),
    "numeric_col4": np.random.normal(
        50, 10, size=50
    ),  # Normal distribution centered around 50
}

# Create a categorical column with predefined categories
categories = ["Category A", "Category B", "Category C"]
data["categorical_col"] = np.random.choice(categories, size=50)

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

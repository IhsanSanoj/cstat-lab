import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataset
data = {
    'Attrition_Flag': ['Existing', 'Attrited', 'Existing', 'Existing',
                       'Attrited', 'Existing', 'Attrited', 'Existing'],
    'Gender': ['M', 'F', 'F', 'M', 'F', 'M', 'M', 'F'],
    'Education_Level': ['Graduate', 'High School', 'Graduate', 'College',
                        'Graduate', 'College', 'High School', 'Graduate'],
    'Marital_Status': ['Married', 'Single', 'Married', 'Single',
                       'Divorced', 'Married', 'Single', 'Married'],
    'Card_Category': ['Blue', 'Blue', 'Silver', 'Blue',
                      'Gold', 'Silver', 'Blue', 'Gold'],
    'Customer_Age': [25, 45, 35, 40, 50, 30, 55, 38],
    'Credit_Limit': [3000, 5000, 7000, 4000, 9000, 6000, 8000, 5500],
    'Total_Trans_Amt': [1200, 2500, 1800, 2200, 3000, 1500, 2800, 2000]
}

df = pd.DataFrame(data)

# 1. Bar chart of Attrition Flag
df['Attrition_Flag'].value_counts().plot(kind='bar')
plt.title("Customer Attrition")
plt.xlabel("Attrition Flag")
plt.ylabel("Count")
plt.show()

# 2. Bar charts for categorical variables
columns = ['Gender', 'Education_Level',
           'Marital_Status', 'Card_Category']

for col in columns:
    df[col].value_counts().plot(kind='bar')
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# 3. Box plots
df[['Customer_Age', 'Credit_Limit',
    'Total_Trans_Amt']].plot(kind='box')

plt.title("Customer Data Box Plots")
plt.show()

# 4. Correlation heatmap
corr = df.select_dtypes(include='number').corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

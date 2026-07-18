import pandas as pd
import matplotlib.pyplot as plt
import calendar

data = [
    {"Name": "John Doe", "Sales Amount": 500.50, "Transaction Date": "2024-01-15", "Full Address": "123 Main St, Springfield"},
    {"Name": "Jane Smith", "Sales Amount": 750.00, "Transaction Date": "15/02/2024", "Full Address": "456 Oak St, Springfield"},
    {"Name": "Jane Smith", "Sales Amount": 750.00, "Transaction Date": "15/02/2024", "Full Address": "456 Oak St, Springfield"},
    {"Name": "Mike Brown", "Sales Amount": 1200.00, "Transaction Date": "2024/03/01", "Full Address": "789 Pine St, Shelbyville"},
    {"Name": "Anna Lee", "Sales Amount": 950.75, "Transaction Date": "03-05-2024", "Full Address": "101 Maple St, Springfield"},
    {"Name": "John Doe", "Sales Amount": 500.50, "Transaction Date": "2024-01-15", "Full Address": "123 Main St, Springfield"},
    {"Name": "Paul Adams", "Sales Amount": None, "Transaction Date": None, "Full Address": "987 Elm St, Shelbyville"},
    {"Name": "Lara Croft", "Sales Amount": 1450.25, "Transaction Date": "2024/07/08", "Full Address": "555 Cedar St, Capital City"},
    {"Name": "Nina Ross", "Sales Amount": 1250.00, "Transaction Date": "08-07-2024", "Full Address": "333 Birch St, Capital City"},
    {"Name": "Mike Brown", "Sales Amount": 1200.00, "Transaction Date": "03-05-2024", "Full Address": "789 Pine St, Shelbyville"}
]

df = pd.DataFrame(data)

 # Delete duplicate rows and rows with null values in "Sales Amount" and "Transaction Date".
df_cleaned = (df.drop_duplicates()                                                                                         
              .dropna(subset=["Sales Amount", "Transaction Date"])) 
         
#Standarize the format of the "Transaction Date" column to 'YYYY-MM-DD'.                                               
df_cleaned['Transaction Date'] = pd.to_datetime(df_cleaned['Transaction Date'], format='mixed').dt.strftime('%Y-%m-%d')   

#Split the "Full Address" column into two new columns: "Street" and "City".
df_cleaned[['Street', 'City']] = df_cleaned['Full Address'].str.split(', ', expand=True)     

#Delete the original "Full Address" column after splitting it and reset the DataFrame index to reflect the changes.
df_cleaned = (df_cleaned.drop(columns=['Full Address']).sort_values(by='Transaction Date', ascending=True).reset_index(drop=True))                                                                                     

# Group the cleaned DataFrame by month and calculate the total sales for each month.
monthly_sales = df_cleaned.groupby(pd.to_datetime(df_cleaned['Transaction Date']).dt.month)[['Sales Amount']].sum()
monthly_sales.index = monthly_sales.index.map(lambda x: calendar.month_name[x])

# Print the cleaned DataFrame and monthly sales.
print(df_cleaned)
print("\nMonthly Sales:\n", monthly_sales)

plt.bar(monthly_sales.index, monthly_sales['Sales Amount'], edgecolor='white')
plt.title('Monthly Sales Amount')
plt.xlabel('Months')
plt.ylabel('Sales Amount ($)')
plt.show()
import sqlite3

import duckdb
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


df=pd.read_csv(r"C:\Users\Sneha\Downloads\sales_data_sample cleaning.csv")

# print(df)


conn=sqlite3.connect('sales_data.db')

df.to_sql('sample_sales',conn,if_exists='replace')

conn.close()

 # sum of sales
sql_query1= "Select sum(SALES) from df"
result=duckdb.query(sql_query1).to_df()

print(result)

sql_query2= "Select * from df"

result2 =duckdb.query(sql_query2).to_df()
print(result2)


sql_query3= "select count(ORDERNUMBER) from df"
result3 =duckdb.query(sql_query3).to_df()
print(result3)

sql_query4="select sum(QUANTITYORDERED * PRICEEACH) as total_revenue from df GROUP BY PRODUCTLINE"
result4 =duckdb.query(sql_query4).to_df()
print(result4)

df_top_10_sales = df.sort_values(by='SALES', ascending=False).head(10)


bar_chart=df_top_10_sales.plot(kind='bar' , x='PRODUCTLINE', y='SALES',figsize=(25, 6))
plt.xticks(rotation=90,ha='right',fontsize=5)
plt.tight_layout()
plt.savefig('bar_chart.png')
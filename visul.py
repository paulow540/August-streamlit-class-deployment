import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("Reports", anchor=False)

# to work with Excel files install ----  pip install xlrd ---- 
with st.expander("Dataframe"):
    data = pd.read_excel("sample superstore.xls", sheet_name="Orders")  # Read the Excel file and specify the sheet name
    data

    
    # st.table(data)

# tab1, tab2, tab3 = st.tabs(["SUM OF SALES", "SUM OF PROFIT", "SUM OF QUANTITY"])
# tab1.subheader("SUM OF SALES")
# sum_sales = data["Sales"].sum()
# tab1.metric(label="Total Sales", value=f"${sum_sales:,.2f}")
# tab2.subheader("SUM OF PROFIT")
# sum_profit = data["Profit"].sum()
# tab2.metric(label="Total Profit", value=f"${sum_profit:,.2f}")  
# tab3.subheader("SUM OF QUANTITY")
# sum_quantity = data["Quantity"].sum()
# tab3.metric(label="Total Quantity", value=f"{sum_quantity:,}")

col1, col2, col3 = st.columns(3)
with col1:
    # st.write("##### SUM OF SALES")
    sum_sales = data["Sales"].sum()
    st.metric(label="Total Sales", value=f"${sum_sales:,.2f}")
with col2:
    # st.write("##### SSUM OF PROFIT")
    sum_profit = data["Profit"].sum()
    st.metric(label="Total Profit", value=f"${sum_profit:,.2f}")           
with col3:
    # st.write("##### SSUM OF QUANTITY")
    sum_quantity = data["Quantity"].sum()
    st.metric(label="Total Quantity", value=f"{sum_quantity:,}")



# # Bar chart
# Segment by sum of sales
segment_sales = data.groupby("Segment")["Sales"].sum().reset_index()
st.bar_chart(data=segment_sales,x="Segment", y="Sales", use_container_width=True)

# LINE
# st.plotly_chart(px.line(data, x="Order Date", y="Sales"), use_container_width=True)
month_order = data.groupby(data["Order Date"].dt.to_period("M"))["Sales"].sum().reset_index()
month_order["Order Date"] = month_order["Order Date"].dt.to_timestamp()
st.line_chart(data=month_order, x="Order Date", y="Sales", use_container_width=True)




# ASSIGNMENT 1
# ANALYSIS THE DATASET AND CREATE A 15 REPORT WITH DIFFERENT CHARTS AND GRAPHS 



















#  we use diff dataset here PRESIDENT HEIGHT DATASET
# # histogram
# st.plotly_chart(px.histogram(data, x="height(cm)", nbins=10), use_container_width=True)

# # pie chart
# st.plotly_chart(px.pie(data, names="name", values="height(cm)"), use_container_width=True)

# st.plotly_chart(px.density_heatmap(data, x="height(cm)", y="name"), use_container_width=True)

# st.plotly_chart(px.scatter(data, x="height(cm)", y="name", color="height(cm)"), use_container_width=True)

# st.plotly_chart(px.line(data, x="name", y="height(cm)"), use_container_width=True)

# st.plotly_chart(px.box(data, x="name", y="height(cm)"), use_container_width=True)

# # st.plotly_chart(px.violin(data, x="name", y="height(cm)"), use_container_width=True)

# st.plotly_chart(px.scatter_map(data, lat="height(cm)", lon="height(cm)", color="name"), use_container_width=True)
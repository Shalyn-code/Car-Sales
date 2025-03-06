import streamlit as st
import pandas as pd
import plotly.express as px

vehicles = pd.read_csv('vehicles_us.csv')

st.header('Vehicles for Sale')

st.write('Below is a histogram showing the amount of cars listed based on mileage:')

fig = px.histogram(vehicles, x='odometer')

fig.update_layout(
    xaxis_range=[0, 500000],
    xaxis_title='Mileage'
)

fig.show()

st.write(fig)


custom_colors = ['red', 'green', 'blue', 'yellow', 'coral']
fig = px.scatter(vehicles, x ='model_year', y='price', color='type', color_discrete_sequence=custom_colors, size='days_listed')

fig.update_layout(xaxis_title='Year of Vehicle')
fig.show()

event = st.plotly_chart(fig, key='type', on_select='rerun')

others = ['coupe', 'hatchback', 'wagon', 'minivan', 'other', 'offroad', 'bus']
sedan = st.checkbox('Sedan')
suv = st.checkbox('SUV')
truck = st.checkbox('Truck')
van = st.checkbox('Van')
convertible = st.checkbox('Convertible')
pickup = st.checkbox('Pickup')

# Filter DataFrame based on selected checkboxes
filtered_df = pd.DataFrame()

if sedan:
    filtered_df = pd.concat([filtered_df, vehicles[vehicles['type'] == 'sedan']])

if suv:
    filtered_df = pd.concat([filtered_df, vehicles[vehicles['type'] == 'SUV']])

if truck:
    filtered_df = pd.concat([filtered_df, vehicles[vehicles['type'] == 'truck']])

if pickup:
    filtered_df = pd.concat([filtered_df, vehicles[vehicles['type'] == 'van']])

if convertible:
    filtered_df = pd.concat([filtered_df, vehicles[vehicles['type'] == 'convertible']])

if others:
    filtered_df = pd.concat([filtered_df, vehicles[vehicles['type'] == 'others']])

# Display the filtered DataFrame
st.write(filtered_df[['price', 'model_year', 'model']])

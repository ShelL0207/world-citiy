import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('World Cites')
df = pd.read_csv('worldcities.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
population_filter = st.slider('Minimal Population (Millions):', 0.0, 40.0, 3.6)  # min, max, default

# create a multi select左侧选择项
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  # options
     df.capital.unique())  # defaults

# create a input form左侧选择项下面的框country name（显示）
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")


# filter by population链接上面的filter与实际数据
df = df[df.population >= population_filter]

# filter by capital
df = df[df.capital.isin(capital_filter)]

if country_filter!='ALL':#左侧country name（实际操作内容）
    df = df[df.country == country_filter]

# show on map
st.map(df)

# show dataframe
st.subheader('City Details:')
st.write(df[['city', 'country', 'population']])

# show the plot
st.subheader('Total Population By Country')
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)
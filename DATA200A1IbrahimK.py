
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("./Fish.csv")
st.header("Some fishy data")
st.write("The following are some interesting graphs related to a fish dataset")
st.write("Here is a sample of the dataset:")
st.write(df.head())

st.markdown("---")
data_bar = df["Species"].value_counts()
fig, ax = plt.subplots()
ax.bar(data_bar.index, data_bar)
plt.title("Fish count by species")
plt.xlabel("Species name")
plt.ylabel("Count")
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("---")
data_pie = df["Species"].value_counts().to_dict()
fig, ax = plt.subplots()
plt.pie(data_pie.values(), labels=data_pie.keys())
plt.legend(loc='upper center', bbox_to_anchor=(1.2, 1))
plt.title("Pie chart of number of fish species")
st.pyplot(fig)

st.markdown("---")
data_scatter_x = df.loc[df["Species"] == "Pike", "Weight"]
data_scatter_y = df.loc[df["Species"] == "Pike", "Width"]
fig, ax = plt.subplots()
plt.scatter(data_scatter_x, data_scatter_y)
plt.xlabel("Weight in grams")
plt.ylabel("Width in inches")
plt.title("Scatter plot of weight vs width for all pike fish")
st.pyplot(fig)

st.markdown("---")
data_box = {species : df.loc[df["Species"] == species, "Width"].tolist() for species in df["Species"].unique()}
data_box_labels = list(data_box.keys())
data_box_values = list(data_box.values())
fig, ax = plt.subplots()
plt.boxplot(data_box_values, labels=data_box_labels)
plt.xlabel("Species")
plt.ylabel("Weight in grams")
plt.title("Box plot of the weights of each type of fish")
st.pyplot(fig)

st.markdown("---")
species = df["Species"].unique()
selected_species = st.selectbox("Get the lengths of the selected species over the course of 3 weeks (will be limited to the first 5 fish of the selected species)",species)
data_line = df.loc[df["Species"] == selected_species, ["Length1", "Length2", "Length3"]]
fig, ax = plt.subplots()
count = 0
max_count = 5
initial_idx = 0
for idx, row in data_line.iterrows():
    if initial_idx == 0:
        initial_idx = idx - 1
    if count >= max_count:
        break
    count += 1
    plt.plot(["1", "2", "3"],row.values, label="{} #{}".format(selected_species, idx-initial_idx))
plt.legend(bbox_to_anchor=(1,1))
plt.title("Length of all {} over period of 3 weeks".format(selected_species))
plt.xlabel("Week")
plt.ylabel("Length in inches")
st.pyplot(fig)


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

class AutoSidebar():
    def __init__(self):
        self.__sidebar = []

    def header(self, text, tag):
        st.header(text, tag)
        self.__sidebar.append({"type": "header", "text": f"[{text}](#{tag})"})

    def subheader(self, text, tag):
        st.subheader(text, tag)
        self.__sidebar.append({"type": "subheader", "text": f"[{text}](#{tag})"})

    def title(self, text, tag):
        st.title(text, tag)
        self.__sidebar.append({"type": "title", "text": f"[{text}](#{tag})"})

    def make(self):
        for s in self.__sidebar:
            if s["type"] == "header":
                st.sidebar.header(s["text"])
            elif s["type"] == "subheader":
                st.sidebar.subheader("> "+s["text"])
            else:
                st.sidebar.title(s["text"])

sidebar = AutoSidebar()

df = pd.read_csv("./Fish.csv")
sidebar.title("Some fishy data", "home")
st.write("The following are some interesting graphs related to a fish dataset")
st.write("To get started, lets take a look at the kind of dataset we are looking at")
st.write("Here is the dataset in full, including some of its statistics")
st.write(df)
st.write(df.describe())

data_bar = df["Species"].value_counts()
data_pie = data_bar.to_dict()

st.markdown("---")
sidebar.header("Populations", "populations")
sidebar.subheader("Pie chart", "pie_chart")
st.write("Proportions of all the species present in the database")
fig, ax = plt.subplots()
plt.pie(data_pie.values(), labels=data_pie.keys())
plt.title("Pie chart of number of fish species")
st.pyplot(fig)

sidebar.subheader("Bar chart", "bar_chart")
st.write("Here is the same data as a bar chart")
fig, ax = plt.subplots()
ax.bar(data_bar.index, data_bar)
plt.title("Fish count by species")
plt.xlabel("Species name")
plt.ylabel("Count")
plt.xticks(rotation=45)
st.pyplot(fig)

data_bar_names = data_bar.keys()
most_common_name = data_bar_names[0]
most_common_count = data_bar[0]
second_name = data_bar_names[1]
least_name = data_bar_names[-1]
least_count = data_bar[-1]
st.write("""As we can see from the above, the {} species is the most common, with a total of {} specimen, then followed by {}. {} has the least 
         number of specimen at {} members.""".format(most_common_name, most_common_count, second_name, least_name, least_count))

st.markdown("---")
sidebar.header("Scatter plot", "scatter")
st.write("Next, lets take a look at the weight and widths of all the Pikes")
data_scatter_x = df.loc[df["Species"] == "Pike", "Weight"]
data_scatter_y = df.loc[df["Species"] == "Pike", "Width"]
fig, ax = plt.subplots()
plt.scatter(data_scatter_x, data_scatter_y)
plt.xlabel("Weight in grams")
plt.ylabel("Width in inches")
plt.title("Scatter plot of weight vs width for all pike fish")
st.pyplot(fig)

st.markdown("---")
sidebar.header("Statistical view of all fish widths", "box_plots")
data_box = {species : df.loc[df["Species"] == species, "Width"].tolist() for species in df["Species"].unique()}
data_box_labels = list(data_box.keys())
data_box_values = list(data_box.values())
fig, ax = plt.subplots()
plt.boxplot(data_box_values, labels=data_box_labels)
plt.xlabel("Species")
plt.ylabel("Widths in inches")
plt.title("Box plot of the widths of each type of fish")
st.pyplot(fig)

st.markdown("---")
sidebar.header("Interactive fish lengths", "lengths")
species = df["Species"].unique()
st.write("Get the lengths of the selected species over the course of 3 weeks (will be limited to the first 5 fish of the selected species)")
selected_species = st.selectbox("select", species)
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
plt.title("Length of first 5 {} over period of 3 weeks".format(selected_species))
plt.xlabel("Week")
plt.ylabel("Length in inches")
st.pyplot(fig)

sidebar.make()
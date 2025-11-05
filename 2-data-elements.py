import streamlit as st
import pandas as pd
import numpy as np

# defining random values in a datarfame using pandas and numpy
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10)))

# Bagian 1 : Highlighting minimum value objects
st.dataframe(df.style.highlight_min(axis=0))

# Bagian 2 : Defining data in table
st.table(df)

# Bagian 3 : Defining Metrics
st.metric(label="Temperature", value="31 C", delta="1.2 C")
    
# Defining Columns
c1, c2, c3 = st.columns(3)
# Defining Metrics
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Populatuon", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")

# Defining multiple arguments in write function
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

# importing Necessary Libraries
import altair as alt
# Defining random values for chart
df = pd.DataFrame(
np.random.randn(10,2),
columns=['a', 'b'])
# Defining Chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b'])
# Defining Chart in write() function
st.write(chart)

# Bagian 4 : Magic
# math calculations with no functions defined
"Adding 5 & 4 =", 5+4
# Displaying variable 'a' and its value
a = 5
'a', a

# Markdown with magic
"""
# Magic Feature
Markdown working without defining its function explicity.
"""
# Dataframe using magic
import pandas as pd
df = pd.DataFrame({'col' : [1,2]})
'dataframe', df

# Magic working on charts
import matplotlib.pyplot as plt
import numpy as np
s = np.random.logistic(10,5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
# Magic chart
"chart", chart


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("book_data.csv")

# Display the data
st.title('Book Data Visualization')

# Visualize the distribution of book prices
st.subheader('Distribusi Harga Buku:')
fig, ax = plt.subplots()
sns.histplot(data['Harga'], bins=20, color='skyblue', edgecolor='black')
ax.set_xlabel('Harga ($)')
ax.set_ylabel('Jumlah Buku')
st.pyplot(fig)

# Visualize the number of books with each rating
st.subheader('Jumlah Buku dengan Setiap Rating:')
rating_counts = data['Rating'].value_counts()
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(rating_counts.index, rating_counts.values, color='lightgreen', edgecolor='black')
ax.set_xlabel('Rating')
ax.set_ylabel('Jumlah Buku')
st.pyplot(fig)

# Visualize the average book price for each rating category
st.subheader('Rata-rata Harga Buku untuk Setiap Rating:')
average_price_by_rating = data.groupby('Rating')['Harga'].mean().reset_index()
fig, ax = plt.subplots()
sns.barplot(x='Rating', y='Harga', data=average_price_by_rating, palette='viridis', order=['One', 'Two', 'Three', 'Four', 'Five'])
ax.set_xlabel('Rating')
ax.set_ylabel('Rata-rata Harga ($)')
st.pyplot(fig)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title(
    "Bike Sharing Data Analysis"
)

day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")


# Menggabungkan data season dan cnt
pilih_data = day_df.groupby('season')['cnt'].mean().reset_index()

# Mengonversi DataFrame menjadi array numpy
data_array = pilih_data.to_numpy()

# Memisahkan variabel x (independen) dan y (dependent)
x = data_array[:, 0]
y = data_array[:, 1]

# Set up Streamlit app
st.header("Pengaruh musim terhadap jumlah pengguna rental sepeda")
musim_labels = {1: 'Musim Semi', 2: 'Musim panas', 3: 'Musim gugur', 4: 'Musim Dingin'}
x_labels = [musim_labels[int(val)] for val in x.flatten()]

# Plot the bar chart
fig, ax = plt.subplots()
ax.bar(x, y)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Pengguna")
ax.set_xticks(x.flatten().astype(int))
ax.set_xticklabels(x_labels)

# Display the plot using Streamlit
st.pyplot(fig)


# menggabungkan data yr dan cnt
pilih_data = day_df.groupby('yr')['cnt'].mean().reset_index()

# mengonversi dataframe menjadi array numpy
data_array = pilih_data.to_numpy()

# memisahkan variabel x (independen) dan y (dependent)
x = data_array[:,0]
y = data_array[:, 1]

st.header(" data dari tahun 2011 to 2012 terhadap jumlah pengguna rental sepeda")
tahun_labels = {0: '2011', 1: '2012'}
x_labels = [tahun_labels[int(val)] for val in x.flatten()]

fig, ax = plt.subplots()
ax.bar(x,y)
ax.set_xlabel("tahun")
ax.set_ylabel("jummlah pengguna")
ax.set_xticks(x.flatten().astype(int))
ax.set_xticklabels(x_labels)

# Display the plot using Streamlit
st.pyplot(fig)

# Mengelompokkan data untuk tahun 2011 dan 2012
yr_0_df = day_df[day_df['yr'] == 0]
yr_1_df = day_df[day_df['yr'] == 1]
isi = [yr_0_df['cnt'].sum(), yr_1_df['cnt'].sum()]

# Plotting pie chart
labelss = ("2011", "2012")
colors = ['#8B4513', '#FFF8DC']
explode = (0.1, 0)

st.header("Persentase Jumlah pengguna rental sepeda tahun 2011 dan 2012")
fig , ax = plt.subplots()
ax.pie(
    x=isi,
    labels=labelss,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode,
    startangle=90,  # Untuk mulai pie chart dari sudut 90 derajat (di atas)

)


st.pyplot(fig)

# menggabungkan data weathersit
pilih_data = day_df.groupby('weathersit')['cnt'].mean().reset_index()

# mengonversi dataframe menjadi array numpy
data_array = pilih_data.to_numpy()

# memisahkan variabel x (independen) dan y (dependent)
x = data_array[:,0]
y = data_array[:, 1]

st.header("pengaruh cuaca terhadap jumlah pengguna rental sepeda")
cuaca_labels = {1: 'Cerah dan/atau Berawan', 2: 'Berkabut dan Berawan', 3: 'Bersalju,Hujan,dan/atau Petir'}
x_labels = [cuaca_labels[int(val)] for val in x.flatten()]

fig, ax = plt.subplots()
ax.bar(x,y)
ax.set_xlabel("Cuaca")
ax.set_ylabel("jummlah pengguna")
ax.set_xticks(x.flatten().astype(int),x_labels,rotation=20)
ax.set_xticklabels(x_labels)

st.pyplot(fig)

# menggabungkan data sweathersit
pilih_data = hour_df.groupby('hr')['cnt'].mean().reset_index()

# mengonversi dataframe menjadi array numpy
data_array = pilih_data.to_numpy()

# memisahkan variabel x (independen) dan y (dependent)
x = data_array[:,0]
y = data_array[:, 1]

# memisahkan variabel x (independen) dan y (dependent)
st.header("pengaruh jam terhadap jumlah pengguna rental sepeda")
tahun_labels = {}
for i in range(24):
    tahun_labels[i] = i + 1
x_labels = [tahun_labels[int(val)] for val in x.flatten()]

# Plot the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x, y)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Pengguna")
ax.set_xticks(x.flatten().astype(int))
ax.set_xticklabels(x_labels)

# Display the plot using Streamlit
st.pyplot(fig)

# membuat garis regresi linear tanpa menggunakan algoritma machine learning
fig, ax = plt.subplots()
sns.regplot(
    x=day_df['instant'],
    y=day_df['cnt']
)
st.header("Seluruh record data terhadap jumlah pengguna rental sepeda")
ax.set_xlabel("record data")
ax.set_ylabel("jumlah pengguna")

st.pyplot(fig)

st.header("Conclusion")

st.write(
    """
- Berdasarkan visualisasi data mengenai pengaruh musim terhadap jumlah pengguna rental sepeda , diketahui bahwa musim gugur merupakan musim dengan jumlah pengguna rental sepeda terbanyak , kemungkinan hal ini dikarenakan musim gugur memiliki pemandangan yang indah serta cuaca yang nyaman sehingga banyak yang ingin melakukan aktivitas - aktivitas diluar salah satunya adalah aktivitas sepeda.
- Kondisi rental sepeda dari tahun 2011 hingga 2012 mengalami kenaikan , hal ini menandakan bahwa peminat aktivitas sepeda semakin tinggi serta bisnis rental sepeda mengalamai peningkatan sebesar 64%
- pengaruh hari liburan , hari kerja dan juga hari-hari dalam seminggu terhadap jumlah pengguna tidaklah memiliki selisih yang signifikan , walaupun begitu pada hari liburan memliki pengguna rental sepeda yang terbanyak daripada hari lain
- pengaruh cuaca terhadap jumalh pengguna memilkiki pengaruh yang signifikan dimana banyak pengguna rental sepeda melakukan aktivitas pada cuaca yang cerah dan/atau berawan
- Dapat Diketahui bahwa jumlah pengguna rental sepeda rata-rata terbanyak adalah pada waktu jam 6 sore dan rata-rata paling sedikit adalah jam 12 malam
- Berdasarkan jumlah record data yang ada yaitu merepresentasikan data dari tanggal 2011-01-01 hingga 2012-12-31 terhadap jumlah penggunanya diketahui terdapat kenaikan rata-rata jumlah pengguna rental ini menunjukkan bahwa bisnis berjalan dengan sangat baik dan disertai dnegan nilai korelasi yang positif yaitu 1 menunjukkan bahwa hubungannya bersifat saling bersesuaian.
    """
)
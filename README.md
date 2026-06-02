# Sistem Pakar Diagnosa Penyakit Bawang Merah Varietas Bima

Aplikasi ini adalah sistem pakar berbasis Streamlit untuk membantu melakukan diagnosa awal penyakit dan hama pada tanaman bawang merah varietas Bima. Sistem menggunakan kombinasi metode Forward Chaining dan Certainty Factor untuk mencocokkan gejala yang dipilih pengguna dengan basis aturan yang tersedia.

Project ini dibuat dengan struktur modular supaya mudah dibaca, dirawat, dan dikembangkan. Data pengetahuan disimpan dalam file CSV, logic diagnosa dipisahkan di folder `core`, sedangkan tampilan dan styling dipisahkan di folder `components`.

## Ringkasan Project

- Nama aplikasi: Sistem Pakar Diagnosa Penyakit Bawang Merah Varietas Bima
- Framework utama: Streamlit
- Bahasa: Python
- Metode diagnosa: Forward Chaining dan Certainty Factor
- Jumlah gejala: 53 gejala
- Jumlah penyakit/hama: 12 jenis
- Jumlah aturan: 54 rules
- Data source lokal: CSV di folder `data`
- Tema tampilan: Light mode dan Dark mode

## Fitur Utama

1. Diagnosa penyakit berdasarkan gejala tanaman bawang merah.
2. Pemilihan banyak gejala sekaligus melalui multiselect.
3. Pengelompokan gejala berdasarkan area tanaman:
   - Gejala pada daun
   - Gejala pada umbi
   - Gejala pada akar dan batang
   - Gejala umum pada tanaman
4. Perhitungan tingkat kepastian diagnosis dengan Certainty Factor.
5. Hasil diagnosis utama ditampilkan sebagai kartu besar.
6. Kemungkinan penyakit lain tetap ditampilkan sebagai hasil pembanding.
7. Tampilan statistik jumlah gejala, penyakit, dan rules.
8. Informasi ringkas tentang metode Forward Chaining dan Certainty Factor.
9. Empty state, warning state, dan no-match state yang sudah diberi styling.
10. Pilihan tema Light atau Dark dari halaman aplikasi.

## Teknologi Yang Digunakan

- Python
- Streamlit
- Pandas
- HTML dan CSS custom untuk styling komponen Streamlit
- CSV sebagai basis data pengetahuan

## Struktur Folder

```text
projekpakar/
├── app.py
├── README.md
├── components/
│   ├── __init__.py
│   ├── styles.py
│   └── ui.py
├── core/
│   ├── __init__.py
│   ├── data_loader.py
│   └── engine.py
└── data/
    ├── gejala.csv
    ├── penyakit.csv
    └── rules.csv
```

## Penjelasan File

### `app.py`

File utama aplikasi Streamlit. Tugasnya:

- Mengatur konfigurasi halaman Streamlit.
- Mengatur state tema Light/Dark.
- Meng-inject CSS dari `components/styles.py`.
- Memuat data dari CSV.
- Menampilkan hero section, statistik, input gejala, tombol diagnosa, hasil diagnosa, dan footer.
- Menghubungkan input pengguna dengan engine diagnosa.

### `core/data_loader.py`

File ini bertanggung jawab untuk memuat data CSV:

- `gejala.csv`
- `penyakit.csv`
- `rules.csv`

Data dimuat menggunakan Pandas dan di-cache dengan `st.cache_data` supaya aplikasi tidak membaca ulang CSV secara berlebihan setiap kali halaman rerun.

File ini juga berisi fungsi `get_symptom_categories()` untuk mengelompokkan gejala berdasarkan kata kunci pada nama gejala, misalnya `daun`, `umbi`, `akar`, `batang`, `bercak`, dan sejenisnya.

### `core/engine.py`

File ini berisi logic utama diagnosa:

- Menerima daftar gejala yang dipilih pengguna.
- Melakukan filtering rules berdasarkan gejala yang cocok.
- Mengelompokkan rule berdasarkan penyakit.
- Menghitung nilai Certainty Factor tiap penyakit.
- Mengurutkan hasil dari persentase tertinggi ke terendah.

Catatan penting: logic matematika pada file ini diberi catatan sebagai logic final dan sebaiknya tidak diubah sembarangan.

### `components/ui.py`

File ini berisi fungsi render komponen tampilan, seperti:

- Hero section
- Statistik aplikasi
- Kartu metodologi
- Empty state
- Warning jika gejala belum dipilih
- Pesan jika tidak ada kecocokan
- Kartu hasil diagnosis utama
- Daftar kemungkinan penyakit lain
- Footer

### `components/styles.py`

File ini berisi CSS custom untuk mempercantik tampilan Streamlit. Styling mencakup:

- Hero section
- Section header
- Multiselect
- Tombol diagnosa
- Kartu hasil
- Progress bar Certainty Factor
- Footer
- Empty state
- Light theme
- Dark theme

Fungsi `get_theme_css(theme_mode)` digunakan untuk memilih CSS berdasarkan tema yang sedang aktif.

### Folder `data`

Folder ini menyimpan basis pengetahuan sistem pakar dalam format CSV.

#### `gejala.csv`

Berisi daftar gejala.

Kolom:

```text
id_gejala,nama_gejala
```

Contoh:

```text
G001,Umbi membusuk
G003,Daun terdapat bercak melekuk
G012,Tanaman kerdil
```

#### `penyakit.csv`

Berisi daftar penyakit dan hama yang dapat didiagnosa.

Kolom:

```text
id_penyakit,nama_penyakit
```

Contoh:

```text
P001,"Penyakit Trotol, Bercak Ungu (Purple blotch)"
P004,Penyakit Moler atau Layu Fusarium (Fusarium Basal Plate Rot)
P010,Hama Putih atau Trips (Thrips)
```

#### `rules.csv`

Berisi aturan hubungan antara penyakit, gejala, dan bobot Certainty Factor.

Kolom:

```text
id_rule,id_penyakit,id_gejala,bobot_cf
```

Contoh:

```text
R001,P001,G001,0.8
R004,P001,G004,0.6
R020,P004,G020,1
```

## Daftar Penyakit dan Hama

Sistem ini mencakup 12 penyakit/hama:

1. P001 - Penyakit Trotol, Bercak Ungu (Purple blotch)
2. P002 - Penyakit Embun Buluk/Tepung Palsu (Downy mildew)
3. P003 - Penyakit otomatis, Antraknose (Antrachnose)
4. P004 - Penyakit Moler atau Layu Fusarium (Fusarium Basal Plate Rot)
5. P005 - Mati pucuk
6. P006 - Penyakit Buluk Penicillium (Blue Mold)
7. P007 - Virus Kerdil Kuning, Virus Mosaik (Onion Yellow Dwarf Virus)
8. P008 - Penyakit Nematoda Buncak Akar (Root Knot Nemotade)
9. P009 - Ulat grayak atau ngengat Spodoptera exigua L
10. P010 - Hama Putih atau Trips (Thrips)
11. P011 - Ulat Tanah (Cut Worm)
12. P012 - Lalat Pengorok Daun (Liriomyza chinensis)

## Daftar Gejala

Sistem ini menggunakan 53 gejala:

| ID | Nama Gejala |
| --- | --- |
| G001 | Umbi membusuk |
| G002 | Jaringan umbi mengering |
| G003 | Daun terdapat bercak melekuk |
| G004 | Bercak daun berwarna putih atau kelabu |
| G005 | becak tampak bercincin, dan warnanya agak keunguan |
| G006 | Ujung daun kering |
| G007 | Umbi berwarna kecoklatan |
| G008 | Umbi berwarna kecoklatan |
| G009 | Bagian umbi dalam tampak kering dan pucat |
| G010 | Ujung daun terdapat bercak hijau pucat |
| G011 | Terdapat miselium dan spora pada bercak daun |
| G012 | Tanaman kerdil |
| G013 | Adanya bercak putih berbentuk lonjong hingga bulat, kadang-kadang berbentuk belah ketupat pada daun bawang |
| G014 | Bercak daun berwarna putih |
| G015 | daun yang terinfeksi akan patah dan terkulai |
| G016 | Daun bawah rebah |
| G017 | Tanaman bawang merah mendadak layu |
| G018 | Akar tanaman membusuk dan mudah dicabut |
| G019 | Daun tanaman terkulai |
| G020 | Daun melintir dan mengerut |
| G021 | Umbi membusuk dan juga terdapat jamur berwarna putih yang membuat tanaman bawang merah mati. |
| G022 | Ujung daun busuk kebasah-basahan |
| G023 | Ujung daun berwarna coklat |
| G024 | Ujung daun mati |
| G025 | Tanaman menimbulkan bau busuk yang menyengat |
| G026 | Lapisan umbi terdapat bercak merah keunguan |
| G027 | Lapisan umbi tampak basah |
| G028 | Lapisan umbi terpisah-pisah |
| G029 | Umbi berair |
| G030 | Umbi berukuran kecil |
| G031 | Bentuk daun lebih kecil |
| G032 | Warna daun belang hijau pucat sampai kekuningan |
| G033 | Daun berpilin |
| G034 | Tanaman menguning |
| G035 | Tanaman lebih kaku |
| G036 | Tanaman lebih kerdil |
| G037 | Rambut akar sedikit |
| G038 | Terdapat puru berbentuk bulat pada akar |
| G039 | Akar lebih pendek |
| G040 | Akar lebih Sedikit |
| G041 | Terdapat bekas gigitan ulat |
| G042 | Daun berlubang tidak beraturan |
| G043 | Jika serangan berat daun menjadi gundul |
| G044 | Umbi berukuran kecil |
| G045 | Daun bernoda putih mengkilat seperti perak |
| G046 | Seluruh daun berwarna putih jika sudah parah |
| G047 | Pangkal batang menunjukkan bekas gigitan ulat |
| G048 | Pangkal batang terpotong potong |
| G049 | Batang rebah |
| G050 | Batang rusak dan berceceran |
| G051 | Terdapat bintik-bintik putih pada daun |
| G052 | daun penuh dengan korokan |
| G053 | Daun menjadi kering dan warna daun seperti terbakar |

## Ringkasan Rules Per Penyakit

| ID Penyakit | Jumlah Rule |
| --- | ---: |
| P001 | 6 |
| P002 | 7 |
| P003 | 4 |
| P004 | 5 |
| P005 | 3 |
| P006 | 5 |
| P007 | 4 |
| P008 | 7 |
| P009 | 3 |
| P010 | 3 |
| P011 | 4 |
| P012 | 3 |

## Cara Kerja Sistem

### 1. Pengguna Memilih Gejala

Pengguna memilih satu atau lebih gejala yang terlihat pada tanaman bawang merah melalui input multiselect. Setiap pilihan memiliki format:

```text
[ID_GEJALA] Nama gejala
```

Contoh:

```text
[G001] Umbi membusuk
```

Setelah dipilih, aplikasi mengambil ID gejala dari label tersebut.

### 2. Forward Chaining

Forward Chaining digunakan untuk mencari aturan yang sesuai dengan fakta awal, yaitu gejala yang dipilih pengguna.

Secara sederhana:

```python
matched_rules = rules_df[rules_df["id_gejala"].isin(selected_gejala)]
```

Jika tidak ada rule yang cocok, aplikasi menampilkan pesan bahwa diagnosis tidak ditemukan.

### 3. Pengelompokan Berdasarkan Penyakit

Rules yang cocok dikelompokkan berdasarkan `id_penyakit`.

```python
grouped = matched_rules.groupby("id_penyakit")
```

Dengan cara ini, setiap penyakit akan dihitung berdasarkan kumpulan gejala yang cocok dengan penyakit tersebut.

### 4. Perhitungan Certainty Factor

Setiap rule memiliki `bobot_cf`, yaitu bobot tingkat keyakinan pakar terhadap hubungan antara gejala dan penyakit.

Rumus kombinasi CF yang digunakan:

```text
CFcombine = CFold + CFgejala * (1 - CFold)
```

Nilai akhir kemudian dikonversi menjadi persentase:

```text
persentase = cf_akhir * 100
```

### 5. Ranking Hasil

Setelah CF tiap penyakit dihitung, hasil diagnosis diurutkan dari persentase tertinggi ke terendah.

Hasil teratas ditampilkan sebagai diagnosis utama, sedangkan hasil lain ditampilkan sebagai kemungkinan penyakit lainnya.

## Alur Penggunaan Aplikasi

1. Jalankan aplikasi Streamlit.
2. Pilih tema Light atau Dark jika diperlukan.
3. Buka bagian kategori gejala.
4. Pilih gejala yang sesuai dengan kondisi tanaman.
5. Klik tombol `Mulai Diagnosa Penyakit`.
6. Lihat diagnosis utama dan tingkat kepastiannya.
7. Periksa juga kemungkinan penyakit lainnya jika muncul.

## Instalasi

Pastikan Python sudah terinstall di komputer.

Clone atau buka folder project:

```bash
cd projekpakar
```

Install dependency:

```bash
pip install streamlit pandas
```

Jika ingin lebih rapi, gunakan virtual environment:

```bash
python -m venv .venv
```

Aktifkan virtual environment di Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Lalu install dependency:

```bash
pip install streamlit pandas
```

## Menjalankan Aplikasi

Jalankan perintah berikut dari root folder project:

```bash
streamlit run app.py
```

Atau:

```bash
python -m streamlit run app.py
```

Biasanya aplikasi akan terbuka di:

```text
http://localhost:8501
```

## Cara Mengubah atau Menambah Data

### Menambah Gejala

Tambahkan baris baru ke `data/gejala.csv`.

Format:

```text
G054,Nama gejala baru
```

Pastikan ID gejala tidak sama dengan ID yang sudah ada.

### Menambah Penyakit

Tambahkan baris baru ke `data/penyakit.csv`.

Format:

```text
P013,Nama penyakit baru
```

Pastikan ID penyakit tidak sama dengan ID yang sudah ada.

### Menambah Rule

Tambahkan relasi baru ke `data/rules.csv`.

Format:

```text
R055,P013,G054,0.8
```

Keterangan:

- `R055` adalah ID rule.
- `P013` adalah ID penyakit.
- `G054` adalah ID gejala.
- `0.8` adalah bobot Certainty Factor.

Bobot CF sebaiknya berada pada rentang 0 sampai 1.

## Cara Mengubah Tampilan

Sebagian besar tampilan bisa diubah melalui:

```text
components/styles.py
components/ui.py
```

Gunakan `components/styles.py` untuk mengubah warna, ukuran, radius, shadow, dan theme. Gunakan `components/ui.py` untuk mengubah struktur HTML komponen yang dirender oleh Streamlit.

## Theme Light dan Dark

Project ini sudah mendukung pemilihan tema:

- `Light`
- `Dark`

Pilihan tema disimpan di `st.session_state.theme_mode`.

Flow theme:

```text
app.py -> st.session_state.theme_mode -> get_theme_css(theme_mode) -> CSS injected ke Streamlit
```

Jika `theme_mode` bernilai `Dark`, aplikasi memakai CSS dasar ditambah override dark theme. Jika `theme_mode` bernilai `Light`, aplikasi hanya memakai CSS dasar.

## Troubleshooting

### Streamlit tidak bisa jalan

Pastikan dependency sudah terinstall:

```bash
pip install streamlit pandas
```

Lalu jalankan:

```bash
python -m streamlit run app.py
```

### Port 8501 sudah digunakan

Jalankan aplikasi di port lain:

```bash
python -m streamlit run app.py --server.port=8502
```

### Data tidak muncul atau error saat membaca CSV

Pastikan folder `data` ada dan berisi:

```text
gejala.csv
penyakit.csv
rules.csv
```

Pastikan nama kolom tetap sesuai:

```text
gejala.csv   -> id_gejala,nama_gejala
penyakit.csv -> id_penyakit,nama_penyakit
rules.csv    -> id_rule,id_penyakit,id_gejala,bobot_cf
```

### Hasil diagnosis tidak ditemukan

Kemungkinan penyebab:

- Gejala yang dipilih tidak memiliki rule yang cocok.
- Data pada `rules.csv` belum mencakup kombinasi gejala tersebut.
- ID gejala pada `rules.csv` tidak cocok dengan ID di `gejala.csv`.

## Catatan Pengembangan

- Logic diagnosis utama berada di `core/engine.py`.
- Hindari mengubah rumus CF tanpa validasi ulang.
- Jika menambah data, pastikan ID pada semua CSV konsisten.
- Jika ingin menambah kategori gejala, ubah logic di `get_symptom_categories()`.
- Jika ingin menambah tema baru, tambahkan CSS override di `components/styles.py`.

## Status

Project ini adalah aplikasi lokal berbasis Streamlit dan dapat dijalankan langsung dari root folder project.

## Lisensi

Belum ditentukan.

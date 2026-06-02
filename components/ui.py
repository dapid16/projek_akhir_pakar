import streamlit as st

def render_symptom_selector(gejala_df):
    """
    Menampilkan daftar gejala berdasarkan kategori.
    User harus mencentang checkbox terlebih dahulu sebelum bisa memilih tingkat keyakinan.
    Tingkat keyakinan default diset ke pilihan paling bawah ('Tidak Yakin').
    """
    # List pilihan dari yang paling rendah tingkat kemungkinannya sesuai Jurnal
    cf_options = [
        "Tidak Yakin (0.0)",
        "Sangat Tidak Tahu (+0.2)",
        "Mungkin (+0.4)",
        "Kemungkinan Besar (+0.6)",
        "Hampir Pasti (+0.8)",
        "Pasti (1.0)"
    ]
    
    # Mapping string pilihan ke nilai float Certainty Factor User
    cf_mapping = {
        "Tidak Yakin (0.0)": 0.0,
        "Sangat Tidak Tahu (+0.2)": 0.2,
        "Mungkin (+0.4)": 0.4,
        "Kemungkinan Besar (+0.6)": 0.6,
        "Hampir Pasti (+0.8)": 0.8,
        "Pasti (1.0)": 1.0
    }
    
    selected_symptoms = {}
    
    for index, row in gejala_df.iterrows():
        id_gejala = row['id_gejala']
        nama_gejala = row['nama_gejala']
        
        # 1. Bikin checkbox utama buat nandain gejala dialami atau kagak
        is_checked = st.checkbox(
            label=f"**{id_gejala}** - {nama_gejala}",
            key=f"check_{id_gejala}"
        )
        
        # 2. Kalo dicentang, baru munculin tingkat keyakinannya
        if is_checked:
            # Pake indentasi visual dikit biar rapi di UI
            col1, col2 = st.columns([0.1, 0.9])
            with col2:
                chosen_cf_text = st.radio(
                    label=f"Seberapa yakin tanaman mengalami gejala {id_gejala}?",
                    options=cf_options,
                    index=0,  # Otomatis milih indeks 0: 'Tidak Yakin (0.0)'
                    key=f"cf_{id_gejala}",
                    horizontal=True # Bikin mendatar biar ga makan tempat ke bawah
                )
                # Masukin nilai float-nya ke dictionary output
                selected_symptoms[id_gejala] = cf_mapping[chosen_cf_text]
                
        st.write("---") # Pembatas antar gejala biar ga numpuk
        
    return selected_symptoms
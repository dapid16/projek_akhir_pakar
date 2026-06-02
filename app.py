import streamlit as st

st.set_page_config(
    page_title="Sistem Pakar Bawang Merah",
    page_icon="🧅",
    layout="wide",
)

# Kodingan bersih tanpa load data solusi
from core.data_loader import load_data, get_symptom_categories
from core.engine import diagnose

# =========================
# LOAD DATA
# =========================
# Kita abaikan solusi_df, cuma load gejala, penyakit, dan rules sesuai orisinalitas jurnal
gejala_df, penyakit_df, rules_df, _ = load_data()

# =========================
# HEADER
# =========================
st.title("🧅 Sistem Pakar Diagnosa Penyakit Bawang Merah")
st.caption("Metode Forward Chaining + Certainty Factor (Pure Scientific Verification)")

st.divider()

# =========================
# CERTAINTY OPTIONS
# =========================
certainty_options = {
    "Tidak Yakin": 0.0,
    "Sangat Tidak Tahu": 0.2,
    "Mungkin": 0.4,
    "Cukup Yakin": 0.6,
    "Yakin": 0.8,
    "Sangat Yakin": 1.0,
}

# =========================
# INPUT GEJALA
# =========================
st.subheader("🩺 Pilih Gejala Tanaman")

categories = get_symptom_categories(
    gejala_df,
    rules_df,
    penyakit_df
)

selected_gejala = []
user_cf_map = {}

for cat_name, symptoms in categories.items():

    if not symptoms:
        continue

    with st.expander(f"{cat_name} ({len(symptoms)} gejala)"):

        for gid, nama_gejala in symptoms:

            col1, col2 = st.columns([3, 2])

            with col1:
                checked = st.checkbox(
                    f"**{gid}** - {nama_gejala}",
                    key=f"cb_{gid}"
                )

            with col2:
                if checked:
                    selected_level = st.selectbox(
                        f"Keyakinan {gid}",
                        options=list(certainty_options.keys()),
                        index=0,
                        key=f"cf_{gid}",
                        label_visibility="collapsed",
                    )
                else:
                    st.selectbox(
                        f"Keyakinan {gid} (disabled)",
                        options=["Tidak Yakin"],
                        index=0,
                        disabled=True,
                        key=f"disabled_cf_{gid}",
                        label_visibility="collapsed",
                    )

            if checked:
                selected_gejala.append(gid)
                user_cf_map[gid] = certainty_options[selected_level]

# =========================
# VALIDASI & RUN ENGINE
# =========================
st.divider()

if len(selected_gejala) > 0:
    st.success(f"🔥 {len(selected_gejala)} gejala aktif dipilih")

if st.button(
    "🔍 Mulai Diagnosa",
    type="primary",
    use_container_width=True
):

    if len(selected_gejala) < 3:
        st.warning(
            "⚠️ Disarankan memilih minimal 3 gejala untuk hasil diagnosa yang lebih akurat. Silakan pilih lebih banyak gejala atau pastikan tingkat keyakinan sudah diatur dengan benar."
        )

    else:
        valid_gejala = [gid for gid in selected_gejala if user_cf_map[gid] > 0.0]

        if not valid_gejala:
            st.error("Semua gejala yang dipilih memiliki tingkat keyakinan 'Tidak Yakin'. Silakan pilih tingkat keyakinan yang lebih tinggi untuk setidaknya satu gejala.")
        else:
            hasil = diagnose(
                selected_gejala=valid_gejala,
                user_cf_map=user_cf_map,
                rules_df=rules_df,
                penyakit_df=penyakit_df,
            )

            if hasil is None:
                st.error("Maaf, tidak ditemukan kecocokan antara gejala yang dipilih dengan aturan yang ada. Coba pilih kombinasi gejala yang berbeda atau pastikan tingkat keyakinan sudah diatur dengan benar.")

            else:
                st.subheader("📊 Hasil Analisis Diagnosa")

                utama = hasil[0]

                st.success(
                    f"🏆 **DIAGNOSIS UTAMA:** Penyakit {utama['nama_penyakit']} ({utama['id_penyakit']})"
                )

                st.metric(
                    "Tingkat Kepastian (Certainty Factor)",
                    f"{utama['persentase']:.2f}%"
                )

                st.progress(
                    min(max(int(utama["persentase"]), 0), 100)
                )

                st.write("### 📋 Detail Aturan (Rule Match)")

                st.write(
                    f"""
                    - **Gejala yang cocok:** {utama['matched_count']} gejala
                    - **Total aturan pada penyakit:** {utama['total_rule_gejala']} rule
                    - **Persentase kecocokan aturan:** {utama['match_percentage']}%
                    """
                )

                # =========================
                # GEJALA PENDUKUNG
                # =========================
                st.write("### 🩺 Gejala yang Mendukung Analisis")

                for item in utama["matched_gejala"]:
                    st.info(
                        f"""
                        **Kode:** {item['id_gejala']}  
                        | CF Pakar: `{item['cf_pakar']}`  
                        | CF User: `{item['cf_user']}`  
                        | Perhitungan Akhir: `{round(item['cf_final'], 2)}`
                        """
                    )

                # =========================
                # PENYAKIT LAIN
                # =========================
                if len(hasil) > 1:
                    st.write("## 📋 Kemungkinan Jenis Penyakit Lain")

                    for item in hasil[1:]:
                        with st.expander(
                            f"{item['nama_penyakit']} ({item['id_penyakit']}) — Tingkat Keyakinan: {item['persentase']:.2f}%"
                        ):

                            st.progress(
                                min(max(int(item["persentase"]), 0), 100)
                            )

                            st.write(
                                f"""
                                - **Gejala cocok:** {item['matched_count']}
                                - **Total rule penyakit:** {item['total_rule_gejala']}
                                - **Persentase rule cocok:** {item['match_percentage']}%
                                """
                            )
else:
    st.info(
        "Silakan pilih gejala yang dialami tanaman bawang merah Anda di atas, lalu klik tombol 'Mulai Diagnosa' untuk melihat hasilnya!"
    )
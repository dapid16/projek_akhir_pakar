"""
Sistem Pakar Diagnosa Penyakit Bawang Merah Varietas Bima
=========================================================
Metode: Forward Chaining & Certainty Factor

Main entry point — clean, modular, and beautifully styled.
Run with: streamlit run app.py
"""

import streamlit as st

# --- Page Configuration (must be the first Streamlit command) ---
st.set_page_config(
    page_title="Sistem Pakar — Diagnosa Penyakit Bawang Merah",
    page_icon="🧅",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Imports ---
from core.data_loader import load_data, get_symptom_categories
from core.engine import diagnose
from components.styles import get_theme_css
from components.ui import (
    render_hero,
    render_stats,
    render_methodology_info,
    render_empty_state,
    render_warning_no_selection,
    render_no_match,
    render_main_result,
    render_other_results,
    render_footer,
)

# --- Theme State ---
if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "Light"

# --- Inject Custom CSS ---
st.markdown(get_theme_css(st.session_state.theme_mode), unsafe_allow_html=True)

# --- Theme Picker ---
theme_spacer, theme_picker = st.columns([4, 1.4])
with theme_picker:
    st.radio(
        "Tema",
        options=["Light", "Dark"],
        horizontal=True,
        key="theme_mode",
    )

# --- Load Data ---
gejala_df, penyakit_df, rules_df = load_data()

# ==========================================
# 1. HERO SECTION
# ==========================================
render_hero()

# ==========================================
# 2. STATS ROW
# ==========================================
render_stats(
    gejala_count=len(gejala_df),
    penyakit_count=len(penyakit_df),
    rules_count=len(rules_df),
)

# ==========================================
# 3. METHODOLOGY INFO
# ==========================================
with st.expander("ℹ️  Tentang Metode yang Digunakan", expanded=False):
    render_methodology_info()

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 4. SYMPTOM INPUT SECTION
# ==========================================
st.markdown("""
<div class="section-header">
    <div class="section-icon section-icon-green">🩺</div>
    <div class="section-title">Pilih Gejala Tanaman</div>
</div>
<p class="section-desc">Pilih semua gejala yang terlihat pada tanaman bawang merah Anda. Semakin banyak gejala yang dipilih, semakin akurat hasil diagnosa.</p>
""", unsafe_allow_html=True)

# Get symptom categories for organized display
categories = get_symptom_categories(gejala_df, rules_df, penyakit_df)

# Collect all selected symptoms across categories
selected_gejala = []

for cat_name, symptoms in categories.items():
    if not symptoms:
        continue

    with st.expander(f"{cat_name}  ({len(symptoms)} gejala)", expanded=False):
        # Build options for multiselect
        options = [f"[{gid}] {name}" for gid, name in symptoms]

        selected = st.multiselect(
            label=f"Pilih gejala {cat_name}",
            options=options,
            placeholder="Klik untuk memilih gejala...",
            label_visibility="collapsed",
            key=f"ms_{cat_name}",
        )

        # Extract the symptom IDs from the selected labels
        for sel in selected:
            # sel format: "[G001] Umbi membusuk"
            gid = sel.split("]")[0].replace("[", "").strip()
            selected_gejala.append(gid)

# Show selected count
if selected_gejala:
    st.markdown(
        f'<div class="selected-counter">✅ {len(selected_gejala)} gejala dipilih</div>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 5. DIAGNOSE BUTTON & RESULTS
# ==========================================
col_btn_l, col_btn_c, col_btn_r = st.columns([1, 2, 1])
with col_btn_c:
    diagnose_clicked = st.button(
        "🔍  Mulai Diagnosa Penyakit",
        type="primary",
        use_container_width=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

if diagnose_clicked:
    if not selected_gejala:
        render_warning_no_selection()
    else:
        # Run the engine (Forward Chaining + CF — UNTOUCHED logic)
        hasil = diagnose(selected_gejala, rules_df, penyakit_df)

        if hasil is None:
            render_no_match()
        else:
            # Render the primary result
            st.markdown("""
            <div class="section-header">
                <div class="section-icon section-icon-green">📊</div>
                <div class="section-title">Hasil Diagnosa</div>
            </div>
            <p class="section-desc">Berikut hasil analisis berdasarkan gejala yang Anda pilih.</p>
            """, unsafe_allow_html=True)

            # Main diagnosis
            penyakit_utama = hasil[0]
            render_main_result(penyakit_utama)

            # Other possible diseases
            if len(hasil) > 1:
                render_other_results(hasil[1:])
else:
    # Show empty state when no diagnosis has been run yet
    render_empty_state()

# ==========================================
# 6. FOOTER
# ==========================================
render_footer()

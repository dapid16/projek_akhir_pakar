import pandas as pd
import streamlit as st
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

@st.cache_data
def load_data():
    """Load all CSV data files and return as DataFrames."""
    gejala_df = pd.read_csv(os.path.join(DATA_DIR, 'gejala.csv'))
    penyakit_df = pd.read_csv(os.path.join(DATA_DIR, 'penyakit.csv'))
    rules_df = pd.read_csv(os.path.join(DATA_DIR, 'rules.csv'))
    return gejala_df, penyakit_df, rules_df


def get_symptom_categories(gejala_df, rules_df, penyakit_df):
    """
    Group symptoms by the body part / area of the plant they affect.
    Returns a dict: { category_name: [(id_gejala, nama_gejala), ...] }
    """
    # Manual categorization based on symptom text for a clean UX
    categories = {
        "🌿 Gejala pada Daun": [],
        "🧅 Gejala pada Umbi": [],
        "🌱 Gejala pada Akar & Batang": [],
        "🌾 Gejala pada Tanaman (Umum)": [],
    }

    for _, row in gejala_df.iterrows():
        gid = row['id_gejala']
        name = row['nama_gejala']
        name_lower = name.lower()

        if any(k in name_lower for k in ['daun', 'bercak', 'miselium', 'spora', 'korokan']):
            categories["🌿 Gejala pada Daun"].append((gid, name))
        elif any(k in name_lower for k in ['umbi', 'lapisan']):
            categories["🧅 Gejala pada Umbi"].append((gid, name))
        elif any(k in name_lower for k in ['akar', 'batang', 'pangkal', 'puru']):
            categories["🌱 Gejala pada Akar & Batang"].append((gid, name))
        else:
            categories["🌾 Gejala pada Tanaman (Umum)"].append((gid, name))

    return categories

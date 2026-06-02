"""
Engine module — contains the Forward Chaining + Certainty Factor logic.

CRITICAL: The mathematical logic below is verified and MUST NOT be altered.
The groupby, the cf_old loop, and the combination formula are final.
"""


def diagnose(selected_gejala, rules_df, penyakit_df):
    """
    Run Forward Chaining filtering + Certainty Factor calculation.

    Parameters
    ----------
    selected_gejala : list
        List of selected symptom IDs (e.g. ['G001', 'G003'])
    rules_df : pd.DataFrame
        Rules dataframe with columns: id_rule, id_penyakit, id_gejala, bobot_cf
    penyakit_df : pd.DataFrame
        Disease dataframe with columns: id_penyakit, nama_penyakit

    Returns
    -------
    list[dict] or None
        Sorted list of diagnosis results (highest CF first), or None if no match.
    """
    # Proses Forward Chaining: Filter rule berdasarkan gejala yang dipilih user
    matched_rules = rules_df[rules_df['id_gejala'].isin(selected_gejala)]

    if matched_rules.empty:
        return None

    hasil_diagnosa = []

    # Kelompokkan data berdasarkan penyakit untuk dihitung CF-nya
    grouped = matched_rules.groupby('id_penyakit')

    # Proses Perhitungan Certainty Factor (CF)
    for penyakit_id, group in grouped:
        cf_old = 0
        for cf_gejala in group['bobot_cf']:
            if cf_old == 0:
                cf_old = cf_gejala
            else:
                cf_old = cf_old + cf_gejala * (1 - cf_old)

        # Ambil nama penyakit dari penyakit.csv
        nama_penyakit = penyakit_df[penyakit_df['id_penyakit'] == penyakit_id]['nama_penyakit'].values[0]
        persentase = cf_old * 100

        hasil_diagnosa.append({
            'id_penyakit': penyakit_id,
            'nama_penyakit': nama_penyakit,
            'cf_akhir': cf_old,
            'persentase': persentase
        })

    # Urutkan hasil dari persentase tertinggi ke terendah
    hasil_diagnosa = sorted(hasil_diagnosa, key=lambda x: x['persentase'], reverse=True)

    return hasil_diagnosa

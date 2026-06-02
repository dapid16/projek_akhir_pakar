"""
Engine module — contains the Forward Chaining + Certainty Factor logic with Extended UI Metrics.
"""
import pandas as pd

def diagnose(selected_gejala, user_cf_map, rules_df, penyakit_df):
    """
    Run Forward Chaining filtering + Certainty Factor calculation with UI support.
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
        matched_gejala_list = []
        
        # Hitung CF Combine sekaligus kumpulin detail gejala yang cocok
        for _, row_rule in group.iterrows():
            gid = row_rule['id_gejala']
            cf_pakar = float(row_rule['bobot_cf'])
            cf_user = float(user_cf_map.get(gid, 0.0))
            
            # Rumus CF final per gejala = CF pakar * CF user
            cf_final_gejala = cf_pakar * cf_user
            
            if cf_old == 0:
                cf_old = cf_final_gejala
            else:
                cf_old = cf_old + cf_final_gejala * (1 - cf_old)
                
            matched_gejala_list.append({
                'id_gejala': gid,
                'cf_pakar': cf_pakar,
                'cf_user': cf_user,
                'cf_final': cf_final_gejala
            })

        # Ambil nama penyakit dari penyakit.csv
        nama_penyakit = penyakit_df[penyakit_df['id_penyakit'] == penyakit_id]['nama_penyakit'].values[0]
        persentase = cf_old * 100
        
        # Hitung total rules yang terdaftar untuk penyakit ini di database
        total_rules_penyakit = len(rules_df[rules_df['id_penyakit'] == penyakit_id])
        matched_count = len(group)
        match_percentage = round((matched_count / total_rules_penyakit) * 100, 2)

        # Return data super komplit biar UI lu gak KeyError lagi, pak!
        hasil_diagnosa.append({
            'id_penyakit': penyakit_id,
            'nama_penyakit': nama_penyakit,
            'cf_akhir': cf_old,
            'persentase': persentase,
            'matched_count': matched_count,
            'total_rule_gejala': total_rules_penyakit,
            'match_percentage': match_percentage,
            'matched_gejala': matched_gejala_list
        })

    # Urutkan hasil dari persentase tertinggi ke terendah
    hasil_diagnosa = sorted(hasil_diagnosa, key=lambda x: x['persentase'], reverse=True)

    return hasil_diagnosa
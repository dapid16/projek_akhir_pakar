import pandas as pd


def calculate_cf(cf_values):
    """
    Combine certainty factor values.
    Formula sesuai jurnal:
    CFcombine = CFold + CFgejala * (1 - CFold)
    """
    cf_old = 0

    for cf in cf_values:
        if cf_old == 0:
            cf_old = cf
        else:
            cf_old = cf_old + cf * (1 - cf_old)

    return round(cf_old, 4)


def diagnose(
    selected_gejala,
    user_cf_map,
    rules_df,
    penyakit_df,
    min_match_percentage=0.6,
):
    """
    Improved Forward Chaining + Certainty Factor Engine
    """

    if not selected_gejala:
        return None

    hasil_diagnosa = []

    grouped_rules = rules_df.groupby("id_penyakit")

    for penyakit_id, rule_group in grouped_rules:

        total_rule_gejala = len(rule_group)

        gejala_rule = set(rule_group["id_gejala"].tolist())

        selected_match = gejala_rule.intersection(set(selected_gejala))

        matched_count = len(selected_match)

        if matched_count == 0:
            continue

        match_percentage = matched_count / total_rule_gejala

        # FILTER MINIMAL KEC0COKAN RULE
        if match_percentage < min_match_percentage:
            continue

        cf_values = []

        matched_gejala_detail = []

        for _, row in rule_group.iterrows():

            gejala_id = row["id_gejala"]

            if gejala_id in selected_match:

                cf_pakar = float(row["bobot_cf"])

                cf_user = float(user_cf_map.get(gejala_id, 0))

                # CF pakar × CF user
                final_cf = cf_pakar * cf_user

                cf_values.append(final_cf)

                matched_gejala_detail.append({
                    "id_gejala": gejala_id,
                    "cf_pakar": cf_pakar,
                    "cf_user": cf_user,
                    "cf_final": final_cf,
                })

        if not cf_values:
            continue

        cf_akhir = calculate_cf(cf_values)

        # normalisasi berdasarkan kelengkapan rule
        cf_akhir = cf_akhir * match_percentage

        penyakit_row = penyakit_df[
            penyakit_df["id_penyakit"] == penyakit_id
        ].iloc[0]

        hasil_diagnosa.append({
            "id_penyakit": penyakit_id,
            "nama_penyakit": penyakit_row["nama_penyakit"],
            "cf_akhir": round(cf_akhir, 4),
            "persentase": round(cf_akhir * 100, 2),
            "matched_count": matched_count,
            "total_rule_gejala": total_rule_gejala,
            "match_percentage": round(match_percentage * 100, 2),
            "matched_gejala": matched_gejala_detail,
        })

    if not hasil_diagnosa:
        return None

    hasil_diagnosa = sorted(
        hasil_diagnosa,
        key=lambda x: x["persentase"],
        reverse=True
    )

    return hasil_diagnosa
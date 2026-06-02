import pandas as pd


def load_data():

    gejala_df = pd.read_csv("data/gejala.csv")
    penyakit_df = pd.read_csv("data/penyakit.csv")
    rules_df = pd.read_csv("data/rules.csv")
    solusi_df = pd.read_csv("data/solusi.csv")

    return (
        gejala_df,
        penyakit_df,
        rules_df,
        solusi_df,
    )


def get_symptom_categories(
    gejala_df,
    rules_df,
    penyakit_df
):

    categories = {}

    for _, penyakit in penyakit_df.iterrows():

        pid = penyakit["id_penyakit"]

        gejala_ids = rules_df[
            rules_df["id_penyakit"] == pid
        ]["id_gejala"].tolist()

        gejala_filtered = gejala_df[
            gejala_df["id_gejala"].isin(gejala_ids)
        ]

        categories[penyakit["nama_penyakit"]] = list(
            zip(
                gejala_filtered["id_gejala"],
                gejala_filtered["nama_gejala"],
            )
        )

    return categories
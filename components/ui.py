"""
UI Components for rendering Hero section, results, and empty states.
"""
import streamlit as st


def render_hero():
    """Render the top hero / header section."""
    st.markdown("""
    <div class="hero-container">
        <div class="hero-badge">🧅 Sistem Pakar v2.0</div>
        <div class="hero-title">Diagnosa Penyakit<br>Bawang Merah Varietas Bima</div>
        <div class="hero-subtitle">
            Identifikasi penyakit pada tanaman bawang merah Anda secara akurat 
            menggunakan teknologi kecerdasan buatan berbasis rule.
        </div>
        <div class="hero-method-tags">
            <span class="hero-tag">⚡ Forward Chaining</span>
            <span class="hero-tag">📊 Certainty Factor</span>
            <span class="hero-tag">🗃️ 53 Gejala</span>
            <span class="hero-tag">🦠 12 Penyakit</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_stats(gejala_count, penyakit_count, rules_count):
    """Render the quick stats row."""
    st.markdown(f"""
    <div class="stat-row">
        <div class="stat-item">
            <div class="stat-value">{gejala_count}</div>
            <div class="stat-label">Total Gejala</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">{penyakit_count}</div>
            <div class="stat-label">Jenis Penyakit</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">{rules_count}</div>
            <div class="stat-label">Aturan / Rules</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_methodology_info():
    """Render explanation cards about the methods used."""
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="method-card">
            <div class="method-card-title">⚡ Forward Chaining</div>
            <div class="method-card-desc">
                Metode penalaran maju yang dimulai dari fakta-fakta (gejala yang dipilih) 
                kemudian mencocokkan dengan aturan untuk mencapai kesimpulan berupa diagnosis penyakit.
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="method-card">
            <div class="method-card-title">📊 Certainty Factor</div>
            <div class="method-card-desc">
                Metode untuk menghitung tingkat kepastian diagnosis berdasarkan bobot 
                setiap gejala. Semakin banyak gejala cocok, semakin tinggi nilai kepastian.
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_empty_state():
    """Render the empty state when no symptoms are selected."""
    st.markdown("""
    <div class="empty-state">
        <span class="empty-state-icon">🔬</span>
        <div class="empty-state-title">Belum ada gejala yang dipilih</div>
        <div class="empty-state-desc">
            Pilih gejala-gejala yang terlihat pada tanaman bawang merah Anda di atas, 
            kemudian klik tombol <strong>Diagnosa</strong> untuk memulai analisis.
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_warning_no_selection():
    """Render styled warning for no symptom selected."""
    st.markdown("""
    <div class="empty-state warning-state">
        <span class="empty-state-icon">⚠️</span>
        <div class="empty-state-title">Oops! Belum ada gejala yang dipilih</div>
        <div class="empty-state-desc">
            Silakan pilih minimal satu gejala dari daftar di atas sebelum melakukan diagnosa.
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_no_match():
    """Render styled message when no disease matches."""
    st.markdown("""
    <div class="empty-state no-match-state">
        <span class="empty-state-icon">❌</span>
        <div class="empty-state-title">Tidak Ditemukan Kecocokan</div>
        <div class="empty-state-desc">
            Tidak ditemukan penyakit yang cocok dengan kombinasi gejala tersebut. 
            Coba pilih gejala yang berbeda atau tambahkan gejala lainnya.
        </div>
    </div>
    """, unsafe_allow_html=True)


def _get_cf_class(pct):
    """Return CSS class based on CF percentage."""
    if pct >= 60:
        return "high"
    elif pct >= 30:
        return "medium"
    else:
        return "low"


def render_main_result(result):
    """Render the primary diagnosis result as a big styled card."""
    cf_class = _get_cf_class(result['persentase'])
    pct_display = f"{result['persentase']:.2f}"

    st.markdown(f"""
    <div class="result-main-card">
        <div class="result-badge">🏆 DIAGNOSIS UTAMA</div>
        <div class="result-disease-name">{result['nama_penyakit']}</div>
        <div class="result-disease-id">Kode: {result['id_penyakit']}</div>
        <div class="result-cf-display">
            <span class="result-cf-value">{pct_display}</span>
            <span class="result-cf-unit">%</span>
        </div>
        <div class="result-cf-label">Tingkat Kepastian (Certainty Factor)</div>
        <div class="cf-progress-wrapper">
            <div class="cf-progress-bar cf-bar-{cf_class}" style="width: {result['persentase']:.1f}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_other_results(results):
    """Render the other possible diagnoses as a list of compact cards."""
    if not results:
        return

    st.markdown("""
    <div class="section-header" style="margin-top: 1.5rem;">
        <div class="section-icon section-icon-blue">📋</div>
        <div class="section-title">Kemungkinan Penyakit Lainnya</div>
    </div>
    <p class="section-desc">Berdasarkan gejala yang beririsan dengan penyakit lain.</p>
    """, unsafe_allow_html=True)

    for hd in results:
        cf_class = _get_cf_class(hd['persentase'])
        st.markdown(f"""
        <div class="other-disease-card">
            <div class="other-disease-info">
                <div class="other-disease-name">{hd['nama_penyakit']}</div>
                <div class="other-disease-id">{hd['id_penyakit']}</div>
            </div>
            <div class="other-disease-cf cf-{cf_class}">{hd['persentase']:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)


def render_footer():
    """Render the app footer."""
    st.markdown("""
    <div class="app-footer">
        Sistem Pakar Diagnosa Penyakit Bawang Merah — Metode Forward Chaining &amp; Certainty Factor<br>
        Dibuat dengan ❤️ menggunakan Streamlit &amp; Python
    </div>
    """, unsafe_allow_html=True)

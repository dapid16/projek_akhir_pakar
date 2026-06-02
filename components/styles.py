"""
Custom CSS styles for the Streamlit Expert System app.
Injected via st.markdown(..., unsafe_allow_html=True).
"""

MAIN_CSS = """
<style>
    /* ===== Google Font ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ===== Global ===== */
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }
    .block-container {
        padding-top: 2rem !important;
        max-width: 1100px;
    }

    /* ===== Hero Section ===== */
    .hero-container {
        background: linear-gradient(135deg, #0f4c2e 0%, #1a6b42 40%, #237a4b 70%, #2d9254 100%);
        border-radius: 20px;
        padding: 2.5rem 3rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(15, 76, 46, 0.3);
    }
    .hero-container::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(255,255,255,0.06) 0%, transparent 70%);
        border-radius: 50%;
    }
    .hero-container::after {
        content: '';
        position: absolute;
        bottom: -30%;
        left: 10%;
        width: 250px;
        height: 250px;
        background: radial-gradient(circle, rgba(255,255,255,0.04) 0%, transparent 70%);
        border-radius: 50%;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        color: #a8e6c3;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.35rem 1rem;
        border-radius: 50px;
        letter-spacing: 0.5px;
        margin-bottom: 1rem;
        text-transform: uppercase;
    }
    .hero-title {
        color: #ffffff;
        font-size: 2.2rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 0.5rem;
        position: relative;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    .hero-subtitle {
        color: rgba(255,255,255,0.8);
        font-size: 1.05rem;
        font-weight: 400;
        line-height: 1.6;
        max-width: 550px;
    }
    .hero-method-tags {
        display: flex;
        gap: 0.5rem;
        margin-top: 1.2rem;
        flex-wrap: wrap;
    }
    .hero-tag {
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.18);
        color: #c9f0dc;
        font-size: 0.78rem;
        font-weight: 500;
        padding: 0.3rem 0.9rem;
        border-radius: 8px;
        backdrop-filter: blur(5px);
    }

    /* ===== Section Headers ===== */
    .section-header {
        display: flex;
        align-items: center;
        gap: 0.7rem;
        margin-bottom: 0.3rem;
    }
    .section-icon {
        width: 40px;
        height: 40px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        flex-shrink: 0;
    }
    .section-icon-green { background: linear-gradient(135deg, #e8f5e9, #c8e6c9); }
    .section-icon-blue { background: linear-gradient(135deg, #e3f2fd, #bbdefb); }
    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #1a1a2e;
    }
    .section-desc {
        color: #6b7280;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
        padding-left: 3.2rem;
    }

    /* ===== Symptom Cards inside Expanders ===== */
    .symptom-category-info {
        background: linear-gradient(135deg, #f0fdf4, #ecfdf5);
        border: 1px solid #bbf7d0;
        border-radius: 12px;
        padding: 0.9rem 1.2rem;
        margin-bottom: 0.8rem;
        font-size: 0.82rem;
        color: #166534;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* ===== Multiselect Styling ===== */
    div[data-baseweb="select"] {
        border-radius: 12px !important;
    }
    div[data-baseweb="select"] > div {
        border-radius: 12px !important;
        border: 2px solid #e2e8f0 !important;
        background: #fafbfc !important;
        min-height: 48px;
        transition: all 0.2s ease;
    }
    div[data-baseweb="select"] > div:hover {
        border-color: #22c55e !important;
        box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.1) !important;
    }
    div[data-baseweb="select"] > div:focus-within {
        border-color: #16a34a !important;
        box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.15) !important;
    }

    /* ===== Buttons ===== */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #16a34a, #15803d) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.8rem 2.5rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        letter-spacing: 0.3px;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(22, 163, 74, 0.3) !important;
    }
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(22, 163, 74, 0.4) !important;
    }

    /* ===== Result Cards ===== */
    .result-main-card {
        background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
        border: 2px solid #6ee7b7;
        border-radius: 20px;
        padding: 2rem 2.2rem;
        margin: 1rem 0;
        position: relative;
        overflow: hidden;
    }
    .result-main-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 150px;
        height: 150px;
        background: radial-gradient(circle, rgba(34,197,94,0.15) 0%, transparent 70%);
        border-radius: 50%;
    }
    .result-badge {
        display: inline-block;
        background: linear-gradient(135deg, #16a34a, #15803d);
        color: white;
        font-size: 0.72rem;
        font-weight: 700;
        padding: 0.3rem 0.9rem;
        border-radius: 50px;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }
    .result-disease-name {
        font-size: 1.6rem;
        font-weight: 800;
        color: #064e3b;
        margin-bottom: 0.4rem;
        line-height: 1.3;
    }
    .result-disease-id {
        color: #6b7280;
        font-size: 0.85rem;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    .result-cf-display {
        display: flex;
        align-items: baseline;
        gap: 0.4rem;
        margin-top: 0.5rem;
    }
    .result-cf-value {
        font-size: 2.8rem;
        font-weight: 800;
        color: #16a34a;
        line-height: 1;
    }
    .result-cf-unit {
        font-size: 1.1rem;
        font-weight: 600;
        color: #22c55e;
    }
    .result-cf-label {
        font-size: 0.82rem;
        color: #6b7280;
        font-weight: 500;
        margin-top: 0.3rem;
    }

    /* ===== Other Diseases Card ===== */
    .other-disease-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 0.7rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        transition: all 0.2s ease;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .other-disease-card:hover {
        border-color: #a7f3d0;
        box-shadow: 0 4px 12px rgba(16,185,129,0.1);
        transform: translateX(4px);
    }
    .other-disease-info {
        flex: 1;
    }
    .other-disease-name {
        font-size: 0.95rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 0.15rem;
    }
    .other-disease-id {
        font-size: 0.78rem;
        color: #9ca3af;
        font-weight: 500;
    }
    .other-disease-cf {
        font-size: 1.15rem;
        font-weight: 700;
        padding: 0.4rem 1rem;
        border-radius: 10px;
        min-width: 75px;
        text-align: center;
    }
    .cf-high { background: #dcfce7; color: #16a34a; }
    .cf-medium { background: #fef9c3; color: #a16207; }
    .cf-low { background: #fee2e2; color: #dc2626; }

    /* ===== Empty State ===== */
    .empty-state {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #f8fafc, #f1f5f9);
        border: 2px dashed #cbd5e1;
        border-radius: 20px;
        margin: 1.5rem 0;
    }
    .empty-state-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        display: block;
    }
    .empty-state-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #334155;
        margin-bottom: 0.4rem;
    }
    .empty-state-desc {
        font-size: 0.9rem;
        color: #94a3b8;
        max-width: 400px;
        margin: 0 auto;
        line-height: 1.5;
    }

    /* ===== Progress bar inside result ===== */
    .cf-progress-wrapper {
        background: #e2e8f0;
        border-radius: 10px;
        height: 10px;
        width: 100%;
        margin-top: 0.8rem;
        overflow: hidden;
    }
    .cf-progress-bar {
        height: 100%;
        border-radius: 10px;
        transition: width 0.6s ease;
    }
    .cf-bar-high { background: linear-gradient(90deg, #22c55e, #16a34a); }
    .cf-bar-medium { background: linear-gradient(90deg, #facc15, #eab308); }
    .cf-bar-low { background: linear-gradient(90deg, #f87171, #ef4444); }

    /* ===== Footer ===== */
    .app-footer {
        text-align: center;
        padding: 2rem 0 1rem;
        color: #94a3b8;
        font-size: 0.8rem;
        border-top: 1px solid #e2e8f0;
        margin-top: 3rem;
    }

    /* ===== Info Methodology Card ===== */
    .method-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        height: 100%;
    }
    .method-card-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .method-card-desc {
        font-size: 0.83rem;
        color: #64748b;
        line-height: 1.6;
    }

    /* ===== Stat counter ===== */
    .stat-row {
        display: flex;
        gap: 1rem;
        margin: 1.5rem 0;
        flex-wrap: wrap;
    }
    .stat-item {
        flex: 1;
        min-width: 140px;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 1.2rem 1rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .stat-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #16a34a;
        line-height: 1;
    }
    .stat-label {
        font-size: 0.78rem;
        color: #94a3b8;
        font-weight: 500;
        margin-top: 0.3rem;
    }

    /* ===== Expander refinements ===== */
    .streamlit-expanderHeader {
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        border-radius: 12px !important;
    }

    /* ===== Selected counter badge ===== */
    .selected-counter {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: linear-gradient(135deg, #16a34a, #15803d);
        color: white;
        padding: 0.5rem 1.2rem;
        border-radius: 50px;
        font-size: 0.88rem;
        font-weight: 600;
        box-shadow: 0 2px 8px rgba(22,163,74,0.25);
        margin-bottom: 1rem;
    }

    /* ===== Matched symptoms in result ===== */
    .matched-symptom-tag {
        display: inline-block;
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        color: #166534;
        font-size: 0.75rem;
        font-weight: 500;
        padding: 0.25rem 0.7rem;
        border-radius: 6px;
        margin: 0.15rem;
    }

    /* ===== Theme picker ===== */
    div[data-testid="stRadio"] {
        margin-bottom: 0.75rem;
    }
    div[data-testid="stRadio"] > label {
        justify-content: flex-end;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 999px;
        padding: 0.25rem 0.45rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    div[data-testid="stRadio"] label {
        margin: 0;
        padding-right: 0.5rem;
    }
    div[data-testid="stRadio"] label span {
        color: #334155;
        font-size: 0.84rem;
        font-weight: 600;
    }

    /* ===== Alert states ===== */
    .warning-state {
        border-color: #fbbf24;
        background: linear-gradient(135deg, #fffbeb, #fef3c7);
    }
    .warning-state .empty-state-title { color: #92400e; }
    .warning-state .empty-state-desc { color: #b45309; }

    .no-match-state {
        border-color: #fca5a5;
        background: linear-gradient(135deg, #fef2f2, #fee2e2);
    }
    .no-match-state .empty-state-title { color: #991b1b; }
    .no-match-state .empty-state-desc { color: #dc2626; }
</style>
"""


DARK_THEME_CSS = """
<style>
    :root {
        color-scheme: dark;
    }
    html, body, [class*="st-"] {
        color: #e5e7eb;
    }
    .stApp,
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #0b1115 0%, #111827 100%) !important;
    }
    [data-testid="stHeader"] {
        background: rgba(11, 17, 21, 0.88) !important;
    }
    [data-testid="stSidebar"] {
        background: #0f172a !important;
    }
    .block-container {
        color: #e5e7eb;
    }

    div[data-testid="stRadio"] > label > div {
        color: #cbd5e1 !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] {
        background: rgba(15, 23, 42, 0.94);
        border-color: #334155;
        box-shadow: 0 1px 10px rgba(0,0,0,0.18);
    }
    div[data-testid="stRadio"] label span {
        color: #d1d5db !important;
    }

    .hero-container {
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.38);
    }
    .section-title {
        color: #f8fafc;
    }
    .section-desc {
        color: #9ca3af;
    }
    .section-icon-green {
        background: linear-gradient(135deg, #064e3b, #065f46);
    }
    .section-icon-blue {
        background: linear-gradient(135deg, #1e3a8a, #1d4ed8);
    }

    .stat-item,
    .method-card,
    .other-disease-card {
        background: #111827;
        border-color: #334155;
        box-shadow: 0 1px 10px rgba(0,0,0,0.18);
    }
    .stat-value {
        color: #4ade80;
    }
    .stat-label,
    .method-card-desc,
    .other-disease-id,
    .result-disease-id,
    .result-cf-label {
        color: #94a3b8;
    }
    .method-card-title,
    .other-disease-name {
        color: #f8fafc;
    }

    .symptom-category-info,
    .matched-symptom-tag {
        background: rgba(20, 83, 45, 0.35);
        border-color: #166534;
        color: #bbf7d0;
    }
    div[data-baseweb="select"] > div {
        background: #0f172a !important;
        border-color: #334155 !important;
        color: #f8fafc !important;
    }
    div[data-baseweb="select"] > div:hover,
    div[data-baseweb="select"] > div:focus-within {
        border-color: #22c55e !important;
        box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.18) !important;
    }
    div[data-baseweb="select"] span,
    div[data-baseweb="select"] input {
        color: #e5e7eb !important;
    }
    div[role="listbox"] {
        background: #111827 !important;
        color: #e5e7eb !important;
    }
    [data-testid="stExpander"] {
        background: #111827;
        border-color: #334155 !important;
        border-radius: 12px;
    }
    [data-testid="stExpander"] details,
    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] p,
    [data-testid="stExpander"] label,
    [data-testid="stExpander"] span {
        color: #e5e7eb !important;
    }

    .result-main-card {
        background: linear-gradient(135deg, #052e16 0%, #064e3b 100%);
        border-color: #10b981;
    }
    .result-main-card::before {
        background: radial-gradient(circle, rgba(74,222,128,0.18) 0%, transparent 70%);
    }
    .result-disease-name {
        color: #dcfce7;
    }
    .result-cf-value {
        color: #4ade80;
    }
    .result-cf-unit {
        color: #86efac;
    }
    .cf-progress-wrapper {
        background: #1f2937;
    }
    .other-disease-card:hover {
        border-color: #10b981;
        box-shadow: 0 4px 16px rgba(16,185,129,0.14);
    }
    .cf-high {
        background: rgba(34,197,94,0.18);
        color: #86efac;
    }
    .cf-medium {
        background: rgba(250,204,21,0.16);
        color: #fde68a;
    }
    .cf-low {
        background: rgba(248,113,113,0.16);
        color: #fca5a5;
    }

    .empty-state {
        background: linear-gradient(135deg, #111827, #0f172a);
        border-color: #334155;
    }
    .empty-state-title {
        color: #f8fafc;
    }
    .empty-state-desc {
        color: #94a3b8;
    }
    .warning-state {
        border-color: #f59e0b;
        background: linear-gradient(135deg, rgba(120, 53, 15, 0.45), rgba(146, 64, 14, 0.28));
    }
    .warning-state .empty-state-title {
        color: #fde68a;
    }
    .warning-state .empty-state-desc {
        color: #fcd34d;
    }
    .no-match-state {
        border-color: #ef4444;
        background: linear-gradient(135deg, rgba(127, 29, 29, 0.42), rgba(153, 27, 27, 0.26));
    }
    .no-match-state .empty-state-title {
        color: #fecaca;
    }
    .no-match-state .empty-state-desc {
        color: #fca5a5;
    }

    .app-footer {
        color: #64748b;
        border-top-color: #1f2937;
    }
</style>
"""


def get_theme_css(theme_mode):
    """Return the base app CSS plus the selected theme overrides."""
    if str(theme_mode).lower() == "dark":
        return MAIN_CSS + DARK_THEME_CSS
    return MAIN_CSS

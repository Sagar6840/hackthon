"""
CipherSearch UI Theme — Premium Cybersecurity SaaS
==================================================
Attractive, professional palette: light base + vibrant accents.
Applies to ALL pages: Login, Dashboard, Upload, Search, Security Proof, Benchmark.
"""

CIPHERSEARCH_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* ──────────────────────────────────────────────────────────────────
   COLOR PALETTE — Attractive, professional, not just dark
   Light base + vibrant teal/coral accents + depth
   ────────────────────────────────────────────────────────────────── */
:root {
  /* Light, airy backgrounds — premium SaaS feel */
  --bg:           #f8fafc;
  --bg-warm:      #fefefe;
  --surface:      #ffffff;
  --panel:        #ffffff;
  --panel-hover:  #f8fafc;
  --sidebar-bg:   #f1f5f9;

  /* Borders — soft, professional */
  --border:       rgba(15, 23, 42, 0.08);
  --border-strong: rgba(15, 23, 42, 0.12);

  /* Primary — vibrant teal (trust + tech) */
  --accent:       #0d9488;
  --accent-dim:   rgba(13, 148, 136, 0.12);
  --accent-glow:  rgba(13, 148, 136, 0.25);

  /* Secondary — warm coral (energy, security) */
  --accent2:      #0891b2;
  --accent-gradient: linear-gradient(135deg, #0d9488 0%, #0891b2 50%, #06b6d4 100%);

  /* Tertiary — soft violet for highlights */
  --accent3:      #7c3aed;
  --accent3-dim:  rgba(124, 58, 237, 0.1);

  /* Semantic */
  --green:        #059669;
  --green-dim:    rgba(5, 150, 105, 0.12);
  --red:          #dc2626;
  --red-dim:      rgba(220, 38, 38, 0.1);
  --amber:        #d97706;
  --amber-dim:    rgba(217, 119, 6, 0.1);

  /* Text — warm, readable */
  --text:         #0f172a;
  --text-secondary: #475569;
  --text-muted:   #64748b;

  /* Typography */
  --font-sans:    'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono:    'JetBrains Mono', 'SF Mono', monospace;
}

/* ──────────────────────────────────────────────────────────────────
   BASE & LAYOUT — All pages
   ────────────────────────────────────────────────────────────────── */
.stApp {
  background: var(--bg) !important;
  background-image:
    radial-gradient(ellipse 100% 60% at 50% -10%, rgba(13, 148, 136, 0.06), transparent 50%),
    radial-gradient(ellipse 80% 50% at 100% 50%, rgba(124, 58, 237, 0.04), transparent 50%) !important;
}
[data-testid="stAppViewContainer"] {
  background: transparent !important;
}
[data-testid="stHeader"] {
  background: transparent !important;
}

.main .block-container {
  padding: 2rem 3rem 4rem !important;
  max-width: 1400px !important;
  margin: 0 auto !important;
  position: relative !important;
  z-index: 2 !important;
}

/* ──────────────────────────────────────────────────────────────────
   SIDEBAR — All pages
   ────────────────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
  background: var(--sidebar-bg) !important;
  border-right: 1px solid var(--border) !important;
  padding-top: 1.5rem !important;
}
[data-testid="stSidebar"] > div:first-child {
  padding-top: 0.5rem !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdown"]:first-of-type {
  font-family: var(--font-sans) !important;
  font-weight: 700 !important;
  font-size: 16px !important;
  color: var(--text) !important;
  letter-spacing: -0.02em !important;
}

[data-testid="stSidebar"] .stRadio > div {
  background: transparent !important;
  padding: 0.25rem 0.5rem !important;
  gap: 2px !important;
}
[data-testid="stSidebar"] .stRadio > div > label {
  background: transparent !important;
  border-radius: 12px !important;
  padding: 10px 14px !important;
  margin: 2px 0 !important;
  border: 1px solid transparent !important;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
[data-testid="stSidebar"] .stRadio > div > label:hover {
  background: var(--accent-dim) !important;
  border-color: rgba(13, 148, 136, 0.2) !important;
}
[data-testid="stSidebar"] .stRadio > div > label:has(input:checked) {
  background: var(--accent-dim) !important;
  border-color: rgba(13, 148, 136, 0.3) !important;
  box-shadow: 0 0 0 2px rgba(13, 148, 136, 0.15) !important;
}
[data-testid="stSidebar"] .stRadio label span {
  font-family: var(--font-sans) !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  color: var(--text-secondary) !important;
}
[data-testid="stSidebar"] .stRadio label:has(input:checked) span {
  color: var(--accent) !important;
}

[data-testid="stSidebar"] [data-testid="stSuccess"],
[data-testid="stSidebar"] [data-testid="stError"] {
  padding: 8px 12px !important;
  border-radius: 12px !important;
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  margin: 8px 0 !important;
}
[data-testid="stSidebar"] [data-testid="stSuccess"] {
  background: var(--green-dim) !important;
  color: var(--green) !important;
  border: 1px solid rgba(5, 150, 105, 0.25) !important;
}
[data-testid="stSidebar"] [data-testid="stError"] {
  background: var(--red-dim) !important;
  color: var(--red) !important;
  border: 1px solid rgba(220, 38, 38, 0.25) !important;
}

/* ──────────────────────────────────────────────────────────────────
   TYPOGRAPHY — All pages
   ────────────────────────────────────────────────────────────────── */
.main h1 {
  font-family: var(--font-sans) !important;
  font-size: 28px !important;
  font-weight: 700 !important;
  color: var(--text) !important;
  letter-spacing: -0.03em !important;
  line-height: 1.25 !important;
}
.main h2 {
  font-family: var(--font-sans) !important;
  font-size: 20px !important;
  font-weight: 600 !important;
  color: var(--text) !important;
}
.main h3 {
  font-family: var(--font-sans) !important;
  font-size: 16px !important;
  font-weight: 600 !important;
  color: var(--text-secondary) !important;
}
.main p, .main span, .main label {
  font-family: var(--font-sans) !important;
  color: var(--text-secondary) !important;
  font-size: 14px !important;
  line-height: 1.6 !important;
}
.main [data-testid="stCaptionContainer"] {
  color: var(--text-muted) !important;
  font-family: var(--font-sans) !important;
}

/* ──────────────────────────────────────────────────────────────────
   METRIC CARDS — Dashboard, Search, Security Proof, Benchmark
   ────────────────────────────────────────────────────────────────── */
div[data-testid="stMetric"] {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 16px !important;
  padding: 24px !important;
  text-align: center !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
}
div[data-testid="stMetric"]:hover {
  transform: translateY(-2px) !important;
  border-color: rgba(13, 148, 136, 0.3) !important;
  box-shadow: 0 12px 24px -8px rgba(13, 148, 136, 0.15), 0 4px 12px -4px rgba(0, 0, 0, 0.08) !important;
}
div[data-testid="stMetric"] label {
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  font-weight: 500 !important;
  color: var(--text-muted) !important;
  text-transform: uppercase !important;
  letter-spacing: 0.06em !important;
}
div[data-testid="stMetric"] [data-testid="stMetricValue"] {
  font-family: var(--font-sans) !important;
  font-size: 32px !important;
  font-weight: 700 !important;
  color: var(--accent) !important;
  letter-spacing: -0.02em !important;
}

/* ──────────────────────────────────────────────────────────────────
   BUTTONS — All pages
   ────────────────────────────────────────────────────────────────── */
.stButton > button {
  font-family: var(--font-sans) !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  border-radius: 12px !important;
  padding: 12px 24px !important;
  transition: all 0.2s ease !important;
  border: none !important;
}
.stButton > button[kind="primary"] {
  background: var(--accent-gradient) !important;
  color: #fff !important;
  box-shadow: 0 2px 8px -2px rgba(13, 148, 136, 0.4) !important;
}
.stButton > button[kind="primary"]:hover {
  transform: translateY(-1px) !important;
  box-shadow: 0 8px 20px -4px rgba(13, 148, 136, 0.4) !important;
  filter: brightness(1.02) !important;
}
.stButton > button[kind="secondary"] {
  background: var(--surface) !important;
  border: 1px solid var(--border-strong) !important;
  color: var(--text-secondary) !important;
}
.stButton > button[kind="secondary"]:hover {
  background: var(--panel-hover) !important;
  border-color: var(--accent) !important;
  color: var(--accent) !important;
}

/* ──────────────────────────────────────────────────────────────────
   INPUTS — Login, Upload, Search, Security Proof
   ────────────────────────────────────────────────────────────────── */
.stTextInput input, .stTextArea textarea {
  background: var(--surface) !important;
  border: 1px solid var(--border-strong) !important;
  border-radius: 12px !important;
  font-family: var(--font-sans) !important;
  font-size: 14px !important;
  color: var(--text) !important;
  padding: 12px 16px !important;
  transition: all 0.2s ease !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 3px var(--accent-dim) !important;
  outline: none !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder {
  color: var(--text-muted) !important;
}

/* ──────────────────────────────────────────────────────────────────
   RADIO / TABS — Search, Security Proof
   ────────────────────────────────────────────────────────────────── */
.stRadio > div {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  padding: 6px !important;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04) !important;
}
.stRadio label {
  font-family: var(--font-sans) !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  color: var(--text-secondary) !important;
  border-radius: 8px !important;
  padding: 8px 16px !important;
  transition: all 0.2s ease !important;
}
.stRadio label:hover {
  color: var(--text) !important;
  background: var(--accent-dim) !important;
}

.stTabs [data-baseweb="tab-list"] {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  padding: 4px !important;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04) !important;
}
.stTabs [data-baseweb="tab"] {
  font-family: var(--font-sans) !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  color: var(--text-muted) !important;
  border-radius: 8px !important;
  padding: 8px 16px !important;
  transition: all 0.2s ease !important;
}
.stTabs [aria-selected="true"] {
  background: var(--accent-dim) !important;
  color: var(--accent) !important;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.06) !important;
}

/* ──────────────────────────────────────────────────────────────────
   CODE BLOCKS & EXPANDERS — Upload, Search, Security Proof
   ────────────────────────────────────────────────────────────────── */
.stCodeBlock, code {
  background: #f1f5f9 !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  font-family: var(--font-mono) !important;
  font-size: 12px !important;
  color: var(--text-secondary) !important;
}
.streamlit-expanderHeader {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  color: var(--text) !important;
  font-family: var(--font-sans) !important;
  font-weight: 500 !important;
  transition: all 0.2s ease !important;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04) !important;
}
.streamlit-expanderHeader:hover {
  background: var(--panel-hover) !important;
  border-color: rgba(13, 148, 136, 0.2) !important;
}
.streamlit-expanderContent {
  background: #fafbfc !important;
  border: 1px solid var(--border) !important;
  border-top: none !important;
  border-radius: 0 0 12px 12px !important;
}

/* ──────────────────────────────────────────────────────────────────
   ALERTS — All pages
   ────────────────────────────────────────────────────────────────── */
.stAlert {
  border-radius: 12px !important;
  font-family: var(--font-sans) !important;
  font-size: 13px !important;
  border: 1px solid !important;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="info"] {
  background: var(--accent-dim) !important;
  border-color: rgba(13, 148, 136, 0.3) !important;
  color: #0f766e !important;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="success"] {
  background: var(--green-dim) !important;
  border-color: rgba(5, 150, 105, 0.3) !important;
  color: var(--green) !important;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="error"] {
  background: var(--red-dim) !important;
  border-color: rgba(220, 38, 38, 0.3) !important;
  color: var(--red) !important;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="warning"] {
  background: var(--amber-dim) !important;
  border-color: rgba(217, 119, 6, 0.3) !important;
  color: var(--amber) !important;
}

/* Progress bar */
.stProgress > div > div {
  background: var(--accent-gradient) !important;
  border-radius: 4px !important;
}

/* ──────────────────────────────────────────────────────────────────
   CLIENT/SERVER HEADERS — Upload page
   ────────────────────────────────────────────────────────────────── */
.client-header {
  background: var(--green-dim) !important;
  border: 1px solid rgba(5, 150, 105, 0.25) !important;
  padding: 14px 18px !important;
  border-radius: 12px !important;
  margin-bottom: 12px !important;
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  color: var(--green) !important;
}
.server-header {
  background: var(--red-dim) !important;
  border: 1px solid rgba(220, 38, 38, 0.25) !important;
  padding: 14px 18px !important;
  border-radius: 12px !important;
  margin-bottom: 12px !important;
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  color: var(--red) !important;
}

/* ──────────────────────────────────────────────────────────────────
   LOGIN PAGE
   ────────────────────────────────────────────────────────────────── */
.login-container {
  min-height: calc(100vh - 120px);
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.login-box {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 24px !important;
  padding: 48px !important;
  position: relative !important;
  overflow: hidden !important;
  max-width: 440px !important;
  margin: 0 auto !important;
  box-shadow: 0 24px 48px -12px rgba(0, 0, 0, 0.12), 0 0 0 1px rgba(0, 0, 0, 0.04) !important;
}
.login-box::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important; left: 0 !important; right: 0 !important;
  height: 4px !important;
  background: var(--accent-gradient) !important;
}
.login-title {
  font-family: var(--font-sans) !important;
  font-size: 26px !important;
  font-weight: 700 !important;
  color: var(--text) !important;
  text-align: center !important;
  margin-bottom: 8px !important;
  letter-spacing: -0.03em !important;
}
.login-sub {
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  color: var(--text-muted) !important;
  text-align: center !important;
  letter-spacing: 0.08em !important;
}
.security-note {
  margin-top: 24px !important;
  padding: 16px !important;
  background: #f8fafc !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  font-family: var(--font-mono) !important;
  font-size: 10px !important;
  font-weight: 600 !important;
  color: var(--text-muted) !important;
  letter-spacing: 0.08em !important;
}
.security-note-desc {
  font-size: 13px !important;
  font-weight: 400 !important;
  color: var(--text-secondary) !important;
  line-height: 1.6 !important;
  margin-top: 8px !important;
}

/* Blockquotes (Security Proof, Dashboard) */
.main blockquote {
  background: var(--surface) !important;
  border-left: 4px solid var(--accent) !important;
  border-radius: 0 12px 12px 0 !important;
  padding: 20px 24px !important;
  margin: 16px 0 !important;
  color: var(--text-secondary) !important;
  font-style: normal !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
}

/* ──────────────────────────────────────────────────────────────────
   ANIMATIONS
   ────────────────────────────────────────────────────────────────── */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}
.fade-in {
  animation: fadeInUp 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

/* ──────────────────────────────────────────────────────────────────
   SCROLLBAR & DIVIDERS
   ────────────────────────────────────────────────────────────────── */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: #f1f5f9; border-radius: 4px; }
::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

hr {
  border: none !important;
  height: 1px !important;
  background: var(--border) !important;
  margin: 1.5rem 0 !important;
}
"""

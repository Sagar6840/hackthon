"""
CipherSearch UI Theme — Premium Cybersecurity SaaS
==================================================
Top-tier dashboard aesthetic: refined, professional, judge-impressive.
Inspired by Vercel, Linear, CrowdStrike — production-grade polish.
"""

CIPHERSEARCH_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ──────────────────────────────────────────────────────────────────
   1. COLOR PALETTE — Refined cybersecurity SaaS
   ────────────────────────────────────────────────────────────────── */
:root {
  /* Core backgrounds — deep, sophisticated */
  --bg:           #080c14;
  --bg-elevated:  #0d1321;
  --surface:      #131b2e;
  --panel:        #1a2538;
  --panel-hover:  #1e2d44;

  /* Borders — subtle, layered */
  --border:       rgba(148, 163, 184, 0.08);
  --border-focus: rgba(59, 130, 246, 0.4);

  /* Primary accent — trust-inducing blue (Vercel/Stripe vibe) */
  --accent:       #3b82f6;
  --accent-dim:   rgba(59, 130, 246, 0.15);
  --accent-glow:  rgba(59, 130, 246, 0.25);

  /* Secondary — teal for "secure" feeling */
  --accent2:      #0ea5e9;
  --accent-gradient: linear-gradient(135deg, #3b82f6 0%, #0ea5e9 100%);

  /* Semantic */
  --green:        #22c55e;
  --green-dim:    rgba(34, 197, 94, 0.12);
  --red:          #ef4444;
  --red-dim:      rgba(239, 68, 68, 0.12);
  --amber:        #f59e0b;
  --amber-dim:    rgba(245, 158, 11, 0.12);

  /* Text hierarchy */
  --text:         #f1f5f9;
  --text-secondary: #94a3b8;
  --text-muted:   #64748b;

  /* Typography */
  --font-sans:    'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono:    'JetBrains Mono', 'SF Mono', monospace;
}

/* ──────────────────────────────────────────────────────────────────
   2. BASE & LAYOUT — Production-grade structure
   ────────────────────────────────────────────────────────────────── */
.stApp {
  background: var(--bg) !important;
  background-image:
    radial-gradient(ellipse 80% 50% at 50% -20%, rgba(59, 130, 246, 0.08), transparent),
    radial-gradient(ellipse 60% 40% at 100% 0%, rgba(14, 165, 233, 0.04), transparent) !important;
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
   3. SIDEBAR — Premium nav with active glow
   ────────────────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
  background: var(--bg-elevated) !important;
  border-right: 1px solid var(--border) !important;
  padding-top: 1.5rem !important;
}
[data-testid="stSidebar"] > div:first-child {
  padding-top: 0.5rem !important;
}

/* Sidebar title — refined branding */
[data-testid="stSidebar"] [data-testid="stMarkdown"]:first-of-type {
  font-family: var(--font-sans) !important;
  font-weight: 700 !important;
  font-size: 15px !important;
  color: var(--text) !important;
  letter-spacing: -0.02em !important;
  padding-left: 1rem !important;
}

/* Radio nav — custom pill/active style */
[data-testid="stSidebar"] .stRadio > div {
  background: transparent !important;
  padding: 0.25rem 0.75rem !important;
  gap: 0 !important;
}
[data-testid="stSidebar"] .stRadio > div > label {
  background: transparent !important;
  border-radius: 10px !important;
  padding: 10px 14px !important;
  margin: 2px 0 !important;
  border: 1px solid transparent !important;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
  position: relative !important;
}
[data-testid="stSidebar"] .stRadio > div > label:hover {
  background: var(--accent-dim) !important;
  border-color: var(--border) !important;
}
[data-testid="stSidebar"] .stRadio > div > label:has(input:checked) {
  background: var(--accent-dim) !important;
  border-color: rgba(59, 130, 246, 0.3) !important;
  box-shadow: 0 0 0 1px rgba(59, 130, 246, 0.2), 0 0 20px -5px var(--accent-glow) !important;
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

/* Status badge in sidebar */
[data-testid="stSidebar"] [data-testid="stSuccess"],
[data-testid="stSidebar"] [data-testid="stError"] {
  padding: 8px 12px !important;
  border-radius: 10px !important;
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  letter-spacing: 0.5px !important;
  margin: 8px 0 !important;
}
[data-testid="stSidebar"] [data-testid="stSuccess"] {
  background: var(--green-dim) !important;
  color: var(--green) !important;
  border: 1px solid rgba(34, 197, 94, 0.2) !important;
}

/* ──────────────────────────────────────────────────────────────────
   4. TYPOGRAPHY — Clear hierarchy, premium feel
   ────────────────────────────────────────────────────────────────── */
.main h1 {
  font-family: var(--font-sans) !important;
  font-size: 28px !important;
  font-weight: 700 !important;
  color: var(--text) !important;
  letter-spacing: -0.03em !important;
  line-height: 1.25 !important;
  margin-bottom: 0.5rem !important;
}
.main h2 {
  font-family: var(--font-sans) !important;
  font-size: 20px !important;
  font-weight: 600 !important;
  color: var(--text) !important;
  letter-spacing: -0.02em !important;
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
.main .stMarkdown {
  color: var(--text-secondary) !important;
}

/* ──────────────────────────────────────────────────────────────────
   5. METRIC CARDS — Glass-like, gradient border, hover lift
   ────────────────────────────────────────────────────────────────── */
div[data-testid="stMetric"] {
  background: linear-gradient(135deg, var(--panel) 0%, var(--surface) 100%) !important;
  border: 1px solid var(--border) !important;
  border-radius: 16px !important;
  padding: 24px !important;
  text-align: center !important;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
  position: relative !important;
  overflow: hidden !important;
}
div[data-testid="stMetric"]::before {
  content: '' !important;
  position: absolute !important;
  inset: 0 !important;
  border-radius: 16px !important;
  padding: 1px !important;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), transparent 40%, transparent 60%, rgba(14, 165, 233, 0.1)) !important;
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0) !important;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0) !important;
  -webkit-mask-composite: xor !important;
  mask-composite: exclude !important;
  pointer-events: none !important;
}
div[data-testid="stMetric"]:hover {
  transform: translateY(-2px) !important;
  border-color: rgba(59, 130, 246, 0.25) !important;
  box-shadow: 0 12px 40px -12px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(59, 130, 246, 0.1) !important;
}
div[data-testid="stMetric"] label {
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  font-weight: 500 !important;
  color: var(--text-muted) !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
}
div[data-testid="stMetric"] [data-testid="stMetricValue"] {
  font-family: var(--font-sans) !important;
  font-size: 32px !important;
  font-weight: 700 !important;
  color: var(--text) !important;
  letter-spacing: -0.02em !important;
  background: var(--accent-gradient) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
}

/* ──────────────────────────────────────────────────────────────────
   6. BUTTONS — Refined CTAs with subtle glow
   ────────────────────────────────────────────────────────────────── */
.stButton > button {
  font-family: var(--font-sans) !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  letter-spacing: -0.01em !important;
  border-radius: 12px !important;
  padding: 12px 24px !important;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
  border: none !important;
}
.stButton > button[kind="primary"] {
  background: var(--accent-gradient) !important;
  color: #fff !important;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2) !important;
}
.stButton > button[kind="primary"]:hover {
  transform: translateY(-1px) !important;
  box-shadow: 0 8px 25px -5px var(--accent-glow), 0 4px 10px -6px var(--accent-glow) !important;
  filter: brightness(1.05) !important;
}
.stButton > button[kind="secondary"] {
  background: var(--panel) !important;
  border: 1px solid var(--border) !important;
  color: var(--text-secondary) !important;
}
.stButton > button[kind="secondary"]:hover {
  background: var(--panel-hover) !important;
  border-color: rgba(59, 130, 246, 0.3) !important;
  color: var(--accent) !important;
}

/* ──────────────────────────────────────────────────────────────────
   7. INPUTS — Clean, focus ring
   ────────────────────────────────────────────────────────────────── */
.stTextInput input, .stTextArea textarea {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
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
   8. RADIO / TABS — Pill-style selection
   ────────────────────────────────────────────────────────────────── */
.stRadio > div {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  padding: 6px !important;
  gap: 4px !important;
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

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  padding: 4px !important;
  gap: 4px !important;
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
  background: var(--panel) !important;
  color: var(--accent) !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2) !important;
}

/* ──────────────────────────────────────────────────────────────────
   9. CODE BLOCKS & EXPANDERS — Terminal-like
   ────────────────────────────────────────────────────────────────── */
.stCodeBlock, code {
  background: var(--bg-elevated) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  font-family: var(--font-mono) !important;
  font-size: 12px !important;
  color: var(--text-secondary) !important;
}
.streamlit-expanderHeader {
  background: var(--panel) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  color: var(--text) !important;
  font-family: var(--font-sans) !important;
  font-weight: 500 !important;
  transition: all 0.2s ease !important;
}
.streamlit-expanderHeader:hover {
  background: var(--panel-hover) !important;
  border-color: rgba(59, 130, 246, 0.2) !important;
}
.streamlit-expanderContent {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-top: none !important;
  border-radius: 0 0 12px 12px !important;
}

/* ──────────────────────────────────────────────────────────────────
   10. ALERTS — Semantic, refined
   ────────────────────────────────────────────────────────────────── */
.stAlert {
  border-radius: 12px !important;
  font-family: var(--font-sans) !important;
  font-size: 13px !important;
  border: 1px solid !important;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="info"] {
  background: var(--accent-dim) !important;
  border-color: rgba(59, 130, 246, 0.3) !important;
  color: var(--accent2) !important;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="success"] {
  background: var(--green-dim) !important;
  border-color: rgba(34, 197, 94, 0.3) !important;
  color: var(--green) !important;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="error"] {
  background: var(--red-dim) !important;
  border-color: rgba(239, 68, 68, 0.3) !important;
  color: var(--red) !important;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="warning"] {
  background: var(--amber-dim) !important;
  border-color: rgba(245, 158, 11, 0.3) !important;
  color: var(--amber) !important;
}

/* ──────────────────────────────────────────────────────────────────
   11. PROGRESS BAR — Gradient fill
   ────────────────────────────────────────────────────────────────── */
.stProgress > div > div {
  background: var(--accent-gradient) !important;
  border-radius: 4px !important;
}

/* ──────────────────────────────────────────────────────────────────
   12. CUSTOM BLOCKS — Client/Server headers
   ────────────────────────────────────────────────────────────────── */
.client-header {
  background: var(--green-dim) !important;
  border: 1px solid rgba(34, 197, 94, 0.25) !important;
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
  border: 1px solid rgba(239, 68, 68, 0.25) !important;
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
   13. LOGIN PAGE — Premium auth box
   ────────────────────────────────────────────────────────────────── */
.login-container {
  min-height: calc(100vh - 120px);
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.login-box {
  background: linear-gradient(135deg, var(--panel) 0%, var(--surface) 100%) !important;
  border: 1px solid var(--border) !important;
  border-radius: 20px !important;
  padding: 48px !important;
  position: relative !important;
  overflow: hidden !important;
  max-width: 420px !important;
  margin: 0 auto !important;
  box-shadow: 0 24px 48px -12px rgba(0, 0, 0, 0.5) !important;
}
.login-box::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important; left: 0 !important; right: 0 !important;
  height: 3px !important;
  background: var(--accent-gradient) !important;
}
.login-title {
  font-family: var(--font-sans) !important;
  font-size: 24px !important;
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
  background: var(--surface) !important;
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

/* ──────────────────────────────────────────────────────────────────
   14. ANIMATIONS — Subtle, professional
   ────────────────────────────────────────────────────────────────── */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}
.fade-in {
  animation: fadeInUp 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

/* ──────────────────────────────────────────────────────────────────
   15. SCROLLBAR — Minimal
   ────────────────────────────────────────────────────────────────── */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb {
  background: var(--text-muted);
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: var(--text-secondary);
}

/* ──────────────────────────────────────────────────────────────────
   16. DIVIDERS
   ────────────────────────────────────────────────────────────────── */
hr {
  border: none !important;
  height: 1px !important;
  background: var(--border) !important;
  margin: 1.5rem 0 !important;
}
"""

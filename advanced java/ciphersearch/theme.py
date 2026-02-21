"""CipherSearch UI Theme - Dark cyberpunk aesthetic matching HTML reference."""

CIPHERSEARCH_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@400;600;700;800&display=swap');

:root {
  --bg:        #020408;
  --surface:   #080d14;
  --panel:     #0c1520;
  --border:    #0f2035;
  --accent:    #00d4ff;
  --accent2:   #0066ff;
  --green:     #00ff88;
  --red:       #ff3355;
  --text:      #c8dff0;
  --muted:     #4a6a80;
  --font-mono: 'Space Mono', monospace;
  --font-main: 'Syne', sans-serif;
}

/* Animated grid background (like reference) */
.stApp::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image:
    linear-gradient(rgba(0,212,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,212,255,0.03) 1px, transparent 1px);
  background-size: 40px 40px;
  pointer-events: none;
  z-index: 0;
}
/* Scan line animation */
@keyframes scanLine {
  to { top: 200%; }
}
.stApp::after {
  content: '';
  position: fixed;
  top: -100%;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--accent), transparent);
  animation: scanLine 6s linear infinite;
  pointer-events: none;
  z-index: 0;
  opacity: 0.4;
}

/* Base overrides */
.stApp {
  background: var(--bg) !important;
}
[data-testid="stAppViewContainer"] {
  background: var(--bg) !important;
}
[data-testid="stHeader"] {
  background: transparent !important;
}
.main .block-container {
  padding: 2rem 2.5rem !important;
  max-width: 100% !important;
  position: relative !important;
  z-index: 2 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
  background: var(--surface) !important;
  border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] [data-testid="stMarkdown"] {
  font-family: var(--font-mono) !important;
  color: var(--text) !important;
}
[data-testid="stSidebar"] .stRadio > div {
  background: transparent !important;
  padding: 4px 0 !important;
}
[data-testid="stSidebar"] label {
  color: var(--muted) !important;
  font-family: var(--font-mono) !important;
  font-size: 12px !important;
}
[data-testid="stSidebar"] label:hover {
  color: var(--accent) !important;
}

/* Main content text */
.main h1, .main h2, .main h3 {
  font-family: var(--font-main) !important;
  color: #fff !important;
  font-weight: 800 !important;
  letter-spacing: -0.5px !important;
}
.main h1 span, .main h2 span, .main h3 span {
  color: var(--accent) !important;
}
.main p, .main span, .main label {
  font-family: var(--font-main) !important;
  color: var(--text) !important;
}

/* Metrics / Cards */
div[data-testid="stMetric"] {
  background: var(--panel) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  padding: 20px !important;
  text-align: center !important;
  transition: border-color 0.3s !important;
}
div[data-testid="stMetric"]:hover {
  border-color: rgba(0,212,255,0.3) !important;
}
div[data-testid="stMetric"] label {
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  color: var(--muted) !important;
  text-transform: uppercase !important;
  letter-spacing: 1px !important;
}
div[data-testid="stMetric"] [data-testid="stMetricValue"] {
  font-family: var(--font-mono) !important;
  font-size: 28px !important;
  font-weight: 700 !important;
  color: var(--accent) !important;
}

/* Buttons */
.stButton > button {
  font-family: var(--font-mono) !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  letter-spacing: 1px !important;
  text-transform: uppercase !important;
  border-radius: 8px !important;
  padding: 12px 24px !important;
  transition: all 0.2s !important;
}
.stButton > button[kind="primary"] {
  background: linear-gradient(135deg, var(--accent2), var(--accent)) !important;
  color: #000 !important;
  border: none !important;
}
.stButton > button[kind="primary"]:hover {
  transform: translateY(-1px) !important;
  box-shadow: 0 8px 24px rgba(0,212,255,0.3) !important;
}
.stButton > button[kind="secondary"] {
  background: transparent !important;
  border: 1px solid var(--border) !important;
  color: var(--text) !important;
}
.stButton > button[kind="secondary"]:hover {
  border-color: var(--accent) !important;
  color: var(--accent) !important;
}

/* Text inputs */
.stTextInput input, .stTextArea textarea {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 8px !important;
  font-family: var(--font-mono) !important;
  font-size: 14px !important;
  color: var(--text) !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 3px rgba(0,212,255,0.1) !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder {
  color: var(--muted) !important;
}

/* Radio */
.stRadio > div {
  background: var(--panel) !important;
  border: 1px solid var(--border) !important;
  border-radius: 8px !important;
  padding: 8px !important;
}
.stRadio label {
  font-family: var(--font-mono) !important;
  font-size: 12px !important;
}

/* Code blocks */
.stCodeBlock, code {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 8px !important;
  font-family: var(--font-mono) !important;
  font-size: 12px !important;
  color: var(--text) !important;
}

/* Expanders */
.streamlit-expanderHeader {
  background: var(--panel) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  color: var(--accent) !important;
  font-family: var(--font-mono) !important;
}
.streamlit-expanderContent {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-top: none !important;
  border-radius: 0 0 10px 10px !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
  background: transparent !important;
  border-bottom: 1px solid var(--border) !important;
  gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
  font-family: var(--font-mono) !important;
  font-size: 12px !important;
  color: var(--muted) !important;
  text-transform: uppercase !important;
  letter-spacing: 1px !important;
}
.stTabs [aria-selected="true"] {
  color: var(--accent) !important;
  border-bottom: 2px solid var(--accent) !important;
}

/* Alerts / st.info, st.success, st.error, st.warning */
.stAlert {
  border-radius: 8px !important;
  font-family: var(--font-mono) !important;
  font-size: 12px !important;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="info"] {
  background: rgba(0,212,255,0.15) !important;
  border: 1px solid rgba(0,212,255,0.3) !important;
  color: var(--accent) !important;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="success"] {
  background: rgba(0,255,136,0.15) !important;
  border: 1px solid rgba(0,255,136,0.3) !important;
  color: var(--green) !important;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="error"] {
  background: rgba(255,51,85,0.15) !important;
  border: 1px solid rgba(255,51,85,0.3) !important;
  color: var(--red) !important;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="warning"] {
  background: rgba(255,200,0,0.1) !important;
  border: 1px solid rgba(255,200,0,0.3) !important;
  color: #ffc800 !important;
}

/* Progress bar */
.stProgress > div > div {
  background: linear-gradient(90deg, var(--accent2), var(--accent)) !important;
  border-radius: 2px !important;
}

/* Dividers */
hr {
  border-color: var(--border) !important;
  opacity: 0.6 !important;
}

/* Custom classes for layout */
.client-header {
  background: rgba(0,255,136,0.08) !important;
  border: 1px solid rgba(0,255,136,0.25) !important;
  padding: 12px 16px !important;
  border-radius: 10px !important;
  margin-bottom: 12px !important;
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  letter-spacing: 2px !important;
  color: var(--green) !important;
}
.server-header {
  background: rgba(255,51,85,0.08) !important;
  border: 1px solid rgba(255,51,85,0.25) !important;
  padding: 12px 16px !important;
  border-radius: 10px !important;
  margin-bottom: 12px !important;
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  letter-spacing: 2px !important;
  color: var(--red) !important;
}

/* Login container - wraps login page content */
.login-container {
  min-height: calc(100vh - 100px);
  display: flex;
  flex-direction: column;
  justify-content: center;
}
/* Login box wrapper */
.login-box {
  background: var(--panel) !important;
  border: 1px solid var(--border) !important;
  border-radius: 16px !important;
  padding: 40px !important;
  position: relative !important;
  overflow: hidden !important;
  max-width: 420px !important;
  margin: 0 auto !important;
}
.login-box::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important; left: 0 !important; right: 0 !important;
  height: 2px !important;
  background: linear-gradient(90deg, var(--accent2), var(--accent)) !important;
}
.login-title {
  font-family: var(--font-main) !important;
  font-size: 22px !important;
  font-weight: 800 !important;
  color: #fff !important;
  text-align: center !important;
  margin-bottom: 8px !important;
}
.login-sub {
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  color: var(--muted) !important;
  text-align: center !important;
  letter-spacing: 1px !important;
}
.security-note {
  margin-top: 20px !important;
  padding: 14px !important;
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: 8px !important;
  font-family: var(--font-mono) !important;
  font-size: 10px !important;
  color: var(--muted) !important;
  letter-spacing: 1px !important;
}
.security-note-desc {
  font-size: 12px !important;
  color: var(--muted) !important;
  line-height: 1.6 !important;
  margin-top: 8px !important;
}

/* Card-style sections */
.card-section {
  background: var(--panel) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  padding: 24px !important;
  margin-bottom: 16px !important;
}
.card-section::before {
  content: '' !important;
  display: block !important;
  height: 1px !important;
  background: linear-gradient(90deg, transparent, rgba(0,212,255,0.3), transparent) !important;
  margin: -24px -24px 20px -24px !important;
}
.card-title {
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  letter-spacing: 2px !important;
  text-transform: uppercase !important;
  color: var(--accent) !important;
  margin-bottom: 16px !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--muted); }

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: none; }
}
.fade-in { animation: fadeIn 0.4s ease; }
"""

"""
CipherSearch — Streamlit UI
===========================
Interactive demo of secure string matching on encrypted data.
Shows client-side and server-side perspectives simultaneously.
Theme: Dark cyberpunk aesthetic (CipherSearch reference).
"""

import streamlit as st
import time
import re
from crypto_engine import CipherSearchEngine, SecureServer
from theme import CIPHERSEARCH_CSS

# ──────────────────────────────────────────────────────────────────
# Page config & theme (MUST be first Streamlit call)
# ──────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="CipherSearch",
    page_icon="🔐",
    layout="wide",
)

st.markdown(f"<style>{CIPHERSEARCH_CSS}</style>", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────
# Session state initialization
# ──────────────────────────────────────────────────────────────────

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'engine' not in st.session_state:
    st.session_state.engine = None
if 'server' not in st.session_state:
    st.session_state.server = SecureServer("ciphersearch.db")
if 'plaintext_cache' not in st.session_state:
    st.session_state.plaintext_cache = {}
if 'search_history' not in st.session_state:
    st.session_state.search_history = []
if 'username' not in st.session_state:
    st.session_state.username = ""

# ──────────────────────────────────────────────────────────────────
# LOGIN PAGE — blocks everything until logged in (themed like reference)
# ──────────────────────────────────────────────────────────────────

if not st.session_state.logged_in:
    # Centered login layout matching HTML reference
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("""
        <div class="login-box fade-in">
            <div style="text-align: center; margin-bottom: 24px;">
                <div style="font-size: 40px; margin-bottom: 12px;">🔐</div>
                <div class="login-title">CipherSearch</div>
                <div class="login-sub">SECURE ENCRYPTED SEARCH SYSTEM</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        username = st.text_input("Username", placeholder="Enter your username", key="login_user")
        password = st.text_input(
            "Master Password",
            type="password",
            placeholder="Min 6 characters",
            key="login_pass"
        )

        if st.button("LOGIN & DERIVE KEYS", type="primary", use_container_width=True):
            if username and len(password) >= 6:
                with st.spinner("Deriving keys with PBKDF2 (100,000 iterations)..."):
                    engine = CipherSearchEngine(password)
                st.session_state.engine = engine
                st.session_state.username = username
                st.session_state.logged_in = True
                st.session_state.saved_salt = engine.get_salt_b64()
                st.rerun()
            else:
                st.error("Enter a username and password (minimum 6 characters)")

        st.markdown("""
        <div class="security-note">
            <div>SECURITY NOTE</div>
            <div class="security-note-desc">
                Keys are derived locally using PBKDF2 (100,000 iterations).
                They never leave your device.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align: center; font-family: Space Mono, monospace; "
        "font-size: 11px; color: #4a6a80; margin-top: 24px;'>HACK-A-LEAGUE 4.0</div>",
        unsafe_allow_html=True
    )
    st.stop()

# ──────────────────────────────────────────────────────────────────
# Sample data
# ──────────────────────────────────────────────────────────────────

SAMPLE_DOCS = {
    "MR-001": (
        "Patient: John Smith | Age: 45 | Gender: Male\n"
        "Diagnosis: Type 2 Diabetes Mellitus, Hypertension\n"
        "Medications: Metformin 500mg twice daily, Lisinopril 10mg daily\n"
        "Symptoms: Increased thirst, frequent urination, fatigue\n"
        "Lab Results: HbA1c 7.8%, Fasting glucose 165 mg/dL, BP 148/92\n"
        "Notes: Family history of diabetes. Dietary counseling provided."
    ),
    "MR-002": (
        "Patient: Sarah Johnson | Age: 32 | Gender: Female\n"
        "Diagnosis: Chronic Migraine, Generalized Anxiety Disorder\n"
        "Medications: Sumatriptan 50mg PRN, Sertraline 100mg daily\n"
        "Symptoms: Severe headache, photosensitivity, nausea, worry\n"
        "Lab Results: CBC normal, Thyroid panel normal\n"
        "Notes: Migraine diary started. Cognitive behavioral therapy referral."
    ),
    "MR-003": (
        "Patient: Robert Chen | Age: 58 | Gender: Male\n"
        "Diagnosis: Coronary Artery Disease, Type 2 Diabetes, Hyperlipidemia\n"
        "Medications: Aspirin 81mg, Atorvastatin 40mg, Metformin 1000mg\n"
        "Symptoms: Exertional chest pain, dyspnea, fatigue\n"
        "Lab Results: LDL 145, HbA1c 8.5%, Troponin negative, ECG normal\n"
        "Notes: Cardiac catheterization scheduled. High cardiovascular risk."
    ),
    "MR-004": (
        "Patient: Emily Davis | Age: 28 | Gender: Female\n"
        "Diagnosis: Bronchial Asthma, Allergic Rhinitis\n"
        "Medications: Albuterol inhaler PRN, Fluticasone nasal spray\n"
        "Symptoms: Wheezing, shortness of breath, nasal congestion\n"
        "Lab Results: Spirometry mild obstruction, IgE elevated\n"
        "Notes: Avoid dust and pollen triggers. Peak flow monitoring."
    ),
    "MR-005": (
        "Patient: Michael Brown | Age: 67 | Gender: Male\n"
        "Diagnosis: Hypertension, Chronic Kidney Disease Stage 3, Gout\n"
        "Medications: Amlodipine 10mg, Losartan 100mg, Allopurinol 300mg\n"
        "Symptoms: Joint swelling, elevated blood pressure, reduced urine\n"
        "Lab Results: Creatinine 1.8, eGFR 45, Uric acid 9.2\n"
        "Notes: Renal function declining. Nephrology referral placed."
    ),
    "FIN-001": (
        "Transaction Report — Account: XXXX-7842\n"
        "Customer: Acme Corporation | Type: Wire Transfer\n"
        "Amount: $125,000 | Currency: USD | Date: 2024-01-15\n"
        "Recipient: Global Supplies Ltd, Singapore\n"
        "Compliance Flag: Large international transfer, requires review\n"
        "Notes: Verified beneficial ownership. Sanctions screening clear."
    ),
}

# ──────────────────────────────────────────────────────────────────
# Sidebar navigation (only shown after login)
# ──────────────────────────────────────────────────────────────────

st.sidebar.title("🔐 CipherSearch")
st.sidebar.caption("Secure String Matching\non Encrypted Data")
st.sidebar.markdown("---")

page = st.sidebar.radio("Navigate", [
    "🏠 Dashboard",
    "📤 Encrypt & Upload",
    "🔍 Search",
    "🛡️ Security Proof",
    "📊 System Benchmark",
])

st.sidebar.markdown("---")
st.sidebar.markdown("### Status")
if st.session_state.engine:
    st.sidebar.success("🟢 Keys Active")
else:
    st.sidebar.error("🔴 No Keys")

stats = st.session_state.server.get_stats()
st.sidebar.caption(f"📄 {stats['documents']} docs stored")
st.sidebar.caption(f"🏷️ {stats['index_entries']} tokens indexed")

# Search history in sidebar
if st.session_state.search_history:
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🕐 Recent Searches")
    for s in reversed(st.session_state.search_history[-5:]):
        st.sidebar.caption(f"🔍 {s}")

# User + logout
st.sidebar.markdown("---")
st.sidebar.markdown(f"👤 **{st.session_state.username}**")
if st.sidebar.button("🚪 Logout"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# ──────────────────────────────────────────────────────────────────
# PAGE: Dashboard
# ──────────────────────────────────────────────────────────────────

if page == "🏠 Dashboard":
    st.title(f"Welcome, {st.session_state.username} 👋")
    st.markdown("---")

    stats = st.session_state.server.get_stats()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📄 Documents Stored", stats['documents'])
    c2.metric("🏷️ Keywords Indexed", stats['unique_tokens'])
    c3.metric("🔍 Searches Performed", len(st.session_state.search_history))
    c4.metric("🔑 Encryption", "AES-256-GCM ✅")

    st.markdown("---")
    st.markdown("### How It Works")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 🟢 Client (You)")
        st.markdown("""
- Holds master password
- Derives encryption keys locally
- Encrypts documents before upload
- Generates search tokens from queries
- Decrypts results locally
        """)
    with col2:
        st.markdown("#### 📡 In Transit")
        st.markdown("""
- Only encrypted content flows
- Only opaque tokens for search
- **No plaintext ever transmitted**
- **No keys ever transmitted**
        """)
    with col3:
        st.markdown("#### 🔴 Server (Cloud)")
        st.markdown("""
- Stores encrypted blobs
- Stores opaque HMAC tokens
- Matches tokens blindly
- Returns encrypted results
- **ZERO knowledge of content**
        """)

    st.markdown("---")
    st.markdown("### Cryptographic Building Blocks")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("🔒 **AES-256-GCM**\n\nAuthenticated encryption. Provides confidentiality and integrity. Detects tampering.")
    with c2:
        st.info("🔑 **HMAC-SHA256**\n\nDeterministic one-way tokens. Same keyword → same token. Cannot reverse token → keyword.")
    with c3:
        st.info("🔐 **PBKDF2**\n\n100,000 iterations. Converts password → cryptographic keys. Brute-force resistant.")

    st.markdown("---")
    st.markdown("### Recent Activity")
    if st.session_state.server.audit_log:
        for entry in reversed(st.session_state.server.audit_log[-5:]):
            st.caption(f"• {entry['action']} — {entry['timestamp']}")
    else:
        st.info("No activity yet. Go to Encrypt & Upload to get started.")

# ──────────────────────────────────────────────────────────────────
# PAGE: Encrypt & Upload
# ──────────────────────────────────────────────────────────────────

elif page == "📤 Encrypt & Upload":
    st.title("📤 Encrypt & Upload Documents")

    engine = st.session_state.engine
    server = st.session_state.server

    st.markdown("### 📋 Quick Start — Load Sample Data")
    if st.button("Load 6 Sample Documents (Healthcare + Finance)", type="primary", use_container_width=True):
        progress = st.progress(0, text="Encrypting...")
        for i, (doc_id, content) in enumerate(SAMPLE_DOCS.items()):
            enc = engine.encrypt_document(doc_id, content)
            keywords = engine.extract_keywords(content)
            for kw in keywords:
                ng_tokens = engine.generate_ngram_tokens(kw)
                kw_hash = engine.generate_token(kw)
                server.store_ngram_tokens(doc_id, ng_tokens, kw_hash)
            server.store_document(enc)
            st.session_state.plaintext_cache[doc_id] = content
            progress.progress((i + 1) / len(SAMPLE_DOCS), text=f"Encrypted {doc_id}")
            time.sleep(0.15)
        st.success(f"✅ {len(SAMPLE_DOCS)} documents encrypted and uploaded!")
        st.rerun()

    st.markdown("---")
    st.markdown("### ✏️ Manual Upload")
    doc_id = st.text_input("Document ID", placeholder="e.g., DOC-001")
    content = st.text_area("Document Content (plaintext)", height=180, placeholder="Type or paste content here...")

    if st.button("🔐 Encrypt & Upload") and doc_id and content:
        enc = engine.encrypt_document(doc_id, content)
        keywords = engine.extract_keywords(content)
        for kw in keywords:
            ng_tokens = engine.generate_ngram_tokens(kw)
            kw_hash = engine.generate_token(kw)
            server.store_ngram_tokens(doc_id, ng_tokens, kw_hash)
        server.store_document(enc)
        st.session_state.plaintext_cache[doc_id] = content

        st.markdown("---")
        st.markdown("### Encryption Process Breakdown")
        col_c, col_s = st.columns(2)
        with col_c:
            st.markdown('<div class="client-header"><b>🟢 CLIENT SIDE</b></div>', unsafe_allow_html=True)
            st.markdown("**Step 1 — Extract keywords:**")
            st.code(f"{keywords[:10]}{'...' if len(keywords) > 10 else ''}")
            st.markdown("**Step 2 — Generate HMAC tokens:**")
            preview = {kw: engine.generate_token(kw)[:24] + "..." for kw in keywords[:4]}
            st.json(preview)
            st.markdown("**Step 3 — AES-256-GCM encrypt:**")
            st.code(
                f"Ciphertext: {enc.encrypted_content[:60]}...\n"
                f"Nonce: {enc.nonce}\n"
                f"AAD (tamper-proof binding): {doc_id}"
            )
        with col_s:
            st.markdown('<div class="server-header"><b>🔴 SERVER RECEIVES</b></div>', unsafe_allow_html=True)
            st.code(
                f"doc_id: {doc_id}\n"
                f"content: {enc.encrypted_content[:50]}... [ENCRYPTED]\n"
                f"tokens: {len(enc.tokens)} opaque strings\n"
                f"nonce: {enc.nonce}"
            )
            st.error("❌ Server cannot read the content or keywords!")

        st.success(f"✅ Document {doc_id} uploaded — {enc.keyword_count} keywords, {len(enc.tokens)} tokens")

    st.markdown("---")
    st.markdown("### 📋 Uploaded Documents")
    docs = server.get_all_documents_raw()
    if docs:
        for d in docs:
            col_a, col_b, col_c = st.columns([2, 2, 1])
            with col_a:
                st.write(f"📄 `{d['doc_id']}`")
            with col_b:
                st.caption(f"Keywords: {d['keyword_count']} | {str(d.get('created_at', ''))[:16]}")
            with col_c:
                if st.button("🗑️", key=f"del_{d['doc_id']}"):
                    server.delete_document(d['doc_id'])
                    st.rerun()
    else:
        st.info("No documents uploaded yet.")

# ──────────────────────────────────────────────────────────────────
# PAGE: Search
# ──────────────────────────────────────────────────────────────────

elif page == "🔍 Search":
    st.title("🔍 Search Encrypted Data")

    engine = st.session_state.engine
    server = st.session_state.server

    query = st.text_input("🔎 Search query", placeholder="e.g., diabetes, migraine, metformin")
    mode = st.radio(
        "Search mode",
        [
            "Exact keyword",
            "Multi-keyword AND (comma-separated)",
            "Multi-keyword OR (comma-separated)",
            "Fuzzy / Typo-tolerant",
        ],
        horizontal=True,
    )

    if st.button("🔍 Search", type="primary", use_container_width=True) and query:
        # Save to search history
        if query not in st.session_state.search_history:
            st.session_state.search_history.append(query)

        st.markdown("---")
        st.markdown("#### Step 1 — 🟢 Client generates search token(s)")

        if mode == "Exact keyword":
            kw = query.strip()
            token = engine.generate_token(kw)
            st.code(f'"{kw}" → HMAC token: {token[:48]}...')
            tokens = [token]
        elif mode.startswith("Multi-keyword AND") or mode.startswith("Multi-keyword OR"):
            kws = [k.strip() for k in query.split(",") if k.strip()]
            tokens = []
            for kw in kws:
                t = engine.generate_token(kw)
                st.code(f'"{kw}" → {t[:48]}...')
                tokens.append(t)
        else:
            kw = query.strip()
            tokens = engine.generate_ngram_tokens(kw)
            st.code(f'"{kw}" → {len(tokens)} n-gram tokens generated')
            st.caption(f"First 3 tokens: {[t[:20] + '...' for t in tokens[:3]]}")

        st.info("💡 Only token(s) are sent to the server — the query text stays on the client.")

        st.markdown("#### Step 2 — 🔴 Server matches tokens (blindly)")
        with st.spinner("Server searching encrypted index..."):
            time.sleep(0.2)
            if mode == "Exact keyword":
                enc_results = server.search_token(tokens[0])
            elif mode.startswith("Multi-keyword AND"):
                enc_results = server.search_multi(tokens, "AND")
            elif mode.startswith("Multi-keyword OR"):
                enc_results = server.search_multi(tokens, "OR")
            else:
                enc_results = server.search_fuzzy(tokens, threshold=0.5)

        st.code(f"Server found {len(enc_results)} matching document(s)")
        if enc_results:
            st.caption("Server returns these **still-encrypted** blobs:")
            for r in enc_results[:2]:
                st.code(f"{r['doc_id']}: {r['encrypted_content'][:50]}... [ENCRYPTED]")
            st.warning(f"⚠️ Server matched tokens but has **no idea** what '{query}' means!")

        st.markdown("#### Step 3 — 🟢 Client decrypts results")
        if enc_results:
            for r in enc_results:
                try:
                    decrypted = engine.decrypt_text(
                        r['encrypted_content'],
                        r['nonce'],
                        r['doc_id']
                    )
                    display = decrypted
                    search_terms = [k.strip().lower() for k in query.split(",")]
                    for term in search_terms:
                        display = re.sub(
                            f'(?i)({re.escape(term)})',
                            r'**\1**',
                            display
                        )
                    with st.expander(f"📄 {r['doc_id']}", expanded=True):
                        st.markdown(display)
                except Exception as e:
                    st.error(f"Decryption failed for {r['doc_id']}: {e}")
        else:
            st.info("No matching documents found.")

        st.markdown("---")
        st.markdown("#### 🔒 Privacy Summary for This Search")
        pc1, pc2, pc3 = st.columns(3)
        with pc1:
            st.metric("Query text sent to server", "NEVER ❌")
        with pc2:
            st.metric("Plaintext on server", "NEVER ❌")
        with pc3:
            st.metric("Decryption location", "Client only ✅")

# ──────────────────────────────────────────────────────────────────
# PAGE: Security Proof
# ──────────────────────────────────────────────────────────────────

elif page == "🛡️ Security Proof":
    st.title("🛡️ Security Proof — The Server's Perspective")
    st.markdown("""
> Everything below is what an **attacker** or **curious server admin** would
> see if they accessed the database. **Spoiler: it's all gibberish.**
    """)

    server = st.session_state.server
    tab1, tab2, tab3 = st.tabs([
        "📄 Stored Documents",
        "🏷️ Token Index",
        "📋 Audit Log"
    ])

    with tab1:
        docs = server.get_all_documents_raw()
        if docs:
            for d in docs:
                with st.expander(f"📄 {d['doc_id']}"):
                    st.code(
                        f"encrypted_content (first 120 chars):\n"
                        f" {d['encrypted_content'][:120]}...\n\n"
                        f"nonce: {d['nonce']}\n"
                        f"keyword_count: {d['keyword_count']}\n"
                        f"created_at: {d.get('created_at', 'N/A')}"
                    )
                    st.error("❌ Cannot decrypt — no key available on server!")
        else:
            st.info("No documents uploaded yet.")

    with tab2:
        tokens = server.get_all_tokens_raw()
        if tokens:
            st.caption(f"Showing {len(tokens)} index entries")
            for t in tokens:
                st.code(f"Token: {t['token'][:36]}... → Doc: {t['doc_id']}")
            st.error("❌ Cannot determine what keywords these tokens represent!")
        else:
            st.info("No tokens indexed yet.")

    with tab3:
        if server.audit_log:
            for entry in reversed(server.audit_log[-15:]):
                with st.expander(f"{entry['action']} — {entry['timestamp']}"):
                    st.json(entry)
        else:
            st.info("No activity recorded yet.")

    # ── Attack Simulation ──
    st.markdown("---")
    st.markdown("### ⚔️ Attack Simulation")
    st.markdown("What happens if an attacker tries to search without the correct key?")

    attack_query = st.text_input("Attacker's search term", value="diabetes", key="attack_query")
    if st.button("🔴 Simulate Attack", key="attack_btn"):
        fake_engine = CipherSearchEngine("wrong_password_attacker")
        fake_token = fake_engine.generate_token(attack_query)
        real_token = st.session_state.engine.generate_token(attack_query)
        results = server.search_token(fake_token)

        st.error(f"❌ Attack result: {len(results)} documents found — attacker gets NOTHING")
        st.code(
            f"Attacker's token: {fake_token[:40]}...\n"
            f"Real token:       {real_token[:40]}...\n"
            f"Match:            ❌ NEVER"
        )
        st.success("✅ Without the correct key, the search token never matches — zero information leaked.")

# ──────────────────────────────────────────────────────────────────
# PAGE: System Benchmark
# ──────────────────────────────────────────────────────────────────

elif page == "📊 System Benchmark":
    st.title("📊 System Benchmark")

    stats = st.session_state.server.get_stats()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📄 Documents", stats['documents'])
    c2.metric("🏷️ Index Entries", stats['index_entries'])
    c3.metric("🔑 Unique Tokens", stats['unique_tokens'])
    c4.metric("📋 Audit Events", stats['audit_events'])

    st.markdown("---")
    st.markdown("### ⚡ Performance Benchmark")
    if st.button("Run Benchmark", use_container_width=True):
        engine = st.session_state.engine
        server = st.session_state.server
        test = "Benchmark test document for measuring performance."

        t0 = time.time()
        for i in range(200):
            engine.encrypt_text(test, f"bench_{i}")
        enc_ms = (time.time() - t0) / 200 * 1000

        t0 = time.time()
        for i in range(200):
            engine.generate_token(f"keyword{i}")
        tok_ms = (time.time() - t0) / 200 * 1000

        token = engine.generate_token("benchmark")
        t0 = time.time()
        for _ in range(200):
            server.search_token(token)
        search_ms = (time.time() - t0) / 200 * 1000

        b1, b2, b3 = st.columns(3)
        b1.metric("Encrypt (per doc)", f"{enc_ms:.3f} ms")
        b2.metric("Token Gen (per keyword)", f"{tok_ms:.3f} ms")
        b3.metric("Search (per query)", f"{search_ms:.3f} ms")
        st.success(
            f"📈 At this speed, the system can encrypt ~{int(1000 / enc_ms)} "
            f"docs/sec and search ~{int(1000 / search_ms)} queries/sec."
        )

    st.markdown("---")
    if st.button("🗑️ Clear All Data", type="secondary"):
        st.session_state.server.clear_all()
        st.session_state.plaintext_cache = {}
        st.session_state.search_history = []
        st.success("All data cleared.")
        st.rerun()
# CipherSearch Design System

**Premium Cybersecurity SaaS UI** — Production-grade, judge-impressive.

---

## 1. Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| **Background** | `#080c14` | Deep base |
| **Surface** | `#131b2e` | Cards, inputs |
| **Panel** | `#1a2538` | Elevated elements |
| **Border** | `rgba(148,163,184,0.08)` | Subtle separation |
| **Primary Accent** | `#3b82f6` | CTAs, links, active states |
| **Secondary Accent** | `#0ea5e9` | Gradients, highlights |
| **Success** | `#22c55e` | Keys active, secure |
| **Error** | `#ef4444` | Warnings, server zone |
| **Text** | `#f1f5f9` | Primary content |
| **Text Muted** | `#64748b` | Labels, secondary |

**Glow:** `rgba(59, 130, 246, 0.25)` for focus rings and hover shadows.

---

## 2. Typography

- **Sans:** Inter — headings, body, UI
- **Mono:** JetBrains Mono — code, IDs, technical data

Hierarchy: 28px (h1) → 20px (h2) → 16px (h3) → 14px (body). Letter-spacing: -0.03em for large headings.

---

## 3. Cards

- Gradient background: `panel` → `surface`
- 16px border-radius, 1px border
- Gradient border on hover (blue accent)
- Hover: `translateY(-2px)`, soft shadow
- Metric values: gradient text fill

---

## 4. Sidebar

- Active item: accent background, glow border
- Hover: subtle accent tint
- 10px padding, 10px border-radius
- Status badge: pill with semantic color

---

## 5. Animations

- **fadeInUp:** 0.5s cubic-bezier on page load
- **Hover transitions:** 0.2s ease on buttons, cards
- **Focus:** 3px accent ring on inputs

---

## 6. Layout

- Max-width: 1400px, centered
- 3rem horizontal padding
- 8px grid for spacing
- Radial gradient orbs in background for depth

---

## Implementation

All styles live in `theme.py` and are injected via `st.markdown()`. Streamlit config in `.streamlit/config.toml` sets base theme colors.

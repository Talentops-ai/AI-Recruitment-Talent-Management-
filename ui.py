import streamlit as st

# =========================================================# # AI RECRUITMENT COPILOT — "Luminous Mint" Enterprise Theme
# ==========================================================
# Design language: deep emerald ink on a lit mint-glass surface, a
# luminous mint->jade "shine" that actually glows (soft radiant box
# shadows, a moving shine sweep, a gentle pulse) rather than sitting
# flat, plus a warm gold hairline used sparingly for premium/verdict
# signals.

# ---- Core surface ----
VOID    = "#EFFBF6"   # Page background (top of gradient)
VOID2   = "#DCF3E8"   # Page background (bottom of gradient)
PANEL   = "#FFFFFF"   # Glass card surface
PANEL2  = "#F1FBF7"   # Raised / inset surface (inputs, active rows)
LINE    = "#BFEBDA"   # Hairline borders
LINE_SOFT = "#D7F2E6" # Fainter divider

# ---- Ink ----
INK     = "#0F2B22"   # Primary text -- deep forest ink (richer than gray)
INK_SOFT= "#24473B"   # Secondary heading ink
MIST    = "#5C7A6E"   # Muted secondary text

# ---- Signal colors ----
SIGNAL  = "#0DAF9C"   # Core brand mint-teal -- labels, icons, eyebrows, primary CTAs
VERDICT = "#0E9F6E"   # Success / excellent match
CAUTION = "#B9820F"   # Warm gold -- average / attention
RISK    = "#DC4C4C"   # Coral red -- low match / deficit

# ---- Mint gradient family (the "glow") ----
MINT_A  = "#3FF2C4"   # Bright luminous mint -- the glow color
MINT_B  = "#A6FCE0"   # Pale mint shine
MINT_C  = "#0B7F73"   # Deep teal (gradient anchor / hover)
GOLD    = "#D4AF37"   # Reserved accent -- premium badges only
CORAL   = "#FF7B72"   # Reserved accent -- risk/deficit signals in dark sections

# ---- True void (dark terminal-section backgrounds) ----
# Used by .terminal-cta / .showcase-shell instead of the previous
# hand-picked greenish darks, so every dark section anchors to the
# same two near-black stops.
VOID_DARK  = "#030706"
VOID_DARK2 = "#07110E"

# ---- Extended accent family (sidebar nav variety, secondary chips) ----
INDIGO  = "#6366F1"
VIOLET  = "#8B5CF6"
ROSE    = "#DB5A8C"
SKY     = "#0EA5E9"

# Per-item accent for the recruiter sidebar nav, in the exact order the
# nav items are declared in app.py (Dashboard, Job Postings, Upload
# Resume, Interviews, Candidates, Analytics, Profile) -- a harmonious
# but varied palette so the sidebar isn't monochrome, while every item
# still shares the same pill shape, spacing and hover motion.
NAV_ACCENTS = [SIGNAL, INDIGO, VIOLET, ROSE, CAUTION, VERDICT, SKY]

# ---- Night Mode surfaces (see _inject_night_mode_css in load_css) ----
# Deep-space navy/black glass, matching the reference dashboard screenshot.
NIGHT_PANEL  = "#0E141B"   # Card surface
NIGHT_PANEL2 = "#141C24"   # Raised / inset surface (inputs)
NIGHT_LINE   = "#22303A"   # Hairline borders
NIGHT_TEXT   = "#E7F5EF"   # Primary text on dark
NIGHT_MUTED  = "#7C93A0"   # Muted secondary text on dark

# Compatibility aliases (used across other modules)
PRIMARY = SIGNAL
SUCCESS = VERDICT
WARNING = CAUTION
DANGER  = RISK
BG      = VOID
CARD    = PANEL
TEXT    = INK
MUTED   = MIST
BORDER  = LINE


def load_css():
    # Per-item accent CSS for the sidebar nav (see NAV_ACCENTS above) --
    # built here as plain CSS text and dropped into the stylesheet below,
    # so each nav pill gets its own hover/active hue via CSS custom
    # properties instead of everything being one flat teal.
    nav_accent_css = "".join(
        f'[data-testid="stSidebar"] [role="radiogroup"] label:nth-of-type({i}) {{ '
        f'--nav-solid: {c}; --nav-wash: {c}22; --nav-wash2: {c}12; '
        f'--nav-border: {c}55; --nav-border-soft: {c}40; }}\n'
        for i, c in enumerate(NAV_ACCENTS, start=1)
    )

    st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700;800&family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
    background: {VOID};
    color: {INK};
}}

.stApp {{
    background:
        radial-gradient(1100px 520px at 12% -8%, rgba(63,242,196,0.30), transparent 60%),
        radial-gradient(900px 460px at 105% 8%, rgba(212,175,55,0.18), transparent 55%),
        radial-gradient(750px 540px at 90% 90%, rgba(14,159,110,0.18), transparent 60%),
        radial-gradient(600px 420px at 0% 75%, rgba(220,76,76,0.06), transparent 55%),
        repeating-linear-gradient(120deg, rgba(13,175,156,0.035) 0px, rgba(13,175,156,0.035) 1px, transparent 1px, transparent 34px),
        linear-gradient(165deg, {VOID} 0%, {VOID2} 100%);
    background-attachment: fixed;
}}

.block-container {{
    max-width: 1600px;
    padding: 1.5rem 2rem 3rem 2rem;
}}

h1, h2, h3, h4 {{
    font-family: 'Space Grotesk', sans-serif !important;
    color: {INK} !important;
    font-weight: 700;
    letter-spacing: -0.3px;
}}

p, span, div, label, li {{ color: {INK}; }}

::selection {{ background: {MINT_A}55; color: {INK}; }}

::-webkit-scrollbar {{ width: 9px; height: 9px; }}
::-webkit-scrollbar-track {{ background: transparent; }}
::-webkit-scrollbar-thumb {{ background: {MINT_A}66; border-radius: 8px; }}
::-webkit-scrollbar-thumb:hover {{ background: {SIGNAL}88; }}

/* ---------------------------------------------------------
   NATIVE STREAMLIT CHROME
   --------------------------------------------------------- */
header[data-testid="stHeader"] {{ background: transparent !important; }}
[data-testid="stToolbar"] {{ background: transparent !important; }}
[data-testid="stDecoration"] {{
    background: linear-gradient(90deg, {MINT_C}, {MINT_A}, {GOLD}) !important;
    height: 3px !important;
}}

[data-testid="stSidebar"] {{
    background: linear-gradient(190deg, #FFFFFF 0%, #E4F7ED 55%, #CDEEDF 100%) !important;
    border-right: 1px solid {LINE};
    box-shadow: 6px 0 24px rgba(13,175,156,0.06);
}}
[data-testid="stSidebar"] * {{ color: {INK} !important; }}
[data-testid="stSidebar"] hr {{
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, {LINE} 20%, {LINE} 80%, transparent);
    margin: 14px 0;
}}

[data-testid="stSidebar"] [role="radiogroup"] {{
    display: flex;
    flex-direction: column;
    align-items: stretch;
    gap: 4px;
}}
[data-testid="stSidebar"] [role="radiogroup"] label {{
    position: relative;
    display: flex;
    align-items: center;
    width: 100%;
    box-sizing: border-box;
    background: rgba(255,255,255,0.55);
    border: 1px solid transparent;
    border-radius: 13px;
    padding: 11px 14px 11px 16px;
    margin-bottom: 0;
    font-weight: 600;
    font-size: 14px;
    transition: all 0.2s cubic-bezier(0.25,0.8,0.25,1);
}}
{nav_accent_css}
[data-testid="stSidebar"] [role="radiogroup"] label:hover {{
    background: #FFFFFF;
    border-color: var(--nav-border-soft, {LINE});
    transform: translateX(3px);
    box-shadow: 0 4px 14px rgba(13,175,156,0.10);
}}
[data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"] {{
    background: linear-gradient(90deg, var(--nav-wash, {MINT_A}22), var(--nav-wash2, {SIGNAL}12));
    border-color: var(--nav-border, {SIGNAL}55);
    box-shadow: 0 6px 18px rgba(13,175,156,0.14);
}}
[data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"]::before {{
    content: "";
    position: absolute;
    left: 0; top: 20%; bottom: 20%;
    width: 3px;
    border-radius: 0 4px 4px 0;
    background: var(--nav-solid, {SIGNAL});
}}
[data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"] p {{
    color: var(--nav-solid, {MINT_C}) !important;
    font-weight: 700 !important;
}}

.sidebar-session-card {{
    padding: 16px 16px 14px 16px !important;
    margin-bottom: 4px;
}}
.sidebar-logo-card {{
    margin-bottom: 4px !important;
}}
[data-testid="stSidebar"] .stButton>button {{
    background: {PANEL2} !important;
    color: {RISK} !important;
    border: 1.5px solid {RISK}35 !important;
    box-shadow: none !important;
    font-weight: 700 !important;
    animation: none !important;
}}
[data-testid="stSidebar"] .stButton>button:hover {{
    background: {RISK}12 !important;
    border-color: {RISK}70 !important;
    transform: translateY(-1px);
}}

[data-testid="stDataFrame"] {{
    border: 1px solid {LINE};
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 6px 20px rgba(13,175,156,0.06);
}}

.stTabs [data-baseweb="tab-list"] {{
    gap: 4px;
    background: {PANEL2};
    padding: 5px;
    border-radius: 13px;
    border: 1px solid {LINE};
}}
.stTabs [data-baseweb="tab"] {{
    color: {MIST};
    font-weight: 700;
    font-size: 13.5px;
    border-radius: 9px !important;
    padding: 9px 20px !important;
    transition: color 0.18s ease;
}}
.stTabs [data-baseweb="tab"]:hover {{ color: {INK_SOFT}; }}
.stTabs [aria-selected="true"] {{
    color: {SIGNAL} !important;
    background: #FFFFFF;
    box-shadow: 0 4px 14px -2px {SIGNAL}35;
}}
.stTabs [data-baseweb="tab-highlight"] {{ background: transparent !important; }}
.stTabs [data-baseweb="tab-border"] {{ background: transparent !important; }}

/* ---------------------------------------------------------
   CARDS -- glass with a hairline "shine" edge on top
   --------------------------------------------------------- */
.glass {{
    position: relative;
    background: {PANEL};
    border: 1.5px solid {LINE};
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 10px 30px 0 rgba(13,175,156,0.09);
    transition: all 0.28s cubic-bezier(0.25, 0.8, 0.25, 1);
    overflow: hidden;
}}
.glass::before {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, {MINT_C}, {MINT_A} 45%, {GOLD} 100%);
    opacity: 0.0;
    transition: opacity 0.25s ease;
}}
.glass:hover {{
    transform: translateY(-3px);
    border-color: rgba(13,175,156,0.45);
    box-shadow: 0 18px 44px 0 rgba(63,242,196,0.20);
}}
.glass:hover::before {{ opacity: 1; }}

.glass-flat {{
    background: {PANEL};
    border: 1.5px solid {LINE};
    border-radius: 18px;
    padding: 18px 20px;
}}

.aperture-eyebrow {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: {SIGNAL};
    display: flex;
    align-items: center;
    gap: 8px;
    margin: 6px 0 14px 0;
}}

.hero-badge {{
    display: inline-flex;
    align-items: center;
    gap: 9px;
    padding: 9px 20px;
    background: linear-gradient(90deg, {MINT_A}14, {SIGNAL}10);
    border: 1px solid {SIGNAL}3d;
    border-radius: 999px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11.5px;
    letter-spacing: 2px;
    color: {MINT_C};
    text-transform: uppercase;
    font-weight: 600;
    box-shadow: 0 4px 16px rgba(13,175,156,0.10);
}}
.hero-dot {{
    width: 7px; height: 7px; border-radius: 50%;
    background: {MINT_A};
    box-shadow: 0 0 0 0 rgba(63,242,196,0.6);
    animation: pulseDot 2s infinite;
}}
@keyframes pulseDot {{
    0%   {{ box-shadow: 0 0 0 0 rgba(63,242,196,0.55); }}
    70%  {{ box-shadow: 0 0 0 8px rgba(63,242,196,0); }}
    100% {{ box-shadow: 0 0 0 0 rgba(63,242,196,0); }}
}}

.shine-text {{
    background: linear-gradient(100deg, {MINT_C} 0%, {SIGNAL} 35%, {MINT_A} 60%, {MINT_C} 100%);
    background-size: 220% auto;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shineMove 7s ease-in-out infinite;
}}
@keyframes shineMove {{
    0% {{ background-position: 0% center; }}
    50% {{ background-position: 100% center; }}
    100% {{ background-position: 0% center; }}
}}

.step-pill {{
    display: inline-flex;
    align-items: center;
    padding: 7px 16px;
    background: {SIGNAL}14;
    border: 1px solid {LINE};
    border-radius: 999px;
    color: {MINT_C};
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin: 4px 0 14px 0;
}}

.profile-field {{
    background: {PANEL2};
    border: 1px solid {LINE};
    border-radius: 14px;
    padding: 14px 16px;
    margin-bottom: 10px;
    transition: border-color 0.2s ease;
}}
.profile-field:hover {{ border-color: {SIGNAL}55; }}
.profile-field-label {{
    font-size: 11px;
    color: {MIST};
    text-transform: uppercase;
    letter-spacing: 0.6px;
    font-weight: 700;
    margin-bottom: 4px;
}}
.profile-field-value {{
    font-size: 15px;
    color: {INK};
    font-weight: 600;
    word-break: break-word;
}}

.chip {{
    display: inline-block;
    padding: 6px 13px;
    margin: 3px 4px 3px 0;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    background: {SIGNAL}14;
    border: 1px solid {SIGNAL}40;
    color: {MINT_C};
    transition: all 0.15s ease;
}}
.chip:hover {{ background: {SIGNAL}22; transform: translateY(-1px); }}

.list-card-item {{
    padding: 9px 0;
    border-bottom: 1px dashed {LINE};
    color: {INK};
    font-size: 13px;
}}
.list-card-item:last-child {{ border-bottom: none; }}

/* ---------------------------------------------------------
   BUTTONS -- primary (solid signal gradient + glow), secondary
   (ghost outline that fills on hover), and a quiet icon-scale
   press response shared by both. Every state has a visible
   focus ring for keyboard users.
   --------------------------------------------------------- */
.stButton>button {{
    position: relative;
    width: 100%;
    height: 48px;
    background: linear-gradient(135deg, {MINT_A} 0%, {SIGNAL} 55%, {MINT_C} 100%);
    background-size: 170% 170%;
    background-position: 0% 0%;
    color: #06231C;
    border: none;
    border-radius: 12px;
    font-size: 14.5px;
    font-weight: 700;
    letter-spacing: 0.2px;
    transition: transform 0.16s cubic-bezier(0.25,0.8,0.25,1),
                box-shadow 0.22s ease, background-position 0.35s ease;
    box-shadow: 0 1px 0 rgba(255,255,255,0.35) inset,
                0 8px 20px -4px {SIGNAL}70,
                0 0 22px -4px {MINT_A}80;
    animation: buttonGlowPulse 2.8s ease-in-out infinite;
}}
.stButton>button p {{ color: #06231C !important; font-weight: 700 !important; }}
.stButton>button:hover {{
    transform: translateY(-2px);
    background-position: 100% 100%;
    box-shadow: 0 1px 0 rgba(255,255,255,0.45) inset,
                0 14px 30px -6px {SIGNAL}85,
                0 0 34px -2px {MINT_A}b0;
}}
.stButton>button:active {{ transform: translateY(0px) scale(0.985); }}
.stButton>button:focus-visible {{
    outline: none;
    box-shadow: 0 0 0 3px {PANEL}, 0 0 0 6px {SIGNAL}80, 0 0 26px -2px {MINT_A}90;
}}
@keyframes buttonGlowPulse {{
    0%, 100% {{ box-shadow: 0 1px 0 rgba(255,255,255,0.35) inset, 0 8px 20px -4px {SIGNAL}70, 0 0 16px -4px {MINT_A}60; }}
    50%      {{ box-shadow: 0 1px 0 rgba(255,255,255,0.35) inset, 0 8px 24px -4px {SIGNAL}80, 0 0 30px -4px {MINT_A}a0; }}
}}

/* Secondary / ghost buttons -- quiet by design, so the one primary
   action on a screen still reads as the thing to press. */
button[kind="secondary"] {{
    background: {PANEL} !important;
    color: {MINT_C} !important;
    border: 1.5px solid {LINE} !important;
    box-shadow: none !important;
    font-weight: 700 !important;
    animation: none !important;
}}
button[kind="secondary"] p {{ color: {MINT_C} !important; font-weight: 700 !important; }}
button[kind="secondary"]:hover {{
    background: {SIGNAL}0F !important;
    border-color: {SIGNAL}70 !important;
    transform: translateY(-1px);
    box-shadow: 0 6px 18px -6px {MINT_A}60 !important;
}}
button[kind="secondary"]:focus-visible {{
    outline: none;
    box-shadow: 0 0 0 3px {PANEL}, 0 0 0 6px {SIGNAL}55 !important;
}}

/* Every primary (solid) button gets a slow luminous shine sweep on
   top of the glow-pulse above, so the call-to-action reads as lit
   from within -- most noticeable on the sign-in / register CTAs. */
.stButton>button {{ overflow: hidden; }}
.stButton>button::after {{
    content: "";
    position: absolute;
    top: 0; left: -60%;
    width: 40%; height: 100%;
    background: linear-gradient(100deg, transparent, rgba(255,255,255,0.55) 50%, transparent);
    transform: skewX(-20deg);
    animation: authSheen 3.6s ease-in-out infinite;
    pointer-events: none;
}}
button[kind="secondary"]::after {{ display: none; }}
@keyframes authSheen {{
    0%   {{ left: -60%; }}
    55%  {{ left: 140%; }}
    100% {{ left: 140%; }}
}}

.stTextInput input, .stTextArea textarea,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"],
.stDateInput input, .stTimeInput input {{
    background: {PANEL2} !important;
    border: 1.5px solid {LINE} !important;
    border-radius: 11px !important;
    color: {INK} !important;
    transition: border-color 0.18s ease, box-shadow 0.18s ease, background 0.18s ease;
}}
.stTextInput input:hover, .stTextArea textarea:hover {{ border-color: {SIGNAL}60 !important; }}
.stTextInput input:focus, .stTextArea textarea:focus {{
    background: {PANEL} !important;
    border-color: {SIGNAL} !important;
    box-shadow: 0 0 0 3px {SIGNAL}22 !important;
}}
.stTextInput label, .stTextArea label, .stSelectbox label, .stNumberInput label,
.stDateInput label, .stTimeInput label {{
    font-weight: 600 !important;
    font-size: 13px !important;
    color: {INK_SOFT} !important;
}}

[data-testid="stFileUploader"] {{
    border: 1.5px dashed {SIGNAL}55;
    border-radius: 16px;
    padding: 26px;
    background: {PANEL2};
    transition: border-color 0.2s ease, background 0.2s ease;
}}
[data-testid="stFileUploader"]:hover {{ border-color: {SIGNAL}; background: {SIGNAL}0A; }}

.stProgress > div > div {{
    background: linear-gradient(90deg, {MINT_C}, {SIGNAL}, {GOLD}) !important;
}}

.stCheckbox label p {{ font-size: 13px !important; color: {MIST} !important; }}

[data-testid="stAlert"] {{
    border-radius: 14px !important;
    border: 1px solid {LINE} !important;
}}

div[role="radiogroup"] label {{
    background: {PANEL2};
    border: 1px solid {LINE};
    border-radius: 999px !important;
    padding: 6px 14px !important;
    margin-right: 6px !important;
    font-size: 12.5px !important;
    font-weight: 600 !important;
    transition: all 0.16s ease;
}}

/* ---------------------------------------------------------
   NATIVE BORDERED CONTAINERS (st.container(border=True))
   Used instead of the raw-HTML open/close-div trick, which
   cannot actually wrap real widgets — restyle Streamlit's own
   bordered container to look like our glass cards instead.
   --------------------------------------------------------- */
[data-testid="stVerticalBlockBorderWrapper"] {{
    background: {PANEL} !important;
    border: 1.5px solid {LINE} !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 30px 0 rgba(13,175,156,0.09) !important;
}}
[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlock"] {{
    gap: 0.6rem;
}}

/* Split-hero landing panel (left brand column) */
.hero-panel {{
    position: relative;
    border-radius: 26px;
    padding: 46px 40px;
    height: 100%;
    min-height: 560px;
    background:
        radial-gradient(520px 320px at 15% 0%, rgba(255,255,255,0.16), transparent 60%),
        radial-gradient(420px 300px at 100% 100%, rgba(212,175,55,0.22), transparent 55%),
        linear-gradient(155deg, {MINT_C} 0%, {SIGNAL} 55%, {MINT_A} 120%);
    box-shadow: 0 24px 60px rgba(11,127,115,0.28);
    overflow: hidden;
}}
.hero-panel::after {{
    content: "";
    position: absolute;
    right: -60px; bottom: -60px;
    width: 240px; height: 240px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255,255,255,0.14), transparent 70%);
}}
.hero-feature {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 16px;
}}
.hero-feature-icon {{
    width: 30px; height: 30px; min-width: 30px; border-radius: 9px;
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.3);
    display: flex; align-items: center; justify-content: center;
    font-size: 14px;
}}

/* ---------------------------------------------------------
   3D LANDING SECTIONS -- tilt cards, flow orbs, terminal CTA.
   Pure-CSS "3D": perspective + rotateX/rotateY on hover,
   layered inset/outset shadows to fake sphere/button depth,
   translateZ to lift elements off the card plane.
   --------------------------------------------------------- */
.tilt-card {{
    position: relative;
    background: {PANEL};
    border: 1.5px solid {LINE};
    border-radius: 20px;
    padding: 26px 24px;
    height: 100%;
    box-sizing: border-box;
    transform-style: preserve-3d;
    perspective: 900px;
    transition: transform 0.35s cubic-bezier(0.22,1,0.36,1), box-shadow 0.35s ease, border-color 0.3s ease;
    box-shadow: 0 14px 34px -14px var(--tilt-accent, {SIGNAL})55;
    overflow: hidden;
    animation: tiltCardGlow 3.4s ease-in-out infinite;
}}
@keyframes tiltCardGlow {{
    0%, 100% {{ box-shadow: 0 14px 34px -14px var(--tilt-accent, {SIGNAL})40; }}
    50%      {{ box-shadow: 0 18px 40px -14px var(--tilt-accent, {SIGNAL})70; }}
}}
.tilt-card::before {{
    content: "";
    position: absolute; inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.55), transparent 45%);
    opacity: 0.7;
    pointer-events: none;
}}
.tilt-card:hover {{
    transform: rotateX(6deg) rotateY(-6deg) translateY(-6px) translateZ(6px);
    border-color: var(--tilt-accent, {SIGNAL})88;
    box-shadow: 0 34px 60px -14px var(--tilt-accent, {SIGNAL})80;
    animation-play-state: paused;
}}
.tilt-card-num {{
    width: 44px; height: 44px; border-radius: 14px;
    background: radial-gradient(circle at 30% 25%, var(--tilt-accent-light, {MINT_A}), var(--tilt-accent, {SIGNAL}) 65%, var(--tilt-accent, {MINT_C}));
    display: flex; align-items: center; justify-content: center;
    font-family: 'Space Grotesk', sans-serif; font-weight: 800; color: #FFFFFF; font-size: 17px;
    transform: translateZ(24px);
    margin-bottom: 14px;
    animation: tiltIconPulse 2.6s ease-in-out infinite;
}}
@keyframes tiltIconPulse {{
    0%, 100% {{
        box-shadow: 0 10px 18px -5px var(--tilt-accent, {SIGNAL})77,
            inset 0 1px 1px rgba(255,255,255,0.55), inset 0 -3px 4px rgba(0,0,0,0.18),
            0 0 0 0 var(--tilt-accent, {SIGNAL})55;
    }}
    50% {{
        box-shadow: 0 12px 22px -5px var(--tilt-accent, {SIGNAL})99,
            inset 0 1px 1px rgba(255,255,255,0.6), inset 0 -3px 4px rgba(0,0,0,0.18),
            0 0 0 6px var(--tilt-accent, {SIGNAL})00;
    }}
}}
.tilt-card-title {{
    font-family: 'Space Grotesk', sans-serif; font-weight: 800; font-size: 15px;
    color: {INK}; margin-bottom: 8px; transform: translateZ(14px);
}}
.tilt-card-body {{
    font-size: 12.5px; color: {MIST}; line-height: 1.6; transform: translateZ(10px);
}}

.flow-row {{
    display: flex; align-items: flex-start; gap: 0; margin: 6px 0 8px 0;
}}
.flow-step {{
    flex: 1; text-align: center; position: relative; padding: 0 16px;
}}
.flow-step::after {{
    content: "";
    position: absolute; top: 32px; left: 50%; width: 100%; height: 2px;
    background: repeating-linear-gradient(90deg, {SIGNAL}99 0 8px, transparent 8px 15px);
    z-index: 1;
}}
.flow-step:last-child::after {{ display: none; }}
.flow-orb {{
    width: 64px; height: 64px; border-radius: 50%;
    margin: 0 auto 16px auto;
    background: radial-gradient(circle at 32% 26%, {MINT_A}, {SIGNAL} 55%, {MINT_C} 100%);
    display: flex; align-items: center; justify-content: center;
    font-size: 24px;
    box-shadow: 0 16px 26px -8px {SIGNAL}66, inset -5px -6px 10px rgba(0,0,0,0.18), inset 3px 4px 8px rgba(255,255,255,0.4);
    position: relative; z-index: 2;
    transition: transform 0.3s ease;
}}
.flow-step:hover .flow-orb {{ transform: translateY(-4px) scale(1.05); }}
.flow-step-title {{
    font-family: 'Space Grotesk', sans-serif; font-weight: 800; font-size: 14px; color: {INK}; margin-bottom: 6px;
}}
.flow-step-body {{
    font-size: 12px; color: {MIST}; line-height: 1.55; max-width: 220px; margin: 0 auto;
}}

.terminal-cta {{
    position: relative;
    border-radius: 26px;
    padding: 46px 44px;
    margin: 12px 0 8px 0;
    background: linear-gradient(155deg, {VOID_DARK} 0%, {VOID_DARK2} 55%, #0B7F73 150%);
    box-shadow: 0 34px 70px -18px rgba(11,42,34,0.55), inset 0 1px 0 rgba(255,255,255,0.06), 0 0 0 0 {MINT_A}00;
    overflow: hidden;
    animation: terminalGlow 3.6s ease-in-out infinite;
}}
@keyframes terminalGlow {{
    0%, 100% {{
        box-shadow: 0 34px 70px -18px rgba(11,42,34,0.55), inset 0 1px 0 rgba(255,255,255,0.06), 0 0 30px -4px {MINT_A}00;
    }}
    50% {{
        box-shadow: 0 40px 80px -18px rgba(11,42,34,0.6), inset 0 1px 0 rgba(255,255,255,0.08), 0 0 50px -2px {MINT_A}55;
    }}
}}
.terminal-cta::before {{
    content: "";
    position: absolute; inset: -20%;
    background-image:
        linear-gradient(rgba(63,242,196,0.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(63,242,196,0.08) 1px, transparent 1px);
    background-size: 34px 34px;
    transform: perspective(500px) rotateX(55deg) scale(1.6);
    transform-origin: top;
    opacity: 0.55;
    pointer-events: none;
}}
.terminal-cta::after {{
    content: "";
    position: absolute; right: -80px; top: -80px; width: 260px; height: 260px; border-radius: 50%;
    background: radial-gradient(circle, rgba(63,242,196,0.24), transparent 70%);
    pointer-events: none;
}}
.terminal-shine {{
    position: absolute;
    top: 0; left: -160%;
    width: 55%; height: 100%;
    background: linear-gradient(100deg, transparent, rgba(63,242,196,0.20) 45%, rgba(255,255,255,0.10) 55%, transparent);
    transform: skewX(-20deg);
    animation: kpiSweep 5.5s ease-in-out infinite;
    pointer-events: none;
    z-index: 1;
}}
.terminal-cta-inner {{ position: relative; z-index: 2; }}

/* ---------------------------------------------------------
   LANDING PRODUCT SHOWCASE -- dark glass "app inside a card"
   mockup with visual-only demo tabs (st.tabs, real keyboard-
   navigable widget, no backend calls). Deliberately hardcoded
   dark regardless of Night Mode, like .terminal-cta, since this
   is meant to read as a miniature app window, not a themed
   page section.
   --------------------------------------------------------- */
.showcase-shell {{
    position: relative;
    border-radius: 24px;
    padding: 30px 32px 8px 32px;
    background: linear-gradient(165deg, {VOID_DARK} 0%, {VOID_DARK2} 60%, #0E2B22 130%);
    border: 1px solid rgba(63,242,196,0.16);
    box-shadow: 0 30px 64px -20px rgba(3,7,6,0.55), inset 0 1px 0 rgba(255,255,255,0.05);
    overflow: hidden;
    margin-bottom: 8px;
}}
.showcase-shell .stTabs [data-baseweb="tab-list"] {{
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
}}
.showcase-shell .stTabs [data-baseweb="tab"] {{ color: #9BB8AE !important; }}
.showcase-shell .stTabs [data-baseweb="tab"]:hover {{ color: #F4FFFA !important; }}
.showcase-shell .stTabs [aria-selected="true"] {{
    color: {MINT_A} !important;
    background: rgba(63,242,196,0.12) !important;
    box-shadow: 0 4px 14px -2px rgba(63,242,196,0.25) !important;
}}
.showcase-label {{
    font-family: 'IBM Plex Mono', monospace; font-size: 10.5px; letter-spacing: 1.4px;
    text-transform: uppercase; color: #6C8B80; margin: 6px 0 12px 0;
}}
.showcase-row {{
    display: flex; justify-content: space-between; align-items: center;
    padding: 12px 14px; border-radius: 12px; margin-bottom: 8px;
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06);
    transition: background 0.2s ease, border-color 0.2s ease;
}}
.showcase-row.active {{
    background: rgba(63,242,196,0.10); border-color: rgba(63,242,196,0.35);
}}
.showcase-row-name {{ font-weight: 700; font-size: 13.5px; color: #F4FFFA; }}
.showcase-row-sub {{ font-size: 11px; color: #7C93A0; margin-top: 1px; }}
.showcase-row-score {{ font-family: 'Space Grotesk', sans-serif; font-weight: 800; font-size: 14px; color: {MINT_A}; }}
.showcase-profile {{
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px; padding: 20px 22px;
}}
.showcase-mini-label {{
    font-size: 10px; text-transform: uppercase; letter-spacing: 0.5px; color: #6C8B80; font-weight: 700;
}}
.showcase-mini-value {{ font-family: 'Space Grotesk', sans-serif; font-weight: 800; font-size: 15px; color: #F4FFFA; margin-top: 2px; }}
.showcase-bar-track {{
    height: 8px; border-radius: 6px; background: rgba(255,255,255,0.08);
    overflow: hidden;
}}
.showcase-bar-fill {{ height: 100%; border-radius: 6px; transition: width 0.5s ease; }}
.showcase-terminal {{
    background: rgba(0,0,0,0.18); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px; padding: 22px 24px; font-family: 'Inter', sans-serif;
}}

.faq-wrap [data-testid="stExpander"] {{
    background: {PANEL};
    border: 1.5px solid {LINE} !important;
    border-radius: 16px !important;
    box-shadow: 0 10px 26px -10px rgba(13,175,156,0.16);
    margin-bottom: 10px;
    overflow: hidden;
    transition: box-shadow 0.25s ease, border-color 0.25s ease;
}}
.faq-wrap [data-testid="stExpander"]:hover {{
    border-color: {SIGNAL}55 !important;
    box-shadow: 0 16px 34px -10px rgba(13,175,156,0.24);
}}
.faq-wrap [data-testid="stExpander"] summary {{
    font-weight: 700 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    color: {INK} !important;
    position: relative;
    padding-left: 40px !important;
}}
/* Hide Streamlit's default caret/chevron icon -- replaced below with a
   glowing 3D orb + a plus/cross toggle glyph. Several selectors so this
   holds across Streamlit versions that mark up the icon differently. */
.faq-wrap [data-testid="stExpander"] summary svg,
.faq-wrap [data-testid="stExpander"] [data-testid="stExpanderToggleIcon"],
.faq-wrap [data-testid="stExpander"] summary [data-testid^="stIcon"] {{
    display: none !important;
}}
.faq-wrap [data-testid="stExpander"] summary::before {{
    content: "";
    position: absolute; left: 0; top: 50%;
    width: 24px; height: 24px;
    margin-top: -12px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 25%, {MINT_A}, {SIGNAL} 55%, {MINT_C} 100%);
    box-shadow:
        0 0 0 0 {MINT_A}55,
        0 6px 14px -3px {SIGNAL}88,
        inset -3px -4px 6px rgba(0,0,0,0.22),
        inset 2px 3px 5px rgba(255,255,255,0.5);
    transition: box-shadow 0.3s ease, transform 0.3s cubic-bezier(0.22,1,0.36,1);
    animation: faqOrbGlow 2.2s ease-in-out infinite;
    transform-origin: center;
    z-index: 1;
}}
.faq-wrap [data-testid="stExpander"] summary::after {{
    content: "";
    position: absolute; left: 8px; top: 50%;
    width: 8px; height: 8px;
    margin-top: -4px;
    background:
        linear-gradient(#FFFFFF, #FFFFFF) center / 100% 2px no-repeat,
        linear-gradient(#FFFFFF, #FFFFFF) center / 2px 100% no-repeat;
    filter: drop-shadow(0 1px 1px rgba(0,0,0,0.35));
    transition: transform 0.35s cubic-bezier(0.22,1,0.36,1);
    transform: rotate(0deg);
    pointer-events: none;
    z-index: 2;
}}
.faq-wrap [data-testid="stExpander"] summary:hover::before {{
    transform: scale(1.15);
    box-shadow:
        0 0 0 6px {MINT_A}22,
        0 8px 18px -3px {SIGNAL}aa,
        inset -3px -4px 6px rgba(0,0,0,0.22),
        inset 2px 3px 5px rgba(255,255,255,0.55);
}}
.faq-wrap [data-testid="stExpander"] details[open] > summary::after,
.faq-wrap [data-testid="stExpander"] summary[aria-expanded="true"]::after {{
    transform: rotate(45deg);
}}
@keyframes faqOrbGlow {{
    0%, 100% {{
        box-shadow:
            0 0 0 0 {MINT_A}55,
            0 6px 14px -3px {SIGNAL}88,
            inset -3px -4px 6px rgba(0,0,0,0.22),
            inset 2px 3px 5px rgba(255,255,255,0.5);
    }}
    50% {{
        box-shadow:
            0 0 0 5px {MINT_A}00,
            0 8px 20px -3px {SIGNAL}cc,
            inset -3px -4px 6px rgba(0,0,0,0.22),
            inset 2px 3px 5px rgba(255,255,255,0.6);
    }}
}}

/* ---------------------------------------------------------
   KPI / METRIC CARDS -- color-matched glass with a moving
   glow bar, a diagonal shine sweep, and a pulsing icon ring.
   Colors are supplied per-card via inline CSS custom
   properties (--kpi-*) so this one ruleset drives every KPI
   card on every page, whatever its accent color is.
   --------------------------------------------------------- */
.kpi-card {{
    position: relative;
    border-radius: 20px;
    padding: 22px;
    margin-bottom: 0;
    border: 1.5px solid var(--kpi-border, {LINE});
    background: var(--kpi-bg, {PANEL});
    box-shadow: var(--kpi-shadow, 0 10px 30px 0 rgba(13,175,156,0.09));
    overflow: hidden;
    transition: transform 0.3s cubic-bezier(0.25,0.8,0.25,1), box-shadow 0.3s ease;
}}
.kpi-card:hover {{
    transform: translateY(-5px);
    box-shadow: var(--kpi-shadow-hover, 0 18px 44px 0 rgba(63,242,196,0.20));
}}
.kpi-top-bar {{
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: var(--kpi-bar);
    background-size: 200% auto;
    animation: kpiBarMove 3.2s linear infinite;
}}
@keyframes kpiBarMove {{
    0%   {{ background-position: 0% center; }}
    100% {{ background-position: 200% center; }}
}}
.kpi-shine {{
    position: absolute;
    top: 0; left: -160%;
    width: 55%; height: 100%;
    background: linear-gradient(100deg, transparent, var(--kpi-sheen, rgba(255,255,255,0.5)) 50%, transparent);
    transform: skewX(-20deg);
    animation: kpiSweep 5s ease-in-out infinite;
    pointer-events: none;
}}
@keyframes kpiSweep {{
    0%   {{ left: -160%; }}
    45%  {{ left: 160%; }}
    100% {{ left: 160%; }}
}}
.kpi-icon {{
    width: 46px; height: 46px; border-radius: 13px;
    display: flex; align-items: center; justify-content: center;
    font-size: 21px;
    position: relative; z-index: 1;
    background: var(--kpi-icon-bg);
    border: 1px solid var(--kpi-border, transparent);
    animation: kpiIconGlow 2.6s ease-in-out infinite;
}}
@keyframes kpiIconGlow {{
    0%, 100% {{ box-shadow: 0 0 0 0 var(--kpi-ring, rgba(0,0,0,0)); }}
    50%      {{ box-shadow: 0 0 0 7px var(--kpi-ring, rgba(0,0,0,0)); }}
}}
.kpi-dot {{
    width: 8px; height: 8px; border-radius: 50%;
    background: var(--kpi-solid, {MINT_A});
    box-shadow: 0 0 0 4px var(--kpi-ring, rgba(63,242,196,0.15));
    position: relative; z-index: 1;
}}
.kpi-value {{
    position: relative; z-index: 1;
}}

/* ---------------------------------------------------------
   WELCOME HERO -- big "AI Recruitment Copilot" style banner
   with a soft radial glow behind the greeting.
   --------------------------------------------------------- */
.hero-welcome {{
    position: relative;
    border-radius: 22px;
    padding: 28px 32px;
    border: 1.5px solid {LINE};
    background:
        radial-gradient(480px 240px at 92% -10%, {SKY}22, transparent 60%),
        radial-gradient(420px 260px at 100% 100%, {VIOLET}18, transparent 55%),
        linear-gradient(150deg, {MINT_C}12 0%, {PANEL} 55%, {SIGNAL}0A 100%);
    box-shadow: 0 12px 34px 0 rgba(13,175,156,0.10);
    overflow: hidden;
}}
.hero-welcome-orb {{
    position: absolute; right: -40px; top: -40px;
    width: 220px; height: 220px; border-radius: 50%;
    background: radial-gradient(circle, {SKY}28, transparent 70%);
    filter: blur(4px);
}}

/* ---------------------------------------------------------
   ATS DONUT -- pure-CSS conic-gradient ring + side legend,
   matching the reference layout exactly and needing no chart
   library, so it repaints for free under Night Mode.
   --------------------------------------------------------- */
.ats-donut-wrap {{ display:flex; align-items:center; gap: 22px; }}
.ats-donut {{
    width: 128px; height: 128px; min-width: 128px; border-radius: 50%;
    display:flex; align-items:center; justify-content:center;
    box-shadow: 0 6px 20px rgba(13,175,156,0.10);
}}
.ats-donut-inner {{
    width: 88px; height: 88px; border-radius: 50%;
    background: {PANEL};
    display:flex; flex-direction:column; align-items:center; justify-content:center;
}}
.ats-donut-value {{ font-size: 22px; font-weight: 800; font-family:'Space Grotesk'; color: {INK}; }}
.ats-donut-label {{ font-size: 10px; color: {MIST}; margin-top: 2px; text-align:center; }}
.ats-legend {{ font-size: 12.5px; line-height: 2.1; color: {INK_SOFT}; }}
.ats-legend .dot {{
    display:inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 8px;
}}
.ats-legend .pct {{ color: {MIST}; font-weight: 600; }}

/* ---------------------------------------------------------
   ATS SCORE CARD -- single-value circular match score (conic
   gradient), banded to the same 85/70/50 thresholds used
   elsewhere (ats_donut, recent_candidates_mini), plus a fact
   row and an expandable evidence panel. Framed as
   "AI-assisted" per the product-language guidance -- never a
   verdict, never a fabricated weighted breakdown.
   --------------------------------------------------------- */
.score-card {{
    display: flex;
    align-items: center;
    gap: 26px;
    flex-wrap: wrap;
}}
.score-ring-col {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    min-width: 132px;
}}
.score-ring {{
    width: 116px; height: 116px; min-width: 116px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 6px 20px rgba(13,175,156,0.10);
    transition: background 0.6s ease;
}}
.score-ring-inner {{
    width: 92px; height: 92px; border-radius: 50%;
    background: {PANEL};
    display: flex; flex-direction: column; align-items: center; justify-content: center;
}}
.score-ring-value {{ font-size: 30px; font-weight: 800; font-family: 'Space Grotesk', sans-serif; line-height: 1; }}
.score-ring-unit {{ font-size: 10px; color: {MIST}; margin-top: 3px; font-family: 'IBM Plex Mono', monospace; }}
.score-band-pill {{
    padding: 4px 12px; border-radius: 999px; border: 1px solid;
    font-size: 11px; font-weight: 700; letter-spacing: 0.3px;
    white-space: nowrap;
}}
.score-detail-col {{ flex: 1; min-width: 220px; }}
.score-facts {{ display: flex; gap: 22px; flex-wrap: wrap; margin-top: 10px; }}
.score-fact {{ display: flex; flex-direction: column; gap: 2px; }}
.score-fact-label {{
    font-size: 10.5px; text-transform: uppercase; letter-spacing: 0.6px;
    color: {MIST}; font-weight: 700;
}}
.score-fact-value {{ font-size: 15px; font-weight: 700; color: {INK}; font-family: 'Space Grotesk', sans-serif; }}

/* ---------------------------------------------------------
   HIRING PIPELINE FUNNEL -- horizontal tapered bars, widest
   stage first, each labeled with its count.
   --------------------------------------------------------- */
.funnel-row {{ margin-bottom: 12px; }}
.funnel-label {{
    display: flex; justify-content: space-between; align-items: baseline;
    font-size: 12.5px; font-weight: 700; color: {MIST}; margin-bottom: 5px;
}}
.funnel-label b {{ color: {INK}; font-size: 13.5px; font-family:'Space Grotesk'; }}
.funnel-track {{
    height: 14px; border-radius: 8px;
    background: {PANEL2}; border: 1px solid {LINE};
    overflow: hidden;
}}
.funnel-fill {{
    height: 100%; border-radius: 8px;
    transition: width 0.4s ease;
}}

/* ---------------------------------------------------------
   SKILL DEMAND -- ranked horizontal bars.
   --------------------------------------------------------- */
.skill-row {{ margin-bottom: 11px; }}
.skill-label {{
    display: flex; justify-content: space-between;
    font-size: 12.5px; font-weight: 600; color: {INK_SOFT}; margin-bottom: 4px;
}}
.skill-track {{
    height: 9px; border-radius: 6px;
    background: {PANEL2}; border: 1px solid {LINE};
    overflow: hidden;
}}
.skill-fill {{ height: 100%; border-radius: 6px; }}

/* ---------------------------------------------------------
   RECENT CANDIDATES mini table + AI insight rows
   --------------------------------------------------------- */
.mini-row {{
    display: flex; align-items: center; justify-content: space-between;
    padding: 10px 2px; border-bottom: 1px solid {LINE_SOFT};
    font-size: 13px;
}}
.mini-row:last-child {{ border-bottom: none; }}
.mini-name {{ font-weight: 700; color: {INK}; }}
.mini-sub {{ color: {MIST}; font-size: 11.5px; margin-top: 1px; }}
.mini-badge {{
    padding: 4px 11px; border-radius: 999px; font-size: 11px; font-weight: 700;
    white-space: nowrap;
}}

.insight-row {{
    display: flex; align-items: flex-start; gap: 10px;
    padding: 11px 12px; border-radius: 12px;
    background: {PANEL2}; border: 1px solid {LINE};
    margin-bottom: 8px; font-size: 12.5px;
}}
.insight-row:last-child {{ margin-bottom: 0; }}

/* Dashboard "Recent AI Insights" mini-cards (icon-on-top layout, distinct
   from .insight-row's flex-row layout). Given a real class so the night
   mode layer below can repaint it -- previously these were raw inline
   `style="background:{PANEL2}..."` divs with no class, which nothing in
   night mode could target, so they stayed light-mode white with
   near-invisible text on top. */
.ai-insight-card {{
    background: {PANEL2}; border: 1px solid {LINE}; border-radius: 14px;
    padding: 12px 14px; height: 100%;
}}

/* Decorative (non-functional) AI Copilot input mock */
.copilot-card {{ display: flex; flex-direction: column; height: 100%; }}
.copilot-input-mock {{
    margin-top: 12px;
    padding: 11px 14px;
    border-radius: 12px;
    background: {PANEL2};
    border: 1px solid {LINE};
    color: {MIST};
    font-size: 12.5px;
    display: flex; align-items: center; justify-content: space-between;
}}

/* ---------------------------------------------------------
   CANDIDATE OVERVIEW -- horizontal pipeline stepper, dashboard
   mini list-cards ("Recent Activity" / "Upcoming Interviews" /
   "Messages from Recruiters" / "Recent Applications"), and the
   small quote card next to the welcome banner.
   --------------------------------------------------------- */
.quote-card {{
    height: 100%;
    display: flex; align-items: center; justify-content: center;
    text-align: center;
    padding: 18px 20px;
}}
.quote-card-text {{
    color: {MIST}; font-size: 12.5px; font-style: italic; line-height: 1.55;
}}

.stepper-row {{
    display: flex; align-items: flex-start; justify-content: space-between;
    gap: 2px; padding: 2px 4px 6px 4px;
}}
.stepper-node {{
    display: flex; flex-direction: column; align-items: center; text-align: center;
    min-width: 60px; flex: 1;
}}
.stepper-circle {{
    width: 50px; height: 50px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 19px; border: 1.5px solid; margin-bottom: 8px;
}}
.stepper-label {{ font-size: 11.5px; color: {MIST}; font-weight: 700; }}
.stepper-count {{
    font-size: 19px; font-weight: 800; color: {INK};
    font-family: 'Space Grotesk', sans-serif; margin-top: 2px;
}}
.stepper-arrow {{
    color: {LINE}; font-size: 17px; margin-top: 17px; flex-shrink: 0;
}}
.rejected-mini-card {{
    display: flex; align-items: center; gap: 12px;
    background: {RISK}0d; border: 1px solid {RISK}30; border-radius: 14px;
    padding: 10px 16px; margin-top: 16px; max-width: 55%;
}}

.view-all-link {{ color: {SIGNAL}; font-size: 11.5px; font-weight: 700; white-space: nowrap; }}

.list-row {{
    display: flex; align-items: center; gap: 12px;
    padding: 10px 0; border-bottom: 1px solid {LINE_SOFT};
}}
.list-row:last-child {{ border-bottom: none; }}
.list-row-icon {{
    width: 36px; height: 36px; min-width: 36px; border-radius: 11px;
    display: flex; align-items: center; justify-content: center; font-size: 15px;
}}
.list-row-text {{ flex: 1; min-width: 0; }}
.list-row-title {{
    font-weight: 700; color: {INK}; font-size: 12.5px;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}}
.list-row-sub {{
    color: {MIST}; font-size: 11px; margin-top: 1px;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}}
.list-row-badge {{
    padding: 4px 10px; border-radius: 999px; font-size: 10px; font-weight: 700;
    border: 1px solid; white-space: nowrap;
}}
.card-footer-link {{
    margin-top: 10px; padding-top: 10px; border-top: 1px solid {LINE_SOFT};
    text-align: center; color: {SIGNAL}; font-size: 12px; font-weight: 700;
}}

.tip-banner {{
    padding: 16px 24px; background: {SIGNAL}0d; border-color: {SIGNAL}30 !important;
    display: flex; align-items: center; gap: 14px; height: 100%;
}}
</style>
""", unsafe_allow_html=True)

    if st.session_state.get("dark_mode"):
        _inject_night_mode_css()


def _inject_night_mode_css():
    """Night Mode override layer -- deep-space navy/black surfaces with a
    neon mint-teal glow, matching the reference dashboard screenshot.
    Layered on TOP of load_css()'s normal stylesheet via !important rules
    targeting the same class names (.glass, .glass-flat, sidebar, etc.)
    rather than rewriting every f-string color everywhere in the app --
    those still bake in the light-theme hex values, but !important on an
    external rule beats a plain (non-!important) inline style, so this
    repaints every surface without touching the 15+ files that call
    metric_card() / render inline HTML with the light palette."""
    st.markdown(f"""
<style>
.stApp {{
    background:
        radial-gradient(1200px 600px at 75% -10%, rgba(14,165,233,0.10), transparent 55%),
        radial-gradient(900px 500px at 15% 90%, rgba(139,92,246,0.10), transparent 55%),
        radial-gradient(800px 560px at 100% 60%, rgba(63,242,196,0.07), transparent 60%),
        linear-gradient(165deg, #02050B 0%, #050A14 55%, #070B0E 100%) !important;
    background-attachment: fixed !important;
}}
html, body, [class*="css"] {{ background: transparent !important; color: {NIGHT_TEXT} !important; }}
p, span, div, label, li, td, th {{ color: {NIGHT_TEXT} !important; }}
h1, h2, h3, h4 {{ color: {NIGHT_TEXT} !important; }}
.stCaption, [data-testid="stCaptionContainer"] {{ color: {NIGHT_MUTED} !important; }}

[data-testid="stSidebar"] {{
    background: linear-gradient(190deg, #090D11 0%, #0C1319 55%, #0A0F13 100%) !important;
    border-right: 1px solid {NIGHT_LINE} !important;
}}
[data-testid="stSidebar"] * {{ color: {NIGHT_TEXT} !important; }}

.glass, .glass-flat {{
    background: linear-gradient(160deg, {NIGHT_PANEL} 0%, {NIGHT_PANEL2} 100%) !important;
    border: 1.5px solid {NIGHT_LINE} !important;
    box-shadow: 0 10px 30px 0 rgba(63,242,196,0.06) !important;
}}
.glass:hover {{ border-color: {MINT_A}66 !important; box-shadow: 0 18px 44px 0 rgba(63,242,196,0.16) !important; }}

[data-testid="stMetric"], .stDataFrame, .stTable, [data-testid="stExpander"], [data-testid="stForm"] {{
    background: {NIGHT_PANEL} !important;
    border: 1px solid {NIGHT_LINE} !important;
    border-radius: 14px !important;
    color: {NIGHT_TEXT} !important;
}}
[data-testid="stExpander"] summary {{ color: {NIGHT_TEXT} !important; }}

input, textarea, select, .stTextInput input, .stNumberInput input, .stSelectbox [data-baseweb="select"] > div {{
    background: {NIGHT_PANEL2} !important;
    color: {NIGHT_TEXT} !important;
    border-color: {NIGHT_LINE} !important;
}}
.stButton button, .stDownloadButton button {{
    background: {NIGHT_PANEL2} !important;
    color: {NIGHT_TEXT} !important;
    border: 1px solid {NIGHT_LINE} !important;
}}
.stButton button[kind="primary"], .stButton button[data-testid="baseButton-primary"] {{
    background: linear-gradient(90deg, {MINT_C}, {SIGNAL}) !important;
    color: #04120E !important;
    border: none !important;
}}
[data-testid="stChatInput"], [data-testid="stChatMessage"] {{
    background: {NIGHT_PANEL2} !important;
    color: {NIGHT_TEXT} !important;
    border-color: {NIGHT_LINE} !important;
}}
hr {{ border-color: {NIGHT_LINE} !important; background: {NIGHT_LINE} !important; }}

/* --- Tabs (Live Interview / Evaluation & Hiring Decision / Interview
   Pipeline, etc.) -- load_css() bakes light-theme PANEL2/white into
   these, so without this repaint the tab bar stays a bright white
   strip floating on the dark page. --- */
.stTabs [data-baseweb="tab-list"] {{
    background: {NIGHT_PANEL2} !important;
    border-color: {NIGHT_LINE} !important;
}}
.stTabs [data-baseweb="tab"] {{ color: {NIGHT_MUTED} !important; }}
.stTabs [data-baseweb="tab"]:hover {{ color: {NIGHT_TEXT} !important; }}
.stTabs [aria-selected="true"] {{
    color: {MINT_A} !important;
    background: {NIGHT_PANEL} !important;
    box-shadow: 0 4px 14px -2px rgba(63,242,196,0.25) !important;
}}

/* --- Other native Streamlit chrome that shares the same
   never-repainted-for-night-mode gap as the tabs above. --- */
[data-testid="stFileUploader"] {{
    background: {NIGHT_PANEL2} !important;
    border-color: {SIGNAL}55 !important;
}}
[data-testid="stFileUploader"]:hover {{ background: {SIGNAL}14 !important; border-color: {SIGNAL} !important; }}
[data-testid="stAlert"] {{
    background: {NIGHT_PANEL2} !important;
    border-color: {NIGHT_LINE} !important;
    color: {NIGHT_TEXT} !important;
}}
[data-testid="stVerticalBlockBorderWrapper"] {{
    background: {NIGHT_PANEL} !important;
    border-color: {NIGHT_LINE} !important;
    box-shadow: 0 10px 30px 0 rgba(63,242,196,0.06) !important;
}}
div[role="radiogroup"] label {{
    background: {NIGHT_PANEL2} !important;
    border-color: {NIGHT_LINE} !important;
    color: {NIGHT_MUTED} !important;
}}
/* The generic rule above is !important, which -- regardless of selector
   specificity -- beats the sidebar nav's own (non-!important) pill
   background/hover/checked rules in load_css(), flattening the nav
   pills into bare radio bullets. Restore them here, explicitly, after
   the generic rule so these win both on !important and source order. */
[data-testid="stSidebar"] [role="radiogroup"] label {{
    background: rgba(255,255,255,0.04) !important;
    border-color: transparent !important;
    color: {NIGHT_TEXT} !important;
}}
[data-testid="stSidebar"] [role="radiogroup"] label:hover {{
    background: rgba(255,255,255,0.08) !important;
    border-color: var(--nav-border-soft, {NIGHT_LINE}) !important;
}}
[data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"] {{
    background: linear-gradient(90deg, var(--nav-wash, {MINT_A}22), var(--nav-wash2, {SIGNAL}12)) !important;
    border-color: var(--nav-border, {SIGNAL}55) !important;
}}
[data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"] p {{
    color: var(--nav-solid, {MINT_A}) !important;
}}
.stCheckbox label p {{ color: {NIGHT_MUTED} !important; }}

/* --- Date / Time pickers -- load_css() never styled .stDateInput /
   .stTimeInput at all (only text/number/select inputs), so these have
   always rendered as bare browser-default white fields; it just didn't
   show against the light theme. Fixing for both modes matters, but the
   night-mode !important repaint is what makes it visible here. --- */
.stDateInput input, .stTimeInput input,
.stDateInput [data-baseweb="input"], .stTimeInput [data-baseweb="input"],
.stDateInput [data-baseweb="base-input"], .stTimeInput [data-baseweb="base-input"] {{
    background: {NIGHT_PANEL2} !important;
    color: {NIGHT_TEXT} !important;
    border-color: {NIGHT_LINE} !important;
}}
.stDateInput svg, .stTimeInput svg {{ fill: {NIGHT_MUTED} !important; }}

/* --- Dashboard widgets for the "AI Recruitment Copilot" layout ---
   These bake light-theme hex values into their inline styles just like
   the rest of the app, so they need the same !important repaint here. */
.kpi-card {{
    background: linear-gradient(160deg, {NIGHT_PANEL} 0%, {NIGHT_PANEL2} 100%) !important;
    border-color: {NIGHT_LINE} !important;
}}
.hero-welcome {{
    background:
        radial-gradient(480px 240px at 92% -10%, rgba(35,152,255,0.20), transparent 60%),
        radial-gradient(420px 260px at 100% 100%, rgba(123,85,255,0.16), transparent 55%),
        linear-gradient(150deg, #07101D 0%, #091526 60%, #070E17 100%) !important;
    border-color: {NIGHT_LINE} !important;
}}
.hero-welcome-orb {{ background: radial-gradient(circle, rgba(35,152,255,0.30), transparent 70%) !important; }}
.ats-donut-inner {{ background: {NIGHT_PANEL} !important; }}
.score-ring-inner {{ background: {NIGHT_PANEL} !important; }}
.score-fact-value {{ color: {NIGHT_TEXT} !important; }}
.score-fact-label {{ color: {NIGHT_MUTED} !important; }}
.chip {{ filter: brightness(1.15); }}
.funnel-track {{ background: {NIGHT_PANEL2} !important; border-color: {NIGHT_LINE} !important; }}
.skill-track {{ background: {NIGHT_PANEL2} !important; border-color: {NIGHT_LINE} !important; }}
.mini-row {{ border-bottom-color: {NIGHT_LINE} !important; }}
.copilot-input-mock {{
    background: {NIGHT_PANEL2} !important;
    border-color: {NIGHT_LINE} !important;
    color: {NIGHT_MUTED} !important;
}}
.insight-row {{ border-color: {NIGHT_LINE} !important; background: {NIGHT_PANEL2} !important; }}
.ai-insight-card {{ border-color: {NIGHT_LINE} !important; background: {NIGHT_PANEL2} !important; }}
.js-plotly-plot .legendtext, .js-plotly-plot text {{ fill: {NIGHT_TEXT} !important; }}

/* --- Candidate Overview: stepper, mini list-cards, quote/tip banners --- */
.stepper-arrow {{ color: {NIGHT_LINE} !important; }}
.rejected-mini-card {{ background: rgba(220,76,76,0.10) !important; border-color: rgba(220,76,76,0.30) !important; }}
.list-row {{ border-bottom-color: {NIGHT_LINE} !important; }}
.card-footer-link {{ border-top-color: {NIGHT_LINE} !important; }}
.tip-banner {{ background: rgba(13,175,156,0.10) !important; border-color: rgba(13,175,156,0.30) !important; }}
</style>
""", unsafe_allow_html=True)


def landing_proof_section():
    """Four 'tilt' cards (why TalentOps, not another ATS) with a pure-CSS
    3D hover tilt -- perspective + rotateX/rotateY, layered shadows for
    depth."""
    st.markdown(
        '<div class="aperture-eyebrow" style="justify-content:center;">● Why TalentOps</div>'
        f'<div style="text-align:center; font-size:24px; font-weight:800; color:{INK}; '
        'font-family:\'Space Grotesk\'; margin-bottom:26px;">Not another ATS. A hiring decision engine.</div>',
        unsafe_allow_html=True,
    )
    proof_items = [
        ("🎯", "Scored, not skimmed",
         "Every resume receives a structured, weighted role-fit evaluation across skills, experience, and education the moment it's uploaded.",
         SIGNAL, MINT_A),
        ("⏱", "Hours back every week",
         "Recruiters review a prioritized shortlist instead of manually screening hundreds of resumes for every open role.",
         VIOLET, "#C4B5FD"),
        ("🧾", "Audit-ready workflows",
         "Scores, interviews, decisions, and overrides are traceable — recruiters can show their work, not just their outcome.",
         CAUTION, GOLD),
        ("📈", "Learns from outcomes",
         "Organizations can use hiring outcomes to refine future evaluation criteria instead of running the same static rubric forever.",
         VERDICT, MINT_B),
    ]
    cols = st.columns(4, gap="medium")
    for col, (icon, title, body, accent, accent_light) in zip(cols, proof_items):
        with col:
            st.markdown(f"""
                <div class="tilt-card" style="--tilt-accent:{accent}; --tilt-accent-light:{accent_light};">
                    <div class="kpi-top-bar" style="--kpi-bar: linear-gradient(90deg, {accent}00, {accent_light}, {accent}, {accent}00);"></div>
                    <div class="kpi-shine" style="--kpi-sheen: {accent_light}55;"></div>
                    <div class="tilt-card-num">{icon}</div>
                    <div class="tilt-card-title">{title}</div>
                    <div class="tilt-card-body">{body}</div>
                </div>
                """, unsafe_allow_html=True)


def landing_flow_section():
    """3-step architecture walkthrough -- 'orb' nodes connected by a
    dashed line, each orb lifting slightly on hover for a floating
    3D feel."""
    st.markdown(
        '<div class="aperture-eyebrow" style="justify-content:center; margin-top:36px;">● How It Works</div>'
        f'<div style="text-align:center; font-size:24px; font-weight:800; color:{INK}; '
        'font-family:\'Space Grotesk\'; margin-bottom:8px;">From resume to decision, in one flow</div>',
        unsafe_allow_html=True,
    )
    steps = [
        ("📥", "Ingest", "Post a job or upload resumes in bulk. Every resume is parsed into structured candidate data."),
        ("⚙️", "Assess", "Resumes are scored against the job. Shortlisted candidates take an adaptive AI interview."),
        ("✅", "Decide", "Recruiters see ranked candidates, transcripts, and scores in one dashboard — ready to act on."),
    ]
    step_html = "".join(
        '<div class="flow-step">'
        f'<div class="flow-orb">{icon}</div>'
        f'<div class="flow-step-title">{title}</div>'
        f'<div class="flow-step-body">{body}</div>'
        '</div>'
        for icon, title, body in steps
    )
    st.markdown(f'<div class="flow-row">{step_html}</div>', unsafe_allow_html=True)


def landing_showcase_section():
    """Stats strip + a dark 'inside the app' product showcase (visual-
    only demo tabs -- st.tabs is a real widget, but nothing here calls
    the database or ATS engine) + a short trust section. Purely
    additive to the pre-login landing page: doesn't touch the hero,
    portal-selection cards, or any logged-in page/route."""

    # ---- Stats ----
    st.markdown(
        '<div class="aperture-eyebrow" style="justify-content:center; margin-top:8px;">● Product Metrics</div>'
        f'<div style="text-align:center; font-size:24px; font-weight:800; color:{INK}; '
        'font-family:\'Space Grotesk\'; margin-bottom:6px;">What the platform changes</div>'
        f'<div style="text-align:center; color:{MIST}; font-size:12px; margin-bottom:22px;">'
        'Demo-environment figures — not third-party verified benchmarks.</div>',
        unsafe_allow_html=True,
    )
    stats = [
        ("83%", "Less manual resume review", SIGNAL),
        ("94%", "Candidate-to-role match precision", VERDICT),
        ("2.1×", "Faster time-to-shortlist", VIOLET),
        ("0", "Resumes used to train public models", GOLD),
    ]
    scols = st.columns(4, gap="medium")
    for col, (val, label, color) in zip(scols, stats):
        with col:
            st.markdown(f"""
                <div class="glass" style="text-align:center; padding:22px 14px;">
                    <div style="font-family:'Space Grotesk'; font-weight:800; font-size:30px; color:{color};">{val}</div>
                    <div style="color:{MIST}; font-size:12px; margin-top:6px; line-height:1.4;">{label}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)

    # ---- Product Showcase ----
    st.markdown(
        '<div class="aperture-eyebrow" style="justify-content:center; margin-top:28px;">● See It Working</div>'
        f'<div style="text-align:center; font-size:24px; font-weight:800; color:{INK}; '
        'font-family:\'Space Grotesk\'; margin-bottom:4px;">A look inside the recruiter workspace</div>'
        f'<div style="text-align:center; color:{MIST}; font-size:12px; margin-bottom:20px;">'
        'A visual preview — sign in to use the real thing.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="showcase-shell">', unsafe_allow_html=True)
    tab_overview, tab_scoring, tab_interview = st.tabs(["Overview", "Scoring", "AI Interview"])

    with tab_overview:
        lcol, rcol = st.columns([1, 1.3], gap="medium")
        with lcol:
            st.markdown('<div class="showcase-label">Candidate Queue</div>', unsafe_allow_html=True)
            queue = [
                ("Aisha Rahman", "Senior Backend Engineer", 94, True),
                ("Marcus Webb", "Senior Backend Engineer", 81, False),
                ("Priya Nair", "Senior Backend Engineer", 76, False),
            ]
            rows = "".join(f"""
                <div class="showcase-row{' active' if sel else ''}">
                    <div>
                        <div class="showcase-row-name">{name}</div>
                        <div class="showcase-row-sub">{role}</div>
                    </div>
                    <div class="showcase-row-score">{score}%</div>
                </div>
                """ for name, role, score, sel in queue)
            st.markdown(rows, unsafe_allow_html=True)
        with rcol:
            st.markdown('<div class="showcase-label">Candidate Profile</div>', unsafe_allow_html=True)
            skill_chips = "".join(
                f'<span class="chip" style="background:{MINT_A}18;border-color:{MINT_A}44;color:{MINT_A};">{s}</span>'
                for s in ["Go", "PostgreSQL", "Kubernetes", "Distributed Systems"]
            )
            st.markdown(f"""
                <div class="showcase-profile">
                    <div style="font-family:'Space Grotesk'; font-weight:800; font-size:18px; color:#F4FFFA;">Aisha Rahman</div>
                    <div style="color:{MINT_A}; font-size:12.5px; margin-top:2px;">Senior Backend Engineer</div>
                    <div style="margin-top:12px;">{skill_chips}</div>
                    <div style="display:flex; gap:24px; margin-top:16px;">
                        <div><div class="showcase-mini-label">Interview</div><div class="showcase-mini-value" style="color:{MINT_A};">Live</div></div>
                        <div><div class="showcase-mini-label">Signals reviewed</div><div class="showcase-mini-value">3</div></div>
                        <div><div class="showcase-mini-label">Recruiter review</div><div class="showcase-mini-value" style="color:{GOLD};">Required</div></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with tab_scoring:
        scol1, scol2 = st.columns([1, 1.4], gap="medium")
        with scol1:
            st.markdown(f"""
                <div style="display:flex; flex-direction:column; align-items:center; gap:10px; padding:10px 0;">
                    <div class="score-ring" style="background: conic-gradient({MINT_A} 94%, rgba(255,255,255,0.14) 94% 100%);">
                        <div class="score-ring-inner" style="background:#0E241D;">
                            <div class="score-ring-value" style="color:{MINT_A};">94</div>
                            <div class="score-ring-unit" style="color:#9BB8AE;">/ 100</div>
                        </div>
                    </div>
                    <div class="score-band-pill" style="background:{MINT_A}18; color:{MINT_A}; border-color:{MINT_A}44;">AI-assisted match score</div>
                </div>
                """, unsafe_allow_html=True)
        with scol2:
            criteria = [("Skills", 96, MINT_A), ("Experience", 91, SIGNAL), ("Education", 88, VIOLET), ("Role alignment", 93, GOLD)]
            bars = "".join(f"""
                <div style="margin-bottom:12px;">
                    <div style="display:flex; justify-content:space-between; font-size:12px; color:#CFE8DF; margin-bottom:4px;">
                        <span>{name}</span><span style="font-weight:700; color:{c};">{v}%</span>
                    </div>
                    <div class="showcase-bar-track"><div class="showcase-bar-fill" style="width:{v}%; background:linear-gradient(90deg,{c}aa,{c});"></div></div>
                </div>
                """ for name, v, c in criteria)
            st.markdown(bars, unsafe_allow_html=True)
            st.caption("Illustrative weighting — real per-candidate breakdowns appear inside the app once you sign in.")

    with tab_interview:
        st.markdown(f"""
            <div class="showcase-terminal">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div style="font-family:'IBM Plex Mono'; font-size:11px; letter-spacing:1.5px; color:{MINT_A}; text-transform:uppercase;">◆ AI Interviewer</div>
                    <div style="display:flex; align-items:center; gap:6px; font-family:'IBM Plex Mono'; font-size:10.5px; color:#9BB8AE;">
                        <span style="width:7px;height:7px;border-radius:50%;background:#FF6B6B;box-shadow:0 0 0 4px rgba(255,107,107,0.25);"></span> LIVE
                    </div>
                </div>
                <div style="color:#F4FFFA; font-size:14px; margin-top:14px; line-height:1.6;">
                    "Walk me through a production outage you diagnosed under load."
                </div>
                <div style="color:#9BB8AE; font-size:12.5px; margin-top:10px; font-family:'IBM Plex Mono'; line-height:1.7;">
                    &gt; Candidate is responding — the transcript is captured live and reviewable after the interview ends.
                </div>
                <div style="display:flex; gap:24px; margin-top:18px;">
                    <div><div class="showcase-mini-label">Technical depth</div><div class="showcase-mini-value" style="color:{MINT_A};">92</div></div>
                    <div><div class="showcase-mini-label">Communication</div><div class="showcase-mini-value" style="color:{MINT_A};">88</div></div>
                    <div><div class="showcase-mini-label">Problem solving</div><div class="showcase-mini-value" style="color:{MINT_A};">95</div></div>
                </div>
                <div style="margin-top:16px; padding-top:14px; border-top:1px solid rgba(255,255,255,0.08); color:#9BB8AE; font-size:11.5px;">
                    Every signal here is a recommendation — a recruiter reviews the transcript and confirms before any decision.
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # /showcase-shell

    # ---- Trust ----
    st.markdown(
        '<div class="aperture-eyebrow" style="justify-content:center; margin-top:34px;">● Built for Accountable Hiring</div>'
        f'<div style="text-align:center; font-size:24px; font-weight:800; color:{INK}; '
        'font-family:\'Space Grotesk\'; margin-bottom:20px;">Trust, by design</div>',
        unsafe_allow_html=True,
    )
    trust_items = [
        ("🔍", "Explainable scoring", "Every score traces back to defined, weighted criteria tied to the job — never a black box."),
        ("🧑\u200d⚖️", "Human review required", "AI output is a recommendation. Recruiters see the full reasoning and make the final call."),
        ("🔐", "Role-isolated data", "Recruiter, candidate, and admin data are scoped by portal, with audit logging on admin actions."),
        ("⚙️", "Configurable criteria", "Scoring weights and required skills are set per job — not a fixed, opaque formula."),
    ]
    tcols = st.columns(4, gap="medium")
    for col, (icon, title, body) in zip(tcols, trust_items):
        with col:
            st.markdown(f"""
                <div class="glass-flat" style="height:100%;">
                    <div style="font-size:20px;">{icon}</div>
                    <div style="font-weight:800; font-size:13.5px; color:{INK}; margin-top:8px; font-family:'Space Grotesk';">{title}</div>
                    <div style="color:{MIST}; font-size:12px; margin-top:6px; line-height:1.55;">{body}</div>
                </div>
                """, unsafe_allow_html=True)


def landing_faq_section():
    """Objection-handling FAQ, wrapped so native st.expander picks up
    the elevated glass + shadow styling defined in .faq-wrap."""
    st.markdown(
        '<div class="aperture-eyebrow" style="justify-content:center; margin-top:36px;">● Before You Ask</div>'
        f'<div style="text-align:center; font-size:24px; font-weight:800; color:{INK}; '
        'font-family:\'Space Grotesk\'; margin-bottom:20px;">Straight answers, no fine print</div>',
        unsafe_allow_html=True,
    )
    faqs = [
        ("Does TalentOps replace recruiters?",
         "No. TalentOps screens and structures the first interview — recruiters review the scores, transcripts, and reasoning, and make every hiring decision themselves."),
        ("How does AI scoring work?",
         "Resumes are scored against the job on defined, weighted criteria — skills, experience, education, and role alignment — not open-ended judgment. The breakdown is visible, not a black box."),
        ("Can candidates request a human interview?",
         "Yes. The AI interview is a first-round step, not the only step — candidates can request a human interview at any point in their portal."),
        ("How is candidate data handled?",
         "Access is role-based and scoped by portal — recruiter, candidate, and admin data are kept separate, with audit logging on admin actions."),
        ("Can recruiters override AI scores?",
         "Yes. Every AI score and interview result is a recommendation, not a verdict — recruiters can review the full transcript and override any score or decision."),
        ("Does the AI interviewer introduce bias?",
         "Scoring runs on defined, weighted criteria tied to the job description. Every score is visible and reviewable by a human before it affects a candidate's status."),
        ("Can this replace or integrate with our existing ATS?",
         "It's built to run as a standalone hiring workflow — job postings, resume scoring, and interviews in one place — so you're not stitching together separate tools."),
        ("How long does setup take?",
         "Creating a recruiter account and posting your first job takes minutes — there's no setup call required to start screening resumes."),
    ]
    st.markdown('<div class="faq-wrap">', unsafe_allow_html=True)
    for q, a in faqs:
        with st.expander(q):
            st.markdown(f'<div style="color:{MIST}; font-size:13px; line-height:1.6;">{a}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def landing_terminal_cta(button_label="Enter Recruiter Portal →", key="terminal_cta_btn"):
    """Closing CTA panel styled like a dark 'terminal' surface with a
    perspective-warped grid for depth. Returns True the run the button
    is clicked, so the caller can drive session_state / st.rerun()."""
    st.markdown(f"""
        <div class="terminal-cta">
            <div class="terminal-shine"></div>
            <div class="terminal-cta-inner">
                <div style="font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:2px;
                    color:{MINT_A}; text-transform:uppercase; margin-bottom:14px;">◆ Ready When You Are</div>
                <div style="font-family:'Space Grotesk',sans-serif; font-size:28px; font-weight:800;
                    color:#FFFFFF; line-height:1.25; max-width:520px;">
                    Stop reading resumes.<br>Start reviewing decisions.
                </div>
                <div style="color:#CFF3E6; font-size:13px; margin-top:14px; max-width:440px; line-height:1.6;">
                    No setup calls required — create a recruiter account and post your first job in minutes.
                    Candidate and recruiter data stay isolated by design.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    _, btn_col, _ = st.columns([1, 1, 1])
    with btn_col:
        return st.button(button_label, use_container_width=True, type="primary", key=key)


def sidebar_logo():
    st.markdown(f"""
    <div class="glass sidebar-logo-card" style="padding: 22px 10px; text-align: center;">
        <div class="kpi-top-bar" style="--kpi-bar: linear-gradient(90deg, {MINT_C}00, {MINT_A}, {GOLD}, {SIGNAL}, {MINT_C}00);"></div>
        <div style="width: 54px; height: 54px; margin: auto; border-radius: 15px;
            background: linear-gradient(135deg, {MINT_A} 0%, {SIGNAL} 60%, {MINT_C} 100%);
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 8px 20px rgba(13,175,156,0.30);
            color: #06231C; font-size: 22px; font-weight: 800; font-family: 'Space Grotesk';
            animation: kpiIconGlow 2.6s ease-in-out infinite; --kpi-ring: {MINT_A}40;">
            &#11049;
        </div>
        <div style="margin-top: 13px; font-size: 18px; font-weight: 800; font-family: 'Space Grotesk'; color: {INK};">
            TalentOps <span style="color:{SIGNAL};">AI</span>
        </div>
        <div style="color: {MIST}; font-size: 11.5px; margin-top: 2px; letter-spacing: 0.4px;">
            Enterprise Hiring Intelligence
        </div>
    </div>
    """, unsafe_allow_html=True)


def sidebar_session(username, role_display, is_recruiter=True):
    """Premium replacement for the old plain-text 'Active Session' block:
    an avatar chip (first letter of the username), a live status dot,
    and a color-matched role pill -- teal for recruiters, gold for
    candidates -- inside the same glass-card language as the rest of
    the app."""
    initial = (username or "U").strip()[:1].upper() or "U"
    role_color = SIGNAL if is_recruiter else GOLD
    st.markdown(f"""
        <div class="glass-flat sidebar-session-card">
            <div style="display:flex; align-items:center; gap:12px;">
                <div style="position:relative; width:42px; height:42px; min-width:42px;">
                    <div style="width:42px; height:42px; border-radius:12px;
                        background: linear-gradient(135deg, {role_color}2e, {role_color}12);
                        border: 1px solid {role_color}40;
                        display:flex; align-items:center; justify-content:center;
                        font-family:'Space Grotesk'; font-weight:800; font-size:17px; color:{role_color};">
                        {initial}
                    </div>
                    <div style="position:absolute; right:-2px; bottom:-2px; width:11px; height:11px;
                        border-radius:50%; background:{VERDICT}; border:2px solid #FFFFFF;
                        box-shadow:0 0 0 3px {VERDICT}22;"></div>
                </div>
                <div style="min-width:0;">
                    <div style="font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:1.2px;
                        color:{MIST}; font-family:'IBM Plex Mono',monospace;">Active Session</div>
                    <div style="font-size:15px; font-weight:800; color:{INK}; margin-top:2px;
                        overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">{username}</div>
                </div>
            </div>
            <div style="margin-top:12px; display:inline-flex; align-items:center; gap:6px;
                padding:4px 11px; border-radius:999px; background:{role_color}14; border:1px solid {role_color}38;
                font-size:11px; font-weight:700; color:{role_color};">
                <span style="width:6px; height:6px; border-radius:50%; background:{role_color};"></span>
                {role_display}
            </div>
        </div>
        """, unsafe_allow_html=True)


def theme_toggle():
    """Night Mode switch -- shared by both the recruiter and candidate
    sidebars (called once, before the role branch, in app.py) so either
    portal can flip the whole app into the dark 'glass in space' theme
    from the reference screenshot. State lives in st.session_state, so
    it persists across reruns/page changes for the rest of the session."""
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    is_dark = st.session_state.dark_mode
    label = "🌙 Night Mode" if not is_dark else "☀️ Day Mode"
    if st.button(label, key="theme_toggle_btn", use_container_width=True):
        st.session_state.dark_mode = not is_dark
        st.rerun()


def page_title(title, subtitle):
    st.markdown(f"""
    <div class="glass" style="padding: 22px 26px; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="font-size: 26px; font-weight: 800; font-family: 'Space Grotesk'; color: {INK};">{title}</div>
            <div style="margin-top: 4px; color: {MIST}; font-size: 13px;">{subtitle}</div>
        </div>
        <div style="padding: 7px 16px; background: linear-gradient(90deg, {SIGNAL}14, {GOLD}12);
            border: 1px solid {LINE}; border-radius: 999px; color: {MINT_C}; font-weight: 700;
            font-size: 11px; font-family: 'IBM Plex Mono'; letter-spacing: 1px; white-space: nowrap;">
            &#11049; PRO CORE
        </div>
    </div>
    """, unsafe_allow_html=True)


def metric_card(title, value, icon="📊", color=None, trend=None):
    """trend: optional short string like '+12% this week' shown under the value.

    Card is fully color-matched to `color`: tinted glass background, a
    moving glow bar along the top edge, a diagonal shine sweep, and a
    pulsing ring around the icon -- all driven by CSS custom properties
    set inline below, so one shared stylesheet ruleset (see .kpi-card
    in load_css) animates every KPI card on every page consistently.
    """
    color = color or SIGNAL
    trend_html = (
        f'<div class="kpi-value" style="font-size:11px; color:{color}; font-weight:600; margin-top:6px;">{trend}</div>'
        if trend else ""
    )
    card_vars = (
        f"--kpi-bg: linear-gradient(160deg, {color}14 0%, #FFFFFF 55%, {color}0A 100%); "
        f"--kpi-border: {color}35; "
        f"--kpi-shadow: 0 10px 28px 0 {color}1f; "
        f"--kpi-shadow-hover: 0 18px 42px 0 {color}30; "
        f"--kpi-bar: linear-gradient(90deg, {color}00, {color}, {GOLD}, {color}, {color}00); "
        f"--kpi-sheen: {color}2e; "
        f"--kpi-icon-bg: linear-gradient(135deg, {color}30, {color}10); "
        f"--kpi-ring: {color}30; "
        f"--kpi-solid: {color};"
    )
    st.markdown(f"""
        <div class="kpi-card" style="{card_vars}">
            <div class="kpi-top-bar"></div>
            <div class="kpi-shine"></div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <div class="kpi-icon">{icon}</div>
                <div class="kpi-dot"></div>
            </div>
            <div class="kpi-value" style="font-size: 11px; color: {MIST}; font-weight: 700; text-transform: uppercase; letter-spacing: 0.6px;">
                {title}
            </div>
            <div class="kpi-value" style="font-size: 28px; font-weight: 800; font-family: 'Space Grotesk', sans-serif; color: {color}; margin-top: 4px; text-shadow: 0 0 22px {color}2a;">
                {value}
            </div>
            {trend_html}
        </div>
        """, unsafe_allow_html=True)


def welcome_hero(username, subtitle=None, primary_label=None, primary_nav=None,
                  secondary_label=None, secondary_nav=None):
    """Big greeting banner ('Welcome, {username}!') for the top of the
    dashboard, in the style of the reference 'AI Recruitment Copilot'
    layout. `primary_nav`/`secondary_nav` are page labels — if given,
    the buttons stash a `_qa_nav` redirect the same way the existing
    Quick Actions panel does."""
    subtitle = subtitle or "Your AI Recruitment Copilot is ready to find, evaluate and hire the best talent."
    st.markdown(f"""
        <div class="hero-welcome">
            <div class="hero-welcome-orb"></div>
            <div class="hero-badge" style="margin-bottom:14px;"><span class="hero-dot"></span> Live Pipeline</div>
            <div style="position:relative; font-family:'Space Grotesk',sans-serif; font-size: 27px;
                font-weight: 800; letter-spacing: -0.5px; color:{INK};">
                Welcome, {username}!
            </div>
            <div style="position:relative; font-size: 13.5px; color: {MIST}; margin-top: 6px; max-width:640px;">
                {subtitle}
            </div>
        </div>
        """, unsafe_allow_html=True)

    if primary_label or secondary_label:
        st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
        bcols = st.columns([1, 1, 3]) if secondary_label else st.columns([1, 3])
        if primary_label:
            with bcols[0]:
                if st.button(primary_label, use_container_width=True, key="hero_primary_btn"):
                    if primary_nav:
                        st.session_state["_qa_nav"] = primary_nav
                        st.rerun()
        if secondary_label:
            with bcols[1]:
                if st.button(secondary_label, use_container_width=True, key="hero_secondary_btn"):
                    if secondary_nav:
                        st.session_state["_qa_nav"] = secondary_nav
                        st.rerun()


def ats_donut(buckets, colors, total, center_label="Total Candidates"):
    """Pure-CSS conic-gradient donut + legend, replacing the old Plotly
    pie so the ATS Score Distribution card matches the reference layout
    exactly and never needs separate dark-mode chart theming.

    buckets: dict {label: count}, in the order they should appear.
    colors:  list of hex colors, same length/order as buckets.
    total:   sum shown in the donut's center.
    """
    if total <= 0:
        st.markdown(f'<div style="color:{MIST}; font-size:13px; padding:8px 0;">No candidates processed yet — the distribution will appear here once resumes are scored.</div>', unsafe_allow_html=True)
        return

    stops = []
    running = 0.0
    for (label, count), color in zip(buckets.items(), colors):
        start_pct = (running / total) * 100
        running += count
        end_pct = (running / total) * 100
        stops.append(f"{color} {start_pct:.2f}% {end_pct:.2f}%")
    conic = ", ".join(stops)

    legend_rows = ""
    for (label, count), color in zip(buckets.items(), colors):
        pct = round((count / total) * 100)
        legend_rows += (
            f'<div><span class="dot" style="background:{color};"></span>'
            f'{label} <span class="pct">· {pct}%</span></div>'
        )

    st.markdown(f"""
        <div class="ats-donut-wrap">
            <div class="ats-donut" style="background: conic-gradient({conic});">
                <div class="ats-donut-inner">
                    <div class="ats-donut-value">{total}</div>
                    <div class="ats-donut-label">{center_label}</div>
                </div>
            </div>
            <div class="ats-legend">{legend_rows}</div>
        </div>
        """, unsafe_allow_html=True)


def ats_score_card(score, decision=None, confidence=None, matched_skills=None,
                    missing_skills=None, job_role=None, show_evidence=True):
    """Single-candidate ATS match score: a circular conic-gradient ring
    (banded to the same 85/70/50 thresholds used everywhere else in the
    app) plus decision/confidence facts, and an optional expandable
    'How this score was calculated' panel.

    Deliberately shows only what the ATS engine actually returns --
    matched/missing skills as evidence -- never a fabricated weighted
    breakdown (skills/experience/education % splits) the engine doesn't
    compute. Labeled "AI-assisted match score" rather than a verdict,
    per the product-language guidance: this is decision support, not
    an automated hire/reject call.

    score:           0-100 int/float.
    decision, confidence: optional strings from generate_recommendation().
    matched_skills, missing_skills: optional lists of strings.
    job_role:        optional target-role label shown under the eyebrow.
    show_evidence:   set False when the caller already renders matched/
                      missing skill lists elsewhere (e.g. full_report_modal)
                      to avoid showing the same evidence twice.
    """
    try:
        score = int(round(float(score or 0)))
    except (TypeError, ValueError):
        score = 0
    score = max(0, min(100, score))

    matched_skills = [s.strip() for s in (matched_skills or []) if s and s.strip()]
    missing_skills = [s.strip() for s in (missing_skills or []) if s and s.strip()]

    if score >= 85:
        band_color, band_label = VERDICT, "Highly Recommended"
    elif score >= 70:
        band_color, band_label = SIGNAL, "Recommended"
    elif score >= 50:
        band_color, band_label = CAUTION, "Consider"
    else:
        band_color, band_label = RISK, "Not Recommended"

    role_line = (
        f'<div style="color:{MIST}; font-size:12.5px; margin-top:2px;">'
        f'Target role: <span style="color:{SIGNAL}; font-weight:600;">{job_role}</span></div>'
        if job_role else ""
    )

    facts = ""
    if decision:
        facts += (
            f'<div class="score-fact"><span class="score-fact-label">Decision</span>'
            f'<span class="score-fact-value" style="color:{band_color};">{decision}</span></div>'
        )
    if confidence:
        facts += (
            f'<div class="score-fact"><span class="score-fact-label">Confidence</span>'
            f'<span class="score-fact-value">{confidence}</span></div>'
        )

    # Neutral track color (not theme-swapped) so the ring reads correctly
    # on both light glass and dark panel surfaces without needing the
    # inline conic-gradient itself to be repainted per-theme.
    track = "rgba(148,163,160,0.25)"

    st.markdown(f"""
        <div class="glass score-card">
            <div class="score-ring-col">
                <div class="score-ring" style="background: conic-gradient({band_color} {score}%, {track} {score}% 100%);">
                    <div class="score-ring-inner">
                        <div class="score-ring-value" style="color:{band_color};">{score}</div>
                        <div class="score-ring-unit">/ 100</div>
                    </div>
                </div>
                <div class="score-band-pill" style="background:{band_color}18; color:{band_color}; border-color:{band_color}44;">{band_label}</div>
            </div>
            <div class="score-detail-col">
                <div class="aperture-eyebrow" style="margin:0 0 6px 0;">AI-assisted match score</div>
                {role_line}
                <div class="score-facts">{facts}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    if show_evidence and (matched_skills or missing_skills):
        with st.expander("How this score was calculated", expanded=False):
            st.caption(
                "Evidence detected by the resume parser and skill matcher — "
                "not a guarantee of fit. A human reviewer should confirm "
                "before any hiring decision."
            )
            ev1, ev2 = st.columns(2)
            with ev1:
                st.markdown(
                    f'<div style="font-weight:700; font-size:12.5px; color:{VERDICT}; margin-bottom:6px;">'
                    f'✓ Matched — evidence found</div>', unsafe_allow_html=True
                )
                chip_list(matched_skills, VERDICT)
            with ev2:
                st.markdown(
                    f'<div style="font-weight:700; font-size:12.5px; color:{RISK}; margin-bottom:6px;">'
                    f'✕ Missing — not detected</div>', unsafe_allow_html=True
                )
                chip_list(missing_skills, RISK)


def pipeline_funnel(stages):
    """stages: list of (label, count, color) tuples, widest/first stage
    first. Each bar's width is scaled relative to the first stage's
    count so the funnel visually tapers."""
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown(
        f'<div style="font-size:16px; font-weight:800; color:{INK}; font-family:\'Space Grotesk\'; margin-bottom:16px;">'
        f'🧭 Hiring Pipeline</div>',
        unsafe_allow_html=True,
    )
    base = max((s[1] for s in stages), default=0) or 1
    rows = ""
    for label, count, color in stages:
        pct = max(4, round((count / base) * 100))
        rows += f"""
        <div class="funnel-row">
            <div class="funnel-label"><span>{label}</span><b>{count}</b></div>
            <div class="funnel-track"><div class="funnel-fill" style="width:{pct}%; background:linear-gradient(90deg, {color}AA, {color});"></div></div>
        </div>
        """
    st.markdown(rows, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def pipeline_stepper(stages, rejected_count=0, rejected_label="Rejected"):
    """stages: list of (icon, label, count, color) tuples, in pipeline
    order. Renders a horizontal stepper -- circular icon nodes joined
    by arrows -- with a separate small Rejected card underneath, in
    the style of the candidate Overview reference layout.

    Every HTML chunk below is emitted as a SINGLE-LINE string in its
    own st.markdown call. Streamlit's markdown parser treats a run of
    HTML as a raw passthrough block only until it hits a blank (or
    whitespace-only) line -- after that it reverts to normal Markdown
    rules, and any line indented 4+ spaces gets rendered as a literal
    code block instead of HTML. Pretty-printed multi-line f-strings
    are exactly how that blank line sneaks in, so everything here is
    built as one line per call."""
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown(
        f'<div style="font-size:16px; font-weight:800; color:{INK}; font-family:\'Space Grotesk\'; margin-bottom:14px;">🧭 Application Pipeline</div>',
        unsafe_allow_html=True,
    )
    nodes = ""
    for i, (icon, label, count, color) in enumerate(stages):
        nodes += (
            f'<div class="stepper-node">'
            f'<div class="stepper-circle" style="background:{color}18; border-color:{color}55; color:{color};">{icon}</div>'
            f'<div class="stepper-label">{label}</div>'
            f'<div class="stepper-count">{count}</div>'
            f'</div>'
        )
        if i < len(stages) - 1:
            nodes += '<div class="stepper-arrow">&#8594;</div>'
    st.markdown(f'<div class="stepper-row">{nodes}</div>', unsafe_allow_html=True)
    if rejected_count:
        st.markdown(
            f'<div class="rejected-mini-card">'
            f'<div class="stepper-circle" style="width:38px; height:38px; font-size:15px; '
            f'background:{RISK}18; border-color:{RISK}55; color:{RISK}; margin-bottom:0;">❌</div>'
            f'<div><div style="font-weight:800; color:{INK}; font-size:13px;">{rejected_label}</div>'
            f'<div style="color:{MIST}; font-size:11px;">{rejected_count} application(s)</div></div>'
            f'</div>',
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)


def dashboard_list_row(icon, icon_color, title, subtitle, badge_text=None, badge_color=None):
    """Builds one row of HTML for a dashboard_list_card — icon chip on
    the left, title/subtitle in the middle, an optional status pill on
    the right. Emitted as one continuous line (no embedded newlines) so
    concatenating many of these never introduces a blank line that
    would break Streamlit's HTML passthrough (see pipeline_stepper's
    docstring for why that matters)."""
    badge = ""
    if badge_text:
        bc = badge_color or SIGNAL
        badge = (
            f'<span class="list-row-badge" style="background:{bc}18; color:{bc}; border-color:{bc}44;">'
            f'{badge_text}</span>'
        )
    return (
        f'<div class="list-row">'
        f'<div class="list-row-icon" style="background:{icon_color}18; color:{icon_color};">{icon}</div>'
        f'<div class="list-row-text">'
        f'<div class="list-row-title">{title}</div>'
        f'<div class="list-row-sub">{subtitle}</div>'
        f'</div>{badge}</div>'
    )


def dashboard_list_card(icon, title, rows_html="", view_all=True, empty_text="Nothing here yet.", footer_label=None):
    """Small dashboard card used for Recent Activity / Upcoming
    Interviews / Messages from Recruiters / Recent Applications --
    a header (with an optional 'View All' label), a stack of
    dashboard_list_row rows, and an optional footer link label.

    Each section is its own st.markdown call (matching the pattern
    already used by list_card/insight_list elsewhere in this file)
    rather than one big pretty-printed f-string -- that's what keeps
    the footer link from ever landing after a blank line and getting
    rendered as a literal code block."""
    st.markdown(f'<div class="glass" style="padding:20px 22px; height:100%;">', unsafe_allow_html=True)
    header_right = '<span class="view-all-link">View All</span>' if view_all else ""
    st.markdown(
        f'<div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">'
        f'<div style="font-size:15px; font-weight:800; color:{INK}; font-family:\'Space Grotesk\';">{icon} &nbsp;{title}</div>'
        f'{header_right}</div>',
        unsafe_allow_html=True,
    )
    if rows_html:
        st.markdown(rows_html, unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="color:{MIST}; font-size:12.5px; padding:10px 0;">{empty_text}</div>', unsafe_allow_html=True)
    if footer_label:
        st.markdown(f'<div class="card-footer-link">{footer_label} &nbsp;&rarr;</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def quote_card(text):
    """Small italic quote card that sits beside the welcome banner on
    the candidate Overview page."""
    st.markdown(
        f'<div class="glass quote-card"><div class="quote-card-text">&#8220;{text}&#8221;</div></div>',
        unsafe_allow_html=True,
    )


def skill_demand_bars(skills, color=None):
    """skills: list of (skill_name, count) tuples, already sorted
    highest-demand first (e.g. from database.top_skills())."""
    color = color or SIGNAL
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown(
        f'<div style="font-size:16px; font-weight:800; color:{INK}; font-family:\'Space Grotesk\'; margin-bottom:16px;">'
        f'🧩 Skill Demand</div>',
        unsafe_allow_html=True,
    )
    if not skills:
        st.markdown(f'<div style="color:{MIST}; font-size:13px;">No skills recorded yet.</div>', unsafe_allow_html=True)
    else:
        base = max((c for _, c in skills), default=0) or 1
        rows = ""
        for name, count in skills:
            pct = max(4, round((count / base) * 100))
            rows += f"""
            <div class="skill-row">
                <div class="skill-label"><span>{name}</span><span>{count}</span></div>
                <div class="skill-track"><div class="skill-fill" style="width:{pct}%; background:{color};"></div></div>
            </div>
            """
        st.markdown(rows, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def recent_candidates_mini(rows):
    """rows: list of dicts with name, job_role, ats_score keys (as
    returned by database.get_candidates())."""
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown(
        f'<div style="font-size:16px; font-weight:800; color:{INK}; font-family:\'Space Grotesk\'; margin-bottom:6px;">'
        f'🕒 Recent Candidates</div>',
        unsafe_allow_html=True,
    )
    if not rows:
        st.markdown(f'<div style="color:{MIST}; font-size:13px; padding:8px 0;">No candidates processed yet.</div>', unsafe_allow_html=True)
    else:
        body = ""
        for c in rows:
            score = c.get("ats_score") or 0
            if score >= 85:
                badge_color, badge_text = VERDICT, "Highly Recommended"
            elif score >= 70:
                badge_color, badge_text = SIGNAL, "Recommended"
            elif score >= 50:
                badge_color, badge_text = CAUTION, "Consider"
            else:
                badge_color, badge_text = RISK, "Not Recommended"
            body += f"""
            <div class="mini-row">
                <div>
                    <div class="mini-name">{c.get('name','—')}</div>
                    <div class="mini-sub">{c.get('job_role','—')}</div>
                </div>
                <div style="display:flex; align-items:center; gap:10px;">
                    <div style="font-family:'Space Grotesk'; font-weight:800; color:{INK}; font-size:14px;">{score}%</div>
                    <div class="mini-badge" style="background:{badge_color}18; color:{badge_color}; border:1px solid {badge_color}40;">{badge_text}</div>
                </div>
            </div>
            """
        st.markdown(body, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def insight_list(items):
    """items: list of (icon, text, color) tuples — short, real,
    data-derived observations (not fabricated AI copy)."""
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown(
        f'<div style="font-size:16px; font-weight:800; color:{INK}; font-family:\'Space Grotesk\'; margin-bottom:12px;">'
        f'✨ Recent Insights</div>',
        unsafe_allow_html=True,
    )
    if not items:
        st.markdown(f'<div style="color:{MIST}; font-size:13px;">Nothing to report yet.</div>', unsafe_allow_html=True)
    else:
        rows = ""
        for icon, text, color in items:
            rows += f"""
            <div class="insight-row">
                <div style="font-size:15px;">{icon}</div>
                <div style="color:{INK_SOFT};">{text}</div>
            </div>
            """
        st.markdown(rows, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


def copilot_panel():
    """Decorative panel matching the reference layout's 'AI Copilot' box.
    Not wired to a live assistant — purely a visual placeholder, labeled
    honestly so it doesn't imply a working chat feature."""
    st.markdown(f"""
        <div class="glass copilot-card">
            <div style="display:flex; align-items:center; justify-content:space-between;">
                <div style="font-size:16px; font-weight:800; color:{INK}; font-family:'Space Grotesk';">🧠 AI Copilot</div>
                <div style="font-size:10.5px; color:{MIST}; font-family:'IBM Plex Mono';">PREVIEW</div>
            </div>
            <div style="font-size:12.5px; color:{MIST}; margin-top:8px; line-height:1.5;">
                Ask anything about candidates, ATS scoring, or hiring trends.
            </div>
            <div class="copilot-input-mock">
                <span>Ask AI Copilot…</span>
                <span>➤</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


def profile_field(label, value, icon="•"):
    display_value = value if value else "—"
    st.markdown(f"""
        <div class="profile-field">
            <div class="profile-field-label">{icon} &nbsp;{label}</div>
            <div class="profile-field-value">{display_value}</div>
        </div>
        """, unsafe_allow_html=True)


def chip_list(items, color=None):
    color = color or SIGNAL
    items = [i.strip() for i in items if i and i.strip()]
    if not items:
        st.markdown(f'<div style="color:{MIST}; font-size: 13px;">No items detected.</div>',
                    unsafe_allow_html=True)
        return
    chips_html = "".join(
        f'<span class="chip" style="background:{color}16; border-color:{color}44; color:{color};">{item}</span>'
        for item in items
    )
    st.markdown(f'<div style="margin: 6px 0 4px 0;">{chips_html}</div>', unsafe_allow_html=True)


def list_card(title, items, icon="•", color=None):
    color = color or SIGNAL
    if items:
        rows = "".join(f'<div class="list-card-item">• {item}</div>' for item in items)
    else:
        rows = f'<div class="list-card-item" style="color:{MIST};">None detected</div>'

    st.markdown(f"""
        <div class="glass" style="padding: 18px 20px;">
            <div style="font-size: 14px; font-weight: 700; color: {color}; margin-bottom: 10px;">
                {icon} &nbsp;{title}
            </div>
            {rows}
        </div>
        """, unsafe_allow_html=True)


def section_header(icon, title, subtitle=None):
    """Lightweight inline section header, lighter than page_title's hero card."""
    sub = f'<div style="color:{MIST}; font-size:12.5px; margin-top:2px;">{subtitle}</div>' if subtitle else ""
    st.markdown(f"""
        <div style="display:flex; align-items:center; gap:12px; margin: 4px 0 14px 0;">
            <div style="width:38px; height:38px; border-radius:11px; background:{SIGNAL}16;
                display:flex; align-items:center; justify-content:center; font-size:17px;">{icon}</div>
            <div>
                <div style="font-size:16px; font-weight:800; color:{INK}; font-family:'Space Grotesk';">{title}</div>
                {sub}
            </div>
        </div>
        """, unsafe_allow_html=True)


def full_report_modal(details, ats_result, recommendation, job_role):
    """
    Full candidate report. Uses st.dialog when available (Streamlit >= 1.31);
    falls back to an inline expander on older Streamlit versions.
    """
    def _render():
        ats_score_card(
            ats_result["ats"],
            decision=recommendation.get("decision"),
            confidence=recommendation.get("confidence"),
            matched_skills=ats_result.get("matched_skills", []),
            missing_skills=ats_result.get("missing_skills", []),
            job_role=job_role,
            show_evidence=False,  # matched/missing already shown below
        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Candidate Details**")
        profile_field("Full Name", details.get("name", ""), "👤")
        profile_field("Email", details.get("email", ""), "✉")
        profile_field("Phone", details.get("phone", ""), "📞")
        profile_field("Education", details.get("education", ""), "🎓")
        profile_field("Experience", details.get("experience", ""), "🧭")

        st.markdown("**Matched Skills**")
        chip_list(ats_result.get("matched_skills", []), VERDICT)

        st.markdown("**Missing Skills**")
        chip_list(ats_result.get("missing_skills", []), RISK)

        list_card("Projects", details.get("projects", []), "🧩", SIGNAL)
        list_card("Certifications", details.get("certifications", []), "🎓", VERDICT)

    if hasattr(st, "dialog"):
        @st.dialog(f"Full Analysis Report — {details.get('name', 'Candidate')}", width="large")
        def _modal():
            _render()
        _modal()
    else:
        with st.expander(f"📊 Full Analysis Report — {details.get('name', 'Candidate')}", expanded=True):
            _render()


def footer():
    st.markdown(f"""
    <div style="margin-top: 44px; padding: 18px; text-align: center; border-top: 1px solid {LINE};
        color: {MIST}; font-size: 11px; font-family: 'IBM Plex Mono';">
        &#11049; TALENTOPS AI &nbsp;•&nbsp; POLISHED MINT EDITION &nbsp;•&nbsp; ENTERPRISE INTELLIGENCE NETWORK ENGINE
v style="font-size:16px; font-weight:800; color:{INK}; font-family:'Space Grotesk';">{title}</div>
                {sub}
            </div>
        </div>
        """, unsafe_allow_html=True)


def full_report_modal(details, ats_result, recommendation, job_role):
    """
    Full candidate report. Uses st.dialog when available (Streamlit >= 1.31);
    falls back to an inline expander on older Streamlit versions.
    """
    def _render():
        ats_score_card(
            ats_result["ats"],
            decision=recommendation.get("decision"),
            confidence=recommendation.get("confidence"),
            matched_skills=ats_result.get("matched_skills", []),
            missing_skills=ats_result.get("missing_skills", []),
            job_role=job_role,
            show_evidence=False,  # matched/missing already shown below
        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Candidate Details**")
        profile_field("Full Name", details.get("name", ""), "👤")
        profile_field("Email", details.get("email", ""), "✉")
        profile_field("Phone", details.get("phone", ""), "📞")
        profile_field("Education", details.get("education", ""), "🎓")
        profile_field("Experience", details.get("experience", ""), "🧭")

        st.markdown("**Matched Skills**")
        chip_list(ats_result.get("matched_skills", []), VERDICT)

        st.markdown("**Missing Skills**")
        chip_list(ats_result.get("missing_skills", []), RISK)

        list_card("Projects", details.get("projects", []), "🧩", SIGNAL)
        list_card("Certifications", details.get("certifications", []), "🎓", VERDICT)

    if hasattr(st, "dialog"):
        @st.dialog(f"Full Analysis Report — {details.get('name', 'Candidate')}", width="large")
        def _modal():
            _render()
        _modal()
    else:
        with st.expander(f"📊 Full Analysis Report — {details.get('name', 'Candidate')}", expanded=True):
            _render()


def footer():
    st.markdown(f"""
    <div style="margin-top: 44px; padding: 18px; text-align: center; border-top: 1px solid {LINE};
        color: {MIST}; font-size: 11px; font-family: 'IBM Plex Mono';">
        &#11049; TALENTOPS AI &nbsp;•&nbsp; POLISHED MINT EDITION &nbsp;•&nbsp; ENTERPRISE INTELLIGENCE NETWORK ENGINE
    </div>
    """, unsafe_allow_html=True)

import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Traffic Monitor",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* ------------------------------
       MAIN BACKGROUND
    ------------------------------ */

    .stApp {
        background: #0b1120;
        color: #f8fafc;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }


    /* ------------------------------
       SIDEBAR
    ------------------------------ */

    section[data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #1f2937;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }


    /* ------------------------------
       SIDEBAR TITLE
    ------------------------------ */

    .sidebar-title {
        font-size: 22px;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 5px;
    }

    .sidebar-subtitle {
        font-size: 13px;
        color: #94a3b8;
        margin-bottom: 25px;
    }


    /* ------------------------------
       HEADER
    ------------------------------ */

    .dashboard-header {
        background: linear-gradient(
            135deg,
            #111827,
            #172554
        );

        border: 1px solid #1e3a8a;
        border-radius: 18px;

        padding: 28px 32px;
        margin-bottom: 25px;

        box-shadow: 0 10px 30px rgba(0,0,0,0.25);
    }

    .dashboard-title {
        font-size: 36px;
        font-weight: 800;
        color: #f8fafc;
        margin: 0;
    }

    .dashboard-subtitle {
        font-size: 15px;
        color: #94a3b8;
        margin-top: 8px;
    }

    .status-badge {
        display: inline-block;

        margin-top: 15px;
        padding: 7px 14px;

        border-radius: 20px;

        background: #064e3b;
        color: #6ee7b7;

        font-size: 13px;
        font-weight: 600;
    }


    /* ------------------------------
       SECTION TITLES
    ------------------------------ */

    .section-title {
        font-size: 21px;
        font-weight: 700;

        color: #f8fafc;

        margin-top: 25px;
        margin-bottom: 15px;
    }


    /* ------------------------------
       METRIC CARDS
    ------------------------------ */

    .metric-card {
        background: #111827;

        border: 1px solid #1f2937;

        border-radius: 16px;

        padding: 22px;

        min-height: 125px;

        box-shadow: 0 8px 25px rgba(0,0,0,0.18);

        transition: 0.2s;
    }

    .metric-card:hover {
        border-color: #3b82f6;
        transform: translateY(-2px);
    }

    .metric-icon {
        font-size: 26px;
    }

    .metric-title {
        color: #94a3b8;

        font-size: 13px;

        margin-top: 8px;
    }

    .metric-value {
        color: #f8fafc;

        font-size: 30px;

        font-weight: 800;

        margin-top: 3px;
    }

    .metric-description {
        color: #64748b;

        font-size: 12px;

        margin-top: 5px;
    }


    /* ------------------------------
       VIDEO CONTAINER
    ------------------------------ */

    .video-card {
        background: #111827;

        border: 1px solid #1f2937;

        border-radius: 18px;

        padding: 18px;

        box-shadow: 0 8px 25px rgba(0,0,0,0.18);
    }


    /* ------------------------------
       STATUS CARD
    ------------------------------ */

    .traffic-status {
        background: linear-gradient(
            135deg,
            #064e3b,
            #065f46
        );

        border: 1px solid #047857;

        border-radius: 16px;

        padding: 22px;

        margin-top: 15px;
    }

    .traffic-status-title {
        color: #a7f3d0;

        font-size: 13px;

        font-weight: 600;
    }

    .traffic-status-value {
        color: #ecfdf5;

        font-size: 28px;

        font-weight: 800;

        margin-top: 5px;
    }


    /* ------------------------------
       FILE UPLOADER
    ------------------------------ */

    div[data-testid="stFileUploader"] {
        background: #0f172a;

        border: 1px dashed #334155;

        border-radius: 14px;

        padding: 10px;
    }


    /* ------------------------------
       BUTTON
    ------------------------------ */

    .stButton > button {
        width: 100%;

        background: #2563eb;

        color: white;

        border: none;

        border-radius: 10px;

        padding: 10px 20px;

        font-weight: 600;

        transition: 0.2s;
    }

    .stButton > button:hover {
        background: #1d4ed8;

        border: none;

        transform: translateY(-1px);
    }


    /* ------------------------------
       FOOTER
    ------------------------------ */

    .footer {
        text-align: center;

        color: #64748b;

        font-size: 12px;

        margin-top: 45px;

        padding-top: 20px;

        border-top: 1px solid #1f2937;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🚦 Traffic AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">'
        'AI-powered traffic monitoring'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 🎥 Video Input")

    uploaded_video = st.file_uploader(
        "Upload traffic video",
        type=["mp4", "avi", "mov"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("### ⚙️ System")

    st.write("🧠 AI Model")
    st.caption("YOLO")

    st.write("📹 Video Processing")
    st.caption("OpenCV")

    st.write("📊 Analytics")
    st.caption("Pandas + Plotly")

    st.markdown("---")

    st.caption("AI Traffic Monitoring v1.0")


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="dashboard-header">

    <div class="dashboard-title">
        🚦 AI Traffic Monitoring System
    </div>

    <div class="dashboard-subtitle">
        Intelligent vehicle detection, tracking and traffic analytics
        using computer vision.
    </div>

    <div class="status-badge">
        ● SYSTEM ONLINE
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# VIDEO SECTION
# ============================================================

st.markdown(
    '<div class="section-title">🎥 Traffic Video</div>',
    unsafe_allow_html=True
)

if uploaded_video:

    st.markdown(
        '<div class="video-card">',
        unsafe_allow_html=True
    )

    st.video(uploaded_video)

    st.markdown("</div>", unsafe_allow_html=True)

else:

    st.info(
        "Upload a traffic video using the sidebar to begin analysis."
    )


# ============================================================
# STATISTICS
# ============================================================

st.markdown(
    '<div class="section-title">📊 Traffic Overview</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown("""
    <div class="metric-card">

        <div class="metric-icon">🚗</div>

        <div class="metric-title">
            CARS
        </div>

        <div class="metric-value">
            0
        </div>

        <div class="metric-description">
            Detected vehicles
        </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="metric-card">

        <div class="metric-icon">🏍️</div>

        <div class="metric-title">
            MOTORCYCLES
        </div>

        <div class="metric-value">
            0
        </div>

        <div class="metric-description">
            Detected vehicles
        </div>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="metric-card">

        <div class="metric-icon">🚌</div>

        <div class="metric-title">
            BUSES
        </div>

        <div class="metric-value">
            0
        </div>

        <div class="metric-description">
            Detected vehicles
        </div>

    </div>
    """, unsafe_allow_html=True)


with col4:

    st.markdown("""
    <div class="metric-card">

        <div class="metric-icon">🚚</div>

        <div class="metric-title">
            TRUCKS
        </div>

        <div class="metric-value">
            0
        </div>

        <div class="metric-description">
            Detected vehicles
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# TRAFFIC STATUS
# ============================================================

st.markdown(
    '<div class="section-title">🚦 Traffic Condition</div>',
    unsafe_allow_html=True
)


st.markdown("""
<div class="traffic-status">

    <div class="traffic-status-title">
        CURRENT TRAFFIC LEVEL
    </div>

    <div class="traffic-status-value">
        Waiting for analysis
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# ANALYTICS PLACEHOLDER
# ============================================================

st.markdown(
    '<div class="section-title">📈 Traffic Analytics</div>',
    unsafe_allow_html=True
)


chart_col1, chart_col2 = st.columns(2)


with chart_col1:

    st.markdown(
        '<div class="video-card">',
        unsafe_allow_html=True
    )

    st.subheader("Vehicle Distribution")

    st.info(
        "Vehicle distribution chart will appear here "
        "after YOLO analysis is connected."
    )

    st.markdown("</div>", unsafe_allow_html=True)


with chart_col2:

    st.markdown(
        '<div class="video-card">',
        unsafe_allow_html=True
    )

    st.subheader("Traffic Over Time")

    st.info(
        "Traffic timeline will appear here "
        "after video processing is connected."
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    AI Traffic Monitoring System
    <br>
    Computer Vision • YOLO • OpenCV • Streamlit

</div>
""", unsafe_allow_html=True)
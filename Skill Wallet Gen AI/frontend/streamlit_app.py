import streamlit as st
import requests
from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


# ==============================
# Backend API URL
# ==============================

API_URL = "http://127.0.0.1:8000"


# ==============================
# PDF Generator
# ==============================

def create_pdf(topics, suggestions):

    buffer = BytesIO()

    document = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = []


    content.append(
        Paragraph(
            "Personalized Networking Assistant Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )


    content.append(
        Paragraph(
            "Detected Topics",
            styles["Heading2"]
        )
    )


    for topic in topics:

        content.append(
            Paragraph(
                f"• {topic}",
                styles["BodyText"]
            )
        )


    content.append(
        Spacer(1,20)
    )


    content.append(
        Paragraph(
            "Conversation Starters",
            styles["Heading2"]
        )
    )


    for suggestion in suggestions:

        content.append(
            Paragraph(
                f"• {suggestion}",
                styles["BodyText"]
            )
        )


    document.build(content)

    buffer.seek(0)

    return buffer



# ==============================
# Page Configuration
# ==============================

st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝",
    layout="wide"
)



# ==============================
# Session State
# ==============================

if "topics" not in st.session_state:
    st.session_state.topics = []


if "suggestions" not in st.session_state:
    st.session_state.suggestions = []



# ==============================
# Styling
# ==============================

st.markdown(
"""
<style>

.topic-card{

background:#1f2937;

color:white;

padding:15px;

border-radius:10px;

margin-bottom:10px;

font-weight:bold;

border-left:5px solid #3b82f6;

}


.suggestion-card{

background:#1f2937;

color:white;

padding:15px;

border-radius:10px;

margin-bottom:10px;

border-left:5px solid #3b82f6;

}


.fact-box{

background:#fef9c3;

color:#111827;

padding:15px;

border-radius:10px;

font-size:17px;

}


.hero-container{
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    padding:40px;
    border-radius:20px;
    color:white;
    margin-bottom:30px;
    box-shadow:0 8px 24px rgba(0,0,0,0.2);
}

.hero-title{
    font-size:42px;
    font-weight:700;
    margin-bottom:10px;
}

.hero-subtitle{
    font-size:18px;
    opacity:0.95;
    margin-bottom:20px;
}

.hero-badge{
    display:inline-block;
    background:rgba(255,255,255,0.2);
    padding:8px 18px;
    border-radius:999px;
    font-size:14px;
    font-weight:600;
}

.metric-card{
    background: white;
    padding:20px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition:0.3s;
    border:1px solid #e5e7eb;
}

.metric-card:hover{
    transform:translateY(-5px);
    box-shadow:0 10px 24px rgba(37,99,235,0.18);
}

.metric-number{
    font-size:34px;
    font-weight:700;
    color:#2563eb;
}

.metric-title{
    color:#6b7280;
    font-size:15px;
    margin-top:8px;
}

.topic-chip{

display:inline-block;

background:linear-gradient(135deg,#3b82f6,#2563eb);

color:white;

padding:10px 18px;

margin:8px;

border-radius:999px;

font-weight:600;

font-size:15px;

box-shadow:0 5px 15px rgba(37,99,235,.25);

transition:all .3s ease;

cursor:pointer;

}

.topic-chip:hover{

transform:translateY(-3px) scale(1.05);

box-shadow:0 10px 20px rgba(37,99,235,.4);

}

.suggestion-card{

background:white;

padding:22px;

border-radius:18px;

margin-bottom:18px;

border-left:6px solid #2563eb;

box-shadow:0 6px 18px rgba(0,0,0,.08);

transition:.3s;

}

.suggestion-card:hover{

transform:translateY(-4px);

box-shadow:0 12px 28px rgba(37,99,235,.18);

}

.suggestion-title{

font-size:18px;

font-weight:700;

color:#2563eb;

margin-bottom:12px;

}

.suggestion-text{

font-size:16px;

line-height:1.7;

color:#374151;

}


</style>
""",
unsafe_allow_html=True
)



st.markdown("""
<div class="hero-container">

<div class="hero-title">
🤝 Personalized Networking Assistant
</div>

<div class="hero-subtitle">
Build meaningful professional connections with AI-powered recommendations, conversation starters, and networking insights.
</div>

<div class="hero-badge">
🚀 Powered by Google Gemini AI
</div>

</div>
""", unsafe_allow_html=True)

st.markdown("## 📊 Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{len(st.session_state.topics)}</div>
        <div class="metric-title">Detected Topics</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{len(st.session_state.suggestions)}</div>
        <div class="metric-title">AI Suggestions</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">🤖</div>
        <div class="metric-title">Gemini AI</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">🟢</div>
        <div class="metric-title">System Ready</div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# Sidebar
# ==============================

st.sidebar.title("About")


st.sidebar.info(
"""
This AI assistant helps users:

✅ Analyze networking events

✅ Generate personalized topics

✅ Create conversation starters

✅ Save networking history

✅ Verify professional topics

"""
)


# ==============================
# History
# ==============================

st.sidebar.subheader(
"📜 History"
)


if st.sidebar.button("View History"):

    try:

        response = requests.get(
            f"{API_URL}/history"
        )


        if response.status_code == 200:

            history = response.json()


            if history:

                for item in history[-5:]:

                    st.sidebar.write(
                        item
                    )

            else:

                st.sidebar.info(
                    "No history available"
                )


    except Exception as error:

        st.sidebar.error(
            str(error)
        )



left,right = st.columns([1,1.3])

with left:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    st.markdown("## 👤 User Profile")

    profession = st.selectbox(
        "Profession",
        [
            "Student",
            "Developer",
            "Researcher",
            "Entrepreneur"
        ]
    )

    skills = st.text_input(
        "Skills",
        placeholder="Python, Flask, AI..."
    )

    interests = st.text_input(
        "Interests",
        placeholder="Machine Learning, Cloud..."
    )

    st.markdown("</div>", unsafe_allow_html=True)
    
with right:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    st.markdown("## 📝 Event Details")

    event_description = st.text_area(
        "Describe the Event",
        placeholder="Example: AI conference discussing Generative AI and Cloud Computing...",
        height=220
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ==============================
# Generate Suggestions
# ==============================

generate = st.button(
    "🚀 Generate AI Networking Suggestions",
    use_container_width=True
)

if generate:


    if not event_description:

        st.warning(
            "Please enter event details"
        )


    else:


        payload = {

            "description":
                event_description,


            "interests":
                [
                    x.strip()
                    for x in interests.split(",")
                    if x.strip()
                ],


            "skills":
                [
                    x.strip()
                    for x in skills.split(",")
                    if x.strip()
                ],


            "profession":
                profession

        }


        try:

            response = requests.post(

                f"{API_URL}/generate",

                json=payload

            )


            if response.status_code == 200:


                data=response.json()


                st.session_state.topics = (
                    data["topics"]
                )


                st.session_state.suggestions = (
                    data["suggestions"]
                )


                st.success(
                    "Generated successfully!"
                )


            else:

                st.error(
                    "Backend error"
                )


        except Exception as error:

            st.error(
                f"Connection failed: {error}"
            )



# ==============================
# Display Topics
# ==============================

if st.session_state.topics:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    st.header(
        "📌 Detected Topics"
    )


    topic_html = ""

    for topic in st.session_state.topics:

        topic_html += f"""
        <span class="topic-chip">
            ✨ {topic}
        </span>
        """

    st.markdown(topic_html, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# Suggestions + Feedback
# ==============================

if st.session_state.suggestions:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    st.header(
        "💬 Conversation Starters"
    )


    for index, suggestion in enumerate(
        st.session_state.suggestions
    ):


        st.markdown(
            f"""
        <div class="suggestion-card">

        <div class="suggestion-title">
        💬 Conversation Starter #{index+1}
        </div>

        <div class="suggestion-text">
        {suggestion}
        </div>

        </div>
        """,
        unsafe_allow_html=True
        )

        st.code(suggestion)

        st.caption("📋 Copy the text above and use it while networking.")

        col1,col2 = st.columns(2)



        with col1:

            if st.button(
                "👍 Like",
                key=f"like{index}"
            ):

                requests.post(

                    f"{API_URL}/feedback",

                    json={

                        "suggestion":
                            suggestion,

                        "rating":
                            "like"

                    }

                )

                st.success(
                    "Feedback saved"
                )


        with col2:

            if st.button(
                "👎 Dislike",
                key=f"dislike{index}"
            ):

                requests.post(

                    f"{API_URL}/feedback",

                    json={

                        "suggestion":
                            suggestion,

                        "rating":
                            "dislike"

                    }

                )

                st.warning(
                    "Feedback saved"
                )

    st.markdown("</div>", unsafe_allow_html=True)

    # PDF Download

    st.subheader(
        "📄 Download Report"
    )


    pdf = create_pdf(

        st.session_state.topics,

        st.session_state.suggestions

    )


    st.download_button(

        label="Download PDF",

        data=pdf,

        file_name=
        "networking_report.pdf",

        mime=
        "application/pdf"

    )



# ==============================
# Fact Checker
# ==============================

st.divider()


st.header(
"🔎 Professional Topic Fact Checker"
)


query = st.text_input(
    "Enter topic",
    placeholder="Artificial Intelligence"
)



if st.button(
    "Verify Topic"
):


    try:


        response = requests.post(

            f"{API_URL}/fact-check",

            json={
                "query":query
            }

        )


        if response.status_code == 200:


            result=response.json()


            st.markdown(

                f"""
                <div class="fact-box">

                {result["summary"]}

                </div>
                """,

                unsafe_allow_html=True

            )


        else:

            st.error(
                "Unable to verify"
            )


    except Exception as error:

        st.error(
            str(error)
        )



# ==============================
# Footer
# ==============================

st.markdown(
"""
<hr>

<center>
Personalized Networking Assistant |
Google Cloud Generative AI Internship Project
</center>

""",
unsafe_allow_html=True
)

import streamlit as st
from datetime import datetime
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SmartRec",
    page_icon="🎬",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "watch_history" not in st.session_state:
    st.session_state.watch_history = []

if "ratings" not in st.session_state:
    st.session_state.ratings = {}

if "now_playing" not in st.session_state:
    st.session_state.now_playing = None

# ---------------- YOUTUBE EMBED CHECK ----------------
def is_embeddable(video_id):
    url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    try:
        return requests.get(url, timeout=5).status_code == 200
    except:
        return False

# ---------------- CONTENT DATABASE ----------------
content_database = [
    # -------- MUSIC --------
    {
        "id": 1,
        "title": "Chill Lo-Fi Beats",
        "category": "music",
        "mood": ["relaxed", "neutral"],
        "time": ["evening", "night"],
        "ageGroup": "18-35",
        "duration": 180,
        "rating": 4.8,
        "youtubeId": "Y21kE_LHaOY",
    },
    {
        "id": 2,
        "title": "Energetic Pop Hits",
        "category": "music",
        "mood": ["happy", "energetic"],
        "time": ["morning", "afternoon"],
        "ageGroup": "13-30",
        "duration": 150,
        "rating": 4.5,
        "youtubeId": "A8r8PeYOsbc",
    },

    # -------- MOVIES --------
    {
        "id": 4,
        "title": "Action Adventure Trailer",
        "category": "movies",
        "mood": ["energetic", "happy"],
        "time": ["evening", "night"],
        "ageGroup": "all",
        "duration": 300,
        "rating": 4.3,
        "youtubeId": "Iq1bdv5D4YA",
    },

    # -------- COMEDY --------
    {
        "id": 7,
        "title": "Stand-Up Comedy",
        "category": "comedy",
        "mood": ["happy", "neutral"],
        "time": ["evening", "night"],
        "ageGroup": "18+",
        "duration": 180,
        "rating": 4.4,
        "youtubeId": "rBHpA9lXcS0",
    },

    # -------- YOGA --------
    {
        "id": 9,
        "title": "Morning Yoga Flow",
        "category": "yoga",
        "mood": ["neutral", "energetic"],
        "time": ["morning"],
        "ageGroup": "18+",
        "duration": 150,
        "rating": 4.7,
        "youtubeId": "C2RAjUEAoLI",
    },

    # -------- EDUCATION --------
    {
        "id": 10,
        "title": "Data Structures & Algorithms – Full Course",
        "category": "education",
        "mood": ["neutral", "energetic"],
        "time": ["morning", "afternoon"],
        "ageGroup": "18+",
        "duration": 360,
        "rating": 4.9,
        "youtubeId": "IK63UfMh9E8",
    },
    {
        "id": 11,
        "title": "Operating Systems Explained",
        "category": "education",
        "mood": ["neutral"],
        "time": ["afternoon", "evening"],
        "ageGroup": "18+",
        "duration": 300,
        "rating": 4.7,
        "youtubeId": "RozoeWzT7IM",
    },

    # -------- TECHNOLOGY --------
    {
        "id": 12,
        "title": "Complete React JS Tutorial",
        "category": "technology",
        "mood": ["neutral", "energetic"],
        "time": ["afternoon", "evening"],
        "ageGroup": "18-40",
        "duration": 420,
        "rating": 4.8,
        "youtubeId": "s2skans2dP4",
    },
    {
        "id": 13,
        "title": "Artificial Intelligence Explained",
        "category": "technology",
        "mood": ["neutral"],
        "time": ["afternoon", "evening"],
        "ageGroup": "16+",
        "duration": 240,
        "rating": 4.6,
        "youtubeId": "JMUxmLyrhSk",
    },

    # -------- STARTUPS --------
    {
        "id": 14,
        "title": "Startup Ideas for Students",
        "category": "startups",
        "mood": ["energetic", "happy"],
        "time": ["morning", "afternoon"],
        "ageGroup": "18-35",
        "duration": 210,
        "rating": 4.5,
        "youtubeId": "uRNRUIqH_JU",
    },
    {
        "id": 15,
        "title": "How to Build a Startup from Scratch",
        "category": "startups",
        "mood": ["neutral", "energetic"],
        "time": ["afternoon", "evening"],
        "ageGroup": "20-45",
        "duration": 300,
        "rating": 4.7,
        "youtubeId": "NXXjY68tL84",
    },
]

# ---------------- TIME OF DAY ----------------
hour = datetime.now().hour
current_time = (
    "morning" if hour < 12 else
    "afternoon" if hour < 17 else
    "evening" if hour < 21 else
    "night"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎛 User Profile")
age = st.sidebar.slider("Age", 13, 70, 25)
mood = st.sidebar.selectbox(
    "Mood", ["happy", "neutral", "sad", "energetic", "relaxed", "stressed"]
)
category_filter = st.sidebar.selectbox(
    "Category",
    ["all", "music", "movies", "comedy", "yoga", "education", "technology", "startups"]
)

st.sidebar.markdown(f"🕒 **Time:** {current_time}")
st.sidebar.markdown(f"📺 **Watched:** {len(st.session_state.watch_history)}")

# ---------------- SCORING FUNCTION ----------------
def calculate_score(c):
    score = 0
    if mood in c["mood"]:
        score += 30
    if current_time in c["time"]:
        score += 25

    if c["ageGroup"] == "all":
        score += 15
    else:
        if "+" in c["ageGroup"]:
            min_age, max_age = int(c["ageGroup"].replace("+", "")), 100
        else:
            min_age, max_age = map(int, c["ageGroup"].split("-"))
        if min_age <= age <= max_age:
            score += 20

    score += c["rating"] * 5

    if st.session_state.ratings.get(c["id"]) == "up":
        score += 15
    if st.session_state.ratings.get(c["id"]) == "down":
        score -= 20

    return score

# ---------------- FILTER & SORT ----------------
filtered = (
    content_database if category_filter == "all"
    else [c for c in content_database if c["category"] == category_filter]
)

recommended = sorted(filtered, key=calculate_score, reverse=True)

# ---------------- PLAYER VIEW ----------------
if st.session_state.now_playing:
    c = st.session_state.now_playing

    st.button("⬅ Back", on_click=lambda: st.session_state.update({"now_playing": None}))

    if is_embeddable(c["youtubeId"]):
        st.markdown(
            f"""
            <iframe width="100%" height="500"
            src="https://www.youtube.com/embed/{c['youtubeId']}?autoplay=1"
            frameborder="0"
            allow="autoplay; encrypted-media"
            allowfullscreen></iframe>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("⚠️ This video cannot be embedded.")
        st.markdown(f"[🔗 Open on YouTube](https://www.youtube.com/watch?v={c['youtubeId']})")

    st.header(c["title"])
    st.write(f"⭐ Rating: {c['rating']} | ⏱ {c['duration']} sec")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("👍 Like"):
            st.session_state.ratings[c["id"]] = "up"
    with col2:
        if st.button("👎 Dislike"):
            st.session_state.ratings[c["id"]] = "down"

    st.stop()

# ---------------- BROWSE VIEW ----------------
st.title("🎬 SmartRec – Smart Content Recommender")

cols = st.columns(3)
for i, c in enumerate(recommended):
    with cols[i % 3]:
        st.subheader(c["title"])
        st.caption(f"⭐ {c['rating']} | {c['category'].capitalize()}")
        if st.button("▶ Watch", key=c["id"]):
            st.session_state.now_playing = c
            if c["id"] not in st.session_state.watch_history:
                st.session_state.watch_history.append(c["id"])
            st.rerun()


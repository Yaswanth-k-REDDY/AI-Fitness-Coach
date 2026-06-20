import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="AI Fitness Coach",
    page_icon="🏋️",
    layout="wide"
)

# Sidebar
st.sidebar.title("🏋️ AI Fitness Coach")

st.sidebar.info(
    """
Built using:

✅ Python
✅ OpenCV
✅ MediaPipe
✅ Streamlit
"""
)

# Header
st.title("🏋️ AI Fitness Coach Dashboard")

st.caption(
    "AI-powered workout tracking and analytics"
)

# Load Data
df = pd.read_csv("workout_logs.csv")

# Welcome Section
colA, colB = st.columns([2, 1])

with colA:

    st.info(
        f"""
👋 Welcome Back!

📊 Total Logged Workouts: {len(df)}

💪 Total Reps: {df['Reps'].sum()}

⏱️ Total Duration: {df['Duration'].sum()} seconds
"""
    )

with colB:

    st.metric(
        "🎯 Exercises",
        len(df["Exercise"].unique())
    )

# Achievement System
max_reps = df["Reps"].max()

if max_reps >= 100:

    st.success(
        "💎 Elite Athlete - 100+ Reps!"
    )

elif max_reps >= 50:

    st.success(
        "🥇 Gold Athlete - 50+ Reps!"
    )

elif max_reps >= 25:

    st.success(
        "🥈 Silver Athlete - 25+ Reps!"
    )

elif max_reps >= 10:

    st.success(
        "🥉 Bronze Athlete - 10+ Reps!"
    )

# Exercise Filter
exercise = st.selectbox(
    "Select Exercise",
    df["Exercise"].unique()
)

filtered_df = df[
    df["Exercise"] == exercise
]

# Metrics
total_workouts = len(filtered_df)

total_reps = filtered_df["Reps"].sum()

total_duration = filtered_df["Duration"].sum()

best_reps = filtered_df["Reps"].max()

avg_reps = round(
    filtered_df["Reps"].mean(),
    2
)

calories = round(
    total_reps * 0.5,
    2
)

fitness_score = total_reps * 2

# Sidebar Personal Best
st.sidebar.metric(
    "🏆 Personal Best",
    best_reps
)

# Metric Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🏋️ Workouts",
        total_workouts
    )

with col2:
    st.metric(
        "💪 Total Reps",
        total_reps
    )

with col3:
    st.metric(
        "⏱️ Duration",
        total_duration
    )

col4, col5, col6, col7 = st.columns(4)

with col4:
    st.metric(
        "🏆 Best Reps",
        best_reps
    )

with col5:
    st.metric(
        "📈 Avg Reps",
        avg_reps
    )

with col6:
    st.metric(
        "🔥 Calories",
        calories
    )

with col7:
    st.metric(
        "⭐ Fitness Score",
        fitness_score
    )

st.divider()

# Analytics
st.header("📊 Analytics")

# Workout History
st.subheader("📋 Workout History")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.divider()

# Reps Progress
st.subheader("📈 Reps Progress")

st.line_chart(
    filtered_df["Reps"]
)

st.divider()

# Duration Progress
st.subheader("⏱️ Duration Progress")

st.bar_chart(
    filtered_df["Duration"]
)

st.divider()

# Exercise Distribution
st.subheader("🥧 Exercise Distribution")

fig, ax = plt.subplots()

df["Exercise"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax
)

ax.set_ylabel("")

st.pyplot(fig)

# Footer
st.divider()

st.caption(
    "Built by Yaswanth using Python, OpenCV, MediaPipe and Streamlit 🚀"
)
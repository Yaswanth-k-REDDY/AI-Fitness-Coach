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
st.sidebar.markdown("---")

st.sidebar.subheader("📌 Quick Stats")

st.sidebar.markdown(
    """
- 💪 Exercise Tracking
- 📊 Analytics
- 🏆 Achievements
- 🔥 Fitness Score
"""
)

st.sidebar.markdown("---")
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
st.markdown(
    """
    <h1 style='text-align:center; color:#4CAF50;'>
    🏋️ AI Fitness Coach Dashboard
    </h1>
    <p style='text-align:center;'>
    AI-powered workout tracking and analytics
    </p>
    """,
    unsafe_allow_html=True
)

st.caption(
    "AI-powered workout tracking and analytics"
)

# Load Data
import os

if os.path.exists("workout_logs.csv"):
    df = pd.read_csv("workout_logs.csv")
    df["Date"] = pd.to_datetime(df["Date"])
else:
    df = pd.DataFrame({
        "Date": ["Demo"],
        "Exercise": ["Bicep Curl"],
        "Reps": [10],
        "Duration": [30]
    })

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
unique_days = df["Date"].dt.date.nunique()

st.sidebar.metric(
    "🔥 Workout Days",
    unique_days
)
if unique_days >= 30:

    st.success(
        "🏆 Fitness Legend!"
    )

elif unique_days >= 15:

    st.success(
        "🥇 Consistent Performer!"
    )

elif unique_days >= 7:

    st.success(
        "🥈 Weekly Warrior!"
    )

else:

    st.info(
        "🚀 Keep Building Your Streak!"
    )
max_reps = df["Reps"].max()
workout_count = len(df)

if workout_count >= 20:

    st.success(
        "🔥 20 Workout Streak!"
    )

elif workout_count >= 10:

    st.success(
        "🔥 10 Workout Streak!"
    )

elif workout_count >= 5:

    st.success(
        "🔥 5 Workout Streak!"
    )
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
daily_goal = 200
weekly_goal = 1000

# Weekly Goal

weekly_progress = min(
    int((df["Reps"].sum() / weekly_goal) * 100),
    100
)

st.subheader("🏆 Weekly Goal Progress")

st.progress(weekly_progress)

st.write(
    f"{df['Reps'].sum()} / {weekly_goal} Reps"
)
if df["Reps"].sum() >= weekly_goal:

    st.success(
        "🏆 Weekly Goal Achieved!"
    )

elif df["Reps"].sum() >= weekly_goal * 0.75:

    st.info(
        "🔥 Almost There!"
    )

else:

    st.warning(
        "🎯 Keep Going!"
    )
goal_progress = min(
    int((filtered_df["Reps"].sum() / daily_goal) * 100),
    100
)

st.subheader("🎯 Daily Goal Progress")

st.progress(goal_progress)

st.write(
    f"{filtered_df['Reps'].sum()} / {daily_goal} Reps"
)
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
health_score = min(
    int((fitness_score / 500) * 100),
    100
)
if total_reps >= 100:

    status = "🔥 Excellent"

elif total_reps >= 50:

    status = "💪 Active"

else:

    status = "🚀 Getting Started"

# Sidebar Personal Best
st.sidebar.metric(
    "🏆 Personal Best",
    best_reps
)

# Metric Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.success(
        f"🏆 Workouts\n\n# {total_workouts}"
    )

with col2:
    st.info(
        f"💪 Total Reps\n\n# {total_reps}"
    )

with col3:
    st.warning(
        f"⏱️ Duration\n\n# {total_duration}"
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
    "❤️ Health Score",
    f"{health_score}%"
)
    st.metric(
        "⭐ Fitness Score",
        fitness_score
    )
    st.subheader("🧠 AI Coach Insights")

if total_reps >= 100:

    st.success(
        "🔥 Excellent workout consistency detected."
    )

elif total_reps >= 50:

    st.info(
        "💪 Good progress. Keep pushing!"
    )

else:

    st.warning(
        "🎯 Aim for more reps to improve fitness."
    )
st.info(
    f"Current Status: {status}"
)
st.divider()
st.subheader("📅 Weekly Summary")

colA, colB, colC = st.columns(3)

with colA:
    st.metric(
        "Workouts",
        len(df)
    )

with colB:
    st.metric(
        "Reps",
        df["Reps"].sum()
    )

with colC:
    st.metric(
        "Duration",
        df["Duration"].sum()
    )
st.subheader("🏆 Personal Records")

records = df.groupby("Exercise")["Reps"].max()

col1, col2, col3 = st.columns(3)

with col1:

    if "Bicep Curl" in records.index:
        st.metric(
            "💪 Best Bicep Curl",
            records["Bicep Curl"]
        )

with col2:

    if "Squat" in records.index:
        st.metric(
            "🦵 Best Squat",
            records["Squat"]
        )

with col3:

    if "Push-Up" in records.index:
        st.metric(
            "🤸 Best Push-Up",
            records["Push-Up"]
        )

st.divider()
st.divider()
# Analytics
st.subheader("🏆 Personal Records")

records = df.groupby("Exercise")["Reps"].max()

col1, col2, col3 = st.columns(3)

with col1:
    if "Bicep Curl" in records.index:
        st.metric(
            "💪 Best Bicep Curl",
            records["Bicep Curl"]
        )

with col2:
    if "Squat" in records.index:
        st.metric(
            "🦵 Best Squat",
            records["Squat"]
        )

with col3:
    if "Push-Up" in records.index:
        st.metric(
            "🤸 Best Push-Up",
            records["Push-Up"]
        )

st.divider()

# ADD LEADERBOARD HERE 👇

st.subheader("🥇 Exercise Leaderboard")

leaderboard = df.groupby(
    "Exercise"
)["Reps"].sum().sort_values(
    ascending=False
)

st.dataframe(
    leaderboard,
    use_container_width=True
)

st.divider()
st.subheader("📥 Download Workout Report")

csv = df.to_csv(index=False)

st.download_button(
    label="📄 Download Workout Report",
    data=csv,
    file_name="fitness_report.csv",
    mime="text/csv"
)
top_exercise = leaderboard.index[0]

st.success(
    f"🏆 Top Performing Exercise: {top_exercise}"
)
st.divider()
st.subheader("📈 Fitness Trend Analysis")

latest_reps = df["Reps"].iloc[-1]

best_reps_overall = df["Reps"].max()

improvement = best_reps_overall - latest_reps

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Latest Session",
        latest_reps
    )

with col2:
    st.metric(
        "Best Session",
        best_reps_overall
    )

with col3:
    st.metric(
        "Improvement Needed",
        improvement
    )

st.divider()
st.subheader("📈 Fitness Trend Analysis")

latest_reps = df["Reps"].iloc[-1]

best_reps_overall = df["Reps"].max()

improvement = best_reps_overall - latest_reps

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Latest Session",
        latest_reps
    )

with col2:
    st.metric(
        "Best Session",
        best_reps_overall
    )

with col3:
    st.metric(
        "Improvement Needed",
        improvement
    )

st.divider()

# PASTE EXERCISE INSIGHTS HERE 👇

st.subheader("🧠 Exercise Insights")

most_performed = df.groupby(
    "Exercise"
)["Reps"].sum().idxmax()

st.success(
    f"🏆 Most Performed Exercise: {most_performed}"
)

avg_session = round(
    df["Reps"].mean(),
    2
)

st.info(
    f"📊 Average Reps Per Session: {avg_session}"
)

st.divider()

# Analytics starts here 👇
st.subheader("🏅 Fitness Level")

total_reps_all = df["Reps"].sum()

if total_reps_all >= 500:

    level = "💎 Elite"

elif total_reps_all >= 250:

    level = "🥇 Advanced"

elif total_reps_all >= 100:

    level = "🥈 Intermediate"

else:

    level = "🥉 Beginner"

st.success(
    f"Your Fitness Level: {level}"
)

st.divider()

# Analytics starts here 👇
tab1, tab2 = st.tabs(
    ["📊 Analytics", "🏆 Achievements"]
)
st.subheader("🤖 AI Recommendation Engine")

exercise_totals = df.groupby("Exercise")["Reps"].sum()

top_exercise = exercise_totals.idxmax()

if top_exercise == "Bicep Curl":

    st.info(
        "💪 You focus heavily on Bicep Curls. Add more Push-Ups and Squats for balanced strength."
    )

elif top_exercise == "Push-Up":

    st.info(
        "🤸 Great upper body focus. Consider adding Squats for lower body development."
    )

elif top_exercise == "Squat":

    st.info(
        "🦵 Strong lower body training. Include Push-Ups and Bicep Curls for balance."
    )

st.divider()
with tab1:

    st.header("📊 Analytics")
st.subheader("🎖️ Achievement Gallery")

badges = []

if total_reps_all >= 100:
    badges.append("🥉 100 Reps Club")

if total_reps_all >= 250:
    badges.append("🥈 250 Reps Club")

if total_reps_all >= 500:
    badges.append("🥇 500 Reps Club")

if workout_count >= 10:
    badges.append("🔥 10 Workout Streak")

for badge in badges:
    st.write(badge)

st.divider()
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
st.subheader("📊 Exercise Comparison")

exercise_totals = df.groupby(
    "Exercise"
)["Reps"].sum()

st.bar_chart(
    exercise_totals
)

st.divider()
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
with tab2:

    st.subheader("🏆 Achievement Summary")

    st.write(
        f"Workout Sessions: {workout_count}"
    )

    st.write(
        f"Workout Days: {unique_days}"
    )

    st.write(
        f"Total Reps: {total_reps_all}"
    )

    st.write(
        f"Fitness Level: {level}"
    )
st.caption(
    "AI Fitness Coach v2.0 | Built by Yaswanth using Python, OpenCV, MediaPipe and Streamlit 🚀"
)
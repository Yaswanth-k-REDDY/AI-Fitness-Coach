import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pdf_report import generate_report

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
    total_reps_all = df["Reps"].sum()
    df["Date"] = pd.to_datetime(df["Date"])
else:
    df = pd.DataFrame({
        "Date": ["Demo"],
        "Exercise": ["Bicep Curl"],
        "Reps": [10],
        "Duration": [30]
    })
# ======================
# Dashboard Calculations
# ======================

total_reps_all = df["Reps"].sum()

workout_count = len(df)

unique_days = df["Date"].dt.date.nunique()

exercise_totals = df.groupby(
    "Exercise"
)["Reps"].sum()

bicep = exercise_totals.get(
    "Bicep Curl",
    0
)

pushup = exercise_totals.get(
    "Push-Up",
    0
)

squat = exercise_totals.get(
    "Squat",
    0
)

if total_reps_all >= 500:
    fitness_level = "Elite"

elif total_reps_all >= 250:
    fitness_level = "Advanced"

elif total_reps_all >= 100:
    fitness_level = "Intermediate"

else:
    fitness_level = "Beginner"

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
col4, col5, col6, col7, col8 = st.columns(5)

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
with col8:
    st.metric(
        "⭐ Fitness Score",
        fitness_score
    )

# Outside the columns

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


week1, week2,week3,week4 = st.columns(4)

with week1:
    st.metric("🏋️ Workouts", len(df))
with week2:
    st.metric("💪 Reps", total_reps_all)

with week3:
    st.metric("⏱️ Duration", df["Duration"].sum())
with week4:
    st.metric("🎯 Level", fitness_level)


records = df.groupby("Exercise")["Reps"].max()
record1, record2, record3, record4 = st.columns(4)

with record1:

    if "Bicep Curl" in records.index:
        st.metric(
            "💪 Best Bicep Curl",
            records["Bicep Curl"]
        )

with record2:

    if "Squat" in records.index:
        st.metric(
            "🦵 Best Squat",
            records["Squat"]
        )

with record3:

    if "Push-Up" in records.index:
        st.metric(
            "🤸 Best Push-Up",
            records["Push-Up"]
        )
with record4:
    st.metric(
        "⭐ Fitness Score",
        fitness_score
    )
st.divider()

# ADD LEADERBOARD HERE 👇

st.subheader("🥇 Exercise Leaderboard")

leaderboard = df.groupby(
    "Exercise"
)["Reps"].sum().sort_values(
    ascending=False
)

leader_cols = st.columns(
    len(leaderboard)
)

for i, (exercise, reps) in enumerate(
    leaderboard.items()
):

    with leader_cols[i]:

        st.metric(
            exercise,
            reps
        )

st.divider()
st.subheader("📥 Download Workout Report")
if st.button("📄 Generate PDF Report"):
    st.subheader("🏆 Personal Records")
    records = df.groupby("Exercise")["Reps"].max()

    best_bicep = records.get(
        "Bicep Curl",
        0
    )

    best_squat = records.get(
        "Squat",
        0
    )

    best_pushup = records.get(
        "Push-Up",
        0
    )
    total_reps_all = df["Reps"].sum()

    if total_reps_all >= 500:
        level = "Elite"

    elif total_reps_all >= 250:
        level = "Advanced"

    elif total_reps_all >= 100:
        level = "Intermediate"

    else:
        level = "Beginner"

    generate_report(
        len(df),
        df["Reps"].sum(),
        level,
        best_bicep,
        best_squat,
        best_pushup
    )

    st.success(
        "✅ PDF Report Generated!"
    )
csv = df.to_csv(index=False)

st.download_button(
    label="📄 Download Workout Report",
    data=csv,
    file_name="fitness_report.csv",
    mime="text/csv"
)
top_exercise = leaderboard.index[0]

st.metric(
    "🏆 Top Exercise",
    top_exercise
)
st.divider()
st.subheader("📊 Performance Insights")

card1, card2, card3, card4, card5 = st.columns(5)

latest_reps = df["Reps"].iloc[-1]

best_reps_overall = df["Reps"].max()

improvement = best_reps_overall - latest_reps

most_performed = df.groupby(
    "Exercise"
)["Reps"].sum().idxmax()

avg_session = round(
    df["Reps"].mean(),
    2
)

with card1:
    st.metric(
        "🔥 Latest",
        latest_reps
    )

with card2:
    st.metric(
        "🏆 Best",
        best_reps_overall
    )

with card3:
    st.metric(
        "📈 Gap",
        improvement
    )

with card4:
    st.metric(
        "💪 Top Exercise",
        most_performed
    )

with card5:
    st.metric(
        "📊 Avg Reps",
        avg_session
    )
st.divider()
# Workout Quality Score Calculation

score = 0

# Reps Score
score += min(
    int(df["Reps"].sum() / 5),
    40
)

# Workout Count Score
score += min(
    workout_count * 3,
    30
)

# Consistency Score
score += min(
    unique_days * 5,
    30
)
card1, card2, card3, card4 = st.columns(4)
# Analytics starts here 👇
with card1:

    st.subheader("🏆 Quality Score")

    st.metric(
        "Score",
        f"{score}/100"
    )

    st.progress(score / 100)

with card2:

    st.subheader("🧬 Fitness DNA")

    if bicep > pushup and bicep > squat:
        st.success(
            "💪 Strength Focused"
        )

    if pushup > squat:
        st.info(
            "🏋️ Upper Body"
        )

    if unique_days >= 5:
        st.success(
            "⭐ High Consistency"
        )
with card3:

    st.subheader(
        "🎯 Goal"
    )

    target = 250

    progress = min(
        total_reps_all / target,
        1.0
    )

    st.progress(progress)

    st.write(
        f"{total_reps_all}/{target} Reps"
    )
with card4:

    st.subheader(
        "🏅 Fitness Level"
    )

    st.metric(
        "Level",
        fitness_level
    )
st.divider()

# Analytics starts here 👇
st.subheader("🤖 AI Recommendation Engine")
st.subheader("🧠 Personalized Workout Plan")
tab1, tab2 = st.tabs(
    ["📊 Analytics", "🏆 Achievements"]
)


exercise_totals = df.groupby(
    "Exercise"
)["Reps"].sum()

bicep = exercise_totals.get(
    "Bicep Curl",
    0
)

squat = exercise_totals.get(
    "Squat",
    0
)

pushup = exercise_totals.get(
    "Push-Up",
    0
)

if bicep > pushup * 2:

    st.warning(
        "💪 Upper body dominates. Increase Push-Ups."
    )

if bicep > squat * 3:

    st.warning(
        "🦵 Add more Squats for balance."
    )

if pushup < 20:

    st.info(
        "🤸 Target 20+ Push-Ups this week."
    )

if squat < 20:

    st.info(
        "🏋️ Aim for 20+ Squats this week."
    )
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

    st.subheader("📋 Workout History")
    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    st.subheader("📈 Reps Progress")
    st.line_chart(
        filtered_df["Reps"]
    )

    st.subheader("⏱️ Duration Progress")
    st.bar_chart(
        filtered_df["Duration"]
    )

    st.subheader("📊 Exercise Comparison")
    st.bar_chart(
        exercise_totals
    )

with tab2:

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

    badge_cols = st.columns(max(len(badges), 1))

    for i, badge in enumerate(badges):
        with badge_cols[i]:
            st.success(badge)

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
        f"Fitness Level: {fitness_level}"
    )
st.caption(
    "AI Fitness Coach v2.0 | Built by Yaswanth using Python, OpenCV, MediaPipe and Streamlit 🚀"
)
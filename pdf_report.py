from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def generate_report(
    total_workouts,
    total_reps,
    fitness_level,
    best_bicep,
    best_squat,
    best_pushup
):

    doc = SimpleDocTemplate(
        "fitness_report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Fitness Coach Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Total Workouts: {total_workouts}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Total Reps: {total_reps}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Fitness Level: {fitness_level}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        Paragraph(
            "Personal Records",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Bicep Curl: {best_bicep}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Squat: {best_squat}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Push-Up: {best_pushup}",
            styles["Normal"]
        )
    )

    doc.build(content)
class ScoringEngine:

    def calculate(
        self,
        similarity,
        wpm,
        pause_ratio,
        filler_count,
        energy
    ):

        score = similarity * 0.70

        # Speech Rate
        if 100 <= wpm <= 160:
            score += 10
        elif 80 <= wpm <= 180:
            score += 7
        else:
            score += 4

        # Pause Ratio
        if pause_ratio <= 20:
            score += 10
        elif pause_ratio <= 30:
            score += 7
        else:
            score += 4

        # Filler Words
        if filler_count == 0:
            score += 5
        elif filler_count <= 3:
            score += 3

        # Voice Energy
        if energy >= 0.05:
            score += 5
        else:
            score += 3

        final_score = round(min(score, 100), 2)

        if final_score >= 90:
            grade = "A+"
            remark = "🌟 Excellent Presentation"

        elif final_score >= 75:
            grade = "A"
            remark = "✅ Good Understanding"

        elif final_score >= 60:
            grade = "B"
            remark = "🙂 Average Understanding"

        else:
            grade = "C"
            remark = "⚠ Needs Improvement"

        return final_score, grade, remark
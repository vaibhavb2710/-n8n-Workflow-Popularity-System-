def calculate_ratios(views, likes, comments):
    if views == 0:
        return 0.0, 0.0
    return likes / views, comments / views


def calculate_popularity_score(workflow):
    score = (
        (workflow.views or 0) * 0.4 +
        (workflow.likes or 0) * 0.3 +
        (workflow.comments or 0) * 0.2 +
        (workflow.like_to_view_ratio or 0) * 100 * 0.1
    )
    return round(score, 2)
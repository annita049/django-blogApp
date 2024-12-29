from datetime import datetime
from django.utils.timezone import now

def rounded_time_ago(created_at):
    delta = now() - created_at
    if delta.days >= 365:
        return f"{delta.days // 365}y ago"  # Years
    elif delta.days >= 30:
        return f"{delta.days // 30}mo ago"  # Months
    elif delta.days >= 1:
        return f"{delta.days}d ago"  # Days
    elif delta.seconds >= 3600:
        return f"{delta.seconds // 3600}h ago"  # Hours
    elif delta.seconds >= 60:
        return f"{delta.seconds // 60}m ago"  # Minutes
    else:
        return "Just now"

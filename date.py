from datetime import datetime, timedelta

# Subtract five days from current date
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print(five_days_ago.date())

# Print yesterday, today, tomorrow
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print(yesterday.date(), current_date.date(), tomorrow.date())

# Drop microseconds from datetime
dt_without_microseconds = current_date.replace(microsecond=0)
print(dt_without_microseconds)

# Calculate two date difference in seconds
date1 = datetime(2024, 2, 1, 12, 0, 0)
date2 = datetime(2024, 2, 22, 14, 30, 0)
difference_in_seconds = int((date2 - date1).total_seconds())
print(difference_in_seconds)

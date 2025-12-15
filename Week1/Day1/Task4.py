#Task 4

total = 3665

hours = total // 3600
remain_minutes = (total % 3600) // 60
remain_seconds = total % 60

print(hours, remain_minutes, remain_seconds)
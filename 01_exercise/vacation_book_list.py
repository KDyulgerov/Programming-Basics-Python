
total_pages = int(input())
pages_per_hour = int(input())
days_for_read = int(input())

total_time_for_read = total_pages // pages_per_hour
hours_per_day = total_time_for_read // days_for_read

print(hours_per_day)
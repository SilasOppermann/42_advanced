import time
from datetime import datetime


seconds_since_epoch = time.time()

formatted_seconds = f"{seconds_since_epoch:,.4f}"

scientific_notation = f"{seconds_since_epoch:.2e}"

current_date = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific_notation} in scientific notation")
print(current_date)
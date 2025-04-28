from datetime import datetime

def execute() -> None:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    print(f"Current Time: {current_time}")
    print(f"Current Date: {current_date}", end="\n\n")
    return
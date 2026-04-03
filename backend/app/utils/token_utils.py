from datetime import datetime
from secrets import token_hex


def generate_complaint_ticket_id() -> str:
    date_part = datetime.utcnow().strftime("%Y%m%d")
    random_part = token_hex(3).upper()
    return f"#CMP-{date_part}-{random_part}"

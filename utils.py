def datetime_as_string(dt):
    try:
        return dt.strftime("%d/%m/%Y %H:%M:%S")
    except Exception:
        return None

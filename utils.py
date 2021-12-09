

def isfloat(v):
    try:
        float(v)
        return True
    except ValueError:
        return False


def ischar(s):
    return type(s) == str and len(s) == 1


def interpret_type(s):
    s = s.strip()
    if s.lower() in ["true", "false"]:
        return bool
    elif s.isnumeric():
        return int
    elif isfloat(s):
        return float
    elif s:
        return str 
    else:
        return None


def auto_cast(items, allowed_types):
    for i in range(len(items)):
        item_type = interpret_type(items[i])
        if item_type not in allowed_types:
            if items[i] and str in allowed_types:
                items[i] = str(items[i])
            else:
                return []
        else:
            items[i] = item_type(items[i])
    return items

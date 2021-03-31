from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


d1 = '2021-03-31'
d2 = datetime.now().strftime("%Y-%m-%d")

print(days_between(d1, d2))
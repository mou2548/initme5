data = {
    'positive': 0,
    'negative': 0,
    'neutral': 0,
}
ray = input("Ray: ")
for each in ray:
    if each == '+':
        data['positive'] += 1
    elif each == '-':
        data['negative'] += 1
    elif each == '0':
        data['neutral'] += 1

cancel = min(data['positive'], data['negative'])
data['positive'] -= cancel
data['negative'] -= cancel
for key, value in data.items():
    print(f"The {key} ray remains at {value}.")
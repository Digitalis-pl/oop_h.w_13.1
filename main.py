from function import create_instance, open_json

print(create_instance(open_json())[0])

smth = create_instance(open_json())[1]
def show():
    index = -1
    index += 1
    return smth[index]
print(show()[1])


with open('referat.txt', 'r', encoding='utf-8') as file:
    content = file.read()

full_string = content.split()
# print(len(full_string))
# # for word in full_string:
#
#
# print(len(content))
# print(full_string)

no_points = content.replace('.', '!')

print(no_points)

with open('referat2.txt', 'w', encoding='utf-8') as file:
    file.write(no_points)

    
file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('chai aur python')




# with open('youtube.txt', 'r') as file:
#     content = file.read()
#     print(content)



# # 1. First, let's write the initial content (this erases anything old)
# with open('youtube.txt', 'w') as file:
#     file.write('chai aur python')

# # 2. Now, let's APPEND new content (this keeps the old text!)
# with open('youtube.txt', 'a') as file:
#     file.write(' - is awesome')
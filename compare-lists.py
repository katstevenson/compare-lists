count = 0
list_1 = []
import_content = open('list1.txt', 'r')
list_1 = import_content.read()
import_content.close()
list_1 = list_1.split("\n")

list_2 = []
import_content = open('list2.txt', 'r')
list_2 = import_content.read()
import_content.close()
list_2 = list_2.split("\n")

only_in_list_1 = []
only_in_list_2 = []
both_lists = []

for item in list_1:
  item.strip()
  if item not in list_2:
    only_in_list_1.append(item)
  else: 
    both_lists.append(item)
    count += 1
    
for item in list_2:
  item.strip()
  if item not in list_1:
    only_in_list_2.append(item)

go_to_file = open('output_list.txt', 'w')
count = 0
for style in both_lists:
  go_to_file.write(style + "\n")
  count += 1
print(count)
go_to_file.close()
  


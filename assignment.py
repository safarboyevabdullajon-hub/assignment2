
def replace_value(values,index,new_value):
   values[index] = new_value
   return None
def find_first(values,target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1



def summarize(values):
    item = values
    return (min(item), max(item), sum(item))

target = 0
num_days = int(input("Enter the number of days:"))
original = []
for i in range(1,num_days+1):
    num_calls = int(input("Enter the number of calls:"))
    original.append(num_calls)
updated = original[:]
index = int(input("Enter the index to correct: "))
new_calls = int(input("Enter the new number of calls: "))
replace_value(updated, index, new_calls)
target = int(input("Enter number of calls to search for: "))
first_index = find_first(updated, target)
matching_count = updated.count(target)

minumum, maximum, total = summarize(updated)
sort = sorted(updated)
print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sort}")
print(f"Minumum number of calls: {minumum}")
print(f"Maximum number of calls: {maximum}")
print(f"Total number of calls: {total}")

if first_index != -1:
    print(f"Index of target ({target}): {first_index}")
else:
    print("Target not found")
print(f"Matching values: ({matching_count}) ")    



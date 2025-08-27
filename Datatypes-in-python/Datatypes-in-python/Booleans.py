is_boiling = True
stri_count = 5

total_actions = stri_count + is_boiling # upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 # no milk
# bool function returs the Boolean values -> True / False
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = True

# Logical Operators
can_server = water_hot and tea_added
can_or_server = water_hot or tea_added
not_server = not tea_added

print(f"Can serve chai? {can_server}")
print(f"Can serve chai? can_or_server = {can_or_server}")
print(f"Can serve chai? not_server = {not_server}")

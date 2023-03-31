# Example 1: Sort the dictionary based on values


dt = {5:4, 1:6, 6:3}

sorted_dt = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}

print(sorted_dt)



# Example 2: Sort only the values

dt = {5:4, 1:6, 6:3}

sorted_dt_value = sorted(dt.values())
print(sorted_dt_value)

# Creating a list that will contain the total occurences of each number.
results = [0 for i in range(6)]
# Looping through all possibilities.
for i in range(6):
    for j in range(6):
        for k in range(6):
            print((i+1,j+1,k+1))
            # Increasing the count for the largest value
            results[max((i+1,j+1,k+1))-1] += 1

# Calculating E(X).
expected_value = sum(([results[i]/216) * (i+1) for i in range(6)])

print(expected_value)
            

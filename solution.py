import part_a,part_b
# You are given two six-sided dice, Die A and Die B, each with faces numbered from 1 to 6.
Die_A = [1,2,3,4,5,6]
Die_B = [1,2,3,4,5,6]

length_A = len(Die_A)
length_B = len(Die_B)

# You can only roll both the dice together & your turn is guided by the obtained sum.

# Part-A
print("Part-A")
# By Formula
print("Total Combinations: ")
combination_Count = part_a.combination_Finder(length_A,length_B)
print(combination_Count)

# Distribution Display
print("All Possible Distributions: ")
part_a.combined_Display(Die_A,Die_B)

print("Sum Distributions")
part_b.printOrderly(part_a.sum_Distribution(Die_A,Die_B))

print("Sum Probabilities")
print(part_a.all_Probability(Die_A,Die_B))

#Part-B
print("Part-B")
print("New Dice are")
part_b.printOrderly(part_b.transform(Die_A,Die_B))
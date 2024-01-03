# 1. How many total combinations are possible? Show the math along with the code!
"""
Ans: The combination of the dice that are rolled simultaniously can be found out using two common methods. Through iteration or by using formula of, multiplying the total number of sides of the dice
"""
# using the formula here
def combination_Finder(length_A,length_B):
  combination_Count = length_A * length_B
  return combination_Count

# 2. Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together. Show the math along with the code!
# Hint: A 6 x 6 Matrix.
def combined_Display(Die_A,Die_B):
  # creating a 2d array and initializing with 0
  display_Array = [[0 for i in range(len(Die_A))] for j in range(len(Die_B))]
  for a in Die_A:
    for b in Die_B:
      display_Array[a-1][b-1] = a,b
  for i in display_Array:
    print(i)
  return display_Array

def sum_Distribution(Die_A,Die_B):
  # creating a 2d array and initializing with 0
  sum_Array = [[0 for i in range(len(Die_A))] for j in range(len(Die_B))]
  for a in range(len(Die_A)):
    for b in range(len(Die_B)):
      sum_Array[a-1][b-1] = Die_A[a-1]+Die_B[b-1] 
  return sum_Array

# 3. Calculate the Probability of all Possible Sums occurring among the number of combinations from (2).
# Example: P(Sum = 2) = 1/X as there is only one combination possible to obtain Sum = 2. Die A = Die B = 1.

def single_Probability(Die_A,Die_B,sum):
  # to find the probability of any number passed as the sum parameter
  sum_Array = sum_Distribution(Die_A,Die_B)
  count = 0
  for rows in sum_Array:
    for column in rows:
      if(column == sum):
        count = count+1
  # return count(!count check success)
  probability = count/36
  return probability

def all_Probability(Die_A,Die_B):
  prob_dict = {
    "2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0
  }
  for i in range(2,13):
    # used the single_probability method in order to reducet the time and increase reusability of the code
    # print(str(i))(!printing key value pair success!)
    prob_dict[str(i)] = round(single_Probability(Die_A,Die_B,i),4)
  return prob_dict
def list_sum(list1: list, list2: list):
  index = 0
  sum_list = [] # Initialize the list of sums
  while index < len(list1):
    sum_list[index] = sum(list1[index], list2[index])
    index += 1
  return sum_list

if __name__ == "__main__":
  a = [1, 2, 3]
  b = [7, 8, 9]
  print(list_sum(a, b))

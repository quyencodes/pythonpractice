class Node:
  def __init__(self, val):
    self.val = val
    self.next = None



def zipper_lists(head_1, head_2):
  pass


def get_node_value(head, index):
  if head is None:
    return None

  if index == 0:
    return head.val

  return get_node_value(head.next, index - 1)


def linked_list_find(head, target):
  if not head:
    return False

  if head.val == target:
    return True

  linked_list_find(head.next, target)







def sum_list(head):
  if head is None:
    return 0

  return head.val + sum_list(head.next) # 0

sum_list(a)
# a
sum_list(b)
# b
sum_list(c)
# c
sum_list(None)
# return 0

# a -> b -> c -> None
# 1    2    3

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c


def linked_list_values(head):
  # return list containing all values of the nodes
  result = []

  # wrapper function recursion style
  def valueshelper(current):
    # base case
    if current is None:
      return None

    # append values here
    result.append(current.val)
    # keep recursing
    valueshelper(current.next)

  # invoke the function once
  valueshelper(head)
  # return result
  return result


# pure recursion
def pure_recursion(input):

  if input is None:
    return None

  return pure_recursion(input.next)

# wrapper function recursion
def wrapper_function(input):
  values = []

  def inner_recursion(input2):
    pass

  inner_recursion(input)
  return values
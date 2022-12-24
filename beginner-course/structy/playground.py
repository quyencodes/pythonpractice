class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


# a -> b -> c -> d -> e -> f
# a -> b -> d -> e -> f
# h -> i -> j -> i
# h -> j -> i

def remove_node(head, target_val):
  # if node is at the beginning
  if head.val == target_val:
    return head.next

  # if we recurse to the end
  if head is None:
    return None


  if head.next.val == target_val:
    head.next = head.next.next
    return head

  temp = head
  remove_node(head.next, target_val)
  # return head
  return temp



# remove_node(h, 'i')
# if i == 'i': return head

# remove_node(a, 'c')
# return remove_node(b, 'c') = b

# remove_node(b, 'c')
# c.val = c == 'c'
# return b


# None -> 3 -> 3 -> 7 -> 7 -> 7 -> 5
#                           prev curr
# current_streak = 1
# max_streak = 3

def longest_streak(head):
  # initialize variables
  prev = None
  max_streak = 0
  current_streak = 0

  def longesthelper(current):

    nonlocal prev
    nonlocal max_streak
    nonlocal current_streak

    if current is None:
      return None

    # if prev is NONE
    if prev is None or current.val == prev.val:
      current_streak += 1
    else:
      current_streak = 1

    # update max_streak
    if max_streak < current_streak:
      max_streak = current_streak

    # iterate
    prev = current
    longesthelper(current.next)

  longesthelper(head)
  return max_streak

def is_univalue_list(head):
  if head.next == None:
    return True

  if head.val != head.next.val:
    return False

  return is_univalue_list(head.next)

# is_univalue(7) = None:
# 7 != 7 ? FALSE
# is_univalue(7) = true

# is_univalue(7) = true:
# head.next = None? return true

def addTwo(num1, num2):
  num1 + num2

result = addTwo(1, 2) # None

def merge_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None

  if head_1 is None:
    return head_2

  if head_2 is None:
    return head_1

  if head_1.val > head_2.val:
    next_2 = head_2.next
    head_2.next = merge_lists(head_1, next_2)
    return head_2
  else
    next_1 = head_1.next
    head_1.next = merge_lists(next_1, head_2)
    return head_1



1 -> 4 -> 9
2 -> 3 -> 5 -> 6


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
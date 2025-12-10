from bst.tree import BinarySearchTree

def test_basic_operations():
  t = BinarySearchTree()
  t.insert(5, "five")
  t.insert(3, "three")
  t.insert(7, "seven")
  t.insert(4, "four")
  assert t.search(5) == "five"
  assert t.search(4) == "four"
  assert t.search(100) is None

  t.insert(5, "FIVE")
  assert t.search(5) == "FIVE"

def test_delete_cases():
  t = BinarySearchTree()
  for k in [5,3,7,2,4,6,8]:
    t.insert(k, str(k))
  assert t.delete(2) is True
  assert t.delete(3) is True
  assert t.delete(5) is True
  assert t.search(5) is None

def test_height_and_balance():
  t = BinarySearchTree()
  assert t.height() == 0
  t.insert(10, 10)
  assert t.height() == 1

  t2 = BinarySearchTree()
  for k in [1,2,3,4]:
    t2.insert(k, k)
  assert t2.height() == 4
  assert not t2.is_balanced()

  t3 = BinarySearchTree()
  for k in [2,1,3]:
    t3.insert(k, k)
  assert t3.is_balanced()
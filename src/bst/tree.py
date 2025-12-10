class TreeNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.left = None
    self.right = None


class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, key, value):
    def _insert(node, key, value):
      if node is None:
        return TreeNode(key, value)
      if key < node.key:
        node.left = _insert(node.left, key, value)
      elif key > node.key:
        node.right = _insert(node.right, key, value)
      else:
        node.value = value
      return node

    self.root = _insert(self.root, key, value)

  def search(self, key):
    node = self.root
    while node:
      if key == node.key:
        return node.value
      node = node.left if key < node.key else node.right
    return None

  def delete(self, key):
    def _delete(node, key):
      if node is None:
        return None, False
      if key < node.key:
        node.left, removed = _delete(node.left, key)
        return node, removed
      if key > node.key:
        node.right, removed = _delete(node.right, key)
        return node, removed
      if node.left is None and node.right is None:
        return None, True
      if node.left is None:
        return node.right, True
      if node.right is None:
        return node.left, True
      succ = node.right
      while succ.left:
        succ = succ.left
      node.key, node.value = succ.key, succ.value
      node.right, _ = _delete(node.right, succ.key)
      return node, True

    self.root, removed = _delete(self.root, key)
    return removed

  def height(self):
    def _h(node):
      if node is None:
        return 0
      return 1 + max(_h(node.left), _h(node.right))
    return _h(self.root)

  def is_balanced(self):
    def _check(node):
      if node is None:
        return 0, True
      lh, lb = _check(node.left)
      rh, rb = _check(node.right)
      balanced = lb and rb and abs(lh - rh) <= 1
      return 1 + max(lh, rh), balanced

    _, ok = _check(self.root)
    return ok
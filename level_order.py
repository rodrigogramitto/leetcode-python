
def levelOrder(tree):
  res = []
  q = collections.deque()

  if tree:
    q.append(tree)

    while q:
      val = []

      for i in range(len(q)):
        node = q.popleft()

        if node:
          val.append(node.val)
          if node.left:
            q.append(node.left)
          if node.right:
            q.append(node.right)
      res.append(val)

    return res
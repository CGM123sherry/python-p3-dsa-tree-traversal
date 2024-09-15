# class Tree:
#   def __init__(self, root = None):
#     self.root = root

#   def get_element_by_id(self, id):
#     pass

class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, element_id):
        # Depth-first search using recursion
        return self._dfs(self.root, element_id)

    def _dfs(self, node, element_id):
        # Base case: if node is None, return None
        if not node:
            return None
        
        # If the node's id matches the search id, return the node
        if node.get('id') == element_id:
            return node

        # Recursively search through the children
        for child in node.get('children', []):
            result = self._dfs(child, element_id)
            if result:
                return result
        
        # If no matching node is found, return None
        return None


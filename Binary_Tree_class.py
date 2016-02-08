class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.R_child = None
        self.L_child = None
        self.Parent = None
    def __str__(self):
        return "Value is %s" %(str(self.val))
    def get_value(self):
        return self.val
    def set_right_node(self, R_node):
        self.R_child = R_node
    def set_left_node(self, L_node):
        self.L_child = L_node
    def set_parent(self, parent_node):
        self.Parent = parent_node
    def get_right_node(self):
        return self.R_child
    def get_left_node(self):
        return self.L_child
    def get_parent(self):
        return self.Parent
                        
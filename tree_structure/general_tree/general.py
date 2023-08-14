"""Create general tree data structre."""

class TreeNode:
    def __init__(self, data):
        """
        Create tree class and adding objects of a 
        class (data, children and parent).
        :data type: Any
        :rtype: None
        """
        self.data = data
        self.children = list()
        self.parent = None

    def add_child(self, child):
        """
        Add child method also pointing the parent of that
        added child to the instace of the class.
        :child type: Any
        :rtype: None
        """
        self.child = child
        child.parent = self
        self.children.append(child)

    def present_level(self):
        """
        Finding the Level of the current child
        :rtype: int
        """
        level = 0
        prt = self.parent
        while prt:
            prt = prt.parent
            level += 1
        return level

    def display(self):
        """
        Display all level of the tree and create print function.
        :rtype: None
        """
        print('  ' * self.present_level() + '|--', end = '')
        print(self.data)
        if (self.children):
            for each in self.children:
                each.display()

root = TreeNode('Eletronics')

laptop = TreeNode('Laptop')
root.add_child(laptop)
laptop.add_child(TreeNode('Mac'))
laptop.add_child(TreeNode('Windows'))
laptop.add_child(TreeNode('Linux'))

tv = TreeNode('TV')
root.add_child(tv)
tv.add_child(TreeNode('LG'))
tv.add_child(TreeNode('Samsung'))
tv.add_child(TreeNode('Apple'))
root.display()

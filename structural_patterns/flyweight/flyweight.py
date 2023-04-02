""" The flyweight class contains a portion of the state of a
 tree. These fields store values that are unique for each
 particular tree. For instance, you won't find here the tree
 coordinates. But the texture and colors shared between many
 trees are here. Since this data is usually BIG, you'd waste a
 lot of memory by keeping it in each tree object. Instead, we
 can extract texture, color and other repeating data into a
 separate object which lots of individual tree objects can
 reference.
"""
class TreeType:

    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def print_type(self):
        print("Tree Type - name: %s, color: %s, texture: %s" % (self.name, self.color, self.texture))


"""
 Flyweight factory decides whether to re-use existing
 flyweight or to create a new object.
"""
class TreeFactory:
    tree_types = []

    @classmethod
    def get_tree_type(cls, name, color, texture):
        for tree in TreeFactory.tree_types:
            if tree.name == name and tree.color == color and tree.texture == texture:
                return tree
        tree_type = TreeType(name, color, texture)
        TreeFactory.tree_types.append(tree_type)
        return tree_type


"""
 The contextual object contains the extrinsic part of the tree
 state. An application can create billions of these since they
 are pretty small: just two integer coordinates and one
 reference field.
"""


class Tree:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def print_tree(self):
        print("***********Tree************")
        print("Tree coordinates: %s %s" % (self.x, self.y))
        self.type.print_type()
        print("***************************")


"""
 The Tree and the Forest classes are the flyweight's clients.
 You can merge them if you don't plan to develop the Tree
 class any further.
"""
class Forest:

    trees = []

    def plantTree(self, x, y, name, color, texture):
        type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, type)
        Forest.trees.append(tree)

    def print_forest(self):
        for tree in Forest.trees:
            tree.print_tree()


if __name__ == "__main__":
    f = Forest()
    f.plantTree(1, 3, "mango", "yellow", "grown")
    f.plantTree(1, 2, "apple", "red", "new")
    f.plantTree(2, 3, "mango", "yellow", "grown")
    f.plantTree(3, 3, "mango", "yellow", "new")
    f.print_forest()

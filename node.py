class jsonnode:
    def __init__(self,is_leaf,is_root) -> None:
        self.is_root=is_root
        self.is_leaf=is_leaf

    def leaf_render(self,icon):
        pass

    def node_render(self,icon):
        pass

    def render(self,icon):
        pass

class node(jsonnode):
    def __init__(self,name,level,val,is_last,is_leaf,is_root) -> None:
        super().__init__(is_leaf,is_root)
        self.children=[]
        self.name=name
        self.level=level
        self.val=val
        self.is_last=is_last

    def add_child(self,child):
        self.children.append(child)
    

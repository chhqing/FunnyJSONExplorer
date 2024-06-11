from node import node
from jsonstylefactory import AbstractjsonFactory

class TreeFactory(AbstractjsonFactory):
    def create(self,rootnode):
        return treenode(None,0,False,False,True,rootnode)

class treenode(node):
    def __init__(self, name, level, is_last, is_leaf,is_root,json_text) -> None:
        super().__init__(name,level,json_text,is_last,is_leaf,is_root)
        if self.is_leaf==False:
            i=0
            for key,value in json_text.items():
                if i==len(json_text)-1:
                    is_last=True
                else:
                    is_last=False
                if isinstance(value,dict):
                    is_leaf=False
                else:
                    is_leaf=True
                child=treenode(key,self.level+1,is_last,is_leaf,False,value)
                self.add_child(child)
                i+=1

    def render(self,icon):
        if self.is_leaf:
            return self.leaf_render(icon)
        else:
            return self.node_render(icon)

    def leaf_render(self,icon):
        line=''
        if self.is_last:
            line='└─'
        else:
            line='├─'
        line+=icon.leaficon+self.name
        if self.val!=None:
            line+=': '+self.val
        return [line]
    
    def node_render(self,icon):
        line_list=[]
        if self.is_root==False:
            line=''
            if self.is_last:
                line='└─'
            else:
                line='├─'
            line+=icon.nodeicon+self.name
            line_list.append(line)
        for child in self.children:
            child_line=child.render(icon)
            for i in child_line:
                if self.level==0:
                    line_list.append(i)
                elif self.is_last:
                    line_list.append('   '+i)
                else:
                    line_list.append('│  '+i)
        return line_list
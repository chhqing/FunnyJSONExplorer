from node import node
from jsonstylefactory import AbstractjsonFactory

class RectangleFactory(AbstractjsonFactory):
    def create(self,rootnode):
        return rectanglenode(None,0,False,False,True,rootnode)

class rectanglenode(node):
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
                child=rectanglenode(key,self.level+1,is_last,is_leaf,False,value)
                self.add_child(child)
                i+=1

    def render(self,icon):
        if self.is_leaf:
            line_list=self.leaf_render(icon)
        else:
            line_list=self.node_render(icon)
        if self.is_root:
            line_start=list(line_list[0])
            line_start[0]='┌'
            line_start[len(line_start)-1]='┐'
            line_list[0]=''.join(line_start)
            end=len(line_list)-1
            line_end=list(line_list[end])
            for i in range(len(line_end)):
                if line_end[i]=='│':
                    if i==0:
                        line_end[i]='└'  
                    else:
                        line_end[i]='┴'
                elif line_end[i]==' ':
                    line_end[i]='─'
                elif line_end[i]=='├':
                    line_end[i]='┴'
                    break
            line_end[len(line_end)-1]='┘'
            line_list[end]=''.join(line_end)
        return line_list

    def leaf_render(self,icon):
        line='├─'
        line+=icon.leaficon+self.name
        if self.val!=None:
            line+=': '+self.val
        line+=' '
        for i in range(43-len(line)-2-(self.level-1)*3):
            line+='─'
        line+='─┤'
        return [line]
    
    def node_render(self,icon):
        line_list=[]
        if self.is_root==False:
            line='├─'
            line+=icon.nodeicon+self.name+' '
            for i in range(43-len(line)-2-(self.level-1)*3):
                line+='─'
            line+='─┤'
            line_list.append(line)
        for child in self.children:
            child_line=child.render(icon)
            for i in child_line:
                if self.level==0:
                    line_list.append(i)
                else:
                    line_list.append('│  '+i)
        return line_list
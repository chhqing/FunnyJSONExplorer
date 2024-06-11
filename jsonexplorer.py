from icon import icon_family,icon
import treestyle
import rectanglestyle
class jsonexplorer:
    def __init__(self) -> None:
        self.icon_family=icon_family()
        self.style_family={'tree':treestyle.TreeFactory(),'rectangle':rectanglestyle.RectangleFactory()}

    def builder(self,iconname,stylename,rootnode):
        _icon=self.icon_family.get_icon(iconname)
        _jsonnode=self.style_family[stylename].create(rootnode)
        return _icon,_jsonnode
    
    def explorer(self,icon,jsonnode):
        line_list=jsonnode.render(icon)
        for line in line_list:
            print(line)
    
    def add_style(self,stylename,newfacory):
        self.style_family[stylename]=newfacory
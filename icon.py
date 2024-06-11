class icon:
    def __init__(self,_nodeicon,_leaficon) -> None:
        self.leaficon=_leaficon
        self.nodeicon=_nodeicon

class icon_family:
    def __init__(self) -> None:
        self.all_icon={'default':[' ',' '],'poker':['\u2662','\u2664'],'star':['\u2721','\u2726']}

    def add_icon(self,iconname,leaficon,nodeicon):
        self.all_icon[iconname]=[nodeicon,leaficon]
    
    def get_icon(self,iconname):
        myicon=icon(self.all_icon[iconname][0],self.all_icon[iconname][1])
        return myicon
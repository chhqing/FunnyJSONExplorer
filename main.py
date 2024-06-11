import json
import argparse
from jsonexplorer import jsonexplorer
if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f','--file',type=str,help='json file name',required=True)
    parser.add_argument('-s','--style',type=str,help='json style',default='tree')
    parser.add_argument('-i','--icon',type=str,help='json icon',default='default')
    args=parser.parse_args()
    f=open(args.file,'r')
    content=f.read()
    f.close()
    content=json.loads(content)
    jsonbuilder=jsonexplorer()
    icon,jsonnode=jsonbuilder.builder(args.icon,args.style,content)
    jsonbuilder.explorer(icon,jsonnode)

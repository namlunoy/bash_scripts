'''
Update missing svn when check out
Usage: python update_missing_svn.py -f ./repo_list.xml -i 12,11 -t /work/htban3000v_vn/
-f: name of the repo_list.xml
-t: name folder target
-i: index of the files report check out failed!
'''
import os
import sys
import getopt
import xml.etree.ElementTree as ET
targetPath = ''
def svn_co(src, dest, file, action, rev):
    path = targetPath + dest + file
    print dir  
    if os.access(path, os.F_OK):
        print "path exist"
    else:
        print "path not exist -> create a new one!"
        os.makedirs(path)
     
    cmd = 'svn ' + action + ' --revision ' + rev + ' ' +  src + ' ' + path  + ' --quiet'  ;
    print cmd
    os.system(cmd)
     
     
def main(argv):
    global targetPath
    filePath = ''
    ids = []
    #--print argv
    # parse the arguments  
    try:
        opts, args = getopt.getopt(argv,"f:i:t:")
    except getopt.GetoptError as er_mess:
        print "ERROR: ",er_mess
    # update the arguments
    for opt, arg in opts:
        if opt == '-f':
            filePath = arg
        elif opt == '-t':
            targetPath = arg
        elif opt == '-i':
            ids = arg.split(',')
            # convert string to int
            for i in range(0,len(ids)):
                ids[i] = int(ids[i])
             
    # read xml
    tree = ET.parse(filePath)
    root = tree.getroot()
    items = root.findall('download')
    # check out the missing piece
    for index in ids:
        src     = items[index-1].get('src_path')
        dest    = items[index-1].get('dest_path')
        file    = items[index-1].get('dest_file')
        action  = items[index-1].get('action')
        rev = items[index-1].get('revision')
         
        svn_co(src, dest, file, action, rev)
     
     
if __name__ == "__main__":
    main(sys.argv[1:])

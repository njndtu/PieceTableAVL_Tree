from tree import *
import sys
from editor import *


import pdb

def easyInsert():
    myTree = AVL_Tree() 
    root = None

    root = myTree.insert(root, [1,0,2],0,0) 
    root = myTree.insert(root, [1,0,4],2,0) 
    root = myTree.insert(root, [1,0,5],6,0) 
    print(myTree.inOrder(root,[],True))

    assert(myTree.inOrder(root,[]) == [[1,0,2],[1,0,4],[1,0,5]]  )
    print("passed simple insert")

    myTree = AVL_Tree() 
    root = None

    for i in range(100):
        root = myTree.insert(root, [1,0,2],0,0) 
        root = myTree.insert(root, [1,0,4],2,0) 
        root = myTree.insert(root, [1,0,5],6,0) 
    #print(myTree.inOrder(root,[],True))

    assert(myTree.inOrder(root,[]) == [[1,0,2],[1,0,4],[1,0,5]]*100  )
    print("passed simple insert")
def medInsert():
    myTree = AVL_Tree() 
    root = None

    root = myTree.insert(root, [0,0,11],0,0) 
    root = myTree.insert(root, [1,0,1],0,0) 
    root = myTree.insert(root, [1,0,1],0,0)
  

    print(myTree.inOrder(root,[], True))
    assert(myTree.inOrder(root,[]) == [[1,0,1],[1,0,1],[0,0,11]]  )
    print("passed reverse insert")


def easyReverseInsert():
    myTree = AVL_Tree() 
    root = None

    root = myTree.insert(root, [1,0,2],0,0) 
    root = myTree.insert(root, [1,0,4],2,0) 
    root = myTree.insert(root, [1,0,5],6,0)
    root = myTree.insert(root, [1,0,2],11,0) 
    root = myTree.insert(root, [1,0,4],13,0) 
    root = myTree.insert(root, [1,0,5],17,0) 
    print(myTree.inOrder(root,[],True))

    assert(myTree.inOrder(root,[]) == [[1,0,2],[1,0,4],[1,0,5],[1,0,2],[1,0,4],[1,0,5]]  )
    print("passed simple medium insert")


def medReverseInsert():

    myTree = AVL_Tree() 
    root = None

    root = myTree.insert(root, [1,0,5],0,0) 
    root = myTree.insert(root, [1,0,4],0,0) 
    root = myTree.insert(root, [1,0,2],0,0)
    root = myTree.insert(root, [1,0,5],0,0) 
    root = myTree.insert(root, [1,0,4],0,0) 
    root = myTree.insert(root, [1,0,2],0,0) 

    print(myTree.inOrder(root,[], True))
    assert(myTree.inOrder(root,[]) == [[1,0,2],[1,0,4],[1,0,5],[1,0,2],[1,0,4],[1,0,5]]  )
    print("passed reverse medium insert")


def insert132():
    myTree = AVL_Tree() 
    root = None

    root = myTree.insert(root, [1,0,2],0,0) 
    root = myTree.insert(root, [1,0,5],2,0)

    root = myTree.insert(root, [1,0,4],2,0)
    print(myTree.inOrder(root,[],True))

    print(myTree.inOrder(root,[]))
    assert(myTree.inOrder(root,[]) == [[1,0,2],[1,0,4],[1,0,5]]  )

    print("132 passed")
    
def insert312():
    myTree = AVL_Tree() 
    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],0,0) 
    root = myTree.insert(root, [1,0,4],2,0)

    print(myTree.inOrder(root,[],True))


    print(myTree.inOrder(root,[]))
    assert(myTree.inOrder(root,[]) == [[1,0,2],[1,0,4],[1,0,5]]  )

    print("312 passed")


def easySplitInsert():
    myTree = AVL_Tree() 
    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],2,0) 

    print(myTree.inOrder(root,[],True))


    print(myTree.inOrder(root,[]))
    assert(myTree.inOrder(root,[]) == [[1,0,2],[1,0,2],[1,2,3]]  )
    print("easy split passed")

def doubleSplitInsert():
    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],2,0) 
    root = myTree.insert(root,[1,0,4],1,0)
    root = myTree.insert(root,[1,0,7],9,0)
    print(myTree.inOrder(root,[],True))


    print(myTree.inOrder(root,[]))
    assert(myTree.inOrder(root,[]) == [[1,0,1],[1,0,4],[1,1,1],[1,0,2],[1,2,1],[1,0,7],[1,3,2]]  )

    print("double split passed")


    
def getAll():
    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],2,0) 
    root = myTree.insert(root,[1,0,4],1,0)
    root = myTree.insert(root,[1,0,7],9,0)


    print(myTree.getVals(0,18,root,0))
    print(myTree.inOrder(root,[]))
    assert(myTree.inOrder(root,[]) == myTree.getVals(0,18,root,0) )

    print("get all passed")

def getFragment():
    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root, [1,0,5],0,0)



    print(myTree.getVals(1,3,root,0))
    assert([[1,1,2]] == myTree.getVals(1,3,root,0) )

    print(myTree.getVals(1,5,root,0))
    assert([[1,1,4]] == myTree.getVals(1,5,root,0) )

    
    print(myTree.getVals(0,3,root,0))
    assert([[1,0,3]] == myTree.getVals(0,3,root,0) )

    print("get fragment passed")
    

def getStartToMiddle():
    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],2,0) 
    root = myTree.insert(root,[1,0,4],1,0)
    root = myTree.insert(root,[1,0,7],8,0)


    print(myTree.getVals(0,6,root.left,0))
    assert(myTree.inOrder(root.left,[]) == myTree.getVals(0,6,root.left,0) )

    print("get start to middle passed")


def getMiddleToEnd():
    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],2,0) 
    root = myTree.insert(root,[1,0,4],1,0)
    root = myTree.insert(root,[1,0,7],8,0)


    print(myTree.getVals(6,18,root,0))
    assert([[1,0,2]] + myTree.inOrder(root.right,[]) == myTree.getVals(6,18,root,0) )

    print("get middle to end passed")

def getMiddleToMiddle():
    
    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],0,0) 
    root = myTree.insert(root,[1,0,4],0,0)
    root = myTree.insert(root,[1,0,7],0,0)


    print(myTree.getVals(1,17,root,0))
    # [[1,0,7],[1,0,4],[1,0,2],[1,0,5]]
    assert( [[1,1,7],[1,0,4],[1,0,2],[1,0,4],] == myTree.getVals(1,17,root,0) )

    
 
    
    print("get middle to end passed")


def getRepeat():
    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root,[0,0,11],0,0)
    root = myTree.insert(root,[1,0,2],2,0)
    
    root = myTree.insert(root,[1,2,2],2,0)
    print(myTree.inOrder(root,[],True))
    print(myTree.getVals(1,3,root,0))

    
def deleteAll():
    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],2,0) 
    root = myTree.insert(root,[1,0,4],1,0)
    root = myTree.insert(root,[1,0,7],9,0)

    print(myTree.inOrder(root, [],True))

    #pdb.set_trace()

    root = myTree.delete(0,18,root,0)
    
    print(myTree.inOrder(root, []))
    
    assert( [] == myTree.inOrder(root, []) )

 
    print("delete all passed")

def deleteRoot():
    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],2,0) 
    root = myTree.insert(root,[1,0,4],1,0)
    root = myTree.insert(root,[1,0,7],9,0)

    print(myTree.inOrder(root, []))

    #pdb.set_trace()

    root = myTree.delete(6,8,root,0)
    
    print(myTree.inOrder(root, []))
    
    assert( [[1, 0, 1], [1, 0, 4], [1, 1, 1], [1, 2, 1], [1, 0, 7], [1, 3, 2]]  == myTree.inOrder(root, []) )

    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],2,0) 
    root = myTree.insert(root,[1,0,4],1,0)
    root = myTree.insert(root,[1,0,7],9,0)

    print(myTree.inOrder(root, []))

    #pdb.set_trace()

    root = myTree.delete(0,1,root,0)
    
    print(myTree.inOrder(root, []))
    
    assert( [ [1, 0, 4], [1, 1, 1], [1, 0, 2], [1, 2, 1], [1, 0, 7], [1, 3, 2]]
  == myTree.inOrder(root, []) )

 
    print("delete one whole node passed")


def deletePartial():

    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],2,0) 
    root = myTree.insert(root,[1,0,4],1,0)
    root = myTree.insert(root,[1,0,7],9,0)

    print(myTree.inOrder(root, []))

    #pdb.set_trace()

    root = myTree.delete(9,11,root,0)
    
    print(myTree.inOrder(root, []))
    
    assert( [ [1,0,1],[1, 0, 4], [1, 1, 1], [1, 0, 2], [1, 2, 1], [1, 2, 5], [1, 3, 2]]
  == myTree.inOrder(root, []) )

    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],2,0) 
    root = myTree.insert(root,[1,0,4],1,0)
    root = myTree.insert(root,[1,0,7],9,0)

    print(myTree.inOrder(root, []))

    #pdb.set_trace()

    root = myTree.delete(10,16,root,0)
    
    print(myTree.inOrder(root, []))
    
    assert( [ [1,0,1],[1, 0, 4], [1, 1, 1], [1, 0, 2], [1, 2, 1], [1, 0, 1], [1, 3, 2]]
  == myTree.inOrder(root, []) )

    print( "delete partial no split passed ")


    # the split one

    myTree = AVL_Tree() 

    root = None

    root = myTree.insert(root, [1,0,5],0,0)
    root = myTree.insert(root, [1,0,2],2,0) 
    root = myTree.insert(root,[1,0,4],1,0)
    root = myTree.insert(root,[1,0,7],9,0)

    print(myTree.inOrder(root, []))

    #pdb.set_trace()

    root = myTree.delete(10,15,root,0)
    
    print(myTree.inOrder(root, []))
    
    assert( [ [1,0,1],[1, 0, 4], [1, 1, 1], [1, 0, 2], [1, 2, 1], [1, 0, 1], [1,6,1], [1, 3, 2]]
  == myTree.inOrder(root, []) )

def deleteSpecial():
    myTree = AVL_Tree() 

    root = None
    root = myTree.insert(root,[0,0,1],0,0)
    root = myTree.insert(root, [1,1,1],1,0) 
    root = myTree.insert(root,[1,2,2],2,0)
    root = myTree.insert(root,[0,4,7],4,0)
    print(myTree.inOrder(root, [],True))

    root = myTree.delete(1,3,root,0)
    print(myTree.inOrder(root, [],True))

def editorTest():
    editor = SimpleEditor("Hello World")

    while True:
        print("> " + editor.get_text())
        # for visual debugging
        # cut, copy, past commands, get_paste_text returns current "paste" string , inOrde returns in order traversal of tree, so returns the table essentially
        command = input("(-) cut i j (-) copy i j (-) paste i (-) get_paste_text (-)  inOrder :    ")

        if command == "get_paste_text":
            print("clipboard: |" + editor.get_paste_text()+"|")
        elif command == "inOrder":
            print(editor.piece_table.tree.inOrder(editor.piece_table.root,[]))
            
        elif command[0:2] == "cu":
            inputs = command.split(" ")
            editor.cut(int(inputs[1]),int(inputs[2]))

        elif command[0:2] == "co":
            inputs = command.split(" ")
            editor.copy(int(inputs[1]),int(inputs[2]))


        elif command[0:2] == "pa":
            inputs = command.split(" ")
            editor.paste(int(inputs[-1]))
            


def checkWithOld():
    a = SimpleEditor("hello world")

    for n in range(5):
        if n%2 == 0:
            a.cut_old(1,3)
        else:
            a.paste_old(2)

    b = SimpleEditor("hello world")
    
    for n in range(5
                   ):
        if n%2 == 0:
            b.cut(1,3)
        else:
            b.paste(2)
            
    print(a.get_text_old())
    print(b.get_text())
    
    assert(a.get_text_old() == b.get_text())


    a = SimpleEditor("hello world")

    for n in range(5):
        if n%2 == 0:
            a.copy_old(1,3)
        else:
            a.paste_old(2)

    b = SimpleEditor("hello world")
    
    for n in range(5):
        if n%2 == 0:
            b.copy(1,3)
        else:
            b.paste(2)
            
    print(a.get_text_old())
    print(b.get_text())
    
    assert(a.get_text_old() == b.get_text())
    print("check with old implementation passed")
    
def AVL_TreeTest():

    easyInsert()
    medInsert()
    easyReverseInsert()
    medReverseInsert()
    insert132()
    insert312()
    easySplitInsert()
    doubleSplitInsert()

    print("insert tests passed")

    getAll()
    getFragment()
    getStartToMiddle()
    getMiddleToEnd()


    print("get value tests passed")

    deleteAll()
    deleteRoot()
    deletePartial()

    print(" delete passsed " )

    


    
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        pdb.run('AVL_TreeTest()')
        pdb.run('editorTest()')

    else:
        checkWithOld()
        AVL_TreeTest()
        #editorTest()
        #deleteSpecial()
        
    print("Everything passed")

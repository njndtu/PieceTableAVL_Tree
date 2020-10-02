import pdb
# original implementation of avl tree taken from geeksforgeeks, modified for use for piece table and added functions modifications on the tree. 



# Python code to insert a node in AVL tree 
  
# Generic tree node class 
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val
        # val is of the form [buffer, start index, length  ]
        
        self.left = None
        self.right = None

        # number of chars in left/right subtree, sum of all nodes in that subtree's val[2] ~ length
        self.leftLength = 0
        self.rightLength = 0
        
        self.height = 1
  

class AVL_Tree(object): 
  
    # Recursive function to insert val in  
    # subtree rooted with node and returns 
    # new root of subtree.
    # val is of the form [buffer, start index, length  ]
    # key refers to the document index that the "node" should belong to
    # cur keeps track of the document index the node we are at is on. When at root we know that the idx this node starts at in the document is root.left_length + cur (0 when at root). Whenever we traverse to a right child we need to update cur so as to know how many chars were at the left subtree for the parent of this right child. Whenever we go to a left child we do not need to update.
    # to get idx a node belongs in doc, cur+root.left_length 
    
    def insert(self, root, val , key ,cur):
      
        # Step 1 - Perform normal BST
     
        
        if not root:
            return TreeNode(val)
        
        # insert idx is located in left subtree
        elif key <= root.leftLength + cur:
            root.left = self.insert(root.left, val , key, cur)

        # insert idx is located in right subtree
        # >= becayse root.leftLength+cur is starting index, adding the length will give me starting index of one to the right 
        elif key >= root.leftLength + cur + root.val[2] : 
            root.right = self.insert(root.right, val, key, root.leftLength+cur+root.val[2])

        # insert idx in current node string location, need to split current node
        else:
           # insert idx is at beginning (wrong case ignore)
            '''
            if key == root.leftLength + cur:

                newNode = TreeNode(val)

                newNode.left = root.left
                newNode.right = self.insert(root.right,root.val, root.leftLength+cur+val[2]  , root.leftLength+cur+val[2])

                newNode.height = 1 + max(self.getHeight(newNode.left), self.getHeight(newNode.right))
                
                newNode.leftLength = self.getLeftLength(newNode.left)+ self.getLength(newNode.left) +self.getRightLength(newNode.left) 
                newNode.rightLength = self.getRightLength(newNode.right) + self.getLength(newNode.right) + self.getLeftLength(newNode.right)
                return newNode
            '''
            
           # else:
        # split into two

        #
            insertIdx = key - (root.leftLength+cur )

            newNode = TreeNode(val)

            oldLeft = [root.val[0],root.val[1],insertIdx]
            oldRight = [root.val[0],root.val[1]+insertIdx,root.val[2]-insertIdx]

            newNode.left = self.insert(root.left,oldLeft, root.leftLength+cur , cur)

            newNode.right = self.insert(root.right,oldRight, root.leftLength+cur+val[2]  , root.leftLength+cur+val[2]+ (root.val[2] - insertIdx), )

            newNode.height = 1 + max(self.getHeight(newNode.left), 
                                    self.getHeight(newNode.right))

            newNode.leftLength = self.getLeftLength(newNode.left)+ self.getLength(newNode.left) +self.getRightLength(newNode.left) 
            newNode.rightLength = self.getRightLength(newNode.right) + self.getLength(newNode.right) + self.getLeftLength(newNode.right)
                
              

            return newNode
        #pdb.set_trace()
  
        # Step 2 - Update the height, leftLength, rightLength of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right))

        root.leftLength = self.getLeftLength(root.left)+ self.getLength(root.left) + self.getRightLength(root.left)
        root.rightLength = self.getRightLength(root.right)+ self.getLength(root.right) + self.getLeftLength(root.right)

        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases

        #pdb.set_trace()

        # Case 1 - Left Left 
        if balance > 1 and key <= root.left.leftLength+cur: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.leftLength+cur+root.right.val[2]: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.leftLength+cur+root.left.val[2]: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key <= root.right.leftLength+cur: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root


    # delete entire node, i is index the node has as its first index in document
    def deleteEntire(self,i,root,cur):

        if not root :
            return root

        curStart = root.leftLength+cur
        curEnd = curStart+root.val[2] -1

        if i > curEnd:
        # need to move right
            root.right = self.deleteEntire(i,root.right,root.leftLength+cur+root.val[2])

        elif i < curStart:
            # need to move left
            root.left = self.deleteEntire(i,root.left,cur)

        else:
            #found
            if root.left is None:
                    temp = root.right 
                    root = None
                    return temp 
  
            elif root.right is None:
                temp = root.left
                root = None
                return temp 
  
            temp = self.getMinValueNode(root.right)
            root.val = temp.val

            # "removed" root by swapping with next node
            
            root.right = self.delete( root.leftLength + cur + root.val[2] , root.leftLength + cur + root.val[2] * 2 , root.right , root.leftLength + cur + root.val[2])

        if not root:
            return root

        # Step 2 - Update the height, leftLength, rightLength of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                        self.getHeight(root.right))

        root.leftLength = self.getLeftLength(root.left)+ self.getLength(root.left) + self.getRightLength(root.left)
        root.rightLength = self.getRightLength(root.right)+ self.getLength(root.right) + self.getLeftLength(root.right)

        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 

        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases

        #pdb.set_trace()

        # Case 1 - Left Left 
        if balance > 1 and i <= root.left.leftLength+cur: 
            return self.rightRotate(root) 

        # Case 2 - Right Right 
        if balance < -1 and i > root.right.leftLength+cur+root.right.val[2]: 
            return self.leftRotate(root) 

        # Case 3 - Left Right 
        if balance > 1 and i > root.left.leftLength+cur+root.left.val[2]: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 

        # Case 4 - Right Left 
        if balance < -1 and i <= root.right.leftLength+cur: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 



        return root
  

    # delete document[i:j] , returns root of modified tree
    def delete(self,i,j,root,cur):

        #pdb.set_trace()
      
        if not root:
            return root

        # curStat and curEnd are inclusive
        curStart = root.leftLength+cur
        curEnd = curStart+root.val[2] -1

        #print(i,j,curStart,curEnd)



        # two main cases, there is stuff to delete in this node, or no

        # need to first move to correct subtree
        if i > curEnd:
            # need to move right
            root.right = self.delete(i,j,root.right,root.leftLength+cur+root.val[2])
           

        elif j-1 < curStart:
            # need to move left
            root.left = self.delete(i,j,root.left,cur)
           
        else:
            # some operations need to be done on this node

            # 1, delete current node and move left or right, or both
            # 2, modify current node, and move left or right
            
            need = j-i
     
            if (i < curStart and j-1 > curEnd):
                # delete current move left and right
                root.left = self.delete(i,curStart,root.left,cur)
                root.right = self.delete(curEnd+1,j,root.right,root.leftLength+cur+root.val[2])
                root = self.deleteEntire(curStart,root,cur)
                
                
            elif (i == curStart and j-1 == curEnd):
                # delete current node
                root = self.deleteEntire(curStart,root,cur)
            elif (i < curStart and j-1 == curEnd):
                # delete current node and move left
                root.left = self.delete(i,curStart,root.left,cur)
                root = self.deleteEntire(curStart,root,cur)
            elif (i == curStart and j-1 > curEnd):
                # delete current node and move right
                root.right = self.delete(curEnd+1,j,root.right,root.leftLength+cur+root.val[2])
                root = self.deleteEntire(curStart,root,cur)
                
            elif (i > curStart and j-1 >= curEnd):
                # move right(optional) but modify current
                if j > curEnd:
                    root.right = self.delete(curEnd+1,j,root.right,root.leftLength+cur+root.val[2])
                # need to shorten length 
                
                root.val[2] = i - curStart
            elif (j-1 < curEnd and i <= curStart):
                
                # move left(optional) but modify current
                if i < curStart:
                    root.left = self.delete(i,curStart,root.left,cur)

                root.val[1] += (j - curStart)
                root.val[2] = curEnd - (j-1)

            else :
                # split
                oldLeft = [root.val[0], root.val[1], i - curStart]
                oldRight = [root.val[0], root.val[1] + (j- curStart),curEnd - (j-1) ]

                root.left = self.insert(root.left, oldLeft, curStart , cur)
                root.right = self.insert(root.right, oldRight, curEnd + 1 , root.leftLength+cur+root.val[2])

                # delete self
                root = self.deleteEntire(curStart,root,cur)
            


        if not root:
            return root

        # Step 2 - Update the height, leftLength, rightLength of the  
        # ancestor node

        
        root.height = 1 + max(self.getHeight(root.left), 
                        self.getHeight(root.right))

        root.leftLength = self.getLeftLength(root.left)+ self.getLength(root.left) + self.getRightLength(root.left)
        root.rightLength = self.getRightLength(root.right)+ self.getLength(root.right) + self.getLeftLength(root.right)

        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 

        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases

        #pdb.set_trace()

        # Case 1 - Left Left 
        if balance > 1 and i <= root.left.leftLength+cur: 
            return self.rightRotate(root) 

        # Case 2 - Right Right 
        if balance < -1 and i > root.right.leftLength+cur+root.right.val[2]: 
            return self.leftRotate(root) 

        # Case 3 - Left Right 
        if balance > 1 and i > root.left.leftLength+cur+root.left.val[2]: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 

        # Case 4 - Right Left 
        if balance < -1 and i <= root.right.leftLength+cur: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 


        
        return root


    # return list of node "vals" corresponding document[i:j]
    # starts at i not including j
    
    def getVals(self,i,j,root,cur):
        
        if not root:
            return []

        
        
        curStart = root.leftLength+cur
        curEnd = curStart+root.val[2] -1

        if i > curEnd:
            # need to search right
            return self.getVals(i,j,root.right,root.leftLength+cur+root.val[2])
        elif j <= curStart:
            return self.getVals(i,j,root.left,cur)

        need = j-i


        # 3 cases, only need to go left, only need to go right or need to explore left and right


        if ( i >= curStart and j-1 <= curEnd):
            # all in here
            return [[root.val[0],root.val[1] + (i-curStart),need ]]
        else:
            if ( i < curStart and j-1 > curEnd):
                # both directions
                return self.getVals(i,curStart,root.left,cur) + [root.val] + self.getVals(curEnd+1,j,root.right, root.leftLength+cur+root.val[2])
                
            elif (i < curStart):
                # go left 
                return self.getVals(i,curStart,root.left,cur) + [[root.val[0],root.val[1],j-curStart]]

            elif (j-1 > curEnd):
                # go right
                return [[root.val[0], root.val[1]+ (i-curStart), curEnd - i + 1 ]] + self.getVals(curEnd+1,j,root.right,root.leftLength+cur+root.val[2])


        


   
    def getMinValueNode(self, root): 
        current = root

        if root is None or root.left is None: 
            return root 
  
        return self.getMinValueNode(root.left) 
  
      


    
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 

        # Perform rotation 
        y.left = z 
        z.right = T2 

        # Update heights , leftLength, rightLength
        z.height = 1 + max(self.getHeight(z.left), 
                            self.getHeight(z.right))

        z.leftLength = self.getLeftLength(z.left)+ self.getLength(z.left) + self.getRightLength(z.left)
        z.rightLength = self.getRightLength(z.right) + self.getLength(z.right) + self.getLeftLength(z.right)


        y.height = 1 + max(self.getHeight(y.left), 
                            self.getHeight(y.right))

        y.leftLength = self.getLeftLength(y.left)+ self.getLength(y.left) + self.getRightLength(y.left)
        y.rightLength = self.getRightLength(y.right) + self.getLength(y.right) + self.getLeftLength(y.right)


        # Return the new root 
        return y


    
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights , leftLength, rightLength
        z.height = 1 + max(self.getHeight(z.left), 
                            self.getHeight(z.right))

        z.leftLength = self.getLeftLength(z.left)+ self.getLength(z.left) + self.getRightLength(z.left)
        z.rightLength = self.getRightLength(z.right) + self.getLength(z.right) + self.getLeftLength(z.right)


        y.height = 1 + max(self.getHeight(y.left), 
                            self.getHeight(y.right))

        y.leftLength = self.getLeftLength(y.left)+ self.getLength(y.left) + self.getRightLength(y.left)
        y.rightLength = self.getRightLength(y.right) + self.getLength(y.right) + self.getLeftLength(y.right)
        
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height

    def getLeftLength(self,root):
        if not root:
            return 0
        return root.leftLength

    def getRightLength(self,root):
        if not root:
            return 0
        return root.rightLength

    def getLength(self,root):
        if not root:
            return 0
        return root.val[2]
    
    # left - right
    # positive means more on left, negative means more on right
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def inOrder(self, root, order, moreInfo= False): 
        if not root: 
            return order

        if not root.left:
            if moreInfo:
                order.append(root.val+[root.leftLength,root.rightLength,root.height])
            else:
                order.append(root.val)

        else:
            self.inOrder(root.left, order, moreInfo)
            
            if moreInfo:
                order.append(root.val+[root.leftLength,root.rightLength,root.height])
            else:
                order.append(root.val)
            
        self.inOrder(root.right, order, moreInfo) 

        return order
  



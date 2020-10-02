
from tree import *

class PieceTable:


    def __init__(self,document):
        # create two buffers
        # a read only buffer to load in the original document, orig
        # a append only buffer for newly appended text, add

        self.buffers = [[i for i in document],[]]
        
        self.tree = AVL_Tree()
        self.root = None
        self.root = self.tree.insert(self.root, [0,0,len(document)] ,0,0)
    

    
        
        
        
        
    def returnDoc(self):
        return self.substr(0,self.root.leftLength+self.root.rightLength+self.root.val[2])
        
        
    # returns string
    def substr(self,i,j):
        document =  self.tree.getVals(i,j,self.root,0)
        final = ""
        for i in document:
            for j in self.buffers[i[0]][i[1]:i[1]+i[2]]:
                final+=j
            
        return final


    def add(self,text,key):
        newEntry = [1,len(self.buffers[1]),len(text)]
        for i in text:
            self.buffers[1].append(i)

        self.root = self.tree.insert(self.root,newEntry,key,0)

    def remove(self,i,j):
        self.root = self.tree.delete(i,j,self.root,0)
        
        

class SimpleEditor:
    def __init__(self, document):

        # document appears to be in form of a string
        
        self.document = document

        self.piece_table = PieceTable(document)
        
        self.dictionary = set()
        # On windows, the dictionary can often be found at:
        # C:/Users/{username}/AppData/Roaming/Microsoft/Spelling/en-US/default.dic
        with open("/usr/share/dict/words") as input_dictionary:
            for line in input_dictionary:
                words = line.strip().split(" ")
                for word in words:
                    self.dictionary.add(word)

        self.paste_text = ""


    # let n be length of entire doc, m be j-i
    
    # O(n-m)+ O(m) = O(n)
    def cut_old(self, i, j):
        self.paste_text = self.document[i:j]
        self.document = self.document[:i] + self.document[j:]

    # O(m)
    def copy_old(self, i, j):
        self.paste_text = self.document[i:j]

    # O(n+m)
    def paste_old(self, i):
        self.document = self.document[:i] + self.paste_text + self.document[i:]


    # returns the contents of the documents 
    def get_text_old(self):
        return self.document

    # returns count of mispellings. 
    def misspellings_old(self):
        result = 0
        for word in self.document.split(" "):
            if word not in self.dictionary:
                result = result + 1
        return result

    

    def cut(self,i,j):

        # sub
        self.paste_text = self.piece_table.substr(i,j)
        self.piece_table.remove(i,j)
       

        
    def copy(self,i,j):
        self.paste_text = self.piece_table.substr(i,j)

        
    def paste(self,i):
        self.piece_table.add(self.paste_text,i)


        
    def get_text(self):
        return self.piece_table.returnDoc()

    def get_paste_text(self):
        return self.paste_text
        
    
    def misspellings(self):

        result = 0
        
        for word in self.piece_table.returnDoc().split(" "):
            if word not in self.dictionary:
                result = result + 1

        return result


    
import timeit

class EditorBenchmarker:
    new_editor_case = """
from __main__ import SimpleEditor
s = SimpleEditor("{}")"""

    editor_cut_paste = """
for n in range({0}):
    if n%2 == 0:
        if {1}:
            s.cut(1, 3)
        else:
            s.cut_old(1,3)
    else:
        if {1}:
            s.paste(2)
        else:
            s.paste_old(2)
"""


    editor_copy_paste ="""
for n in range({0}):
    if n%2 == 0:
        if {1}:
            s.copy(1, 3)
        else:
            s.copy_old(1,3)
    else:
        if {1}:
            s.paste(2)
        else:
            s.paste_old(2)
"""

    editor_get_text = """
for n in range({0}):
    if {1}:
        s.get_text()
    else:
        s.get_text_old()"""

    editor_mispellings = """
for n in range({0}):
    if {1}:
        s.misspellings()
    else:
        s.misspellings_old()"""

    editor_paste = """
s.copy(1, 3)
for n in range({0}):
    if {1}:
        s.paste(2)
    else:
        s.paste_old(2)"""



    editor_cut_paste_old = """
for n in range({}):
    if n%2 == 0:
        s.cut_old(1, 3)
    else:
        s.paste_old(2)"""

    editor_copy_paste_old = """
for n in range({}):
    if n%2 == 0:
        s.copy_old(1, 3)
    else:
        s.paste_old(2)"""

    editor_get_text_old = """
for n in range({}):
    s.get_text_old()"""

    editor_mispellings_old = """
for n in range({}):
    s.misspellings_old()"""


    def __init__(self, cases, N):
        self.cases = cases
        self.N = N
        self.editor_cut_paste_new = self.editor_cut_paste.format(N[0],"True")
        self.editor_copy_paste_new = self.editor_copy_paste.format(N[1],"True")
        self.editor_get_text_new = self.editor_get_text.format(N[2],"True")
        self.editor_mispellings_new = self.editor_mispellings.format(N[3],"True")
        self.editor_paste_new = self.editor_paste.format(N[4],"True")
        
        self.editor_cut_paste_old = self.editor_cut_paste.format(N[0],"False")
        self.editor_copy_paste_old = self.editor_copy_paste.format(N[1],"False")
        self.editor_get_text_old = self.editor_get_text.format(N[2],"False")
        self.editor_mispellings_old = self.editor_mispellings.format(N[3],"False")
        self.editor_paste_old = self.editor_paste.format(N[4],"False")


    def benchmark(self):
        for idx,case in enumerate(self.cases):
            '''
            print("Evaluating case: {}".format(idx))
            new_editor = self.new_editor_case.format(idx)
            cut_paste_time = timeit.timeit(stmt=self.editor_cut_paste,setup=new_editor,number=1)
            print("{} cut paste operations took {} s".format(self.N, cut_paste_time))
            copy_paste_time = timeit.timeit(stmt=self.editor_copy_paste,setup=new_editor,number=1)
            print("{} copy paste operations took {} s".format(self.N, copy_paste_time))
            get_text_time = timeit.timeit(stmt=self.editor_get_text,setup=new_editor,number=1)
            print("{} text retrieval operations took {} s".format(self.N, get_text_time))
            mispellings_time = timeit.timeit(stmt=self.editor_mispellings,setup=new_editor,number=1)
            print("{} mispelling operations took {} s".format(self.N, mispellings_time))

            print("original implementation -----------------------------")
            
            print("Evaluating case: {}".format(idx))
            new_editor = self.new_editor_case.format(idx)
            cut_paste_time = timeit.timeit(stmt=self.editor_cut_paste_old,setup=new_editor,number=1)
            print("{} cut paste operations took {} s".format(self.N, cut_paste_time))
            copy_paste_time = timeit.timeit(stmt=self.editor_copy_paste_old,setup=new_editor,number=1)
            print("{} copy paste operations took {} s".format(self.N, copy_paste_time))
            get_text_time = timeit.timeit(stmt=self.editor_get_text_old,setup=new_editor,number=1)
            print("{} text retrieval operations took {} s".format(self.N, get_text_time))
            mispellings_time = timeit.timeit(stmt=self.editor_mispellings_old,setup=new_editor,number=1)
            print("{} mispelling operations took {} s".format(self.N, mispellings_time))

            print("------------------------------------------------------")
            '''
            print("Evaluating case : {} lengthed input doc".format(len(case)))
            new_editor = self.new_editor_case.format(case)
            cut_paste_time = timeit.timeit(stmt=self.editor_cut_paste_new,setup=new_editor,number=1)
            copy_paste_time = timeit.timeit(stmt=self.editor_copy_paste_new,setup=new_editor,number=1)

            get_text_time = timeit.timeit(stmt=self.editor_get_text_new,setup=new_editor,number=1)
            mispellings_time = timeit.timeit(stmt=self.editor_mispellings_new,setup=new_editor,number=1)

            paste_time = timeit.timeit(stmt=self.editor_paste_new,setup=new_editor,number=1)

            
            new_editor = self.new_editor_case.format(case)
            cut_paste_time_old = timeit.timeit(stmt=self.editor_cut_paste_old,setup=new_editor,number=1)
            copy_paste_time_old = timeit.timeit(stmt=self.editor_copy_paste_old,setup=new_editor,number=1)

            get_text_time_old = timeit.timeit(stmt=self.editor_get_text_old,setup=new_editor,number=1)
            mispellings_time_old = timeit.timeit(stmt=self.editor_mispellings_old,setup=new_editor,number=1)

        
            paste_time_old = timeit.timeit(stmt=self.editor_paste_old,setup=new_editor,number=1)

            
            print("{} cut paste operations was faster: {}, {} vs {}".format(self.N[0], cut_paste_time < cut_paste_time_old, cut_paste_time, cut_paste_time_old))
            print("{} copy paste operations was faster: {}. {} vs {}".format(self.N[1], copy_paste_time < copy_paste_time_old, copy_paste_time, copy_paste_time_old))
            print("{} text retrieval operations was faster: {}, {} vs {}".format(self.N[2], get_text_time < get_text_time_old, get_text_time, get_text_time_old))
            print("{} mispelling operations was faster: {}, {} vs {}".format(self.N[3], mispellings_time < mispellings_time_old, mispellings_time, mispellings_time_old))

            print("{} paste operations was faster: {}, {} vs {}".format(self.N[4], paste_time < paste_time_old, paste_time, paste_time_old))
            


            
if __name__ == "__main__":
    longStr = "a"*1000000

    Ns = [100,100,100,100,10000]
    b1 = EditorBenchmarker(["hello friends",longStr], Ns)

    b1.benchmark()


    # paste faster with 1,000,000 input, 10,000 inserts


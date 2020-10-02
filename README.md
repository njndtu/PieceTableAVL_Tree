
# Editing Text

I decided to try to speed up some naive string editting operations, this being the cut, copy, paste operations. Given some naive implementations of operations that involve manipulating a document, the goal is to find ways to speed these operations up. Strings are immutable in python, as such cutting and pasting via slicing is not as efficient as it could be (naive way does this).  The operations are O(n), n being the size of the document in characters. The entire document is copied whenever these operations are called. The first thought was to store the document in some data structure instead of simply a string. A quick google search and looking around yielded the idea of a piece table (https://en.wikipedia.org/wiki/Piece_table). The idea behind this is to store two buffers. One for the original document, and the other for any thing you append to the document. The piece table is a table that stores entries containing information on which buffer it belongs to, the starting index and length. To get the string corresponding to the entry, you go to the buffer, go to the index and grab the string. However another data structure is needed to store the table itself and access the entries in an efficient way.  A binary tree comes to mind, a self balancing one will ensure log(n) operations which is something to aim for. I decided to try to implement an AVL tree. GeeksforGreeks had a very basic implementation of an AVL tree and I started out with their code. However to be able to use the AVL tree in this case, many modifications had to be made. First, the nodes store the piece table entries. Secondly, there needs to be additional meta data tracked and updated in the nodes to allow one to know the location a node/entry is in the overall document. Otherwise, in order to know the position of the node in the document, one would have to traverse thru the entire tree via an in order traversal in order to output the position. This defeats the purpose of using a binary tree.  

The objective of this project is to implement a piece table with a AVL tree that allows quicker modifications of a string.

# Files and running program
editor.py : contains the SimpleEditor class, and benchmarking. 
tree.py : Implementation of AVL tree to work with piece table
test.py : contains test cases and an interactive command line string editor. Realtime calls to cut, copy, paste and some other utility functions can be used to help debug if the text editor is working. The test cases are not exhaustive, there could still be mistakes in the code.  
```
python test.py 
```
Will output a lot of debugging output, at the bottom you will see
```
> Hello World 
> (-) cut i j (-) copy i j (-) paste i (-) get_paste_text (-)  inOrder : 
```
"Hello world" is the document loaded into the editor.

To cut something, type in cut i j, to get document[i:j] removed, and so on for the other commands.

The command get_paste_text returns the currently cut-ed or copied string.

Typing inOrder will output the tree in order. It will look something like this
```
[[...],[...],[...]]
```
Each [. . .] is an entry in the piece table. Contents of the size 3 [...] are the buffer, starting index and length respectively. 

Make sure inputs are valid, otherwise it will not work. Valid inputs being the correct indices corresponding to the i and j parameters passed in. 


# Design Decisions
Let M be the size of the entirez
document and N the size of the extracted string.

My implementation to extract(copy) strings offers no speed up. 

In the original implementation it will take O(N) to copy the string, while the new implementation will be O(log(M) + N) as there is the need to traverse the tree to get to the string.

Traversing the tree will be slower then indexing a string.

 1. Paste : Paste is done via an insert into the tree. The insertion can be done in O(log(M)) time. Which is better then the original O(M) way.
 2. Cut : Cut is made of two separate commands. Copy and delete. Delete is hard to analyze because it depends on the number of nodes that span the string you want to delete. Delete is implemented as a recursive delete, if there are nodes that need to be deleted in the left or right subtrees those deletions are performed first. Each deletion will O(log(H)) which is the height of the node to be deleted. To simplify things, deletion takes O(log(M)) and copying takes O(log(M) + N ) which is still better than the O(M) cut previously

# Benchmarks

When testing my implementation against the old implementation it was slower for the first few benchmark cases that I tried. I was very alarmed about this result and thought that I have implemented something incorrectly. Upon ramping up the input document length and the number of operations involved in the benchmark experiment the new implementation eventually beat out the old in terms of speed. The only operations that could not be beaten are the text retrieval operations. As indexing will always be faster than tree traversing. More could be done in bench-marking to find the exact specifications that will cause the original implementation to start slowing down with respect to the new implementation. This specification refers to for example the types of operations, number of operations and the length of the original input document,
 
# Remarks
Not going to lie, I spent more time than expected. Initially figuring out the data structures to use came pretty quickly to me. I thought to myself that implementing it was not going to be that hard perhaps. Boy was I wrong. Actually figuring the intricacies out took a long time. And still I am not 100% confident the code works as intended, however it does pass the tests I wrote. Additionally, the code is messy and many parts can be refactored and cleaned up. I did not follow a specific coding style/practice consistently so viewing ability may be less efficient  and variable naming may potentially be confusing. It was a fun experience trying to implement something like this.
The implementation of the balanced binary tree took more time than expected. I was tempted to just go with a linked list implementation, but knowing that a faster way in the form of the tree was available motivated me to keep going.

# Additional Extensions in future
Providing benchmarks to compare the two implementations. There can be many scenarios to test out. Repeated pastes, inserts, combinations, etc.

Adding more text editing functionality. An example of this is a undo/redo function. 

 


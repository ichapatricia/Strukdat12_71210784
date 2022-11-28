class Node:
    def __init__(self, data, parent):
        self._data = data
        self._children = []
        self._parent = parent

class Tree:
    def __init__(self,data , Node):
        self._data = data
        self._children = []
        self._Node = Node
        
    def addChild(self, data):
        self._children.append(data)

   
    def operator(self):
        return self._data

 
    def parent(self):
        return self._parent

  
    def children(self):
        return self._children

   
    def isRoot(self):
        return self._parent is None

   
    def isExternal(self):
        return len(self._children) == 0

    def minus(node):
        for i in node.children():
            minus(i)
        print(node.operator(), end = ' ')

    def sibling(node):
        jlm += 0
        for i in node.parent().children():
            jlm += 1

val300 = Node(300, None)
val9 = Node(9, val300)
val1 = Node(1, val300)
val11 = Node(11, val9)
val99 = Node(99, val9)
val17 = Node(17,val1)
val28= Node(28, val11)
val72= Node(72,val11)
val90 = Node(90,val99)
val33 = Node(33,val99)
val2 = Node(2,val17)
val4 = Node(4,val17)
val43 = Node(43, val17)
val9.addChild(val11)
val9.addChild(val99)
val1.addChild(val17)
val11.addChild(val28)
val11.addChild(val72)
val99.addChild(val90)
val99.addChild(val33)
val17.addChild(val2)
val17.addChild(val4)
val17.addChild(val43)
val300.addChild(val9)
val300.addChild(val1)

if __name__ =='__main__':
    val300 = Node(300)
    t = Tree(val300) #Level 0
#Level 1 parent 120
    val9 = t.addChild(val300, 9) 
    val1 = t.addChild(val300, 1)
 
    #Level 2 parent 9
    val11 = t.addChild(val9, 11) 
    val99 = t.addChild(val9, 99) 
 
    #Level 2 parent 1
    val17 = t.addChild(val1, 17) 
 
    #Level 3 parent 11
    val28 = t.addChild(val11, 28) 
    val72 = t.addChild(val11, 72)
 
    #Level 3 parent 99
    val90 = t.addChild(val99, 90) 
    val33 = t.addChild(val99, 33)
 
    #Level 3 parent 17
    val17 = t.addChild(val17, 2)
    val17 = t.addChild(val17, 4)
    val17 = t.addChild(val17, 43)
 
    # No 2. #
    print(f'Sisa hasil pengurangan dari node {val300.data} adalah {t.minus(val300)}')
 
    # No 3. #
    print(f'Total nilai dari semua saudara pada node {val90.data} adalah {t.sibling(val90)}')



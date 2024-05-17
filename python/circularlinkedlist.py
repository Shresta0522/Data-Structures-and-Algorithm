# Circular Linked list

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class CircularLinkedList :
  def __init__(self):
    self.head = None

  def insertAtBegin(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.head.next =self.head
    elif self.head != None and self.head.next == self.head:
      self.head.next = new_node
      new_node.next = self.head
      self.head = new_node
    else:
      current_node = self.head
      while(current_node.next != self.head):
        current_node = current_node.next

      current_node.next = new_node
      new_node.next = self.head
      self.head = new_node


    self.printAll()

  def insertAtLast(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.head.next =self.head
      self.printAll()

    else:
      current_node = self.head
      while(current_node.next != self.head):
        current_node = current_node.next

      current_node.next = new_node
      new_node.next = self.head
      self.printAll()
  def insertAtIndex(self,data, index):
    new_node = Node(data)
    if  index ==0:
      self.insertAtBegin(data)

    else:
      current_node = self.head
      position =0
      while(current_node.next != self.head and position != index-1):
        current_node = current_node.next
        position +=1
      print()
      if position+1 < index:
        print("Invalid Index")
        self.printAll()
        return
      else:
        new_node.next = current_node.next
        current_node.next = new_node
    self.printAll()


  def removeAtBegin(self):
    if self.head == None:
      print("Circular linked list is empty")
    else:
      if self.head .next == self.head:
        self.head == None
      else:
        current_node = self.head
        while (current_node.next != self.head):
          current_node = current_node.next
        current_node.next = self.head.next
        self.head = self.head.next
      self.printAll()
  def removeAtLast(self,):
    if self.head == None:
      print("Circular linked list is empty")
      self.printAll()
      return
    else:
      if self.head.next == self.head:
        self.head == None
      else:
        current_node = self.head
        while (current_node.next.next != self.head):
          current_node = current_node.next
        current_node.next = self.head

    self.printAll()
  def removeAtIndex(self, index):
    if index ==0 :
      self.removeAtBegin()
    else:
      current_node = self.head
      position =0
      while (current_node.next != self.head and position != index-1):
        current_node = current_node.next
        position +=1
      if current_node.next == self.head:
        print("Invalid Index")
        self.printAll()
        return
      current_node.next = current_node.next.next
    self.printAll()

  def updateAtIndex(self,data):
    pass
  def printAll(self):
    current_node = self.head
    st =""
    while current_node:
      st+= str(current_node.data) +'--->'
      current_node = current_node.next
      if current_node == self.head:
        break
    print(st)

cll = CircularLinkedList()
cll.insertAtLast(1)
cll.insertAtBegin(2)
cll.insertAtBegin(5)
cll.removeAtBegin()
cll.insertAtBegin(4)
cll.insertAtLast(8)
cll.insertAtBegin(3)
cll.insertAtLast(7)
cll.removeAtBegin()
cll.removeAtLast()
cll.insertAtIndex(7,3)
cll.insertAtIndex(9,5)
cll.insertAtIndex(9,10)
cll.insertAtIndex(3,0)
cll.insertAtIndex(23,1)
cll.removeAtIndex(1)
cll.printAll()
cll.removeAtIndex(7)
cll.removeAtIndex(4)

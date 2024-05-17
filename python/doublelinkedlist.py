# DOUBLE LINKED LIST

class Node:
  def __init__(self,data):
    self.prev = None
    self.data = data
    self.next = None

class DoubleLinkedList:
  def __init__(self):
    self.head = None

  def insertAtBegin(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.printAll()
      return
    else:
      current_node = self.head
      current_node.prev = new_node
      new_node.next = current_node
      self.head = new_node
    self.printAll()

  def insertAtEnd(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.printAll()
      return
    else:
      current_node = self.head
      while (current_node.next!= None):
        current_node = current_node.next
      current_node.next = new_node
      new_node.prev = current_node
      self.printAll()


  def insertAtIndex(self,data,index):
    position = 0
    new_node = Node(data)
    if index==0 and self.head == None:
      self.head = new_node
    elif index>0 and self.head ==None:
      print("Double lInked list is empty and the index is not Zero")
      return
    else:
      current_node = self.head
      if index == 0 and self.head != None:
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.printAll()
      else:
        while(current_node != None and position != index-1):
          current_node = current_node.next
          position +=1
        if position+1 < index:
          print("Invalid index ")
          return
        else:
          print(current_node.data)
          new_node.prev = current_node
          new_node.next = current_node.next
          current_node.next = new_node
          self.printAll()

  def removeAtBegin(self):
    if self.head == None:
      print("Double Linked List is empty")
      self.printAll()
      return
    elif self.head.next == None:
      self.head = None
      self.printAll()
      return
    else:
      self.head = self.head.next
      self.prev = None
      self.printAll()
      return
  def removeAtEnd(self):
    if self.head == None:
      print("Double Linked List is empty")
      self.printAll()
    else:
      current_node = self.head
      while(current_node.next.next != None):
        current_node = current_node.next
      current_node.next = None
      self.printAll()

  def removeAtIndex(self,index):
    if self.head ==None:
      print("List is Empty")
      return
    elif index == 0 and self.head != None:
      self.head = self.head.next
      self.printAll()
      return
    else:
      position = 0
      current_node = self.head
      while(current_node != None and position != index-1):
        current_node = current_node.next
        position +=1
      if position+1 < index:
        print("Invalid index")
      else:
        current_node.next = current_node.next.next
        current_node.next.next.prev = current_node
        self.printAll()

  def updateAtIndex(self,data,index):
    pass

  def printAll(self):
    if self.head is None:
        print("Linkedlist is empty")
        return
    current_node = self.head
    st = ''
    while (current_node != None):
      st+= str(current_node.data) +'<--->'
      current_node = current_node.next
    print(st)

dll = DoubleLinkedList()

dll.insertAtBegin(8)
dll.insertAtBegin(7)
dll.insertAtBegin(6)
dll.insertAtEnd(1)
dll.removeAtBegin()
dll.removeAtEnd()
dll.insertAtBegin(5)
dll.insertAtIndex(6,1)
dll.insertAtIndex(4,0)
dll.insertAtIndex(4,7)
dll.removeAtIndex(1)
dll.removeAtIndex(9)
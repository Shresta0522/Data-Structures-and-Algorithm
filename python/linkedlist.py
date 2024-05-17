# SINGLE LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    # insertion of the node
    def insertAtBegin(self,data):
      new_node =Node(data)
      if self.head ==None:
          self.head = new_node
          return
      else:
          new_node.next=self.head
          self.head = new_node
          return


    def insertAtEnd(self,data):
      new_node=Node(data)
      if self.head == None:
        self.head = new_node
      else:
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        new_node = Node(data)
        current_node.next = new_node
        # print(current_node.data)



    def insertAtIndex(self,data,index):
      new_node = Node(data)
      current_node = self.head
      position = 0
      if index < 0:
        print("Invalid Index")
      if index == 0:
        self.insertAtBegin(data)
      else:
        while(current_node != None and position != index-1):
          if current_node.next != None and position <=index-1 :
            position += 1
            current_node = current_node.next
            # print(current_node.data)
          elif (current_node.next == None and position ==index-1):
            position += 1
            current_node = current_node.next
            # print(current_node.data)
          else:
            print("Invalid Index")
            return

        new_node.next = current_node.next
        current_node.next = new_node


    # removing the node

    def removeAtBegin(self):
      if self.head == None:
        print("LinkedList is empty nothing to remove")
      else:
        current_node = self.head
        if current_node.next == None:
          self.head = None
          return
        self.head = current_node.next



    def removeAtEnd(self):
        if self.head == None:
          print("LinkedList is empty nothing to remove")
        else:
          current_node = self.head
          while(current_node.next.next):
            current_node = current_node.next
          current_node.next = None

    def removeAtIndex(self,index):
      if index <0 :
        print("Invalid Index")
        return
      if index ==0:
        self.removeAtBegin()
      else:
        position =0
        current_node = self.head
        while(current_node != None and position != index-1):
          if current_node.next == None :
            print("Invalid Index")
            return

          position+=1
          current_node = current_node.next
          # print(current_node.data)

        current_node.next = current_node.next.next




    # update the node
    def updateNodeData(self,data,index) :
        pass

    # Print all
    def printAll(self):
      if self.head is None:
        print("Linkedlist is empty")
        return
      current_node = self.head
      st = ''
      while (current_node != None):
        st+= str(current_node.data) +'--->'
        current_node = current_node.next
      print(st)

ll = LinkedList()
ll.insertAtBegin(1)
ll.insertAtBegin(7)
ll.insertAtBegin(9)
ll.insertAtBegin(5)
ll.insertAtBegin(8)
ll.insertAtEnd(2)
ll.printAll()
ll.removeAtBegin()
ll.printAll()
ll.removeAtEnd()
ll.printAll()
ll.insertAtEnd(2)
ll.printAll()
ll.insertAtIndex(4,3)
ll.printAll()
ll.insertAtIndex(6,1)
ll.printAll()
ll.insertAtIndex(6,15)
ll.printAll()
ll.insertAtIndex(6,7)
ll.printAll()
ll.insertAtIndex(1,0)
ll.printAll()
ll.removeAtIndex(3)
ll.printAll()
ll.removeAtIndex(7)
ll.printAll()
ll.removeAtIndex(5)
ll.printAll()
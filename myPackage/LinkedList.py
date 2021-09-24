#from Node import Node
from myPackage.Node import Node

class LinkedList:
    def __init__( self ):
        self.head = None
    
    def insertLast( self, val ):
        newNode = Node( val )
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
    
    def printList( self ):
        current = self.head
        while current != None:
            print( current.val )
            current = current.next

    def insertFirst( self, val ):
        newNode = Node( val )
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def findNode( self, val ): #This will find the first one only...
        current = self.head
        while current != None:
            if current.val == val:
                print(f'Found the {val} (◠ ‿ ◠)')
                return current
            current = current.next
        print(f'{val} Was not found')
        return None

    def deleteNode( self, val ):
        if self.head == None:
            return None
        current = self.head
        previous = self.head
        if self.head.val == val:
            self.head = self.head.next
            current.next = None
        else:
            while current != None and current.val != val:
                previous = current
                current = current.next
            if current != None:
                previous.next = current.next
                current.next = None

    def printnextnext (self):
        current = self.head
        print (current.next.val)

    def insertAtPosition( self, index, val ):
        newNode = Node( val )
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            if current.val == index:
                    newNode.next = current
                    self.head = newNode
            else:
                while current.next != None:
                    if current.next.val == index:
                        newNode.next = current.next
                        current.next = newNode
                        return None
                    else:
                        current = current.next
            print(f'Insert {index} Was not found')

    def lenght (self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def insertAtIndex(self, index, val):
        newNode = Node( val )
        # if self.head == None and index == 0: // Not Needed
        #     self.head = newNode // Not Needed
        # elif self.head == None and index != 0: // Not Needed 
        #     return None // Not Needed
        if index <= self.lenght():
            if index == 0:
                self.insertFirst(val)
            else:
                indexcount = 0
                current = self.head
                while indexcount < index-1:
                    indexcount += 1
                    current = current.next
                newNode.next = current.next
                current.next = newNode
        else:
            print (f'It is not possible to use that index')
                



    
    # def insertAtIndex(self, index, val):
    #     newNode = Node( val )
    #     count = 0
    #     current = self.head
    #     while current != None:
    #         count += 1
    #         current = current.next
    #     if count == 0:
    #         print (f'The list is empty')
    #     elif count < index + 1:
    #         print (f'The index does not exist')
    #     elif index == 0:
    #         newNode.next = self.head
    #         self.head = newNode
    #     else:
    #         indexcheck = 0
    #         while indexcheck < index-1:
    #             current = current.next
    #             indexcheck += 1
    #         newNode.next = current.next
    #         current.next = newNode
    #         return None

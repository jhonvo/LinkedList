from Node import Node

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
        pass

    def findNode( self, val ):
        pass
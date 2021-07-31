#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:50:50 2021

@author: lesliecastelan

Professor: Hangjie Ji
Discussion: 3B
"""

#%%

class Node: 
    """Node class for individual units within LinkedList class
    
    Has next member function, therefore for usage within singly linked
    lists. Of special importance: has __eq__ method
        
    """
    
    def __init__(self,data=None): 
        self.data =data
        self.next = None

        
    def __str__(self): 
        return str(self.data)
    
    def __repr__(self):
        return repr(self.data)
    
    def __eq__(self,other):
        """
        Enables comparison of node data to a value
        """
        
        return self.data == other 
    

class LinkedList:
    """Singly linked list class called LinkedList. 
    
    Methods to note: append, len, __getitem__, __setitem__, add
    """
    
    def __init__(self, data=None):
        current_node = Node(data)
        
        if current_node == None: #if this is the case, have to adjust self.first 
                                        #to real node in append 
            self.first= current_node
            self.last= current_node
            self.n=0
        
        else:
            self.first= current_node
            self.last= current_node
            #print("self.last in linked list:", self.last)
            self.n=0
            self.n = self.n +1
            #print("self.n in Linked Lisg method:", self.n)
    
    def append(self,data):
        """Creates new node and appends to end of LinkedList
        
        Takes in data and creates new node from that. 
        """
        
        new_node= Node(data)
        #print("New_node:" ,new_node)
        #print("self.last:", self.last)
        #print("self.first", self.first)
        #print("self.first.next:", self.first.next)
        #print("self.last.next:", self.last.next)
    
        
        if self.n ==1:
            self.first.next = new_node
            #print("self.first.next after setting to new_node:", self.first.next)
            
            #print("if n=1 self.last.next before changing last to new node:" ,self.last.next)
            
            self.last =new_node #do not have to manually change self.last.next to None 
            #print("if n=1 self.last.next after changing:", self.last.next)
            
            self.n +=1 
            #print("counter at end:", self.n)
            
            
            
        else: 
            self.last.next= new_node
            #print("Self.last.next:" ,self.last.next)
        
            self.last=new_node
            #print("after making last new node, self.last is:", self.last)
            #print("self.last.next after changing self.last to new node:", self.last.next)
        
            self.n +=1 
            #print("counter at end:", self.n)
        
    def __iter__(self):
       # print("iterator called")
        self.current_iter= self.first #reset to the first node 
        return self.generator()
    
    #def __next__(self):
     #   if self.current_iter == None:
      #      raise StopIteration
            
       # counter= self.current_iter 
        #self.current_iter = self.current_iter.next 
        #return counter 
        
    def generator(self): #raise error
        for i in range(0, self.n):
            counter = self.current_iter
            yield counter
            self.current_iter=self.current_iter.next
            
            if i >= self.n:
                raise IndexError
                
        
    
    def __len__(self):
        return self.n
    
    def __str__(self):
        """Allows for LinkedList to be printed out with arrows
        in between. 
        """
        
        node =self.first
      
        linked_list= "["
        
        while (node != None): #make sure node not at end
            if node.next == None: #stop right before end 
                linked_list += str(node)
                break 
            
            linked_list += str(node) + "->"
            node = node.next
        linked_list += "]"
        return linked_list #return concatendated string 
    
    def __repr__(self):
        node =self.first
        
        linked_list= "["
        
        while (node != None):
            if node.next == None:
                linked_list += str(node)
                break 
            linked_list += str(node) + "->"
            node = node.next
        linked_list += "]"
        return linked_list
    
    
    def __getitem__(self, index): #how do I get this to not return a value if IndexError
        
        if index >= self.n:
            raise IndexError("List index out of range")
                
                
        node=self.first
        counter =0 
            
        while( counter < index):
            node=node.next
            counter +=1
        return str(node)
        
    
            
    def __setitem__(self,index, value):

        if index >= self.n: #or should it be just greater than? 
            raise IndexError("List index out of range")
                
        node=self.first
        counter =0
                
        while( counter < index):
            node=node.next
            counter +=1
        node.data= value
            
    
            
    def __add__(self, other):
        """ Allows adding new node to LinkedList using + operator """
        
        new_linked_list=LinkedList(self.first.data)
        
        #print(type(new_linked_list))
        
        i= self.first.next
        #print(i)
        while (i != None):
            new_linked_list.append(i.data)
            #print(new_linked_list)
            i = i.next 
            #print(i)
            
        #print("Self:", self)
        new_linked_list.append(other)
        #print("After appending other to new_linked_list:", self)
        #print("New linked list:", new_linked_list)
        return new_linked_list
    


#n= Node(10)

#print(repr(n))
#print(str(n))
#print(n)

#a=LinkedList(0)
#a.append(1)
#a.append(2)

#print("7 points if this works")
#for n in a:
#    print(n)
    
#print("2 points if this works")
#for n in a:
#    print(n)

#print("")
    
#print("3 points if both of these work")
#for n in a:
#   if n == 2:
#        break
#    else:
#        print(n)

#print("")
   
#for n in a:
#    if n == 2:
#        break
#    else:
#        print(n)

#print("")

#a.append(3)
#a.append(4)
#a.append(5)
#a.append(6)
#a.append(7)
#a.append(8)

#print("1 points if this works")
#print(len(a))
#print("")

#print("1 points if this works")
#print(str(a))
#print("")

#print("1 points if this works")
#print(repr(a))
#print("")

#print("1 points each. That is, 2 points if the output of the next line is correct")
#print("before a[5] was:", a[5])
#a[5] = 20
#print("after, a[5] is now:", a[5])

#print("")

#print("2 points for correct operation of +")
#a+9 # doesn't modify a
#print(a)

#a = a+9 # appends 9 to a
#print(a)


#print("")


#print("1 points for raising correct IndexError")
#try:
#    print(a[999])
#    a[999]=10
#except IndexError as e:
#    print(e)

#%%





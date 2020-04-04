"""
LINKED LIST

"""
class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None 

class linked_list:
    def __init__(self):
        self.head = node()
    #add elements to linked list
    def insert(self,data):
        new_data = node(data)
        last_data = self.head
        while last_data.next != None:
            last_data = last_data.next
        last_data.next = new_data

    #get the length of Linked List
    def length(self):
        last_element = self.head
        total_elements = 0
        while last_element.next != None:
            total_elements += 1
            last_element = last_element.next
        return total_elements
    
    #print Linked List
    def print_linked_list(self):
        elements = []
        cur_element = self.head
        while cur_element.next != None:
            cur_element = cur_element.next
            elements.append(cur_element.data)
        print(elements)

    #feath data from Linked List
    def get(self,index):
        if index >= self.length():
            print("index is out of range !!!")
            return None
        else:
            cur_index = 0
            cur_element = self.head
            while True:
                cur_element = cur_element.next
                if cur_index == index:
                    return cur_element.data
                cur_index += 1

    #remove data from Linked List
    def delete(self,index):
        if index >= self.length():
            print("index is out of range !!!")
            return None
        cur_index = 0
        cur_element = self.head
        while True:
            last_element = cur_element
            cur_element = cur_element.next
            if cur_index == index:
                last_element.next = cur_element.next
                return 
            cur_index += 1

lis = linked_list()

lis.print_linked_list()

#insert data
lis.insert(1)
lis.insert(2)
lis.insert(3)
lis.insert(4)
lis.insert(5)
#print Linked List
lis.print_linked_list()

#fetch present data
print(lis.get(3))

#feacth absent data which gives error
print(lis.get(8))

#delete present data
lis.delete(3)
lis.print_linked_list()

#delete absent data which gives error
lis.delete(8)
lis.print_linked_list()

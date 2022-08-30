class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = -1

    def add_at_tail(self, data) -> bool:
        self.getall()
        print("") 
        print("")
        if (self.head == None):
            temp = Node(data)
            self.head = temp
            temp.next = temp
            temp.previous = temp

        else:
            temp = Node(data)
            temp.previous = self.head.previous
            temp.next = self.head
            self.head.previous.next=temp
            self.head.previous = temp
        self.count = self.count+1

        self.getall()
        print("")
        print("")
        return True


    def add_at_head(self, data) -> bool:
        self.getall()
        print("")
        print("")
        if (self.head == None):
            temp = Node(data)
            self.head = temp
            temp.next = temp
            temp.previous = temp

        else:
            temp = Node(data)
            temp.previous = self.head.previous
            temp.next = self.head
            self.head.previous.next=temp
            self.head.previous = temp
            self.head = temp
        self.count = self.count+1

        self.getall()
        print("")
        print("")
        return True

    def add_at_index(self, index, data) -> bool:
        self.getall()
        print("")
        print("")

        if (self.count < index):
            return False

        ind = 0
        n = self.head
        while(1):
            if(index ==0):
                return self.add_at_head(data)

            elif(index == ind):
                break
            
            else:
                ind = ind + 1
                n = n.next
                
            
        temp = Node(data)
        temp.previous = n.previous
        temp.next = n
        n.previous.next=temp
        n.previous = temp
        self.count = self.count+1

        self.getall()
        print("")
        print("")

        return True


    def get(self, index) -> int:

        if (self.count < index):
            return -1
        
        ind = 0
        n = self.head
        while(1):
            if(index == ind):
                return n.data
                break
            
            else:
                ind = ind + 1
                n = n.next
                
    def getall(self) -> int:

        n = self.head
        print("head : ",self.head)
        for z in range (0,self.count):
            print (n,"  ",n.previous.data," ",n.data,"  ",n.next.data)
            n = n.next



    def delete_at_index(self, index) -> bool:


        self.getall()
        print("")
        print("")

        if (self.count < index):
            return False

        ind = 0
        n = self.head
        while(1):    
            if(index == ind):
                break
            
            else:
                ind = ind + 1
                n = n.next

        if (index == 0):
                if (self.count != 0):
                    self.head = n.next
                else:
                    self.head = NULL
    
        n.previous.next = n.next
        n.next.previous = n.previous
        self.count = self.count-1
        del n

        self.getall()
        print("")
        print("")

        return True

    def get_previous_next(self, index) -> list:
        ind = 0
        n = self.head
        while(1):
            if(index == ind):
                break
            
            else:
                ind = ind + 1
                n = n.next

                
                
        self.getall()
        print("")
        print("")
        return [n.previous.data , n.next.data]

# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)

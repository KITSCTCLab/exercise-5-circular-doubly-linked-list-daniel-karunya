class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
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
        print(self.head,temp.data,temp.next,temp.next,"add tail")
        return True


    def add_at_head(self, data) -> bool:
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
        print(self.head,temp.data,temp.next,temp.next,"add head")
        return True

    def add_at_index(self, index, data) -> bool:
        ind = 0
        n = self.head
        while(1):
            if(index ==0):
                if (self.head == None):
                    temp = Node(data)
                    self.head = temp
                    temp.next = temp
                    temp.previous = temp
                    break

                else:
                    temp = Node(data)
                    temp.previous = self.head.previous
                    temp.next = self.head
                    self.head.previous.next=temp
                    self.head.previous = temp
                    self.head = temp
                    break

            elif(index == ind):
                break
            
            else:
                ind = ind + 1
                n = n.next
                print(n)
                if (ind == index):
                    break
            
        temp = Node(data)
        temp.previous = n.previous
        temp.next = n
        n.previous.next=temp
        n.previous = temp
        print(self.head,temp.data,temp.next,temp.next,"add index",index,ind)
        return True


    def get(self, index) -> int:
        ind = 0
        n = self.head
        while(1):
            if(index == ind):
                break
            
            else:
                ind = ind + 1
                n = n.next
                break

        return n.data

    def delete_at_index(self, index) -> bool:
        ind = 0
        n = self.head
        while(1):
            if(index == ind):
                break
            
            else:
                ind = ind + 1
                n = n.next
                break

        n.previous.next = n.next
        n.next.previous = n.previous

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
                break

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
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)

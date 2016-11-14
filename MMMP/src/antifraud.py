# Created by: Nicholas Cantafio
# Feature 1 Fufillment: Checking past transactions

import pandas as pd

old_data = pd.read_csv('paymo_input/batch_payment.txt')
starting = pd.read_csv('paymo_input/stream_payment.txt')

def repeat_transaction():  # used to see if both parties interacted before
    list1 = []
    try:
        for node in starting:
            if node.id1 & node.id2 == old_data.id1 & old_data.id2:
                return list1.append('trusted')
        else:
                return list1.append('unverified')
    except:
        pass


    f1 = open('./paymo_output/output.txt', 'w')
    f1.write(list1)
    f1.close()


def second_degree():  # searching for second degree of seperation to limit messages with user
    list2 = []
    try:
        for x in starting:
            #for when depth of search is less than 2
        return list2.append('trusted')
    except:
        list2.append('unverified')

    f2 = open('./paymo_output/output2.txt', 'w')
    f2.write(list2)
    f2.close()



# using depth first search to find shortest path from parties
def thrid_degree():  # using the batch_payment.txt and each iteration of stream
    list3 =  []
    visited, stack = set(), [starting]
     try:
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(old_data[vertex] - visited)
     else:
        return list3.append('unverified')

    f3 = open('./paymo_output/output3.txt', 'w')
    f3.write(list3)
    f3.close()

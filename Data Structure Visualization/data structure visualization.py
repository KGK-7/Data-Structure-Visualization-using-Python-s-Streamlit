import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import heapq
import pandas as pd
from collections import deque, ChainMap

# Linked List Implementation
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = LinkedListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next
            return True
        return False

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

# Stack Visualization
def stack_visualization():
    st.header("Stack Visualization")
    st.write("A stack is a linear data structure that follows the LIFO (Last In First Out) principle.")

    stack = st.session_state.get('stack', [])
    action = st.selectbox("Choose an action for the stack", ["Push", "Pop", "View Stack"])
    if action == "Push":
        element = st.text_input("Enter the element to push")
        if st.button("Push to Stack"):
            stack.append(element)
            st.session_state['stack'] = stack
            st.success(f"'{element}' pushed to stack")
    elif action == "Pop":
        if stack:
            popped_element = stack.pop()
            st.session_state['stack'] = stack
            st.success(f"'{popped_element}' popped from stack")
        else:
            st.warning("Stack is empty")
    st.write("Current Stack:", stack)

# Queue Visualization
def queue_visualization():
    st.header("Queue Visualization")
    st.write("A queue is a linear data structure that follows the FIFO (First In First Out) principle.")

    queue = st.session_state.get('queue', deque())
    action = st.selectbox("Choose an action for the queue", ["Enqueue", "Dequeue", "View Queue"])
    if action == "Enqueue":
        element = st.text_input("Enter the element to enqueue")
        if st.button("Enqueue to Queue"):
            queue.append(element)
            st.session_state['queue'] = queue
            st.success(f"'{element}' enqueued to queue")
    elif action == "Dequeue":
        if queue:
            dequeued_element = queue.popleft()
            st.session_state['queue'] = queue
            st.success(f"'{dequeued_element}' dequeued from queue")
        else:
            st.warning("Queue is empty")
    st.write("Current Queue:", list(queue))

# ChainMap Visualization
def chainmap_visualization():
    st.header("ChainMap Visualization")
    st.write("ChainMap is a container that manages multiple dictionaries as a single unit.")

    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    chain = ChainMap(dict1, dict2)
    st.write("Dictionaries:", dict1, dict2)
    st.write("Combined ChainMap:", dict(chain))

# Deque Visualization
def deque_visualization():
    st.header("Deque Visualization")
    st.write("A deque is a double-ended queue that allows insertion and deletion from both ends.")

    deque_data = st.session_state.get('deque', deque())
    action = st.selectbox("Choose an action for the deque", ["Append Left", "Append Right", "Pop Left", "Pop Right", "View Deque"])
    if action == "Append Left":
        element = st.text_input("Enter the element to append left")
        if st.button("Append Left"):
            deque_data.appendleft(element)
            st.session_state['deque'] = deque_data
            st.success(f"'{element}' appended to the left of deque")
    elif action == "Append Right":
        element = st.text_input("Enter the element to append right")
        if st.button("Append Right"):
            deque_data.append(element)
            st.session_state['deque'] = deque_data
            st.success(f"'{element}' appended to the right of deque")
    elif action == "Pop Left":
        if deque_data:
            popped_element = deque_data.popleft()
            st.session_state['deque'] = deque_data
            st.success(f"'{popped_element}' popped from the left of deque")
        else:
            st.warning("Deque is empty")
    elif action == "Pop Right":
        if deque_data:
            popped_element = deque_data.pop()
            st.session_state['deque'] = deque_data
            st.success(f"'{popped_element}' popped from the right of deque")
        else:
            st.warning("Deque is empty")
    st.write("Current Deque:", list(deque_data))

# Priority Queue Visualization
def priority_queue_visualization():
    st.header("Priority Queue Visualization")
    st.write("A priority queue is a data structure where each element is associated with a priority.")

    pq = st.session_state.get('priority_queue', [])
    action = st.selectbox("Choose an action for the priority queue", ["Insert", "Remove", "View Priority Queue"])
    if action == "Insert":
        element = st.text_input("Enter the element")
        priority = st.number_input("Enter the priority", step=1)
        if st.button("Insert into Priority Queue"):
            heapq.heappush(pq, (priority, element))
            st.session_state['priority_queue'] = pq
            st.success(f"'{element}' with priority '{priority}' inserted into priority queue")
    elif action == "Remove":
        if pq:
            removed_element = heapq.heappop(pq)
            st.session_state['priority_queue'] = pq
            st.success(f"'{removed_element[1]}' with priority '{removed_element[0]}' removed from priority queue")
        else:
            st.warning("Priority Queue is empty")
    
    if pq:
        st.table(pd.DataFrame(pq, columns=["Priority", "Element"]))
    else:
        st.warning("Priority Queue is empty")

# Binary Tree Visualization
def binary_tree_visualization():
    st.header("Binary Tree Visualization")
    st.write("A binary tree is a hierarchical structure where each node has at most two children.")
    
    root = st.number_input("Enter Root Node Value", step=1)
    left = st.number_input("Enter Left Child Value", step=1)
    right = st.number_input("Enter Right Child Value", step=1)
    
    if st.button("Visualize Binary Tree"):
        G = nx.DiGraph()
        G.add_edges_from([(root, left), (root, right)])
        
        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='black')
        st.pyplot(plt)

# Graph Visualization
def graph_visualization():
    st.header("Graph Visualization")
    st.write("A graph is a non-linear data structure consisting of nodes and edges.")
    
    edge_input = st.text_area("Enter edges (e.g., '1 2, 2 3, 3 4')")
    edges = [tuple(map(int, edge.split())) for edge in edge_input.split(",")]
    
    if st.button("Visualize Graph"):
        G = nx.Graph()
        G.add_edges_from(edges)
        
        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, edge_color='black')
        st.pyplot(plt)

# Linked List Visualization
def linked_list_visualization():
    st.header("Linked List Visualization")
    st.write("A linked list is a linear data structure where each node points to the next node in the sequence.")

    ll = st.session_state.get('linked_list', LinkedList())
    action = st.selectbox("Choose an action for the linked list", ["Insert", "Delete", "View Linked List"])
    if action == "Insert":
        value = st.text_input("Enter the value to insert")
        if st.button("Insert into Linked List"):
            ll.insert(value)
            st.session_state['linked_list'] = ll
            st.success(f"'{value}' inserted into the linked list")
    elif action == "Delete":
        value = st.text_input("Enter the value to delete")
        if st.button("Delete from Linked List"):
            if ll.delete(value):
                st.session_state['linked_list'] = ll
                st.success(f"'{value}' deleted from the linked list")
            else:
                st.warning(f"'{value}' not found in the linked list")
    st.write("Current Linked List:", ll.display())

# Heap Visualization
def heap_visualization():
    st.header("Heap Visualization")
    st.write("A heap is a special tree-based data structure that satisfies the heap property.")
    
    heap = st.session_state.get('heap', [])
    action = st.selectbox("Choose an action for the heap", ["Insert", "Remove Min", "View Heap"])
    if action == "Insert":
        value = st.number_input("Enter the value to insert", step=1)
        if st.button("Insert into Heap"):
            heapq.heappush(heap, value)
            st.session_state['heap'] = heap
            st.success(f"'{value}' inserted into the heap")
    elif action == "Remove Min":
        if heap:
            removed_value = heapq.heappop(heap)
            st.session_state['heap'] = heap
            st.success(f"'{removed_value}' removed from the heap")
        else:
            st.warning("Heap is empty")
    st.write("Current Heap:", heap)

# Main Application
def main():
    st.title("Data Structure Visualizer")
    st.sidebar.title("Choose Data Structure")
    options = [
        "Stack", "Queue", "ChainMap", "Deque", "Priority Queue", 
        "Binary Tree", "Graph", "Linked List", "Heap"
    ]
    choice = st.sidebar.selectbox("Select a Data Structure", options)

    if choice == "Stack":
        stack_visualization()
    elif choice == "Queue":
        queue_visualization()
    elif choice == "ChainMap":
        chainmap_visualization()
    elif choice == "Deque":
        deque_visualization()
    elif choice == "Priority Queue":
        priority_queue_visualization()
    elif choice == "Binary Tree":
        binary_tree_visualization()
    elif choice == "Graph":
        graph_visualization()
    elif choice == "Linked List":
        linked_list_visualization()
    elif choice == "Heap":
        heap_visualization()

if __name__ == "__main__":
    main()

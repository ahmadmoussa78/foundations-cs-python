class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:

  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node
      
def display(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

def search_and_delete(self, value):
    current = self.head
    prev = None
    while current:
      if current.data == value:
        if prev:
          prev.next = current.next
        else:
          self.head = current.next
        current = current.next
      else:
        prev = current
        current = current
      
def is_palindrome(s):
  s = s.lower().replace(" ", "")
  stack = []
  queue = []

  for char in s:
    stack.append(char)
    queue.insert(0, char)

  while stack:
    if stack.pop() != queue.pop(0):
      return False

  return True

class Student:
  def __init__(self, name, midterm_grade, final_grade, good_attitude):
      self.name = name
      self.midterm_grade = midterm_grade
      self.final_grade = final_grade
      self.good_attitude = good_attitude

  def __repr__(self):
      return f"{self.name}: Midterm Grade - {self.midterm_grade}/100, Final Grade - {self.final_grade}/100, Good Attitude: {self.good_attitude}"
class PriorityQueue:
  def __init__(self):
      self.students = []

  def add_student(self, student):
      self.students.append(student)
      self.students.sort(key=lambda x: (not x.good_attitude, x.final_grade, x.midterm_grade), reverse=True)

def interview_student(self):
      if self.students:
          student = self.students.pop()
          print(f"Interviewing: {student.name}")
      else:
             print("No students in the queue.")
def display_queue(self):
      print("Priority Queue:")
      for student in self.students:
          print(student)
      print()


def add_vertex(graph, vertex):
  if vertex not in graph:
      graph[vertex] = []
def main():
  name = input("Enter your name: ")
  print(f"Welcome, {name}!")

def add_edge(graph, vertex1, vertex2):
  if vertex1 in graph and vertex2 in graph:
      graph[vertex1].append(vertex2)
      graph[vertex2].append(vertex1)

def remove_vertex(graph, vertex):
  if vertex in graph:
      del graph[vertex]
      for vertices in graph.values():
          if vertex in vertices:
              vertices.remove(vertex)
def remove_edge(graph, vertex1, vertex2):
  if vertex1 in graph and vertex2 in graph:
      if vertex2 in graph[vertex1]:
          graph[vertex1].remove(vertex2)
          graph[vertex2].remove(vertex1)

def display_vertices_with_degree(graph, degree):
  print(f"Vertices with a degree of {degree} or more:")
  for vertex in graph:
      if len(graph[vertex]) >= degree:
          print(vertex)

  while True:
    print("\nMain Menu:")
    print("1. Singly Linked List")
    print("2. Check if Palindrome")
    print("3. Priority Queue")
    print("4. Evaluate an Infix Expression")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      linked_list = SinglyLinkedList()
      while True:
        print("\nSingly Linked List Menu:")
        print("a. Add Node")
        print("b. Display Nodes")
        print("c. Search for & Delete Node")
        print("d. Return to main menu")

        sub_choice = input("Enter your choice: ")

        if sub_choice == "a":
          value = int(input("Enter a numerical value: "))
          linked_list.append(value)
        elif sub_choice == "b":
          linked_list.display()
        elif sub_choice == "c":
          value = int(input("Enter a value to search and delete: "))
          linked_list.search_and_delete(value)
        elif sub_choice == "d":
          break

    elif choice == "2":
      string = input("Enter a string: ")
      if is_palindrome(string):
        print("The string is a palindrome.")
      else:
        print("The string is not a palindrome.")
    elif choice == "3":
      print("Priority Queue functionality not implemented.")
    elif choice == "4":
      print("Evaluate Infix Expression functionality not implemented.") 
    elif choice == "5":
      graph = {}
      while True:
          print("\nGraph Operations:")
          print("a. Add vertex")
          print("b. Add edge")
          print("c. Remove vertex")
          print("d. Remove edge")
          print("e. Display vertices with a degree of X or more")
          print("f. Return to main menu")

          sub_choice = input("Enter your choice: ")

          if sub_choice == "a":
              vertex = input("Enter vertex to add: ")
              add_vertex(graph, vertex)
          elif sub_choice == "b":
              vertex1 = input("Enter first vertex: ")
              vertex2 = input("Enter second vertex: ")
              add_edge(graph, vertex1, vertex2)
          elif sub_choice == "c":
              vertex = input("Enter vertex to remove: ")
              remove_vertex(graph, vertex)
          elif sub_choice == "d":
              vertex1 = input("Enter first vertex: ")
              vertex2 = input("Enter second vertex: ")
              remove_edge(graph, vertex1, vertex2)
          elif sub_choice == "e":
              degree = int(input("Enter the degree value: "))
              display_vertices_with_degree(graph, degree)
          elif sub_choice == "f":
              break
          else:
              print("Invalid choice. Please enter a valid option.")
    elif choice == "6":
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
  main()

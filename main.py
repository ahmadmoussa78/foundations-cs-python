class Node:

  def __init__(self, data):
    self.data = data
    self.next = None




def main():
  name = input("Enter your name: ")
  print(f"Welcome, {name}!")

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

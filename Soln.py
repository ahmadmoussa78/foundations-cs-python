import json
# https://youtu.be/9N6a-VLBa2I?si=GBNRa3YhaLPKmKYZ
# https://youtu.be/-51jxlQaxyA?si=AYUfJNq0UhzdewB4
# https://youtu.be/-51jxlQaxyA?si=AYUfJNq0UhzdewB4
# used more than one refernce
import requests
from bs4 import BeautifulSoup
#https://youtu.be/O6nnVHPjcJU?si=10UGLIZb4pGRWC0A
middic = {"tabs": []}
tabs = []

def openTab():
  # worst case =>O(1)
  title = input("Enter title of the new tab: ")
  url = input("Enter url of the new tab: ")
  #title

  if title and url:
    new_tab = {}
    new_tab["title"] = title
    new_tab["title"] = title
    new_tab["nested_tab"] = []
    tabs.append(new_tab)
    print("New tab opened successfully")
  else:
    print("Invalid Input")

  def closeTab(i):  # worst case =>O(n),Where N is the size of tabs list
  #https://www.w3schools.com/python/python_variables_global.asp
  #https://youtu.be/4m8gBTTjoMI?si=0BD-wiSdmY9nVLS-(indians==Top)
  # gloabl is used to declare a variable inside a local scope.This means thats tabs variable will be avaliable in all the functions.
  if i == "":
    if tabs:
      tabs[-1]
      tabs = tabs[:-1]
      print(tabs)
    else:
      print("There are no opened tabs to close")
  elif not i.isdigit():
    print("Invalid input. Please enter a valid index.")
  elif len(tabs) == 0:
    print("There is no opened tabs to close")
  elif 0 <= int(i) < len(tabs):
    index_to_remove = int(i)
    tabs = (tabs[:index_to_remove] + tabs[index_to_remove + 1:])
    print("The tab at index", i, "has been closed")
    print(tabs)
  else:
    print("Invalid input.Please enter an valid index")

def switchTab(num, data):  # worst case =>O(n),Where N is the size of tabs list
  global tabs
  index = -1 if num == "" else int(num)

  if not tabs:
    print("There is no opened tabs to see its content")
  elif 0 <= index < len(tabs):
    html_url = tabs[index]["url"]
    req = requests.get(html_url)
    soup = BeautifulSoup(req.content, "html.parser")
    print(soup.prettify())
  else:
    print("Invalid input")

def displayAllTabs(tabs, indent=""):
  # worst case =>O(n),Where N is the total number of tabs in the nested
  for i in range(len(tabs)):
    print(indent + "Title:", tabs[i]["title"])
    displayAllTabs(tabs[i].get("tabs", []), indent + "  ")
    def openNestedTab(tabs):  # worst case =>O(1)
  index = input("Enter the index of the Parent tab: ")

  if index == "":
    print("Invalid input")
    return

  else:
    nestedtab = {}
    nested_title = input("Enter the title of the nested tab: ")
    nested_url = input("Enter the url of the nested tab: ")
    nestedtab["title"] = nested_title
    nestedtab["url"] = nested_url
    if int(index) < len(tabs):
      # tabs[int(index)]["tabs"].append(nestedtab)
      tabs[int(index)]["nested_tab"].append(nestedtab)
      # with open("data.json", "w") as json_file:
      #   json.dump(data, json_file, indent=2)

    print("Nested tab opened successfully")

    def clearAllTabs(tabs):  # worst case =>O(1) #Constant
  tabs.clear()
  print("All tabs have been cleared")
  return tabs

def saveTabs(
    file_path
):  # worst case =>O(n),Where n is the total number of tabs in the list
  # data_to_save = {"tabs": tabs}
  # with open("data.json", "w") as f:
  #   json.dump(data_to_save,f,indent=2)
  # print("All tabs have been saved")
  # return tabs
  json_string = json.dumps(tabs, indent=2)
  with open(file_path, "w") as f:
    f.write(json_string

    def importTabs(tabs):
     pass
    
def display_Menu():
  print("Welcome to Advanced Browser Tabs Simulation,\nthe menu:")
  print("1. Open Tab")
  print("2. Close Tab")
  print("3. Switch Tab")
  print("4. Display all tabs")
  print("5. Open Nested Tab")
  print("6. Clear All Tabs")
  print("7. Save Tabs")
  print("8. Import Tabs")
  print("9. Exit")


def main():
  # data = {}
  # with open("data.json", "r") as f:
  #   data = json.load(f)
  display_Menu()
  choice = int(input("Enter your choice: "))

  while choice != 9:
    if choice == 1:
      openTab()
    elif choice == 2:
      closeTab(input("Enter the index of the tab to close: "))
    elif choice == 3:
      switchTab(input("Enter the index of the tab to switch to: "))
    elif choice == 4:
      displayAllTabs(tabs)
    elif choice == 5:
      openNestedTab(tabs)
    elif choice == 6:
      clearAllTabs(tabs)
    elif choice == 7:
      file_path = input("Enter the path of your json file:")
      saveTabs(file_path)
    elif choice == 8:
      importTabs(tabs)
    elif choice == 9:
      print("Invalid Input")

    display_Menu()
    choice = int(input("Enter your choice: "))

    #print("Exiting the program")


main()

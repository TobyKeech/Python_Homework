stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverly")

#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0,"Glasgow Queen St")

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")

#4. Print out the index position of "Linlithgow"
index = stops.index(["Linlithgow"])
print(index)

#5. Remove "Livingston" from the list using its name
stops.remove(["Livingston"])
print(stops)

#6. Delete "Cumbernauld" from the list by index
stops.pop(2)
# stops.pop(stops.index("Cumbernauld"))


#7. Print the number of stops there are in the list
total_no_stops = len(stops)
print(total_no_stops)
# prints 7

#8. Sort the list alphabetically
ordered_stops= sorted(stops)
print(ordered_stops)

#9. Reverse the positions of the stops in the list
back_ordered_stops = sorted(stops, reverse = True)

#10 Print out all the stops using a for loop
for total in stops:
     print(total)
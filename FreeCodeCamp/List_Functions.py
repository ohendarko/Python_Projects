
lucky_numbers = [4, 43, 8, 15, 76, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Jim", "Tommy"]
friends2 = friends.copy()  # copy friends into friends2
print(friends)
friends.sort()  # sort in ascending order
print(friends)
lucky_numbers.sort()
friends.extend(lucky_numbers)  # add 2 lists together
friends.append("Creed")  # add another element to the end
friends.insert(1, "Kelly")  # insert element to index pos1
friends.remove("Jim") # remove element:Jim
print(friends)
print(friends.index("Kevin"))  # print index pos of "Kevin"
print(friends.count("Jim"))  # count the number of occurences of "Jim"
lucky_numbers.reverse()  # reverse the presentation
friends.pop()  # pop an element of the list
print(friends)
friends.clear()  # reset list and clear everything
print(friends)
print(friends2)
myfriendlist={"janvi","taanya", "shreya", "sahasra"}
my_mom_friendlist={"naveena", "ritu","vartika","shreya"}
b_daylist=myfriendlist.union(my_mom_friendlist)
print("the people i have invited are",b_daylist)
c_friend=myfriendlist.intersection(my_mom_friendlist)
print("our common friend is", c_friend)
import array as arr
array_num=arr.array("i",[9,1,9,9,2,4,6,3,5,2])
print(array_num.count(9))
(array_num.reverse())
print(array_num)
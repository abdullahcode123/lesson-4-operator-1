print("Enter you marks you scored in four subjects")
math=int(input("enter Math's marks"))
science=int(input("enter Science marks"))
computer=int(input("enter computer marks"))
english=int(input("enter english marks"))
sum=math+science+computer+english
print("sum of your total subjects is =",sum)
perc=(sum/400)*100
print(end="your percentage is ")
print(perc)
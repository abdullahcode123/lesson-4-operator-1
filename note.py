amount = int(input("Enter the Amount You want to take out from ATM"))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print("Notes of hundered =",note_1)
print("Notes of fifty =",note_2)
print("Notes of ten =",note_3)

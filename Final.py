candidate1 = input("enter the 1st candidate name:")
candidate2 = input("enter the 2nd candidate name:")
c1_votes=0
c2_votes=0
voters_id = [1,2,3,4,5,6,7]
no_of_votes =len(voters_id)
while True:
    voters = int(input("enter your voter id:"))
    if voters in voters_id:
        print("YOU ARE A VOTER")
        voters_id.remove(voters)
    else:
        print("SORRY...YOU ARE NOT ELIGIBLE TO VOTE -_-")
        break
    print(f"to vote{candidate1},press key 8...!")
    print(f"to vote{candidate2},press key 9...!")
    vote=int(input("Enter your valueable vote:"))
    if vote==8:
        c1_votes+=1
        print(f"{candidate1}, Thank you for giving your important vote...") 
        print("..........................................")
    elif vote==9:
        c2_votes+=1
        print(f"{candidate2}, Thank you for giving your important vote...") 
        print("..........................................")
    elif vote>9:
        print("you are pressing wrong key...!")
    else:
        print("SORRY...YOU ARE NOT ELIGIBLE TO VOTE -_-")
    if voters_id==[]:
        print('voting session is over-_-')

        if c1_votes >c2_votes:
            percent=(c1_votes/no_of_votes)*100
            print(f'Congratulation {candidate1} has win this election by {percent}%')
            print("***************************************************")
        elif c2_votes >c1_votes:
            percent=(c2_votes/no_of_votes)*100
            print(f'Congratulation {candidate2} has win this election by {percent}%')
            print("***************************************************")
            break

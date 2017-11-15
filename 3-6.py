guests = ['elvis', 'john cleese', 'john lennon']

message1 = "Dear " + guests[0].title() + ", I would be delighted for you to dine with me."
message2 = "Mr. " + guests[1].title() + ", may I have dinner with the funniest man alive?"
message3 = "It would be my honor to dine with " + guests[2].title() + "."

print(message1)
print(message2)
print(message3)

decline = "Sadly, it appears " + guests[2].title() + " is unavailable tonight."

print(decline)

guests.remove('elvis')
guests.append('kate bush')

print(guests)

newmes1 = "You are still invited, " + guests[0].title() + "."
newmes2 = "As are you, " + guests[1].title() + "."
newmes3 = "Are you free to join us, " + guests[2].title() + "?"

print(newmes1)
print(newmes2)
print(newmes3)

print("I have found a table for seven!")

guests.insert(0, 'geddy lee')
guests.insert(2, 'st. vincent')
guests.append('patrick stewart')

print(guests)

redo = "The invitation stands, " + guests[1].title() + "," + guests[3].title() + ", and " + guests[4].title() + "."
inv1 = "There is always room for " + guests[0].title() + " at my dinner table."
inv2 = "Be my guest, " + guests[2].title() + "."
inv3 = "Won't you join us, " + guests[-1].title() + "?"

print(redo)
print(inv1)
print(inv2)
print(inv3)

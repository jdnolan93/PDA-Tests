### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # == should be used instead of =
      return True
    else               # there is a missing colon (:)
      return False
   

  dif highest_card(self, card1 card2): #dif should be changed to def, and a comma should be added between card1 and card2
  if card1.value > card2.value: #if statement needs an indentation
    return card #card should be changed to card1
  else:
    return card2
  


def cards_total(self, cards): #fuction should have an indentation
  total #total should be given a value (0)
  for card in cards:
    total += card.value
    return "You have a total of" + total #return statement should be outside the loop, and it should be written f"You have a total of {total}"
  
```

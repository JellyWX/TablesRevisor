import random
import time




def main():
  yes = 'false'
  while yes == 'false':
    operation = str(input('Choose the operation. (Options: *, /, +, -, MIX, Sq, Cubed) > '))
    if operation == '*':
      yes = 'true'
      multiply()
    elif operation == '/':
      yes = 'true'
      divide()
    elif operation == '-':
      yes = 'true'
      subtract()
    elif operation == '+':
      yes = 'true'
      addition()
    elif operation == 'MIX':
      yes = 'true'
      rand()
    elif operation == 'Sq':
      yes = 'true'
      sq()
    elif operation == 'Cubed':
      yes = 'true'
      Cubed()
    else:
      yes = 'false'
      print('That does not currently exist. Please try again')
      

def sq():
  count = int(0)
  correct = 'right'
  try:
    number = int(input('Choose your maximum Sq, integers only! (eg. if you entered 12, the max. would be 12x) '))
  except:
    print('Uhoh! Something went wrong!')
  while correct != 'wrong':
    num1 = random.randint(1,number)
    
    try:
      answer = int(input('What is ' + str(num1) + 'x' + str(num1) + '? '))
    except:
      print("Uh oh! Something went wrong! Please type in only integers.")
      continue;
      
    if answer == num1 * num1:
      correct = 'right'
      count = count + 1
      
      
    elif answer != num1 * num1:
      correct = 'wrong'
      if count > 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Nice!')
      elif count < 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Better luck next time!')
      elif count == 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Good job!')
        
        
def Cubed():
  count = int(0)
  correct = 'right'
  try:
    number = int(input('Choose your maximum Sq, integers only! (eg. if you entered 12, the max. would be 12^3) '))
  except:
    print('Uhoh! Something went wrong!')
  while correct != 'wrong':
    num1 = random.randint(1,number)
    
    try:
      answer = int(input('What is ' + str(num1) + '^3? '))
    except:
      print("Uh oh! Something went wrong! Please type in only integers.")
      continue;
      
    if answer == num1 * num1 * num1:
      correct = 'right'
      count = count + 1
      
      
    elif answer != num1 * num1 * num1:
      correct = 'wrong'
      if count > 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Nice!')
      elif count < 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Better luck next time!')
      elif count == 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Good job!')
        


def timer(t, c):
  time.sleep(t)
  correct = 'wrong'
  print("You're out of time! You scored " + c + " in " + t + " seconds!")

  
def timed():
  count = int(0)
  correct = 'right'
  try:
    number = int(input('Choose your maximum sum, integers only! (eg. if you entered 12, the max. would be 12x12) '))
  except:
    print('Uhoh! Something went wrong!')   
  try:
    t = int(input('Choose your timer length, integers only! '))
  except:
    print('Uhoh! Something went wrong!') 
   
  while correct != 'wrong':
    num1 = random.randint(1,number)
    num2 = random.randint(1,number)
    operation = random.randint(1,4)
    operation1 = '*'
    if operation == 1:
      operation1 = '+'
    elif operation == 2:
      operation1 = '-'
    elif operation == 3:
      operation1 = '*'
    elif operation == 4:
      operation1 = '/'
    ans = num1 * num2
    
    def func(op, n1, n2, ans):
      if op == 1:
        return(n1 + n2)
      elif op == 2:
        return(n1 - n2)
      elif op == 3:
        return(n1 * n2)
      elif op == 4:
        return(ans / n2)
        
    if operation == 4:
      try:
        answer = int(input('What is ' + str(ans) + str(operation1) + str(num2) + '? > '))
      except:
        print("Uh oh! Something went wrong! Please type in only integers.")
        continue;
    else:
      try:
        answer = int(input('What is ' + str(num1) + str(operation1) + str(num2) + '? > '))
      except:
        print("Uh oh! Something went wrong! Please type in only integers.")
        continue;
 
    if answer == func(operation, num1, num2, ans):
      correct = 'right'
      count += 1
      
      
    elif answer != func(operation, num1, num2, ans):
      print('You got 1 wrong!')
      
  
      
      

def rand():
  count = int(0)
  correct = 'right'
  try:
    number = int(input('Choose your maximum sum, integers only! (eg. if you entered 12, the max. would be 12x12) '))
  except:
    print('Uhoh! Something went wrong!')   
  while correct != 'wrong':
    num1 = random.randint(1,number)
    num2 = random.randint(1,number)
    operation = random.randint(1,4)
    operation1 = '*'
    if operation == 1:
      operation1 = '+'
    elif operation == 2:
      operation1 = '-'
    elif operation == 3:
      operation1 = '*'
    elif operation == 4:
      operation1 = '/'
    ans = num1 * num2
    
    def func(op, n1, n2, ans):
      if op == 1:
        return(n1 + n2)
      elif op == 2:
        return(n1 - n2)
      elif op == 3:
        return(n1 * n2)
      elif op == 4:
        return(ans / n2)
        
    if operation == 4:
      try:
        answer = int(input('What is ' + str(ans) + str(operation1) + str(num2) + '? > '))
      except:
        print("Uh oh! Something went wrong! Please type in only integers.")
        continue;
    else:
      try:
        answer = int(input('What is ' + str(num1) + str(operation1) + str(num2) + '? > '))
      except:
        print("Uh oh! Something went wrong! Please type in only integers.")
        continue;
 
    if answer == func(operation, num1, num2, ans):
      correct = 'right'
      count += 1
      
      
    elif answer != func(operation, num1, num2, ans):
      correct = 'wrong'
      if count > 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Nice!')
      elif count < 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Better luck next time!')
      elif count == 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Good job!')
      scoreboardm(str(count))
      
      
      
      
            
def addition():
  count = int(0)
  correct = 'right'
  try:
    number = int(input('Choose your maximum sum, integers only! (eg. if you entered 12, the max. would be 12+12) '))
  except:
    print('Uhoh! Something went wrong!')   
  while correct != 'wrong':
    num1 = random.randint(1,number)
    num2 = random.randint(1,number)

    try:
      answer = int(input('What is ' + str(num1) + '+' + str(num2) + '? '))
    except:
      print("Uh oh! Something went wrong! Please type in only integers.")
      continue;
      
    if answer == num1 + num2:
      correct = 'right'
      count = count + 1
      
      
    elif answer != num1 + num2:
      correct = 'wrong'
      if count > 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Nice!')
      elif count < 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Better luck next time!')
      elif count == 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Good job!')
      scoreboarda(str(count))







def subtract():
  count = int(0)
  correct = 'right'
  try:
    number = int(input('Choose your maximum subtraction, integers only! (eg. if you entered 12, the max. would be 12-12) '))
  except:
    print('Uhoh! Something went wrong!')   
  while correct != 'wrong':
    num1 = random.randint(1,number)
    num2 = random.randint(1,number)

    try:
      answer = int(input('What is ' + str(num1) + '-' + str(num2) + '? '))
    except:
      print("Uh oh! Something went wrong! Please type in only integers.")
      continue;
      
    if answer == num1 - num2:
      correct = 'right'
      count = count + 1
      
      
    elif answer != num1 - num2:
      correct = 'wrong'
      if count > 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Nice!')
      elif count < 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Better luck next time!')
      elif count == 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Good job!')
      scoreboards(str(count))








def divide():
  count = int(0)
  correct = 'right'
  try:
    number = int(input('Choose your maximum division, integers only! (eg. if you entered 12, the max. would be 12/12) '))
  except:
    print('Uhoh! Something went wrong!')   
  while correct != 'wrong':
    num1 = random.randint(1,number)
    num2 = random.randint(1,number)
    ans = num1 * num2

    try:
      answer = int(input('What is ' + str(ans) + '/' + str(num2) + '? '))
    except:
      print("Uh oh! Something went wrong! Please type in only integers.")
      continue;
      
    if answer == num1:
      correct = 'right'
      count = count + 1
      
      
    elif answer != num1:
      correct = 'wrong'
      if count > 6:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Nice!')
      elif count < 6:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Better luck next time!')
      elif count == 6:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Good job!')
      scoreboardd(str(count))









def multiply():
  count = int(0)
  correct = 'right'
  try:
    number = int(input('Choose your maximum multiplication, integers only! (eg. if you entered 12, the max. would be 12x12) '))
  except:
    print('Uhoh! Something went wrong!')
  while correct != 'wrong':
    num1 = random.randint(1,number)
    num2 = random.randint(1,number)

    try:
      answer = int(input('What is ' + str(num1) + 'x' + str(num2) + '? '))
    except:
      print("Uh oh! Something went wrong! Please type in only integers.")
      continue;
      
    if answer == num1 * num2:
      correct = 'right'
      count = count + 1
      
      
    elif answer != num1 * num2:
      correct = 'wrong'
      if count > 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Nice!')
      elif count < 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Better luck next time!')
      elif count == 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Good job!')
      scoreboardx(str(count))
 
 
      
def scoreboardx(res):
  f = open('scoresMULTIPLY', 'a')
  f.write('\n' + res)
  
  
def scoreboardm(res):
  f = open('scoresMIX', 'a')
  f.write('\n' + res) 
 
    
def scoreboardd(res):
  f = open('scoresDIVIDE', 'a')
  f.write('\n' + res)
  
    
def scoreboards(res):
  f = open('scoresSUBTRACT', 'a')
  f.write('\n' + res)
  
    
def scoreboarda(res):
  f = open('scoresADD', 'a')
  f.write('\n' + res)
  
        
main()
        
    
    

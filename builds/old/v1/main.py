import random
import system


def main():
  yes = 'false'
  while yes == 'false':
    operation = str(input('Choose the operation. (Options: *, /, +, -, MIX, power) > '))
    if operation == '*':
      yes = 'true'
      calc('*')
    elif operation == '/':
      yes = 'true'
      calc('/')
    elif operation == '-':
      yes = 'true'
      calc('-')
    elif operation == '+':
      yes = 'true'
      calc('+')
    elif operation == 'MIX':
      yes = 'true'
      rand()
    elif operation == 'power':
      yes = 'true'
      power()
    else:
      yes = 'false'
      print('That does not currently exist. Please try again')
      

def power():
  count = int(0)
  correct = 'right'
  try:
    number = int(input('Choose your maximum power, integers only! (eg. if you entered 12, the max. sum would be 12^x) '))
  except:
    print('Uhoh! Something went wrong!')
  try:
    p = int(input('Choose your power, integers only! (eg. if you entered 2, the sums would be x^2) '))
  except:
    print('Uhoh! Something went wrong!')
  while correct != 'wrong':
    num1 = random.randint(1,number)
    
    try:
      answer = int(input('What is ' + str(num1) + '^' + str(p) + '? '))
    except:
      print("Uh oh! Something went wrong! Please type in only integers.")
      continue;
      
    if answer == num1**p:
      correct = 'right'
      count = count + 1
      
      
    elif answer != num1**p:
      correct = 'wrong'
      if count > 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Nice!')
      elif count < 10:
        print(str(num1**p) + " : " + str(num1) + " : " + str(p))
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Better luck next time!')
      else: 
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Good job!')
      scoreboard_power(str(count))
        

      

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
      scoreboard_mixture(str(count))
      
      
      
      
            
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
      scoreboard_addition(str(count))







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
      scoreboard_subtraction(str(count))








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
      scoreboard_division(str(count))





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
      scoreboard_multiplication(str(count))


def calc(t):
  count = int(0)
  correct = 'right'
  try:
    number = int(input('Choose your maximum sum, integers only! (eg. if you entered 12, the max. would be 12' + str(t) + '12) >'))
  except:
    print('Uhoh! Something went wrong!')   
  while correct != 'wrong':
    num1 = random.randint(1,number)
    num2 = random.randint(1,number)

    try:
      answer = int(input('What is ' + str(num1) + str(t) + str(num2) + '? '))
    except:
      print("Uh oh! Something went wrong! Please type in only integers.")
      continue;
      
    if answer == eval(str(num1) + str(t) + str(num2)):
      correct = 'right'
      count += 1
      
      
    elif answer != eval(str(num1) + str(t) + str(num2)):
      correct = 'wrong'
      if count > 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Nice!')
      elif count < 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Better luck next time!')
      elif count == 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Good job!')
      #scoreboard_null(str(count))
 
 
def score_write(t, filename)
  f = open(filename, 'a')
  f.write('\n' + str(t))
  x = input(str('Scores saved. Press ENTER to exit.'))
  sys.exit()      
def scoreboard_multiplication(res):
  f = open('scoresMULTIPLY', 'a')
  f.write('\n' + res)
  x = input(str('Scores saved. Press ENTER to exit.'))
  
def scoreboard_mixture(res):
  f = open('scoresMIX', 'a')
  f.write('\n' + res) 
  x = input(str('Scores saved. Press ENTER to exit.'))
    
def scoreboard_division(res):
  f = open('scoresDIVIDE', 'a')
  f.write('\n' + res)
  x = input(str('Scores saved. Press ENTER to exit.'))
    
def scoreboard_subtraction(res):
  f = open('scoresSUBTRACT', 'a')
  f.write('\n' + res)
  x = input(str('Scores saved. Press ENTER to exit.'))
    
def scoreboard_addition(res):
  f = open('scoresADD', 'a')
  f.write('\n' + res)
  x = input(str('Scores saved. Press ENTER to exit.'))

def scoreboard_power(res):
  f = open('scoresPOWER', 'a')
  f.write('\n' + res)
  x = input(str('Scores saved. Press ENTER to exit.'))
  
        
main()
        
    
    

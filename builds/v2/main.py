import random
import sys

def main():
    operation = str(input('Choose the operation. Options: \n * (multiply)\n / (divide)\n + (addition)\n - (subtract)\n MIX (random)\n ** (powers)\n > '))
    if operation == 'MIX':
      rand()
    elif operation == '**':
      power()
    else:
      
      calc(operation)
      #except:
       # print('A fatal error has occured!')
        

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
      count -= 1
      continue;
      
    if answer == num1**p:
      correct = 'right'
      count = count + 1
      
      
    elif answer != num1**p:
      correct = 'wrong'
      if count > 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Nice!')
      elif count < 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Better luck next time!')
      else: 
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Good job!')
      if configuration(6) == True:  
        print(str(num1**p) + " : " + str(num1) + " : " + str(p))
      score_write(count, 'scores**')
        

      

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
        count -= 1
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
      if configuration(6) == True:
        print(str(ans) + ' : ' + str(num1) + ' : ' + str(num2))
      score_write(count, 'scores_mix')


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
    ans = num1 * num2
    
    try:
      if t == '/':
        answer = float(input('What is ' + str(ans) + str(t) + str(num1) + '? '))
      else:
        answer = int(input('What is ' + str(num1) + str(t) + str(num2) + '? '))
    except:
      print("Uh oh! Something went wrong! Please type in only integers.")
      count -= 1
      continue;
    
    if t == '/':
      if configuration(4) == True:
        res = num2
      else:
        res = eval(str(num1) + str(t) + str(num2)) 
    else:
      res = eval(str(num1) + str(t) + str(num2))
    
    if answer == res:
      correct = 'right'
      count += 1
      
    
    elif answer != res:
      correct = 'wrong'
      if count > 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Nice!')
      elif count < 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Better luck next time!')
      elif count == 10:
        print('Uhoh! You got that wrong!! Your overall score was ' + str(count) + '. Good job!')
      if configuration(6) == True:
        print(str(res) + ' : ' + str(num1) + ' : ' + str(num2))
      if t == '/':
        score_write(count, 'scoresDivide')
      else:
        score_write(count, 'scores' + str(t)) 

def configuration(x):
  f = open('config/config.tbr', 'r') 
  p = f.readline(x)
  g = p.strip()
  return bool(g);

def score_write(t, filename):
  f = open('scores/' + filename + '.tbs', 'a')
  if configuration(2) == True:
    f.write('\n' + str(t))
    x = input(str('Scores saved. Press ENTER to exit.'))
  else:
    print('Score saving disabled. You can enable it in the config')

main()

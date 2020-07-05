from typing import List
import itertools

def prog():

  password_right = False
  password_right_num = False
  symbol = ('&','+','@','$','#','%')

def valid_pas():
#Проверка длинны пароля
  if (len(pas)< 5):
    print('error/ long must be min 5 symbol')
    return prog()
  if (len(pas)> 10):
    print('error/ long must be max 10 symbol')
    return prog()
  #Проверка наличия спец символов
  list_x = list(pas)
  if list_x.count('0') or list_x.count("1") >= 1 or list_x.count("2") or list_x.count("3") >= 1 or list_x.count("4") or list_x.count("5") >= 1 or list_x.count("6") or list_x.count ("7") >= 1 or list_x.count ("8") or list_x.count ("9"):
    password_right = True
  else:
    print ('need used number 1...9')
    return prog()
  if list_x.count("@") >= 1 or list_x.count("#") or list_x.count("$") >= 1 or       list_x.count("%") or list_x.count("&") >= 1 or list_x.count("+"):
    password_right_num = True
  else:
    print('need used special symbol @, #, $, %, &, +')
    return prog()
  if list_x.count(" ") >=1:
    print('with out space')
    return prog()
  #print(list_x)
  if password_right == True & password_right_num == True:
    print('Your password correctly')

print ('write password: ')
pas = input()
print ("your password: "+pas)
valid_pas()

prog()
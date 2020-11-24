class Solution:
    def romanToInt(self,s: str) -> int:        
          roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
          result = 0
          try:
            for i in range(len(s)):
              if i>0 and roman[s[i]] > roman[s[i-1]] :
                result += roman[s[i]] - 2*roman[s[i-1]]
              else:
                result += roman[s[i]]
          except KeyError:
            return -1
          return result if 1 <= result <=3999 else 0
if __name__ == "__main__":
  s=input("s = ")
  if 1<=len(s)<=15:
    int_value=Solution().romanToInt(s)
    if int_value>0:
      print(int_value)
    elif int_value==-1:
      print("Ошибка. Не выполняется 2 условие: s содержит недопустимые символы.")
    else:
       print("Ошибка. Вы ввели s вне диапазона [1, 3999]. Не выполняется 3 условие задачи.")
  else:
    print("Ошибка. Длина введенной строки не соответствует 1 условию задачи.")

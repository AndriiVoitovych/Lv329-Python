#https://www.codewars.com/kata/interactive-dictionary
class Dictionary():
    def __init__(self):
        self.dic = {}
    def newentry(self, word, definition):
        self.dic[word] = definition
    def look(self, key):
        if key in self.dic:
            return self.dic[key]
        else:
            return 'Can\'t find entry for ' + key

#https://www.codewars.com/kata/will-you-make-it
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg * fuel_left >= distance_to_pump else False

#https://www.codewars.com/kata/smart-traffic-lights
class SmartTrafficLight():
    def __init__(self, st1, st2):
        self.str1 = st1
        self.str2 = st2
    def turngreen(self):
        if self.str1[0] > self.str2[0]: 
            self.str1[0] = 0
            return self.str1[1]
        elif self.str1[0] < self.str2[0]:
            self.str2[0] = 0
            return self.str2[1]

#https://www.codewars.com/kata/reversing-words-in-a-string
def reverse(st):
    return ' '.join(reversed(st.split(' ')))

#https://www.codewars.com/kata/how-much-will-you-spend
def getTotal(costs, items, tax):
    total = 0
    for i in items:
        if i in costs:
            total +=costs[i]
    return round(total+(tax*total),2)   

#https://www.codewars.com/kata/noob-debug-1-fix-the-string-sum
def add(s1, s2):
    s1 = s1.encode()
    s2 = s2.encode()
    return sum(s1+s2)

#https://www.codewars.com/kata/make-a-square-box
def box(n):
    return ['-' * n] + ['-' + ' ' * (n-2) + '-'] * (n-2) + ['-' * n]


#https://www.codewars.com/kata/pig-atinlay
def pig_latin(word):
    return word[1:]+word[0]+'ay' if len(word)>3 else word
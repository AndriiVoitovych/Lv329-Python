# https://www.codewars.com/kata/counting-sheep-dot-dot-dot
def count_sheeps(arrayOfSheeps):
  count_sheeps = 0
 for sheeps in arrayOfSheeps:
     if sheeps == True:
         count_sheeps += 1
 return count_sheeps

#https://www.codewars.com/kata/surface-area-and-volume-of-a-box
def get_size(w,h,d):
    area = (2 * (w*h)+(w*d)+(h*d)
    volume = w*h*d
return [area, volume]

#https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits
def digitize(n):
    return map(int, reversed(str(n)))

#https://www.codewars.com/kata/a-needle-in-the-haystack
def find_needle(haystack):
    return 'found the needle at position %d' % haystack.index('needle')

#https://www.codewars.com/kata/a-function-within-a-function
def always(n=0):
    def a():
        return n
    return a

#https://www.codewars.com/kata/sum-arrays
def sum_array(a):
    return sum (a)

#https://www.codewars.com/kata/rock-paper-scissors
def rps(p1, p2):
    if p1==p2:
        return 'Draw!'
    elif (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'rock' and p2 == 'scissors'):
        return ('Player 1 won!')
    else: 
        return ('Player 2 won!')

#https://www.codewars.com/kata/formatting-decimal-places-number-0
#def two_decimal_places(n):
   # return float("{0:.2f}".format(n))
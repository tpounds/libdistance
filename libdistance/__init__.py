# Copyright (c) 2011 Trevor Pounds
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

def damerau_levenshtein(lhs, rhs):
   ''' Compute the Damerau-Levenshtein distance counting the minimum number of edits
       (e.g. insert, delete, substition, transposition) to transform one object to
       another.

       see: http://en.wikipedia.org/wiki/Damerau-Levenshtein_distance

       >>> damerau_levenshtein('kitten', 'sitting')
       3
       >>> daemerau_levenshtein('Saturday', 'Sunday')
       3
       >>> daemerau_levenshtein('CA', 'ABC')
       2
   '''
   d = [range(len(lhs)+1) for i in range(len(rhs)+1)]
   for i in range(len(rhs)+1):
      d[i][0] = i
   for i in range(1, len(d)):
      for j in range(1, len(d[0])):
         if rhs[i-1] == lhs[j-1]:
            d[i][j] = min(d[i][j-1], d[i-1][j], d[i-1][j-1])
         else:
            d[i][j] = min(d[i][j-1], d[i-1][j], d[i-1][j-1]) + 1
         if rhs[i-1] == lhs[j-2] and rhs[i-2] == lhs[j-1]:
            d[i][j] = min(d[i][j], d[i-1][j-1])
   return d[-1][-1]

def hamming(lhs, rhs):
   ''' Compute the Hamming distance counting the number of positions in which
       two objects of equal length differ.

       see: http://en.wikipedia.org/wiki/Hamming_distance

       >>> hamming('toned', 'roses')
       3
       >>> hamming('1011101', '1001001')
       2
       >>> hamming('2173896', '2233796')
       3
   '''
   if len(lhs) != len(rhs):
      raise IndexError('Cannot compute Hamming distance for strings of different sizes!')
   return sum(l != r for l, r in zip(lhs, rhs))

def levenshtein(lhs, rhs):
   ''' Compute the Levenshtein distance counting the minimum number of edits
       (e.g. insert, delete, substition) to transform one object to another.

       see: http://en.wikipedia.org/wiki/Levenshtein_distance 

       >>> levenshtein('kitten', 'sitting')
       3
       >>> levenshtein('Saturday', 'Sunday')
       3
       >>> levenshtein('CA', 'ABC')
       3
   '''
   d = [range(len(lhs)+1) for i in range(len(rhs)+1)]
   for i in range(len(rhs)+1):
      d[i][0] = i
   for i in range(1, len(d)):
      for j in range(1, len(d[0])):
         if rhs[i-1] == lhs[j-1]:
            d[i][j] = min(d[i][j-1], d[i-1][j], d[i-1][j-1])
         else:
            d[i][j] = min(d[i][j-1], d[i-1][j], d[i-1][j-1]) + 1
   return d[-1][-1]

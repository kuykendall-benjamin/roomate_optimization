#!/usr/bin/env python
# -*- coding: utf-8 -*-  
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

from itertools import *
import random
import copy
import os

choices = ['Adam', 'Ben', 'Noah', 'Mehrzad', 'Steven', 'Theo']
#choices = ['A','B','C','D']

def main():	
  all_ranks = dict()
  for c in choices:
    all_ranks[c] = get_choice_dictionary(c)
    os.system('reset')
  all_choices = pair_off(choices)
  choice_sum = list()
  for choice in all_choices:
    sum_squares = 0
    for p in choice:
      sum_squares += pow((all_ranks[p[0]][p[1]]),2) + pow((all_ranks[p[1]][p[0]]),2)
    choice_sum.append( (sum_squares, choice) )
  min_val = 10000
  min_choice = []
  for cs in choice_sum:
    if cs[0] == min_val:
      min_choice.append(cs[1])
    elif cs[0] < min_val:
      min_choice = [cs[1]]
  print random.choice(min_choice)
    
def get_choice_dictionary(exclude):
  ranks = dict()
  poss_nums = range(0,len(choices)-1)
  print 'Choices for ' + exclude
  for c in choices:
    if not c == exclude:
      num = get_ok_num(poss_nums, c + ' = ')
      poss_nums.remove(num)
      ranks[c] = num
  return ranks
  
def get_ok_num(poss, quest):
    try:
      num = int(raw_input(quest))
      if num in poss:
        return num
      else:
        print 'AHEM...'
        return get_ok_num(poss, quest)
    except:
      print 'AHEM...'
      return get_ok_num(poss, quest)
      
def pair_off(s):
  all_choices = list()
  if(len(s) == 2):
    one_choice = list()
    one_choice.append(s)
    all_choices.append(one_choice)
  else:
    pairs = list(combinations(s,2))
    done_pairs = list()
    for p in pairs:
      left_over = list(set(s) - set(p))
      lesser = pair_off(left_over)
      for l in lesser:
        already_done = False
        for little_pair in l:
          if little_pair in done_pairs or list(reversed(little_pair)) in done_pairs:
            already_done = True
        if not already_done:
          one_choice = copy.deepcopy(l)
          one_choice.append(list(p))
          all_choices.append(one_choice)
        done_pairs.append(list(p))
  return all_choices

if __name__ == '__main__':
	main()

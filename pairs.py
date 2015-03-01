#!/usr/bin/env python
# -*- coding: utf-8 -*-  

from itertools import *
import copy
import os

choices = ['Adam', 'Ben', 'Noah', 'Merhzad', 'Steven', 'Theo']

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
  min_choice = False
  for cs in choice_sum:
    if cs[0] < min_val:
      min_choice = cs[1]
  print min_choice
    
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

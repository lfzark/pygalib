import string
import pygalib

def calc_avg_value(params,nums,n_set):
  max_sum = float('-inf')
  for _ in range(n_set):
	  t_sum = 0
	  for i in range(len(params)):
		if _ == params[i]:
		    t_sum+=nums[i]    
	  if t_sum > max_sum:
		max_sum = t_sum
  return max_sum


if __name__ == "__main__":

  n_set = 4
  num_set = [1,2,5,7,41,14,41,2,4,8,8,6,3,5,1,8]
 
  indiv = pygalib.Individual(
        gene_set=range(n_set),
        chrom_len = len(num_set),
        fitness_func=lambda x: calc_avg_value(x,num_set ,n_set)
  )

  ga = pygalib.GA(
        p_size = 1000,
        individual=indiv,
        n_generation = 1000,
	max_order=False
  )

  result = ga.run()


  print '[+]Best fitness : [%d]' % result.fitness_value
  print '[+]Solution: %s' % result.chromosome

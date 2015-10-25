
import pygalib

if __name__ == "__main__":

  indiv = pygalib.Individual(
        gene_set=range(1,10),
        chrom_len = 4,
        fitness_func=lambda x:(x[0]+x[1])/x[2]-x[3]
  )

  ga = pygalib.GA(
        p_size = 100,
        individual=indiv,
        n_generation = 1000
  )
    
  print ga.run().chromosome


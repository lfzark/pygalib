import pygalib

def cal_the_value(params):

        x, y, z = params
        
        return x * y / float(z)

if __name__ == '__main__':
    #create a individual
    
    indiv = pygalib.Individual(
        gene_set=range(1, 20),
        chrom_len = 3,
        fitness_func=cal_the_value
    )

    ga = pygalib.GA(
        p_size = 200,
        individual=indiv,
        n_generation = 1000
    )
    
    result = ga.run()

    print '[+]Best fitness : [%d]' % result.fitness_value
    print '[+]Solution: %s' % result.chromosome

    

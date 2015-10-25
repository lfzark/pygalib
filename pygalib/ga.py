#!/usr/bin/python
#
# ga.py - Genetic Algorithm main file, an implementation of genetic algorithm concepts.
# 
# 						By ark1ee.2015.10.24
# Version 0.1.0

'''
Wiki:
Gene is the DNA fragment with function, chromosome is the carrier of DNA, DNA and protein together constitute the chromosome. 
So,chromosome > DNA > gene
'''

import random
import math

class Individual:
	

	def __init__(self,gene_set,chrom_len,fitness_func):
		'''
		gene_set
			the symbol set of gene
			
		chrom_len
			the length of chromosome
			
		fitness_func
			the fitness function
		'''
		
		self.chromosome = []
		self.fitness_value  = 0
		self.gene_len   = len(gene_set)
		self.chrom_len  = chrom_len
		self.is_need_calc_fitness = True
		self.gene_set = gene_set
		self.fitness_func = fitness_func
		

	def get_property(self):
		'''
		get the property of this object
		'''
		
		return  {_:self.__dict__[_]  for _ in ['gene_set','chrom_len','fitness_func']}
	
	def create_chromosome(self):
		'''
		create chromosome for this individual
		'''
		
		self.chromosome=[random.choice(self.gene_set) for _ in range(self.chrom_len)]

		return self
	
 
class GA:
	
	def __init__(self,p_size,individual,n_generation,desired_value=None,max_order=True,crossover_rate = 0.7,mutation_rate = 0.01):
		'''
		Initialize values for genetic algorithm 
		
		p_size
			the size of population
		
		individual
			example individual
			
		n_generation
			max number of generation
			
		desired_value
			the desired value of the fitness
		
		'''
		
		# The size of population 
		self.population_size = p_size

		# Current number of generation 
		self.cur_generation = 0

		# Probability of crossover (%/100)
		self.crossover_rate = crossover_rate

		# Probability of mutation (%/100)
		self.mutation_rate = mutation_rate

		# Desired value
		self.desired_value = desired_value

		# Length per gene
		self.gene_len   = individual.gene_len

		# Length of chromosome 
		self.chrom_len  = individual.chrom_len
		
		# Stored current best fitness value 
		self.best_fitness = float('-inf' ) if max_order else float('inf' )
			
		# Stored current best chromosome
		self.best_chromosome = []
		
		# Default order is descending order
		self.max_order = max_order
		
		# The total number of the generation
		self.n_generation = n_generation
				
		# The population of this object
		self.population  = []
		
		# Example individual
		self.individual_example = individual
		
		# Property of the example individual
		self.individual_property = self.individual_example.get_property()
	
		#TODO
		
		#self.population_fitness_sequence  = []
		
		#self.fitness_sequence=[]
		
		#self.fore_generation_population =[]
		
		#self.person_sequence=[]
		


	def run(self):
		'''
		run the genetic algorithm
		
		'''

		self.init_population()
		self.sort_individual()
		
		while (self.cur_generation < self.n_generation ) and (self.desired_value !=  self.best_fitness):
			
			self.crossover()

			self.mutate()

			self.sort_individual()
			
			#verbose
			#for i in range(self.population_size):
			#	print self.population[i].chromosome, self.population[i].fitness_value
	
			if self.best_fitness <  self.select(0).fitness_value if  self.max_order else self.best_fitness  >  self.select(0).fitness_value:
			
				self.best_fitness =  self.select(0).fitness_value
				self.best_chromosome =  self.select(0).chromosome

			self.cur_generation += 1

		self.sort_individual()
		
		return self.select(0)
	

	def init_population(self):
		'''
	    Initial the population for GA.
	    '''
		self.population = [  self.create_indiv().create_chromosome() for _ in range(self.population_size)] 
	
 



	#Create a new individual
	def create_indiv(self):
		'''
		Create a new individual according to individual_property
		'''
		
		return Individual(**self.individual_property)


	def sort_individual(self):
		'''
		Calculate all the fitness and sort them.
		'''
		
		self.calc_all_fitness()
		self.population.sort(key=lambda x:x.fitness_value,reverse=self.max_order)

	def select(self,topn):
		'''
	    Select the top n individual from the population.
	    '''
		return self.population[topn]


	def crossover(self):
		'''
	    Do probablistic crossover operation.
	    '''
		
		self.crossover_point = random.randint(0,self.chrom_len)
		
		self.sort_individual()
		
		individual_a = self.select(0)
		individual_b = self.select(1)
		
		individual_child = self.create_indiv()

		old_best_fitness = self.best_fitness

		if (random.random() <= self.crossover_rate) :
			
			individual_child.chromosome =individual_a.chromosome[self.crossover_point:] + \
			individual_b.chromosome[:self.crossover_point]

			individual_child.is_need_calc_fitness=True
			child_fitness = self.fitness(individual_child)

			if (child_fitness <= self.population[self.population_size-1].fitness_value) if self.max_order else (child_fitness >= self.population[self.population_size-1].fitness_value):#old_best_fitness:#[self.population_size-2]:
				return 
			else:

				for _ in range(0,self.population_size-1):
					if self.population[_].fitness_value < child_fitness if self.max_order else self.population[_].fitness_value > child_fitness:

						self.population[_] = individual_child
						break

	def mutate(self):
		'''
	    Do probablistic mutate operation.
	    '''

		for _ in range(self.population_size):
			indiv = self.create_indiv()
			indiv.chromosome =  self.population[_].chromosome

			isMutate = False
			
			if (random.random() < self.mutation_rate):
 				
				indiv.is_need_calc_fitness=True

				indiv.chromosome[random.randint(0,self.chrom_len-1)] = random.choice(indiv.gene_set)

				cur_fitness   = self.fitness(indiv)	
				worst_fitness = self.population[self.population_size-1].fitness_value
				
				if (cur_fitness <= worst_fitness) if self.max_order else  (cur_fitness >= worst_fitness):	        
					continue 
				else:
					isMutate=True
			if isMutate:

				self.population[_]=indiv


	def calc_all_fitness(self):
		'''
		Calculate all the fitness of the population 
		'''
		
		for _ in range(self.population_size):
			self.fitness(self.population[_])
			

	def fitness(self,individ):
		'''
		Calculate fitness value for the current individual.
		'''
		
		if individ.is_need_calc_fitness==False :
		    return 
		individ.fitness_value = self.individual_example.fitness_func(individ.chromosome)
		individ.is_need_calc_fitness = False
		return individ.fitness_value



	
	def similar_chromo(self,individual_a,individual_b):
		'''
		Return the radio  similarity of between two chromosomes.
		'''
		similiarN=0.0
		
		for _ in range(self.chrom_len):
			if individual_a.chromosome[_] == individual_b.chromosome[c]:
				similiarN+=1.0
				
		return  (similiarN,self.chrom_len,similiarN/self.chrom_len)
		

	def endCondition(self):
		'''
		TODO
		The terminal condition of genetic algirthm
		'''
		pass
	


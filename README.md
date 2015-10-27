Python Genetic Algorithm Library (pygalib) 
======================= 
### A simple and easy-to-use genetic algorithm library 

---- 

## Installation 
Use pip: 
```
pip install pygalib 
```
if you want to install from source code , you can download from pypi or simple use: 
```
git clone https://github.com/lfzark/pygalib 
```
then run: 
```
python setup.py install 
```

## Example 

```python 

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

```

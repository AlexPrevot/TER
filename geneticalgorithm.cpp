#include <iostream>

#include "geneticalgorithm.h"
#include <omp.h>

Path GeneticAlgorithm::optimize()
{
	omp_set_num_threads(4);

	unsigned int seeds[4];
	int my_thread_id;
	unsigned int seed;
	#pragma omp parallel private (seed, my_thread_id)
	{
		my_thread_id = omp_get_thread_num();
		unsigned int seed = (unsigned)time(NULL);
		srand(unsigned(time(NULL)) * omp_get_thread_num());
		seeds[my_thread_id] = (seed & 0xFFFFFFF0) | (my_thread_id + 1);
	}

	int same_count = 0;
	int best = _population[0].getFitness();
	Path champion = _population[0];

	int count = 1;
	while (same_count < 500)
	{
		_crosser.crossover(_population);

		if (_population.at(0).getFitness() < best)
		{
			same_count = 0;
			best = _population.at(0).getFitness();
			champion = _population.at(0);
		}
		else
			same_count++;
		count++;
	}

	std::cout << "number of generation : " << count << std::endl;

	return champion;
}
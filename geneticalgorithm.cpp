#include "geneticalgorithm.h"
#include <iostream>
Path GeneticAlgorithm::optimize()
{


	int same_count = 0;
	int best = _population[0].getFitness();
	Path champion = _population[0];

	int count = 0;
	while (same_count < 200)
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
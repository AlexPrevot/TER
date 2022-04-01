#include "geneticalgorithm.h"

int GeneticAlgorithm::optimize()
{
	int same_count = 0;
	int best = _population[0].getFitness();
	Path champion = _population[0];

	while (same_count < 200)
	{
		_crosser.crossover(_population);

		if (_population.at(0).getFitness() < best)
		{
			same_count = 0;
			best = _population.at(0).getFitness();
		}
		else
			same_count++;
	}

	return best;
}
#include "geneticalgorithm.h"
#include <iostream>
Path GeneticAlgorithm::optimize()
{


	int same_count = 0;
	int best = _population[0].getFitness();
	Path champion = _population[0];

	int count = 1;
	while (same_count < 200)
	{
		/*
		if (count % 500 == 0)
			_crosser.setMutationRate(_crosser.getMutationRate() + 0.05);

		*/
		if (count % 400 == 0)
		{
			if(_crosser.getSelectionRate() > 0.1)
				_crosser.setSelectionRate(_crosser.getSelectionRate() - 0.05);
		}

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
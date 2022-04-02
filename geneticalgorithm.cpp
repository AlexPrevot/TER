#include "geneticalgorithm.h"
#include <iostream>
Path GeneticAlgorithm::optimize()
{


	int same_count = 0;
	int best = _population[0].getFitness();
	Path champion = _population[0];

	int count = 0;
	while (same_count < 50)
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

		//std::cout << best << std::endl;
		/*std::cout << "ALLOOOOOOOOOOOO" << std::endl;
		for (auto& p : _population)
			p.print();*/

		//std::cout << "step finished" << std::endl;
		//std::cin.get();
	}


	std::cout <<"count new one" << count << std::endl;
	return champion;
}
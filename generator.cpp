#include <algorithm>
#include <random>
#include "generator.h"
#include "path.h"


std::vector<Path> Generator::generate()
{
	std::vector<Path> population;

	std::vector<int> individual_path(_individual_size);

	for (int i = 0; i < _individual_size; i++)
		individual_path.at(i) = i;

	for (int i = 0; i < _population_size; i++)
	{
		std::vector<int> new_path = individual_path;

		std::random_device rd;
		std::mt19937 g(rd());

		std::shuffle(new_path.begin(), new_path.end(),g);


		Path path(new_path);

		population.push_back(path);
	}

	return population;
}

#pragma once
#include <vector>
#include <algorithm>
#include <iostream>

#include "path.h"
#include "generator.h"
#include "crosser.h"

struct comparator
{
	inline bool operator()(Path& p1, Path& p2)
	{
		return (p1.getFitness() < p2.getFitness());
	}
};

class GeneticAlgorithm
{
	public:
		GeneticAlgorithm(std::vector<int> coordinates, int pop_size, int max_iteration = -1)
		{
			srand(time(NULL));

			Path::setCoordinates(coordinates);

			Generator g(coordinates.size() / 2, pop_size);
			_population = g.generate();

			

			std::sort(_population.begin(), _population.end(), comparator());

			std::cout << "start with : " << _population[0].getLength() <<std::endl;

			Crosser crosser(0.1, 0.02);
			_crosser = crosser;
		}

		Path optimize();



	private:
		std::vector<Path> _population;
		Crosser _crosser;



};


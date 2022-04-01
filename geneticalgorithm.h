#pragma once
#include <vector>

#include "path.h"
#include "generator.h"
#include "crosser.h"

class GeneticAlgorithm
{
	public:
		GeneticAlgorithm(std::vector<int> coordinates, int pop_size, int max_iteration = -1)
		{
			Path::setCoordinates(coordinates);

			Generator g(coordinates.size() / 2, pop_size);
			_population = g.generate();

			Crosser crosser(0.25, 0.25);
			_crosser = crosser;
		}

		Path optimize();



	private:
		std::vector<Path> _population;
		Crosser _crosser;



};


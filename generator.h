#pragma once
#include <vector>
#include "path.h"

class Generator
{
	

	public:

		Generator(int individual_size, int population_size)
		{
			_individual_size = individual_size;
			_population_size = population_size;
		}

		std::vector<Path> generate();



	private:

		int _individual_size;
		int _population_size;

};


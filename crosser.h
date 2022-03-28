#pragma once
#include <vector>
#include "Path.h"
class Crosser
{
	public:
		Crosser(double mutation_rate)
		{
			_mutation_rate = mutation_rate;
		}

		Path cross(Path &path1, Path &path2);

	private:
		double _mutation_rate; //chance of mutate the child
		
};


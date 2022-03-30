#pragma once
#include <unordered_set>
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

		int getRandom(std::unordered_set<int> set);
		
};


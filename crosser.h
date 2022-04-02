#pragma once
/*
=========================================== INFORMATION ===============================
This class does a Edge recombination cross over on given population. 
It choses random parent from the first part (accord to the selection rate), and cross them to have children

It then writes theses children onto the 2nd part of the population to erase unselected parents
*/


#include <unordered_set>
#include "Path.h"
class Crosser
{
	public:

		Crosser()
		{
			_mutation_rate = 0.25;
			_selection_rate = 0.25;
		}

		Crosser(double selection_rate,double mutation_rate)
		{
			_mutation_rate = mutation_rate;
			_selection_rate = selection_rate;
		}

		Path cross(Path &path1, Path &path2);
		

		// cross the first part of the population and write children on others
		void crossover(std::vector<Path> &population);

		void setMutationRate(float rate);

		float getMutationRate();
	private:
		double _mutation_rate; //chance of mutate the child
		double _selection_rate; //selected parent (the size in proportion of the first part

		int getRandom(std::unordered_set<int> set);
		void mutate(Path& p);
		
};


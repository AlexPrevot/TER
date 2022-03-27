#pragma once
#include <vector>


/*
=======================INFORMATION===================
A path is a 1-D vector of coordinates. Each coordinate are paired in two
The path does operation similar as if it was a 2D vector.

Everytime the path is updated, the fitness is too.

(!) IMPORTANT : The fitness is not the overall length of the path. 
It only is the sum of differences between contiguous coordinates. 
That way, square roots are avoided.

*/

typedef std::vector<int> coords;

class Path
{
	
	public:
		Path(std::vector<int> path)
		{
			_path = path;
			_computeFitness();
		}

		//---- getters
		int		getSize();
		int		getFitness();

		
	private:

		void _setFitness(float fitness);
		void _computeFitness();

		coords _path;
		int _fitness = -1;

};


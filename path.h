#pragma once
#include <vector>


/*
=======================INFORMATION===================
A path is a 1-D vector of coordinates. Each coordinate are paired in two
The path does operation similar as if it was a 2D vector.



(!) IMPORTANT : The fitness is not the overall length of the path. 
It only is the sum of differences between contiguous coordinates. 
That way, square roots are avoided.

*/
class Path
{
	
	public:
		Path(int size)
		{
			_path = std::vector<int>(size, -1);
		}

		Path(std::vector<int> path)
		{
			_path = path;
		}


	private:

		std::vector<int> _path;
		float fitness = -1;

};


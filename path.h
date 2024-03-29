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
			//(!) do a function that makes the program crash if path size isn't matched with coordinate size
			_path = path;
			_computeFitness();
		}

		void swap(int x1, int x2); //swaps nodes at index x1 and x2
		void print();

		//---- getters
		int		getSize();
		float	getFitness();
		float   getLength();
		int		at(int i);
		
		
		//---- setters
		static void setCoordinates(coords coordinates)
		{
			//(!) DO A FUNCTION THAT MAKE THE PROGRAM CRASH IF THE PROVIDED PATH ISNT EVEN LENGTH
			_coordinates = coordinates;
		}
		
	private:
		static coords _coordinates;
		void _setFitness(float fitness);
		void _computeFitness();

		coords _path;
		float _fitness = -1;

		float _getCost(int p1, int p2); //returns the cost of the arc p1 - p2 (p1 and p2 are nodes, not index)
		float _getLoss(int index); //returns the loss on the fitness if we delete the node at index x;
		

};


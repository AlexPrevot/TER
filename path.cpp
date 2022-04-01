#include "path.h"
#include <cmath>
#include <iostream>

//=== static

coords Path::_coordinates = coords();


//================================= PUBLIC =====================
int Path::getSize()
{
	return _path.size();
}

int Path::getFitness()
{
	return _fitness;
}

int Path::at(int i)
{
	return _path.at(i);
}

void Path::swap(int x1, int x2)
{
	int mem = _path.at(x1);
	_path.at(x1) = _path.at(x2);
	_path.at(x2) = mem;

	_computeFitness();
}

void Path::print()
{
	for (auto i : _path)
		std::cout << i << " ";

	std::cout << " fitness : " << getFitness();
	std::cout << "\n";
}




//================================= PRIVATE =====================

void Path::_setFitness(float fitness)
{
	_fitness = fitness;
}

void Path::_computeFitness()
{
	if (_path.size() <= 1)
		_setFitness(0);

	float length = 0;
	for (int i = 1; i < _path.size(); i++)
	{
		int city1 = _path.at(i)*2;
		int city2 = _path.at(i - 1)*2;

		length += std::pow(_coordinates.at(city1) - _coordinates.at(city2),2) + 
				  std::pow(_coordinates.at(city1 + 1) - _coordinates.at(city2 + 1),2);

	}
	if (_path.size() > 2)
	{
		int city1 = _path.front() * 2;
		int city2 = _path.back() * 2;

		length += std::pow(_coordinates.at(city1) - _coordinates.at(city2), 2) +
			std::pow(_coordinates.at(city1 + 1) - _coordinates.at(city2 + 1), 2);

	}
	_setFitness(length);
}
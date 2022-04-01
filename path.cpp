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

float Path::getFitness()
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

	//no need to computeFitness from the start, can be done in costant time
	_computeFitness();
}

void Path::print()
{
	for (auto i : _path)
		std::cout << i << " ";

	std::cout << " fitness : " << getFitness();
	std::cout << "\n";
}

float Path::getLength()
{
	float length = 0;
	int size = 10;
	for (int i = 0; i < size; i++)
	{
		int next = i + 1;

		if (next >= size)
			next = 0;

		int city1 = _path.at(i) * 2;
		int city2 = _path.at(next) * 2;

		int val1 = std::pow(_coordinates.at(city1) - _coordinates.at(city2), 2);
		int val2 = std::pow(_coordinates.at(city1 + 1) - _coordinates.at(city2 + 1), 2);


		length += sqrt(val1 + val2);
	}

	return length;
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
	int size = _path.size();
	for (int i = 0; i < size; i++)
	{
		int next = i + 1;

		if (next >= size)
			next = 0;

		int city1 = _path.at(i) * 2;
		int city2 = _path.at(next) * 2;

		length +=	std::pow(_coordinates.at(city1) - _coordinates.at(city2), 2) +
					std::pow(_coordinates.at(city1 + 1) - _coordinates.at(city2 + 1), 2);
	}

	
	_setFitness(length);
}
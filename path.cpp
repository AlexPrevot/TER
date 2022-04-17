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
	return _path[i];
}




void Path::swap(int x1, int x2)
{		
	float loss = _getLoss(x1) + _getLoss(x2);
	
	std::swap(_path[x1], _path[x2]);

	float gain = _getLoss(x1) + _getLoss(x2);


	_setFitness(getFitness() - loss + gain);
	
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
	int size = _path.size();
	for (int i = 0; i < size; i++)
	{
		int next = i + 1;

		if (next >= size)
			next = 0;

		int city1 = _path.at(i) * 2;
		int city2 = _path.at(next) * 2;

		float val1 = std::pow(_coordinates.at(city1) - _coordinates.at(city2), 2);
		float val2 = std::pow(_coordinates.at(city1 + 1) - _coordinates.at(city2 + 1), 2);


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

		length += _getCost(_path[i], _path[next]);
	}

	
	_setFitness(length);
}



float Path::_getCost(int p1, int p2)
{
	return	(_coordinates[p1 * 2] - _coordinates[p2*2]) * (_coordinates[p1 * 2] - _coordinates[p2 * 2]) +
			(_coordinates[(p1 * 2) + 1] - _coordinates[(p2 * 2) + 1]) * (_coordinates[(p1 * 2) + 1] - _coordinates[(p2 * 2) + 1]);
}

float Path::_getLoss(int index)
{
	float loss = 0;
	int x = index;
	if (x == getSize() - 1)
	{
		loss += _getCost(_path[x], _path[0]);
		loss += _getCost(_path[x - 1], _path[x]);
	}
	else if (x == 0)
	{
		loss += _getCost(_path[x], _path[x + 1]);
		loss += _getCost(_path.back(), _path[x]);
	}
	else
	{
		loss += _getCost(_path[x], _path[x + 1]);
		loss += _getCost(_path[x - 1], _path[x]);
	}

	return loss;
}
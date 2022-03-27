#include "path.h"
#include <cmath>

//================================= PUBLIC =====================
int Path::getSize()
{
	return _path.size();
}

int Path::getFitness()
{
	return _fitness;
}



//================================= PRIVATE =====================

void Path::_setFitness(float fitness)
{
	_fitness = fitness + 1000;
}

void Path::_computeFitness()
{
	float length = 0;
	for (int i = 2; i < _path.size(); i += 2)
	{
		length += std::pow(_path.at(i) - _path.at(i - 2),2) + std::pow(_path.at(i + 1) - _path.at(i - 1),2);
	}

	_setFitness(length);
}
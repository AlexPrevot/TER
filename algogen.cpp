#define PY_SSIZE_T_CLEAN
#include <Python.h>


#include <stdio.h>
#include <iostream>
#include <vector>
#include <memory>
#include <tuple>
#include <algorithm>
#include <math.h>
#include <time.h>
#include <random>
#include <deque>


//#include "algogen.h"

std::shared_ptr<std::vector<int>> cross(std::vector<int>& path1, std::vector<int>& path2)
{
	std::shared_ptr<std::vector<int>> child =  std::make_shared<std::vector<int>>();

	int size = path1.size();
	
	*child = path2;

	std::deque<int> seen;
	std::vector<int> tmp(size,-1);
	std::deque<int> miss;

	//copy half of path1 in path2
	//std::copy(path1.begin(), path1.begin()+(size/2), (*child));
	for (int i = 0; i < size / 2; i++)
		child->at(i) = path1.at(i);


	//find seen value
	for (int i = 0; i < size; i++)
	{
		if (tmp.at(child->at(i)) == -1)
			tmp.at(child->at(i)) = i;
		else
			seen.push_back(i);
	}

	//find missing value
	for (int i = 0; i < size; i++)
	{
		if (tmp.at(path2.at(i)) == -1)
			miss.push_back(path2.at(i));
	}

	//replace doubled value with missing value in the order of path2
	for (int i = 0; i < seen.size(); i++)
		child->at(seen.at(i)) = miss.at(i);

	return child;
}


void cross_over(std::shared_ptr<std::vector<int>[]> population,int size, int start)
{
	int nbrTown = population[0].size();

	for (int i = 0; i < start; i++)
	{
		for (int j = i; j < start; j++)
		{
			if ((start + j + i * j) < size)
				population[start + j + i * j] = *cross(population[i], population[j]);
			else
				return;
		}
	}
}


float getFitness(std::vector<std::tuple<int, int>>& coord,
				 std::vector<int>				  & path)
{
	float fitness = 0.0;
	int size = path.size();

	for (int i = 0; i < size; i++)
	{
		int val = (i + 1) * (i + 1 < size);
		int co1 = path.at(i);
		int co2 = path.at(val);
		
		int p1X = std::get<0>(coord.at(co1));
		int p1Y = std::get<1>(coord.at(co1));


		int p2X = std::get<0>(coord.at(co2));
		int p2Y = std::get<1>(coord.at(co2));

		fitness += sqrt(pow(p1X - p2X, 2) + pow(p1Y - p2Y, 2));
	}

	return fitness;
}



void sortByFitness(std::vector<std::tuple<int,int>> &paths)
{
	std::sort(paths.begin(), paths.end());
}

//NOTE : Am�liorer le sqrt pour augmenter les performances peut �tre utile ?
std::shared_ptr<std::vector<int>[]> fitness(std::vector<std::tuple<int,int>>		& coord,
											std::shared_ptr<std::vector<int>[]>		& paths, int size)
{

	std::vector<std::tuple<int, int>> element(size);



	for (int k = 0; k < size ; k++)
		element.at(k) = std::make_tuple(getFitness(coord, paths[k]), k);



	sortByFitness(element);

	std::shared_ptr<std::vector<int>[]> sortedPaths(new std::vector<int>[size]);

	for (int k = 0; k < size; k++)
		sortedPaths[k] = paths[std::get<1>(element.at(k))];

	return sortedPaths;
}







//CHANGER LE POINTEUR POUR UN SMART POINTER
std::shared_ptr<std::vector<int>[]> generatePopulation(int pop, int nbrCity)
{
	srand(unsigned(time(NULL)));

	std::shared_ptr<std::vector<int>[]> population(new std::vector<int>[pop]);
	std::vector<int> sample(nbrCity);

	for (int i = 0; i < nbrCity; i++)
		sample.at(i) = i;

	for (int i = 0; i < pop; i++)
	{
		population[i] = sample;

		std::random_shuffle(std::begin(population[i]), std::end(population[i]));

	}

	return population;
}














//FIRST ELEMENT OF EACH TUPLE SHOULD BE THE FITNESS SCORE, the 2nd is the position on the original 
//map position
std::vector<int> Calgogen(std::vector<std::tuple<int,int>> &coordCities, int nbrPaths)
{
	int nbrCities = coordCities.size();


	std::shared_ptr<std::vector<int>[]> chemins = generatePopulation(nbrPaths, nbrCities);
	chemins = fitness(coordCities, chemins, nbrPaths);
	float best = -1;
	int iterations = 0;

	while (iterations < 30)
	{
		cross_over(chemins, nbrPaths, nbrCities/2);
		chemins = fitness(coordCities, chemins, nbrPaths);
		

		float currentBest = getFitness(coordCities, chemins[0]);


		if (best < currentBest || best == -1)
			best = currentBest;
		else
			iterations++;
	}


	return chemins[0];
}

//-----------------------------------------------------------
// send nbrPaths before
static PyObject* genalgo(PyObject* self, PyObject* args)
{
	PyObject *arr;
	int CnbrPaths;
	PyObject* cities;
	
	
	if(!PyArg_ParseTuple(args, "Oi", &cities, &CnbrPaths))
		return NULL;


	PyObject* seq = PySequence_Fast(cities, "argument must be iterable");



	int seqlen = PySequence_Fast_GET_SIZE(seq);
		
	std::vector<std::tuple<int,int>> Ccities;



	//---
	for(int i = 0; i < seqlen; i++)
	{
		PyObject* tup = PyList_GetItem(cities, i);
		int x = (int) PyLong_AsLong(PyList_GetItem(tup, 0));
		int y = (int) PyLong_AsLong(PyList_GetItem(tup, 1));
		Ccities.push_back(std::make_tuple(x,y));
	}
	
	std::vector<int> bestPath = Calgogen(Ccities,CnbrPaths);
	
	//--

	PyObject *result = PyList_New(seqlen);
	
	for(int i = 0; i < seqlen; i++)
	{
		
		PyList_SetItem(result, i,Py_BuildValue("i", bestPath.at(i)));
	}
	
	return result;
	
}


static PyMethodDef myMethods[] = {
	{"genalgo",genalgo,METH_VARARGS,"compte putain de merde"},
	{NULL,NULL,0,NULL}
};

static struct PyModuleDef myModule = {
	PyModuleDef_HEAD_INIT,
	"genalgo",
	"genetic algo module",
	-1,
	myMethods
};

PyMODINIT_FUNC PyInit_myModule(void)
{
	return PyModule_Create(&myModule);
}
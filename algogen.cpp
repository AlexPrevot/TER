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

#include <chrono>
#include <omp.h>
#include <future>

#include <chrono>


#include "algogen.h"


std::shared_ptr<std::vector<std::vector<int>>> makeMatrice(std::vector<int>& path1, std::vector<int>& path2)
{
	int size = path1.size();
	std::shared_ptr<std::vector<std::vector<int>>> m(new std::vector<std::vector<int>>(size));

	std::vector<std::vector<int>> &matrice = *m;
	
	for (int i = 0; i < size; i++)
	{
		int pos = path1.at(i);
		if(i+1 < size)
			matrice.at(pos).push_back(path1.at(i + 1));
		else
			matrice.at(pos).push_back(path1.at(0));
		//---
		if(i-1 >= 0)
			matrice.at(pos).push_back(path1.at(i - 1));
		else
			matrice.at(pos).push_back(path1.at(size-1));
	}


	for (int i = 0; i < size; i++)
	{
		
		int pos = path2.at(i);
		std::vector<int> e = matrice.at(pos);

		if (i + 1 < size)
		{
			bool inside = std::find(e.begin(), e.end(), path2.at(i + 1)) != e.end();

			if (!inside)
				matrice.at(pos).push_back(path2.at(i + 1));
		}

		else
		{
			bool inside = std::find(e.begin(), e.end(), path2.at(0)) != e.end();

			if (!inside)
				matrice.at(pos).push_back(path2.at(0));
		}
		//---
		if (i - 1 >= 0)
		{
			bool inside = std::find(e.begin(), e.end(), path2.at(i - 1)) != e.end();

			if (!inside)
				matrice.at(pos).push_back(path2.at(i - 1));
		}
		else
		{
			bool inside = std::find(e.begin(), e.end(), path2.at(size - 1)) != e.end();

			if (!inside)
				matrice.at(pos).push_back(path2.at(size - 1));
		}
	}

	for(auto& v : matrice)
		std::random_shuffle(std::begin(v), std::end(v));

	return m;
}


//(!) FAIRE EN SORTE DE FOUTRE L'ENFANT DANS LE VECTEUR DE POPULATION DIRECTEMENT
void cross(popvect& pop, int position,std::vector<int>& path1, std::vector<int>& path2)
{
	
	std::shared_ptr<std::vector<std::vector<int>>> m = makeMatrice(path1, path2);
	
	std::vector<std::vector<int>>& matrice = *m;

	int size = path1.size();



	//std::shared_ptr<std::vector<int>> child_ptr(new std::vector<int>(size, -1));
	std::vector<int> child(path1.size(),-1);

	int N = path1.at(0);

	for (int i = 0; i < size; i++)
	{

		//push the node
		std::vector<int> &currVec = matrice.at(N);

		child.at(i) = N;

		//delete the element from all tab in matrice
		for (std::vector<int>& value : matrice)
			value.erase(std::remove(value.begin(), value.end(), N), value.end());


		int smallest = 1;
		int smallestNbr = 2;

		//things to do to know what's the next node to push
		if (!currVec.empty())
		{
			smallest = currVec[0];
			smallestNbr = matrice.size();


			

			for(int j = 0; j < currVec.size() ; j++)
			{
				std::vector<int>& vec = matrice.at(currVec.at(j));

				if ((vec.size() < smallestNbr) && (vec.size() != 0))
				{
					smallest = currVec.at(j);
					smallestNbr = vec.size();
				}
			}

			
		}
		else
		{

			for (int j = 0; j < size; j++)
			{
				
				if (std::find(child.begin(), child.end(), j) == child.end())
				{

					smallest = j;
					smallestNbr = matrice.at(j).size();
					j = size + 1;

				}
			}

		}
		N = smallest;
	}
	
	mutation(child, 0.02);
	
	std::get<1>(pop[position]) = child;
	//std::cout << "faire matrice fin -----------" << std::endl;
	/*
	std::shared_ptr<std::vector<int>> child = std::make_shared<std::vector<int>>();

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
	*/
}

void cross_over(std::vector<std::tuple<int, int>>& coord,popvect& population, int start, unsigned int * seeds)
{

	//int nbrTown = std::get<0>(population[0]);
	int size = population.size();

	
	/*
	for (int i = start+1; i < size; i++)
	{
		int parent1 = rand() % start;
		int parent2 = rand() % start;
		//std::cout << "avant cross" << std::endl;
		cross(population,i,std::get<1>(population[parent1]), std::get<1>(population[parent2]));
		//std::cout << "après cross" << std::endl;
		std::get<0>(population[i]) = getFitness(coord, std::get<1>(population[i]));
	}*/


	
	//unsigned int tid;
        //unsigned int seed;
	#pragma omp parallel
	{
	//tid = omp_get_thread_num();   // my thread id
        //seed = seeds[tid];            // it is much faster to keep a private copy of our seed
		//srand(seed);	
	srand(unsigned(time(NULL) * omp_get_thread_num()));
	
	#pragma omp for	
	for (int i = start + 1; i < size; i++)
	{
		
		int parent1 = rand() % start;
		int parent2 = rand() % start;
		cross(population, i, std::get<1>(population[parent1]), std::get<1>(population[parent2]));
		
		
		std::get<0>(population[i]) = getFitness(coord, std::get<1>(population[i]));
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



//fonction qui sert potentiellement plus à rien
//NOTE : Améliorer le sqrt pour augmenter les performances peut être utile ?
std::shared_ptr<std::vector<int>[]> fitness(std::vector<std::tuple<int,int>>						& coord,
															 std::shared_ptr<std::vector<int>[]>	& paths,
															 int									size)
{

	std::vector<std::tuple<int, int>> element(size);



	for (int k = 0; k < size ; k++)
		element.at(k) = std::make_tuple(getFitness(coord, paths[k]), k);



	sortByFitness2(element);

	std::shared_ptr<std::vector<int>[]> sortedPaths(new std::vector<int>[size]);

	for (int k = 0; k < size; k++)
		sortedPaths[k] = paths[std::get<1>(element.at(k))];

	return sortedPaths;
}






void sortByFitness2(std::vector<std::tuple<int,int>> &paths)
{
	std::sort(paths.begin(), paths.end());
}


void sortByFitness(popvect& paths)
{
	std::sort(paths.begin(), paths.end());
}



//return a list of tuple of "int" (score) and vector (path)
std::shared_ptr<popvect> generatePopulation(std::vector<std::tuple<int, int>>& coord,
											 int pop, int nbrCity)
{
	srand(unsigned(time(NULL)));

	std::shared_ptr<popvect> population(new popvect(pop));

	std::vector<int> sample(nbrCity);

	for (int i = 0; i < nbrCity; i++)
		sample.at(i) = i;

	for (int i = 0; i < pop; i++)
	{

		std::get<1>((*population)[i]) = sample;
		
		std::get<0>((*population)[i]) = 0;

		std::random_shuffle(std::begin(std::get<1>((*population)[i])), std::end(std::get<1>((*population)[i])));

		std::get<0>((*population)[i]) = getFitness(coord, std::get<1>((*population)[i]));
	}

	return population;
}

void mutation(std::vector<int>& chemin, float chance)
{
	for (int i = 0; i < chemin.size(); i++)
	{
		if (chance >= rand() % 100)
		{
			short place = rand() % chemin.size();
			short tmp1 = chemin.at(i);
			chemin.at(i) = chemin.at(place);
			chemin.at(place) = tmp1;
		}
	}
}




void mutation2(std::vector<int>& chemin, float chance)
{
		if (chance > rand() % 100)
		{
			short place1 = rand() % chemin.size();
			short place2 = rand() % chemin.size();
			short tmp1 = chemin.at(place1);
			chemin.at(place1) = chemin.at(place2);
			chemin.at(place2) = tmp1;
		}
}


void BENCHtest(std::vector<std::tuple<int, int>>& co, std::shared_ptr<std::vector<int>[]>& chemins, int nbrPaths, int iteration)
{

	std::cout << " ------------------- " << std::endl;
	std::cout << "ITERATION  " << iteration << std::endl;
	std::cout << "nbrPaths  " << nbrPaths << std::endl;
	std::cout << " " << std::endl;

	for (int i = 0; i < nbrPaths; i++)
	{
		std::cout << "[";
		for (int j = 0; j < co.size(); j++)
		{
			std::cout << chemins[i][j];
			std::cout << ",";
		}
		std::cout << " ]   FITNESS : ";

		std::cout << getFitness(co, chemins[i]);

		std::cout << "number : " << i << std::endl;


	}
}

//assume that population is already sort by fitness
void FUSS(popvect& population, int nbr, std::vector<int>& props)
{
	
	int size = population.size();
	float chunk = population.size() / 10;
	popvect v(nbr);

	float intervalle = (std::get<0>(population.back()) - std::get<0>(population[0]))/10;
	std::vector<int> fitnessGroup(10,-1);

	int count = 0;
	for (int i = 0; i < size; i++)
	{
		if (std::get<0>(population[i]) >= intervalle * count)
		{
			fitnessGroup[count] = i;
			count++;
		}

		if (count > 9)
			break;
	}
	
	for (int i = 0; i < nbr; i++)
	{
		//std::cout << "dernier for : " << i << std::endl;
		
		int index = props.at(rand() % 100);
		float a;
		if (index + 1 > 9)
			a = size - 1;
		else
			a = fitnessGroup[index + 1];
		float b = fitnessGroup[index];
		int element = rand() % int((a - b) + b);
		v[i] = population[element];
		//population[i] = population[element];
	}

	/*
	for (int i = 0; i < nbr; i++)
	{
		int index = props.at(rand() % 100);
		float a = (index + 1) * chunk;
		float b = index * chunk;
		int element = rand() % int((a - b) + b);
		v[i] = population[element];
		//population[i] = population[element];
	}
	*/
	for (int i = 0; i < nbr; i++)
	{
		population[i] = v[i];
	}
}






//FIRST ELEMENT OF EACH TUPLE SHOULD BE THE FITNESS SCORE, the 2nd is the position on the original 
//map position
std::vector<int> Calgogen(std::vector<std::tuple<int,int>> &coordCities, int nbrPaths)
{
	//omp_set_num_threads(5);
	unsigned int seeds[8];
	int my_thread_id;
	unsigned int seed;
	#pragma omp parallel private (seed, my_thread_id)
	{
		my_thread_id = omp_get_thread_num();
		unsigned int seed = (unsigned) time(NULL);
		//srand(unsigned(time(NULL) * omp_get_thread_num());
		seeds[my_thread_id] = (seed & 0xFFFFFFF0) | (my_thread_id + 1);
	}
	
	srand(unsigned(time(NULL)));

	int nbrCities = coordCities.size();


	std::vector<int> props;

	for (int i = 0; i < 61; i++)
		props.push_back(0);

	for (int i = 0; i < 10; i++)
		props.push_back(1);

	for (int i = 0; i < 9; i++)
		props.push_back(2);

	for (int i = 0; i < 8; i++)
		props.push_back(3);

	for (int i = 0; i < 7; i++)
		props.push_back(4);

	for (int i = 0; i < 5; i++)
		props.push_back(5);

	for (int i = 0; i < 4; i++)
		props.push_back(6);

	for (int i = 0; i < 3; i++)
		props.push_back(7);


	for (int i = 0; i < 2; i++)
		props.push_back(8);

	for (int i = 0; i < 1; i++)
		props.push_back(9);





	std::shared_ptr<popvect> chemins = generatePopulation(coordCities,nbrPaths, nbrCities);
	sortByFitness(*chemins);
	
	
	
	//---------------------------------
	int k = 10;
	/*
	std::shared_ptr<surpop> chemins(new surpop(k));

	for (int i = 0; i < k; i++)
	{
		(*chemins)[i] = *generatePopulation(coordCities, nbrPaths/k, nbrCities);
		sortByFitness((*chemins)[i]);
	}
	
	std::vector<int> champion = std::get<1>((*chemins)[0][0]);
	float best = getFitness(coordCities, champion);
	
	for (int i = 0; i < k; i++)
	{
		if ((std::get<0>((*chemins)[i][0])) < best)
		{
			best = std::get<0>((*chemins)[i][0]);
			champion = std::get<1>((*chemins)[i][0]);
		}
	}*/

	//-------------------------------
	
	
	
	std::vector<int> champion = std::get<1>((*chemins)[0]);
	float best = getFitness(coordCities, champion);
	
	

	int iterations = 0;

	int generation = 0;

	int subPopSize = nbrPaths / k;

	int selectionSize = (0.5 * nbrPaths) / k;

	std::vector<individuV> tmpMigrant(selectionSize);

	



	while (iterations < 200)
	{
		
		
		//FUSS(*chemins, 0.5 * nbrPaths, props);

		cross_over(coordCities, *chemins, 0.25 * nbrPaths, seeds);

		sortByFitness(*chemins);
			
			
			
			
		std::vector<int> currentChampion = std::get<1>((*chemins)[0]);
		float currentBest = getFitness(coordCities, currentChampion);

		if (currentBest < best)
		{
			best = currentBest;
			champion = currentChampion;
			iterations = 0;
			
		}
		else
			iterations++;

		generation++;
		
		
		//-------------------------
		/*
		for (int i = 0; i < k; i++)
		{

			FUSS((*chemins)[i], selectionSize, props);

			cross_over(coordCities, (*chemins)[i], selectionSize);

			sortByFitness((*chemins)[i]);

		}

		std::vector<int> currentChampion;//(nbrCities);
		float currentBest = std::get<0>((*chemins)[0][subPopSize-1]);

		for (int i = 0; i < k; i++)
		{
			if ((std::get<0>((*chemins)[i][0])) < best)
			{
				currentBest = std::get<0>((*chemins)[i][0]);
				currentChampion = std::get<1>((*chemins)[i][0]);
			}
		}



		

		if (currentBest < best)
		{
			best = currentBest;
			champion = currentChampion;
			iterations = 0;

		}
		else
			iterations++;

		generation++;

		if ((iterations % 100 == 0) && (iterations != 0))
		{
			
			std::vector<int> tmp(selectionSize);
			for (int i = 0; i < selectionSize; i++)
				tmp[i] = rand() % (subPopSize);

			for (int i = 0; i < k; i++)
			{
				short ind = rand() % k;
				for (int j = 0; j < selectionSize; j++)
				{
					individuV2 mem = (*chemins)[i][tmp[j]];
					(*chemins)[i][tmp[j]] = (*chemins)[ind][tmp[j]];
					(*chemins)[ind][tmp[j]] = mem;
				}
			}

			for(int i = 0; i < k; i++)
				sortByFitness((*chemins)[i]);
		}

			
		*/
		


		

		
	}
	
	return champion;
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

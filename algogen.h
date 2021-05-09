#pragma once
#include <vector>
#include <tuple>
#include <algorithm>
#include <math.h>
#include <deque>

//liste de tuples le premier element est le score, le deuxième élement est l'ordre des villes
typedef std::vector<std::tuple<int, std::vector<int>>> popvect; //je devrais l'appeler subpop mais c'est trop tard
typedef std::vector<popvect> surpop;
typedef std::vector<int> individuV;
typedef std::tuple<int, std::vector<int>> individuV2;

std::vector<int> algogen(std::vector<std::tuple<int, int>>& coordCities, int nbrPaths);

void sortByFitness2(std::vector<std::tuple<int, int>>& paths);
void sortByFitness(popvect& paths);

std::shared_ptr<std::vector<int>[]> fitness(std::vector<std::tuple<int, int>>& coord,
											std::shared_ptr<std::vector<int>[]>& paths, int size);

float getFitness(std::vector<std::tuple<int, int>>& coord,
				 std::vector<int>& path);

std::shared_ptr< popvect> generatePopulation(std::vector<std::tuple<int, int>>& coord,
																		int pop, int nbrCity);

std::shared_ptr<std::vector<std::vector<int>>> makeMatrice(std::vector<int>& path1, std::vector<int>& path2);

void cross_over(std::vector<std::tuple<int, int>>& coord,popvect& population, int start);


void cross(popvect& pop, int position,
	std::vector<int>& path1,
	std::vector<int>& path2);


void BENCHtest(std::vector<std::tuple<int, int>>& co, std::shared_ptr<std::vector<int>[]>& chemins, int nbrPaths, int iteration);

void mutation2(std::vector<int>& chemin, float chance);
void mutation(std::vector<int>& chemin, float chance);
void FUSS(popvect& population, int nbr, std::vector<int>& props);
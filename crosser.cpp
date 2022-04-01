#include "crosser.h"
#include <vector>
#include <unordered_set>

#include <iostream>
#include <time.h>
#include <algorithm>

struct comparator
{
	inline bool operator()(Path& p1, Path& p2)
	{
		return (p1.getFitness() < p2.getFitness());
	}
};


void Crosser::crossover(std::vector<Path> &population)
{
	int size = population.size();
	int start_indice = _selection_rate * size ;

	for (int i = start_indice; i < size; i++)
	{
		int ip1 = rand() % start_indice; // indice of parent 1
		int ip2 = rand() % start_indice; // indice of parent 2

		while(ip2 == ip1)
			ip2 = rand() % start_indice;

		
		population.at(i) = cross(population.at(ip1), population.at(ip2));

		mutate(population.at(i));
	}

	std::sort(population.begin(), population.end(), comparator());

}

Path Crosser::cross(Path & path1, Path& path2)
{
	using namespace std;

	int size = path1.getSize();
	int start = rand() % size;

	vector<unordered_set<int>> adjacencies(size);

	unordered_set<int> rest;

	for (int i = 0; i < size; i++)
		rest.insert(i);

	vector<int> ans(size,-1);

	for (int i = 0; i < size; i++)
	{

		int before = (i - 1) + (i - 1 < 0) * (size);
		int next = (i + 1) * (i + 1 < size);
		adjacencies.at(path1.at(i)).insert(path1.at(next));
		adjacencies.at(path2.at(i)).insert(path2.at(next));

		adjacencies.at(path1.at(i)).insert(path1.at(before));
		adjacencies.at(path2.at(i)).insert(path2.at(before));

	}


	int node = getRandom(adjacencies.at(start));
	ans.at(0) = node;
	int i = 1;
	while(i < size)
	{	
		rest.erase(node);

		

		auto adj = adjacencies.at(node);

		int ran = getRandom(adj);

		while (adj.size() > 0 && rest.find(ran) == rest.end())
		{
			adj.erase(ran);
			ran = getRandom(adj);
		}

		if (rest.size() > 0 && rest.find(ran) == rest.end())
		{
			ran = getRandom(rest);
		}
		
		
		ans.at(i) = ran;
		i++;

		node = ran;
	}
	Path p(ans);

	return p;
}

void Crosser::mutate(Path& p)
{
	for (int i = 0; i < p.getSize(); i++)
	{
		if (_mutation_rate >= rand() % 100)
		{
			int to = rand() % p.getSize();
			p.swap(to, i);
		}
	}
}

int Crosser::getRandom(std::unordered_set<int> set)
{
	if (!set.size())
		return -1;

	int idx = rand() % set.size();
	auto it = set.begin();
	for (int i = 0; i < idx; i++)
		it++;

	return *it;
}
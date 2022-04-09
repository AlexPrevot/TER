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


	for(int i = start_indice; i < size; i++)
	{
		int pot = rand() % 4;

		int ip1 = rand() % (start_indice); // indice of parent 2
		int ip2 = rand() % (start_indice); // indice of parent 1

		while(ip2 == ip1)
			ip2 = rand() % start_indice;

		
		population[i] = cross(population[ip1], population[ip2]);

		mutate(population[i]);
	}


	std::sort(population.begin(), population.end(), comparator());

}


Path Crosser::cross(Path& path1, Path& path2)
{
	using namespace std;

	int size = path1.getSize();
	int start = rand() % size;

	vector<vector<int>> adjacencies(size, vector<int>(4,-1));
	
	unordered_set<int> rest;
	for (int i = size - 1; i > - 1; i--)
		rest.insert(i);

	vector<int> ans(size, -1);

	vector<int> elem_nbr(size,0);

	for (int i = 0; i < size; i++)
	{

		int before = (i - 1) + (i - 1 < 0) * (size);
		int next = i + 1;
		if (next >= size)
			next = 0;

		auto& curr_vec1 = adjacencies[path1.at(i)];
		auto& curr_vec2 = adjacencies[path2.at(i)];

		
		if (!count(curr_vec1.begin(), curr_vec1.end(), path1.at(next)))
		{
			curr_vec1[elem_nbr[path1.at(i)]] = path1.at(next);
			elem_nbr[path1.at(i)]++;
		}

		if (!count(curr_vec1.begin(), curr_vec1.end(), path1.at(before)))
		{
			curr_vec1[elem_nbr[path1.at(i)]] = path1.at(before);
			elem_nbr[path1.at(i)]++;
		}
			//curr_vec1.push_back(path1.at(before));
		

		if (!count(curr_vec2.begin(), curr_vec2.end(), path2.at(next)))
		{
			curr_vec2[elem_nbr[path2.at(i)]] = path2.at(next);
			elem_nbr[path2.at(i)]++;
		}
			//curr_vec2.push_back(path2.at(next));
		
		if (!count(curr_vec2.begin(), curr_vec2.end(), path2.at(before)))
		{
			curr_vec2[elem_nbr[path2.at(i)]] = path2.at(before);
			elem_nbr[path2.at(i)]++;
		}
			//curr_vec2.push_back(path2.at(before));
	}


	for (auto& v : adjacencies)
	{
		while (v.back() == -1)
			v.pop_back();
	}

	//need to shuffle to break the order of the matrix. Otherwise bad results.
	for(auto& v : adjacencies)
		std::random_shuffle(v.begin(), v.end());


	int node = adjacencies[start][rand() % adjacencies[start].size()]; 
	ans[0] = node;
	int i = 1;



	while (i < size)
	{
		rest.erase(node);

		auto& adj = adjacencies[node];

		//no more than 4*4 operations
		for (int v : adj)
		{
			for (int d = 0; d < adjacencies[v].size(); d++)
			{
				if (adjacencies[v][d] == node)
				{
					adjacencies[v].erase(adjacencies[v].begin() + d);
				}

			}
		}

		int new_node = node;
		int max_neighboor = 4;

		//no more than 4 comparisons
		for (int v : adj)
		{
			auto& adjacent = adjacencies[v];
			if (adjacent.size() < max_neighboor)
			{
				max_neighboor = adjacent.size();
				new_node = v;
			}
		}

		if (adj.size() == 0)
		{
			new_node = getRandom(rest);
		}

		ans[i] = new_node;
		i++;

		node = new_node;
	}


	return ans;

}



/*
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
		int next = i + 1;
		if (next >= size)
			next = 0;
		adjacencies[path1.at(i)].insert(path1.at(next));
		adjacencies[path2.at(i)].insert(path2.at(next));
		//adjacencies.at(path2.at(i)).insert(path2.at(next));

		adjacencies[path1.at(i)].insert(path1.at(before));
		adjacencies[path2.at(i)].insert(path2.at(before));
		//adjacencies.at(path1.at(i)).insert(path1.at(before));
		//adjacencies.at(path2.at(i)).insert(path2.at(before));

	}


	int node = getRandom(adjacencies[start]);
	ans.at(0) = node;
	int i = 1;

	while(i < size)
	{	
		rest.erase(node);

		auto &adj = adjacencies[node];

		//no more than 4 deletions
		for (int v : adj)
			adjacencies[v].erase(node);
		
		int new_node = node;
		int max_neighboor = 4;

		//no more than 4 comparisons
		for (int v : adj)
		{
			auto &adjacent = adjacencies[v];
			if (adjacent.size() < max_neighboor)
			{
				max_neighboor = adjacent.size();
				new_node = v;
			}
		}
		
		if (adj.size() == 0)
		{
			new_node = getRandom(rest);
		}

		ans[i] = new_node;
		i++;

		node = new_node;
	}
	//Path p(ans);

	return ans;
}
*/


void Crosser::mutate(Path& p)
{
	//faisable en temps constant
	for (int i = 0; i < p.getSize(); i++)
	{
		if (_mutation_rate * 10 >= rand() % 1000)
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

double Crosser::getMutationRate()
{
	return _mutation_rate;
}

void Crosser::setMutationRate(double rate)
{
	_mutation_rate = rate;
}


double Crosser::getSelectionRate()
{
	return _selection_rate;
}

void Crosser::setSelectionRate(double rate)
{
	_selection_rate = rate;
}
#include "crosser.h"
#include <vector>
#include <unordered_set>

#include <iostream>
#include <time.h>
#include <unordered_map>

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

	for (int i = 0; i < size-1; i++)
	{
		adjacencies.at(path1.at(i)).insert(path1.at(i+1));
		adjacencies.at(path2.at(i)).insert(path2.at(i+1));
	}

	for (int i = 1; i < size; i++)
	{
		adjacencies.at(path1.at(i)).insert(path1.at(i - 1));
		adjacencies.at(path2.at(i)).insert(path2.at(i-1));
	}
	

	int node = getRandom(adjacencies.at(start));
	int i = 0;
	while(i < size)
	{	
		rest.erase(node);

		

		auto adj = adjacencies.at(node);

		int ran = getRandom(adj);

		while (adj.size() > 1 && rest.find(ran) == rest.end())
		{
			adj.erase(ran);
			ran = getRandom(adj);
		}

		if (rest.size() > 0 && rest.find(ran) == rest.end())
		{
			ran = getRandom(rest);
		}
		else
		{
			ans.at(i) = node;
			i++;
		}

		node = ran;
	}


	//Path ans({ 1,2,3 });
	return ans;
}

int Crosser::getRandom(std::unordered_set<int> set)
{
	int idx = rand() % set.size();
	auto it = set.begin();
	for (int i = 0; i < idx; i++)
		it++;

	return *it;
}
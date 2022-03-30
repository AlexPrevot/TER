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

	vector<int> ans_rep(size, -1);

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
	

	for (int i = 0; i < size; i++)
	{
		int node = getRandom(adjacencies.at(start));
		

		ans_rep.at(start) = node;

	}


	Path ans({ 1,2,3 });
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
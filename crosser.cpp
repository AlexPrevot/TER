#include "crosser.h"
#include <vector>
#include <set>

#include <iostream>
#include <time.h>
#include <unordered_map>

Path Crosser::cross(Path & path1, Path& path2)
{

	int node = rand() % path1.getSize();

	std::unordered_map<int, int> path2_rep;

	for (int i = 0; i < path2.getSize(); i++)
		path2_rep.insert({ path2.at(i), i });


	std::unordered_map<int, int> vec_rep; //representq the ouput vector in an unordered_map


	std::vector<int> ans_path(path1.getSize());

	for(int i = 0; i < path1.getSize(); i++)
	{
		int elem = path1.at(node);
		vec_rep.insert({ elem, i });


		


	}
	

	Path ans({ 1,2,3 });
	return ans;
}
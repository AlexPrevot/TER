#include "crosser.h"
#include <vector>
#include <set>

#include <iostream>
#include <time.h>
#include <unordered_map>

Path Crosser::cross(Path & path1, Path& path2)
{
	using namespace std;
	int size = path1.getSize();

	int node = rand() % size;
	
	vector<int> vec1(size, -1);
	vector<int> vec2(size, -1);

	//initialize 1st vector
	for (int i = 0; i < size - 1; i++)
		vec1[path1.at(i)] = path1.at(i + 1);
	vec1[path1.at(size - 1)] = path1.at(0);

	//initialize 2nd vector
	for (int i = 0; i < size - 1; i++)
		vec2[path2.at(i)] = path2.at(i + 1);
	vec2[path2.at(size - 1)] = path2.at(0);


	


	vector<int> ans_rep(size, -1);



	Path ans({ 1,2,3 });
	return ans;
}
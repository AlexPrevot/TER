#include "generator.h"
#include "path.h"


std::vector<Path> Generator::generate()
{
	std::vector<Path> population(_population_size);

	std::vector<int> individual_path(_individual_size);

	for (int i = 0; i < _individual_size; i++)
		individual_path.at(i) = i;


}

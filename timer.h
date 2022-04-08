#pragma 
#include <chrono>
#include <string>
class Timer
{
public:
	
	
	void start();
	

	void stop(std::string txt);


	

private:
	std::chrono::time_point<std::chrono::high_resolution_clock> m_StartTimePoint;

};


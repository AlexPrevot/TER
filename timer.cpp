#include "timer.h"
#include <iostream>

void Timer::start()
{
	m_StartTimePoint = std::chrono::high_resolution_clock::now();
}


void Timer::stop(std::string txt)
{
	auto endTimePoint = std::chrono::high_resolution_clock::now();

	auto start = std::chrono::time_point_cast<std::chrono::milliseconds>(m_StartTimePoint).time_since_epoch().count();
	auto end = std::chrono::time_point_cast<std::chrono::milliseconds>(endTimePoint).time_since_epoch().count();

	auto duration = end - start;

	std::cout << txt << " " << duration << " milliseconds" << "\n";
}




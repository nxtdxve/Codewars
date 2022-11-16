// https://www.codewars.com/kata/5648b12ce68d9daa6b000099/

#include <utility>
#include <vector>

unsigned int number(const std::vector<std::pair<int, int>>& busStops){
    unsigned int people = 0;
    for (auto& stop : busStops)
        people += stop.first - stop.second;
    return people;
}

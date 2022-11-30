// https://www.codewars.com/kata/57f609022f4d534f05000024/

#include <vector>
#include <algorithm>

int stray(std::vector<int> numbers) {
    int count = 0;
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = 0; j < numbers.size(); j++) {
            if (numbers[i] == numbers[j]) {
                count++;
            }
        }
        if (count == 1) {
            return numbers[i];
        }
        count = 0;
    }
    return 0;
};
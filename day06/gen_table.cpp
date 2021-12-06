#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

int main () {

  vector<uint8_t> fishes;
  long long int N;

  fishes.push_back(8);

  const int num_days = 264;

  for (int day = 1; day <= num_days; day += 1) {
    N = fishes.size();
    for (long long int i = 0; i < N; i++) {
      if (fishes[i] == 0) {
        fishes[i] = 6;
        fishes.push_back(8);
      } else {
        fishes[i] -= 1;
      }
    }
    printf("%i %llu\n", day, fishes.size());
  }

  return 0;

}

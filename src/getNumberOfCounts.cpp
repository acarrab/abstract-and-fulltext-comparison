#include <iostream>
#include <cmath>
#include <map>
#include "./progress.hpp"
using namespace std;

int main(int argc, char *argv[]) {
  map<unsigned long long, unsigned long long> counts;
  unsigned long long count;
  string ngram;
  Progress progress(argv[1]);

  while (cin >> count >> ngram) {
    if (counts.find(count) == counts.end()) counts[count] = 1;
    else counts[count]++;
    progress++;
  }

  cout << "occurances in text" << "," << "count" << "," << "log10 of count" << endl;
  for (auto counters : counts)
    cout << counters.first << "," << counters.second << "," << log10(counters.second) << endl;

  return 0;
}

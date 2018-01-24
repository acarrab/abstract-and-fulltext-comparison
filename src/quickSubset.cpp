#include <iostream>
#include <cstdlib>
#include "progress.hpp"

using namespace std;

int main(int argc, char *argv[]) {
  if (argc < 3) {
    cerr << "expects: <subset size> <total lines>" << endl;
    return -1;
  }
  unsigned long long remaining = atoi(argv[1]), total = atoi(argv[2]), i = 0;
  Progress progress(total);
  string line;
  while (remaining && getline(cin, line)) {
    if (0 == rand() % (total-- / remaining)) {
      cout << i++ << " " << line << endl;
      remaining--;
    }
    progress++;
  }
  return 0;
}

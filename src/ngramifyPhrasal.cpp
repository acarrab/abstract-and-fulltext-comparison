#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

class Progress {
  int total, decimalShift, lastValue;
  inline int valueOf(int progress) {
    return progress * decimalShift / total;
  }

public:
  Progress(int totalThings, int decimalPlaces) :
    total(totalThings), decimalShift(pow(10, decimalPlaces))
  {}
  inline void updateProgress(int progress) {
    if (lastValue != valueOf(progress)) {
      lastValue = valueOf(progress);
      fprintf(stderr, "\r%d.%d%%", lastValue / decimalShift, lastValue % decimalShift);
    }
  }
}



int main(int argc, char *argv[]) {
  string doc;
  int readSoFar = 0;
  int docCount = atoi(argv[1]);
  int lastOutput = 0;
  fprintf(stderr, "0%%");

  while (getline(cin, doc)) {
    for (int i = 0; i < doc.length(); i++) {
      // consume phrase
      if (doc[i] == '<') {
	while (doc[++i] != '>');
	while (doc[++i] != '<') {
	  if (doc[i] == ' ') cout << '_';
	  else cout << doc[i];
	}
	while (doc[++i] != '>');
      } else {
	cout << doc[i];
      }
    }
    cout << endl;
    readSoFar++;
    if (readSoFar * 100 / docCount != lastOutput) {
      lastOutput = readSoFar * 100 / docCount;
      fprintf(stderr, "\r%d%%", lastOutput);
    }
  }
}

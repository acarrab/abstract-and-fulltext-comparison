#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

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

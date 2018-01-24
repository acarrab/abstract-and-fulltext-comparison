#include <iostream>
#include <unordered_map>
#include <sstream>
#include <vector>
#include <algorithm>

#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

class Progress {
  int total, decimalShift, lastValue, progress;
  int valueOf(int progress) {
    return progress * decimalShift / total;
  }

public:
  Progress(int totalThings) :
    total(totalThings), decimalShift(100), lastValue(0), progress(0)
  {}
  void updateProgress() {
    if (lastValue != valueOf(progress)) {
      lastValue = valueOf(progress);
      fprintf(stderr, " %.2f%%\r", static_cast<float>(lastValue) / decimalShift);
    }
  }
  void increment() {
    progress++;
    updateProgress();
  }
  void set(int progress) {
    this->progress = progress;
    updateProgress();
  }
};

string removePeriods(string s) {
  string out;
  for (char c : s) if (c != '.') out += c;
  return out;
}

int main(int c, char *argv[]) {
  string document;
  register string word;
  Progress progress(atoi(argv[1]));
  unordered_map<string, int> words;

  while (getline(cin, document)) {
    stringstream documentstream(document);
    documentstream >> word; // get rid of pmid
    while (documentstream >> word) {
      word = removePeriods(word);
      if (words.find(word) == words.end()) {
	words[word] = 1;
      } else {
	words[word]++;
      }
    }
    progress.increment();
  }

  vector< pair< int,  string > > wordsOnCount;
  for (auto  wordCount : words) {
    wordsOnCount.push_back(make_pair(wordCount.second, wordCount.first));
  }
  sort(wordsOnCount.begin(), wordsOnCount.end());
  for (auto countWord : wordsOnCount) {
    cout << countWord.first << " " << countWord.second << endl;
  }

  cerr << "total number of unique words: " << words.size() << endl;
  return 0;
}

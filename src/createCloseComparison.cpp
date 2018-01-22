// input: <ngramFileSmall> <ngramFileBig> <inSmallOnly> <inBigOnly> <inBoth>
#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;


class TwoWayStringMap {
  unordered_map<string, long> s_id;
  vector<string> id_s;

 public:
  TwoWayStringMap() : s_id(), id_s() {}

  long insert(string s) {
    if (s_id.find(s) == s_id.end()) {
      s_id[s] = id_s.size();
      id_s.push_back(s);
    }
    return id_s.size() - 1;
  }

  long get(string s) const { return s_id[s]; }
  string get(long id) const { return id_s[id]; }
};







struct WordNode {
  string word;
  set<string> ngramParts;

  // -1 if not end
  long endOfNgram;

  unordered_map<string, WordNode*> children;
  WordNode(string word, long endOfNgram = -1) : word(word), closestMatch(""), endOfNgram(endOfNgram), children() {}
};


// finds ngrams that are part of other ngrams
class QuickSubgram {
  const WordNode *root;
  TwoWayStringMap ngramMap;
  unordered_map<long, int> ngramLengths;

public:
  QuickSubgram(string inFile) : root(new WordNode("ROOT", false)), ngramMap(), ngramLengths() {
    ifstream fin(inFile);
    for (string ngram; fin >> ngram;) {
      long id = ngramMap.insert(ngram);
      istringstream ss(ngram);
      WordNode *previous = nullptr, *current = root;

      int length = 0;
      for (string word; getline(ss, word, '_'); length++) {
	if (current->children.find(word) == current->children.end()) {
	  current->children[word] = new WordNode(word);
	}
	previous = current;
	current = current->children[word];
      }
      ngramLengths[id] = length;
      if (previous != nullptr) previous->endOfNgram = id;
    }
  }


  vector<string, int> findSubgramAndLengths(string ngram) {
    istringstream ss(ngram);
    unordered_map<string, int> ngramsAndLengths();
    vector<WordNode *> currents({ root });

    for (string word; getline(ss, word, '_');) {
      for (int i = currents.size() - 1; i >= 0; i--) {
	if (currents[i]->children.find(word) == currents[i]->children.end()) {
	  currents.erase(i);
	  continue;
	}
	currents[i] = currents[i]->children[word];
	long id = currents[i]->endOfNgram
	if (id != -1) {
	  ngramsAndLengths[ngramMap.get(id)] = ngramLengths[id];
	}
      }
    }

    vector<string, int> result;
    for (auto word_length : ngramsAndLengths()) {
      result.push_back(word_length);
    }
  }

}




int main (int argc, char *argv[]) {
  if (argc < 6) {
    cout << "input: <ngramFileSmall> <ngramFileBig> <inSmallOnly> <inBigOnly> <inBoth>" << endl;
    return -1;
  }


}

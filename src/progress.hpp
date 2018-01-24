#ifndef PROGRESS_HPP
#define PROGRESS_HPP

#include <cstdio>

class Progress {
  unsigned long long total, value, progress;
  bool updateValue() {
    unsigned long long newValue = progress * 100 * 10 / total;
    if (value != newValue) {
      value = newValue;
      return true;
    }
    return false;
  }


public:
  Progress(unsigned long long totalThings) :
    total(totalThings), value(0), progress(0)
  {updateProgress();}

  Progress(char *arg) :
    total(atoi(arg)), value(0), progress()
  {updateProgress();}

  void updateProgress() {
    if (updateValue())
      fprintf(stderr, "\r%d.%d%%%c", value / 10, value % 10, (value == 1000 ? '\n' : ' '));
  }
  Progress operator++(int) { progress++; updateProgress(); return *this; }
};

#endif

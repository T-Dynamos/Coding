#include <iostream> 
#include <string> 
#include <vector> 
#include <stdio.h>

using namespace std;

vector<string> list(int argc,char** array) {
  vector<string> list_;
  int i;
  for (i = 0; i < argc; ++i) {
    list_.push_back(array[i]);
  }
  return list_;
}

string str(string text, int n ){
  string str_ = "";
  int i;
  for (i = 0; i < n; ++i) {
    str_ = str_ + text;
  }
  return str_;
} 

void print_heading_end(string  text, int maxsize) {
  string space = str(" ", static_cast<int>(maxsize - text.length())/2) ;
  string space2;
  if ((space.length()*2)+text.length() < maxsize) {
    space2 = space + " ";
  } else  {
    space2 = space;
  }
  cout << "║" << space << text << space2 << "║\n";
}


void print_with_end(string  text, int maxsize) {
  string last_space = "";
  if (text.length() == maxsize-2) {
    last_space = " ";
  } else {
    last_space = str(" ", (maxsize-2) - (text.length()-1)); 
  }
  cout << "║" << " " << text << last_space << "║\n";
}

void print_box(vector<string> strings, int maxsize, string  tableof) {
  string space = str(" ",static_cast<int>(maxsize/2)-1);  
  cout << "╔" << str("═",maxsize) << "╗\n";
  print_heading_end(tableof, maxsize);
  cout << "╠" << str("═",maxsize) << "╣\n";
  for (auto x : strings) {
    print_with_end(x, maxsize);
  }
  cout << "╚" << str("═",maxsize) << "╝\n";
}

int main(int argc, char** argv) {
  vector<string> args = list(argc,argv);
  if (args.size() < 3 || args.size() > 3) {
    cout << "Invalid argument format.\nShould be: " << args[0] << " <number> <table_to>\n";
    return 1;
  }
  vector<string> answer;
  int i;
  for (i = 0; i < stoi(args[2]); i++) {
    answer.push_back(args[1] +  " x " + to_string(i+1) + " = " +  to_string((i+1)*stoi(args[1])));
  }
  int last_answer_lenght = to_string( stoi(args[1]) * stoi(args[2]) ).length();
  print_box(answer, args[1].length() + 3 + args[2].length() + 3 + last_answer_lenght + 2 , args[1] + "'s Table");
  return 0;
}

/*
 * Copyright (c) 2023 @T-Dynamos
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <stdio.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <thread>
#include <chrono>

using namespace std;

string red=    "\033[1;31m";
string green=  "\033[1;32m";
string yellow= "\033[1;33m";
string blue=   "\033[1;34m";
string purple= "\033[1;35m";
string cyan=   "\033[1;36m";
string grey=   "\033[1;37m";
string white=  "\033[1;38m";

void
clear ()
{
  cout << "\033[H\033[J";
}

string
str (string text, int n)
{
  string str_ = "";
  int i;
  for (i = 0; i < n; ++i)
    {
      str_ = str_ + text;
    }
  return str_;
}

vector < string > str_list (string text, int n)
{
  vector < string > str_;
  int i;
  for (i = 0; i < n; ++i)
    {
      str_.push_back (text);
    }
  return str_;
}

vector < string > add_list (vector < vector < string >> list)
{
  vector < string > final_;
for (auto x:list)
    {
    for (auto y:x)
	{
	  final_.push_back (y);
	}
    }
  return final_;
}

int mkint(double char_) 
{
  return static_cast<int>(char_);
}


vector<string> init_vector(int lenght,string text) 
{
  vector<string> final_;
  int i;
  for (i = 0;i < lenght; i += 1) {
    final_.push_back(text);
  }
  return final_;
}

vector < string > get_chars (int type)
{
  vector < string > chars;
  if (type == 1)
    {
      chars =
	{ "┏", "━", "┓", "┃", "┡", "┩", "╇", "┳", "┴",
    "└", "┘" };
    }
  else if (type == 2)
    {
      chars =
	{ "╔", "═", "╗", "║", "╠", "╣", "╬", "╦", "╩",
    "╚", "╝" };
    }
  else if (type == 3)
    {
    chars = init_vector(11,"{}");
  }
  else if (type == 4) 
  {
    chars = init_vector(11,"█");

  }
  return chars;
}

vector < int >
terminal_size ()
{
  struct winsize w;
  ioctl (STDOUT_FILENO, TIOCGWINSZ, &w);
  int rows = w.ws_row;
  int cols = w.ws_col;
  vector < int >size = { cols, rows };
  return size;
}

void sleep(int time) 
{
  this_thread::sleep_for(chrono::milliseconds(time));
}

vector < string > get_alphabet (char *alphabet, int height, int char_type)
{

  string alphabet_ = alphabet;
  vector < string > chars = get_chars (char_type);
  vector < string > compiled_alphabet = {alphabet_ + " not Avaliable!" };
  
  vector < vector < string >> tmp_compiled_alphabet;
  
  int upper = mkint(height/3.0);

  // for very small heights
  if (height < 5) {
    upper = 0;
  }

  // minimum height 3
  if (height < 3) {
  height = 3;
  }

  int char_width = mkint(height/1.3);
  int small_char_width = mkint(height/2.0);
  int half_char_width = mkint(char_width/2.0);
 
   // A
   if (strcmp(alphabet, "a") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {chars[0]+ str(chars[1],char_width) + chars[2]},
    {str_list(chars[3] + str(" ",char_width) + chars[3], upper)},
    {chars[4] + str(chars[1],char_width) + chars[5]},
    {str_list(chars[3] + str(" ",char_width) + chars[3], height - upper - 2)},
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }
 
 // B
  if (strcmp(alphabet, "b") == 0 ) 
  {
  if (char_width == 0 ) {
    char_width += 1;
  }
  tmp_compiled_alphabet = {
    {chars[0] + str(chars[1], small_char_width) + chars[2] + str(" ",(char_width)-small_char_width)},
    {str_list(chars[3] + str(" ",small_char_width) + chars[3] + str(" ",(char_width)-small_char_width), upper)},
    {chars[4] + str(chars[1], small_char_width) + chars[8] + str(chars[1],char_width-(small_char_width+1)) + chars[2]},
    {str_list(chars[3] + str(" ",char_width) + chars[3], height - upper - 3)},
    {chars[9]+ str(chars[1],char_width) + chars[10]}
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }

  // C
   if (strcmp(alphabet, "c") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {chars[0]+ str(chars[1],char_width+1)},
    {str_list(chars[3] + str(" ",char_width+1),height-2)},
    {chars[9]+ str(chars[1],char_width+1)}
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }

 // D
  if (strcmp(alphabet, "d") == 0 ) 
  {
  int near_1 = (char_width+2) / 4;
  tmp_compiled_alphabet = {
    {str(chars[1],near_1) + chars[7] + str(chars[1],char_width-near_1) + chars[2]},
    {str_list(str(" ",near_1) + chars[3] + str(" ",char_width-near_1-1) + " " + chars[3], height-2)},
    {str(chars[1],near_1)+ chars[8] + str(chars[1],char_width-near_1) + chars[10]}
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }


  // E
  if (strcmp(alphabet, "e") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {chars[0]+ str(chars[1],char_width+1)},
    {str_list(chars[3] + str(" ",char_width+1), upper)},
    {chars[4] + str(chars[1],char_width+1)},
    {str_list(chars[3] + str(" ",char_width+1), height - upper - 3)},
    {chars[9]+ str(chars[1],char_width+1)},
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }

  // F
  if (strcmp(alphabet, "f") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {chars[0]+ str(chars[1],char_width+1)},
    {str_list(chars[3] + str(" ",char_width+1), upper)},
    {chars[4] + str(chars[1],char_width+1)},
    {str_list(chars[3] + str(" ",char_width+1), height - upper - 3)},
    {chars[3]+ str(" ",char_width+1)},    
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }

  // G
  if (strcmp(alphabet, "g") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {chars[0]+ str(chars[1],char_width) + chars[2]},
    {str_list(chars[3] + str(" ",char_width+1),height-upper-3)},
    {chars[3]+ str(" ",char_width-small_char_width) + chars[0] + str(chars[1],small_char_width-1) + chars[2]},
    {str_list(chars[3] + str(" ",char_width) + chars[3],upper)},
    {chars[9]+ str(chars[1],char_width) + chars[10]}
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }

   // H
   if (strcmp(alphabet, "h") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {chars[3]+ str(" ",char_width) + chars[3]},
    {str_list(chars[3] + str(" ",char_width) + chars[3], upper)},
    {chars[4] + str(chars[1],char_width) + chars[5]},
    {str_list(chars[3] + str(" ",char_width) + chars[3], height - upper - 2)},
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }

  // I
  if (strcmp(alphabet, "i") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {str(chars[1],half_char_width+1) + chars[7] + str(chars[1],char_width-half_char_width)},
    {str_list(str(" ",half_char_width+1) + chars[3] + str(" ",char_width-(half_char_width)),height-2)},
    {str(chars[1],half_char_width+1) + chars[8] + str(chars[1],char_width-half_char_width)},
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }

  // J
  if (strcmp(alphabet, "j") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {str(chars[1],half_char_width+1) + chars[7] + str(chars[1],char_width-half_char_width)},
    {str_list(str(" ",half_char_width+1) + chars[3] + str(" ",char_width-half_char_width-1),small_char_width)},

    {chars[9] + str(chars[1],half_char_width) + chars[10] + str(" ",char_width-half_char_width)},
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }


    // K
   if (strcmp(alphabet, "k") == 0 ) 
  {

  int half = mkint(height/2.0) - 1;
  int op;
  for (op = half  + 1; op >= 0; op -= 1) {
    tmp_compiled_alphabet.push_back({chars[3] + str(" ",op) + chars[3] + str(" ", char_width - op)});
  }
 int o;
  for (o = 1; o <= (height - half) + 1 ; o += 1) {
    tmp_compiled_alphabet.push_back({chars[3] + str(" ",o) + chars[3] + str(" ", char_width - o)});
  }
  compiled_alphabet = add_list(tmp_compiled_alphabet);
 return compiled_alphabet;
  }

  // L
  if (strcmp(alphabet, "l") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {chars[3]+ str(" ",char_width+1)},
    {str_list(chars[3] + str(" ",char_width+1),height-2)},
    {chars[9]+ str(chars[1],char_width+1)}
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }

   // N
   if (strcmp(alphabet, "n") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {chars[0] + str(chars[1],char_width) + chars[2]},
    {str_list(chars[3] + str(" ",char_width) + chars[3], height-1)}
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }


  // O
  if (strcmp(alphabet, "o") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {chars[0]+ str(chars[1],char_width) + chars[2]},
    {str_list(chars[3] + str(" ",char_width) + chars[3],height-2)},
    {chars[9]+ str(chars[1],char_width) + chars[10]}
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }

  if (strcmp(alphabet, " ") == 0) 
  {
  tmp_compiled_alphabet = {
      {str_list(str(" ", char_width+2) , height)}
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }
  // W
  if (strcmp(alphabet, "w") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {str_list(chars[3] + str(" ",char_width) + chars[3] ,height - (height/2) )},
    {str_list(chars[3] + str(" ",half_char_width) + chars[3] + str(" ",char_width-half_char_width-1) + chars[3],(height/2) - 1)},
    {chars[9] + str(chars[1],half_char_width) + chars[8] + str(chars[1],char_width-half_char_width-1) + chars[10]},
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }

   // R
   if (strcmp(alphabet, "r") == 0 ) 
  {
  int lower = height - upper - 2;
  tmp_compiled_alphabet = {
    {chars[0]+ str(chars[1],char_width) + chars[2]},
    {str_list(chars[3] + str(" ",char_width) + chars[3], upper)},
    {chars[4] + str(chars[1],char_width) + chars[10]},
  };
  int o;
  for (o = 1; o <= lower; o += 1) {
    tmp_compiled_alphabet.push_back({chars[3] + str(" ",o) + chars[3] + str(" ", char_width - o)});
  }
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }

  // S
  if (strcmp(alphabet, "s") == 0 ) 
  {
  tmp_compiled_alphabet = {
    {chars[0]+ str(chars[1],char_width+1)},
    {str_list(chars[3] + str(" ",char_width+1), upper)},
    {chars[9] + str(chars[1],char_width)  + chars[2]},
    {str_list(str(" ",char_width+1) + chars[3] , height - upper - 3)},
    {str(chars[1],char_width+1) + chars[10]},
  };
  compiled_alphabet = add_list(tmp_compiled_alphabet);
  }

  return compiled_alphabet;
}

char* char_to_char_ptr(char c) {
    char* str = new char[2];
    str[0] = c;
    str[1] = '\0';
    return str;
}


void
print_decorated (string text, int char_type, int size)
{
  vector < int >term_size = terminal_size ();

  int width = term_size[0];
  int height = term_size[1];

  vector<string> chars = get_chars(char_type);

  int text_size = ( (mkint(size/1.3) + 2)*text.size() ) + (mkint(size/3.0)*(text.size())) ;


  int w_ = width/2 - ((mkint(size/1.3) + 2 + size/3)*text.size())/2;
  int h_ = height/2 - (size/2);

  vector <string> final_word = init_vector(size, "" );

  int i_a = 0;
  int i_b = 0;

  for (;i_a < final_word.size(); i_a += 1) { 
    for (char x : text) {
      vector<string> alphabet_ = get_alphabet(char_to_char_ptr(x), size,char_type);
      final_word[i_a] = final_word[i_a] + str(" ",mkint(size/3.0)) + alphabet_[i_b];
    }
    i_b += 1;
  }

  cout << chars[0] << str(chars[1],width-2) << chars[2] << endl;
  cout << str(chars[3] + str(" ",width-2) + chars[3] + "\n" ,h_-2);

  for (auto f : final_word) {
    int padding  = (width/2 - text_size/2) - 4 ;
    cout << chars[3] << str(" ",padding) << f << str(" ",width-(padding+text_size)-2) << chars[3] << endl;
  }

  cout << str( chars[3] + str(" ",width-2) + chars[3] + "\n"   ,(height - ( 1 + size + h_) ));
  cout << chars[9] << str(chars[1],width-2) << chars[10] << endl;

}

string tostring(vector<string> list, string sep) {
  string final_ = "";
  for (auto x : list ) {
    final_ = final_ + x + sep;
  }
  return final_;
}


int
main (int argc, char **argv)
{

  vector<string> colors = {"red","green","yellow","blue","purple","cyan","white","grey"};
  string colorss = tostring(colors,", ");

  colorss.pop_back();
  colorss.pop_back();

  if (argc > 5 || argc < 5) {
    cout << "Insuffient Args!\nUse: " << argv[0] << "<text> <type of char (1-4)> <sleeptime (in ms)> <color>\nColor can be " + colorss << "\n";
    return 1;
  } 

  string color = "none";
  string c_ = argv[4];
  
  for (auto x :colors) {
    if (x == c_) {
      color = x;
    }
  }

  if (color == "none") {
    cout << "Provide correct color : " +  colorss + "\n";
    return 1;
  }

  string oricolor;  

  if (color == "grey") {
    oricolor = grey;
  } else if (color == "white") {
    oricolor = white;
  } else if (color == "yellow") {
    oricolor = yellow;
  } else if (color == "blue") {
    oricolor = blue;
  } else if (color == "green") {
    oricolor = green;
  } else if (color == "cyan") {
    oricolor = cyan;
  } else if (color == "red") {
    oricolor = red;
  }
  cout << oricolor;

  vector < int >term_size = terminal_size ();

  int width = term_size[0];
  int height = term_size[1];
  int i;
 
  string t = argv[1];
  int max_ = (width - width/5) / t.size();

  if (max_ > height) {
    max_ = height -4;
  }
  int k = max_;
 
  int sleep_time = stoi(argv[3]);

  while (true) {
    for (i = 4; i <= max_; i += 1) {
      clear();
      print_decorated (argv[1], stoi (argv[2]) , i-1);
      sleep(sleep_time);
    }
    for (k = max_ - 1 ; k > 4; k -= 1) {

      clear();
      print_decorated (argv[1], stoi (argv[2]) , k-1);
      sleep(sleep_time);
    }
  
  // Update is terminal size changes
  width = terminal_size()[0];
  max_ = (width - width/5) / t.size();

  if (max_ > height) {
    max_ = height -4;
  }

 }
}

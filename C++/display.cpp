#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <stdio.h>
#include <sys/ioctl.h>
#include <unistd.h>

using namespace std;

#define loading

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

vector < string > get_alphabet (char *alphabet, int height, int char_type)
{
  // 8 Minimum Height
  if (height < 8)
    {
      height = 8;
    }
  vector < string > chars = get_chars (char_type);
  vector < string > compiled_alphabet;
  vector < vector < string >> compiled_alphabet_;
  int near_1 = static_cast < int >(height / height);
  int char_width = static_cast < int >(height / 2);
  // A
  if (strcmp (alphabet, "a") == 0)
    {
      compiled_alphabet_ = {
	{chars[0] + str (chars[1], char_width) + chars[2]},
	{str_list
	 (chars[3] + str (" ", char_width) + chars[3],
	  static_cast < int >(char_width / 2) - near_1)},
	{chars[4] + str (chars[1], char_width) + chars[5]},
	{str_list
	 (chars[3] + str (" ", char_width) + chars[3],
	  static_cast < int >(char_width / 2))}
      };
      compiled_alphabet = add_list (compiled_alphabet_);
    }
  // B
  else if (strcmp (alphabet, "b") == 0)
    {
      char_width += 1;
      compiled_alphabet_ = {
	{chars[0] + str (chars[1], static_cast < int >(char_width / 1.5)) +
	 chars[2]},
	{str_list
	 (chars[3] + str (" ", static_cast < int >(char_width / 1.5)) +
	  chars[3], static_cast < int >(char_width / 2) - (near_1))},
	{chars[4] + str (chars[1], static_cast < int >(char_width / 1.5)) +
	 chars[8] + str (chars[1],
			 char_width - (static_cast <
				       int >(char_width / 1.5)) -2) +
	 chars[2]},
	{str_list
	 (chars[3] +
	  str (" ",
	       static_cast <
	       int >(char_width / 1.5) + 1 + (char_width -
					      (static_cast <
					       int >(char_width / 1.5)) -2)) +
	  chars[3], static_cast < int >(char_width / 2) - (near_1 - 2))},
	{chars[9] +
	 str (chars[1],
	      static_cast <
	      int >(char_width / 1.5) + 1 + (char_width -
					     (static_cast <
					      int >(char_width / 1.5)) -2)) +
	 chars[10]},
      };
      compiled_alphabet = add_list (compiled_alphabet_);
    }
  return compiled_alphabet;
}

void
print_decorated (string text, int char_type, int size, char *char_)
{
  vector < int >term_size = terminal_size ();
  int width = term_size[0];
  int height = term_size[1];
  vector < string > chars = get_chars (char_type);
  //clear();
  vector < string > a = get_alphabet (char_, size, char_type);
for (auto x:a)
    {
      cout << x << endl;
    }
  //cout << chars[0] << str(chars[1],width-2) << chars[2] << "\n" << str(chars[3]+ str(" ",width-2) + chars[3] + "\n",height-4) << chars[9] << str(chars[1],width-2) << chars[10] << "\n";
}

int
main (int argc, char **argv)
{
  print_decorated (argv[1], stoi (argv[2]), stoi (argv[1]), argv[3]);
  //sleep(2);
}

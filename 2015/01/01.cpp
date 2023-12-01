#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <tuple>
#include <typeinfo>

using namespace std;
extern "C" int isdigit(int);


int part1(string input)
{
    long int f = 0;
    for (char c : input)
    {
        if (c == ')') {
            f--;
        }
        else if (c == '(') {
            f++;
        }
    }
    return f;
}

int part2(string input)
{
    long int f = 0;
    long int pos = 0;
    for (char c : input)
    {
        if (c == ')') {
            f--;
        }
        else if (c == '(') {
            f++;
        }
        pos++;
        if (f == -1) {
            return pos;
        }
    }
    return pos;
}

int main(int argc, char* argv[])
{
    if (argc < 2)
    {
        cout << "Not enough arguments" << endl;
        return 0;
    }

    string s;
    ifstream ifs(argv[1]);

    vector<string> input;

    while (getline(ifs, s))
    {
        cout << "Part 1 " << part1(s) << endl;
        cout << "Part 2 " << part2(s) << endl;
    }
    ifs.close();
    
    return 1;
}
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <tuple>
#include <typeinfo>

using namespace std;
extern "C" int isdigit(int);


int part1(vector<string> input)
{
    return 0;
}

int part2(vector<string> input)
{

    return 0;
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
        input.push_back(s);
    }
    ifs.close();
    cout << "Part 1 " << part1(input) << endl;
    cout << "Part 2 " << part2(input) << endl;
    return 1;
}
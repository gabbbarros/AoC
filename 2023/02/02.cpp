#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <tuple>
#include <typeinfo>
#include <map>
#include <climits>

using namespace std;
extern "C" int isdigit(int);
extern "C" int isalpha(int);

const int RED = 0;
const int GREEN = 1;
const int BLUE = 2;
const int MAX_RED = 12;
const int MAX_GREEN = 13;
const int MAX_BLUE = 14;

bool checkGame(vector<int>& count)
{
    if (count[RED] > MAX_RED || count[GREEN] > MAX_GREEN || count[BLUE] > MAX_BLUE)
    {
        return false;
    }
    else {
        return true;
    }
}

int parseValues(vector<int> &count, string s)
{
    count.clear();
    count.push_back(0);
    count.push_back(0);
    count.push_back(0);
    int r = 0;
    int n = 0;
    int index = 0;
    for (size_t i = 5; i < s.size(); i++)
    {
        if (s[i] == ':')
        {
            r = n;
            n = 0;
        }
        else if (s[i] == ';')
        {
            if (!checkGame(count))
            {
                return 0;
            }
            count[0] = count[1] = count[2] = 0;
            n = 0;
        }
        else {
            if (isdigit(s[i]))
            {
                n = n * 10 + (int(s[i] - 48));
            } else if(isalpha(s[i]))
            {
                switch (s[i])
                {
                case 'r':count[RED] = n; break;
                case 'g':count[GREEN] = n; break;
                case 'b':count[BLUE] = n; break;
                }
                n = 0;
                for (size_t j = i + 1; j < s.size(); j++)
                {
                    if (!(isalpha(s[j])))
                    {
                        i = j-1;
                        break;
                    }
                }
            }
        }
    }
    if (!checkGame(count))
    {
        return 0;
    }
    return r;
}


long int findSmallRequiredValues(vector<int>& count, string s)
{
    int r = 0;
    int n = 0;
    int smallest[] = { 0,0,0 };
    for (size_t i = 5; i < s.size(); i++)
    {
        if (s[i] == ':')
        {
            r = n;
            n = 0;
        }
        else if (s[i] == ';')
        {
            n = 0;
        }
        else {
            if (isdigit(s[i]))
            {
                n = n * 10 + (int(s[i] - 48));
            }
            else if (isalpha(s[i]))
            {
                switch (s[i])
                {
                case 'r': if(n > smallest[RED]) smallest[RED] = n; break;
                case 'g': if (n > smallest[GREEN]) smallest[GREEN] = n;  break;
                case 'b': if (n > smallest[BLUE]) smallest[BLUE] = n;  break;
                }
                n = 0;
                for (size_t j = i + 1; j < s.size(); j++)
                {
                    if (!(isalpha(s[j])))
                    {
                        i = j - 1;
                        break;
                    }
                }
            }
        }
    }
    
    return smallest[RED] * smallest[BLUE] * smallest[GREEN];
}

int part1(vector<string> input)
{
    int sum = 0;
    int id = 1;
    vector <int> count;
    for (string s : input) {
        if (parseValues(count, s) > 0)
        {
            sum += id;
        }
        id++;
    }
    return sum;
}

int part2(vector<string> input)
{
    int sum = 0;
    int id = 1;
    vector <int> count;
    for (string s : input) {
        sum += (findSmallRequiredValues(count, s));
    }
    return sum;
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
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <tuple>
#include <typeinfo>
#include <map>

using namespace std;
extern "C" int isdigit(int);

vector<string> split(string& s, string delimeter)
{
    vector<string> r;
    int pos;
    for (size_t i = 0; i < s.size(); i++) {
        pos = s.find(delimeter, i);
        if (pos < s.size())
        {
            r.push_back(s.substr(i, pos - i));
            i = pos;
        }
        else {
            r.push_back(s.substr(i));
            break;
        }
    }

    return r;
}


int part1(vector<string> input)
{
    int r = 0;
    int full = 0;
    int actual = 0;
    for (size_t indexInput = 0; indexInput < input.size(); indexInput++)
    {
        string s = input[indexInput];
        size_t fullSize = s.size();
        size_t less = 2;
        for (size_t i = 1; i < s.size() - 1; i++)
        {
            if (s[i] == '\\')
            {
                less++;
                i++;
                if (s[i] == 'x')
                {
                    i += 2;
                    less+=2;
                }
            }
        }
        r += fullSize - less;
        full += fullSize;
        actual += less;
    }

    return actual;
}

int part2(vector<string> input)
{
    int r = 0;
    int full = 0;
    int actual = 0;

    for (size_t indexInput = 0; indexInput < input.size(); indexInput++)
    {
        string s = input[indexInput];
        size_t fullSize = s.size();
        size_t less = 2;
        for (size_t i = 0; i < s.size(); i++)
        {
            if (s[i] == '\\' || s[i] == '\"')
            {
                less+=2;
            }
            else {
                less += 1;
            }
        }
        r += fullSize - less;
        full += fullSize;
        actual += less;
    }

    return actual-full;
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
        if (s.size() > 0)
        {
            if (s[s.size() - 1] == '\r')
                s = s.substr(0, s.size() - 1);
            input.push_back(s);
        }
    }
    ifs.close();

    int part_1 = part1(input);
    
    int part_2 = part2(input);

    cout << "Part 1 " << part_1 << endl;
    cout << "Part 2 " << part_2 << endl;
    
    
    return 1;
}
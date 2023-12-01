#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <tuple>
#include <typeinfo>

using namespace std;
extern "C" int isdigit(int);

bool hasThird(string s)
{
    if (s.find("ab") < s.size() || s.find("cd") < s.size() || s.find("pq") < s.size() || s.find("xy") < s.size())
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool hasSecond(string s)
{
    for (size_t i = 1; i < s.size(); i++) {
        if (s[i] == s[i - 1])
        {
            return true;
        }
    }
    return false;
}

bool hasFirst(string s)
{
    int v = 0;
    for (size_t i = 0; i < s.size(); i++) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
        {
            v++;
            if (v == 3)
            {
                return true;
            }
        }
    }
    return false;
}

int part1(vector<string> input)
{
    int r = 0;
    for (string s : input)
    {
        if (hasThird(s) || !hasSecond(s) || !hasFirst(s))
        {
            //cout << "this has: " << s << endl;
        }
        else {
            r++;
        }
    }
    return r;
}


bool hasDuplicateDouble(string s)
{
    int v = 0;
    for (size_t i = 0; i+1 < s.size(); i++) {
        string sub = s.substr(i,2);
        //cout << "\ti "<< i << " sub " << sub << " foun? " << s.find(sub, i + 1) << endl;
        if (s.find(sub,i+2) < s.size())
        {
            return true;
        }
    }
    return false;
}

bool hasDuplicateLetterWithPause(string s)
{
    int v = 0;
    for (size_t i = 0; i+2 < s.size(); i++) {
        if (s[i] == s[i + 2])
        {
            return true;
        }
    }
    return false;
}

int part2(vector<string> input)
{
    int r = 0;
    for (string s : input)
    {
        if (hasDuplicateDouble(s) && hasDuplicateLetterWithPause(s))
        {
            r++;
        }
    }
    return r;
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

    cout << "Part 1 " << part1(input) << endl;
    cout << "Part 2 " << part2(input) << endl;
    ifs.close();
    
    return 1;
}
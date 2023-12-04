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


unsigned int part1(vector<string> input)
{
    unsigned int r = 0;
    
    for (size_t indexInput = 0; indexInput < input.size(); indexInput++)
    {
        string s = input[indexInput];
        vector<string> sp = split(split(s, ":")[1], " ");
        map<unsigned int, bool> winning;
        vector<unsigned int> myNum;

        bool switched = false;
        for (size_t i = 0; i < sp.size(); i++)
        {
            if (sp[i].size() <= 0)
            {
                continue;
            }
            if (sp[i] == "|")
            {
                switched = true;
            }
            else {
                if (switched)
                {
                    winning[std::stoi(sp[i])] = true;
                }
                else
                {
                    myNum.push_back(std::stoi(sp[i]));
                }
            }
        }

        unsigned int rr = 0;
        for (unsigned int v : myNum)
        {
            if (winning.find(v) != winning.end())
            {
                if (rr == 0)
                {
                    rr = 1;
                }
                else
                {
                    rr = rr * 2;
                }
            }
        }

        r += rr;
    }

    return r;
}

unsigned int part2(vector<string> input)
{
    unsigned int r = 0;
    vector<unsigned int> cards;

    for (size_t indexInput = 0; indexInput < input.size(); indexInput++)
    {
        cards.push_back(1);
    }

    for (size_t indexInput = 0; indexInput < input.size(); indexInput++)
    {
        string s = input[indexInput];
        vector<string> sp = split(split(s, ":")[1], " ");
        map<unsigned int, bool> winning;
        vector<unsigned int> myNum;

        bool switched = false;
        for (size_t i = 0; i < sp.size(); i++)
        {
            if (sp[i].size() <= 0)
            {
                continue;
            }

            if (sp[i] == "|")
            {
                switched = true;
            }
            else {
                if (switched)
                {
                    winning[std::stoi(sp[i])] = true;
                }
                else
                {
                    myNum.push_back(std::stoi(sp[i]));
                }
            }
        }

        unsigned int rr = 0;
        for (unsigned int j = 0; j < myNum.size(); j++)
        {
            unsigned int v = myNum[j];
            if (winning.find(v) != winning.end())
            {
                rr += 1;
            }
        }

        unsigned int m = 1;
        for (size_t i = indexInput + 1; i < input.size() && i < indexInput +1+ rr; i++)
        {
            cards[i] = cards[i] + (cards[indexInput] * 1);
        }
    }

    r = 0;
    for (size_t i = 0; i < input.size() ; i++)
    {
        r+=cards[i];
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
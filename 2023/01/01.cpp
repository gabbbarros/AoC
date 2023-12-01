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
    int sum = 0;
    for (unsigned size = 0; size < input.size(); size++)
    {
        int a, b;
        a = b = -1;

        for (char c : input[size])
        {
            if (isdigit(c)) {
                if (a == -1) {
                    a = int(c) - 48;
                }
                else {
                    b = int(c) - 48;
                }
            }
        }
        if (b == -1) {
            b = a;
        }
        sum += (a * 10) + b;
    }
    return sum;
}

int findRightmost(string s, string a, string b, int value)
{
    int r = -1;
    unsigned pos1 = s.rfind(a);
    unsigned pos2 = s.rfind(b);
    if ((pos1 != string::npos && pos1 < s.size()) || (pos2 != string::npos && pos2 < s.size()))
    {
        if ((pos1 == string::npos || pos1 >= s.size()) || (pos2 != string::npos && pos2 < s.size() && pos2 > pos1))
        {
            r = pos2;
        }
        else
        {
            r = pos1;
        }
    }
    return r;
}

int findLeftmost(string s, string a, string b, int value)
{
    int r = -1;
    unsigned pos1 = s.find(a);
    unsigned pos2 = s.find(b);
    if ((pos1 != string::npos && pos1 < s.size()) || (pos2 != string::npos && pos2 < s.size()))
    {
        if ((pos1 == string::npos || pos1 >= s.size()) || (pos2 != string::npos && pos2 < s.size() && pos2 < pos1))
        {
            r = pos2;
        }
        else
        {
            r = pos1;
        }
    }
    return r;
}

std::tuple<string, string, int> numbers(int id) {
    switch (id)
    {
    case 1: return { "one","1",1 };
    case 2: return { "two","2",2 };
    case 3: return { "three","3",3 };
    case 4: return { "four","4",4 };
    case 5: return { "five","5",5 };
    case 6: return { "six","6",6 };
    case 7: return { "seven","7",7 };
    case 8: return { "eight","8",8 };
    case 9: return { "nine","9",9 };
    }
    throw std::invalid_argument("id");
}

int part2(vector<string> input)
{
    int sum = 0;

    for (unsigned size = 0; size < input.size(); size++)
    {
        string s = input[size];
        int a, b;
        a = b = -1;
        int va, vb;

        for(int i = 1; i < 10; i++)
        {
            const auto num = numbers(i);
            int x = findRightmost(s, get<0>(num), get<1>(num), get<2>(num));
            if (b < x)
            {
                b = x;
                vb = get<2>(num);
            }

            x = findLeftmost(s, get<0>(num), get<1>(num), get<2>(num));
            if (x!= -1 && (a ==-1 || a > x))
            {
                a = x;
                va = get<2>(num);
            }
        }
        sum += (va * 10) + vb;
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

    int sum = 0;
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
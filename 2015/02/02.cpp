#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <tuple>
#include <climits>

#include<algorithm>
#include <typeinfo>

using namespace std;
extern "C" int isdigit(int);

int part1(string input)
{
    vector<int> numbers;
    int n = 0;
    for (char c : input)
    {
        if (c == 'x') {
            numbers.push_back(n);
            n = 0;
        }
        else if(isdigit(c)) {
            n = (n * 10) + (int(c)-48);
            
        }
    }
    numbers.push_back(n);
    sort(numbers.begin(), numbers.end());

    return (((2 * numbers[0] * numbers[1]) + (2 * numbers[0] * numbers[2]) + (2 * numbers[2] * numbers[1]))) + (numbers[0]*numbers[1]);
}

int part2(string input)
{
    vector<int> numbers;
    int n = 0;
    for (char c : input)
    {
        if (c == 'x') {
            numbers.push_back(n);
            n = 0;
        }
        else if (isdigit(c)) {
            n = (n * 10) + (int(c) - 48);

        }
    }
    numbers.push_back(n);
    sort(numbers.begin(), numbers.end());

    return (((2 * numbers[0]) + (2 * numbers[1]) ) + (numbers[0] * numbers[1] * numbers[2]));
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
    long int sumPart1 = 0, sumPart2 = 0;
    while (getline(ifs, s))
    {
        //input.push_back(s);
        sumPart1 += part1(s);
        sumPart2 += part2(s);
    }
    cout << "Part 1 " << sumPart1 << endl;
    cout << "Part 2 " << sumPart2 << endl;
    
    ifs.close();

    return 1;
}
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <tuple>
#include <typeinfo>
#include <map>

using namespace std;
extern "C" int isdigit(int);

const int w = 1000;
const int h = 1000;

void readNumbers(string s, size_t start, vector<int> *num)
{
    int n = 0;
    for (size_t i = start; i < s.size(); i++) {
        if (isdigit(s[i]))
        {
            n = n * 10 + (int(s[i]) - 48);
        }
        else {
            num->push_back(n);
            n = 0;
            if (s[i] == ' ') {

                for (i = i + 1; i < s.size(); i++)
                {
                    if (s[i] == ' ') {
                        break;
                    }
                }
            }
        }
    }
    if (num->size() < 4)
    {
        num->push_back(n);
    }
}

int count(bool(&grid)[h][w], const bool value)
{
    int r = 0;
    for (size_t j = 0; j < h; j++)
    {
        for (size_t i = 0; i < w; i++)
        {
            //cout << grid[j][i];
            if (grid[j][i] == value)
            {
                r++;
            }
        }
        //cout << endl;
    }
    return r;
}

long int countBrightness(unsigned int(&grid)[h][w])
{
    long int r = 0;
    for (size_t j = 0; j < h; j++)
    {
        for (size_t i = 0; i < w; i++)
        {
            cout << grid[j][i]<<"\t";
            r += grid[j][i];
        }
        cout << endl;
    }
    return r;
}

int part1(vector<string> input)
{
    int r = 0;
    
    bool grid[h][w];
    for (size_t j = 0; j < h; j++)
    {
        for (size_t i = 0; i < w; i++)
        {
            grid[j][i] = false;
        }
    }
    

    for (string s : input)
    {
        vector<int> num;
        short mode;

        if (s[1] == 'o')
        {
            //toggle
            readNumbers(s, 7,&num);  
            mode = 0;
        }
        else
        {
            if (s[6] == 'n')
            {
                //turn on
                readNumbers(s, 8, &num);
                mode = 1;
            }
            else
            {
                //turn off
                readNumbers(s, 9, &num);
                mode = 2;
            }
        }
    

        if (num[1] > num[3])
        {
            int aux = num[1];
            num[1] = num[3];
            num[3] = aux;
        }

        if (num[0] > num[2])
        {
            int aux = num[0];
            num[0] = num[2];
            num[2] = aux;
        }
        /*cout << "\t turned to: " << num.size() << " numbers: [";
        for (int i = 0; i < num.size(); i++)
        {
            cout << num[i] << " ";
        }
        cout << "] mode: " << mode << endl;*/
        for (size_t y = num[1]; y <= num[3]; y++)
        {
            for (size_t x = num[0]; x <= num[2]; x++)
            {
                //cout << "[" << x << "," << y << "] ";
                switch (mode)
                {
                case 0: grid[y][x] = !grid[y][x]; break;
                case 1: grid[y][x] = true; break;
                case 2: grid[y][x] = false; break;
                default:cout << "ERROR! " << mode << endl;
                }
                //cout << grid[y][x] << " ";
            
            }
        }

        /*cout << "\ncounting " << num.size() << " numbers: [";
        for (int i = 0; i < num.size(); i++)
        {
            cout << num[i] << " ";
        }
        cout << "] mode: " << mode << endl;*/

    }
    
    return count(grid, true);
}

unsigned long long part2(vector<string> input)
{
    unsigned long long int r = 0;

    map<tuple<unsigned int, unsigned int>,unsigned int> grid;
    /*for (size_t j = 0; j < h; j++)
    {
        for (size_t i = 0; i < w; i++)
        {
            grid[j][i] = 0;
        }
    }*/

    vector<int> num;
    for (string s : input)
    {
        num.clear();
        short mode;

        if (s[1] == 'o')
        {
            //toggle
            readNumbers(s, 7, &num);
            mode = 0;
        }
        else
        {
            if (s[6] == 'n')
            {
                //turn on
                readNumbers(s, 8, &num);
                mode = 1;
            }
            else
            {
                //turn off
                readNumbers(s, 9, &num);
                mode = 2;
            }
        }


        if (num[1] > num[3])
        {
            int aux = num[1];
            num[1] = num[3];
            num[3] = aux;
        }

        if (num[0] > num[2])
        {
            int aux = num[0];
            num[0] = num[2];
            num[2] = aux;
        }
        /*cout << "\t turned to: " << num.size() << " numbers: [";
        for (int i = 0; i < num.size(); i++)
        {
            cout << num[i] << " ";
        }
        cout << "] mode: " << mode << endl;*/
        for (size_t y = num[1]; y <= num[3]; y++)
        {
            for (size_t x = num[0]; x <= num[2]; x++)
            {
                //cout << "[" << x << "," << y << "] ";
                tuple<int, int> t = { y, x };
                switch (mode)
                {
                case 0: 
                    r += 2;
                    if (grid.find(t) != grid.end())
                    {
                        grid[t] = grid[t]+2;
                    }
                    else
                    {
                        grid[t] = 2;
                    }
                    break;
                case 1: 
                    r++;
                    if (grid.find(t) != grid.end())
                    {
                        grid[t] = grid[t] + 1;
                    }
                          else
                    {
                        grid[t] = 1;
                    }
                    break;
                case 2: 
                    if (r - 1 > 0)
                        r--;
                    if (grid.find(t) != grid.end())
                    {
                        if (grid[t] != 0)
                        {
                            grid[t] = grid[t] - 1;
                        }
                        else {
                            grid[t] = 0;
                        }
                    }
                    break;
                default:cout << "ERROR! " << mode << endl;
                }
                //cout << grid[y][x] << " ";

            }
        }
        /*cout << "\ncounting " << num.size() << " numbers: [";
        for (int i = 0; i < num.size(); i++)
        {
            cout << num[i] << " ";
        }
        cout << "] mode: " << mode << endl;*/

    }
    r = 0;
    for (map <tuple<unsigned int, unsigned int>, unsigned int > ::iterator it = grid.begin(); it != grid.end(); ++it)
    {
        r += it->second;
    }
    return r;// countBrightness(grid);
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

    //cout << "Part 1 " << part1(input) << endl;
    cout << "Part 2 " << part2(input) << endl;
    ifs.close();
    
    return 1;
}
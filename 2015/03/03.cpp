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
    const int h = 1000;
    const int w = 1000;
    bool grid[h][w];
    for (size_t j = 0; j < h; j++) {
        for (size_t i = 0; i < w; i++) {
            grid[j][i] = false;
        }
    }
    int x = w / 2, y = h / 2;
    grid[y][x] = true;
    for (char c : input)
    {
        if (c == '>') {
            x++;
        }
        else if (c == '<') {
            x--;
        }
        else if (c == '^') {
            y--;
        }
        else if (c == 'v') {
            y++;
        }
        if (y >= h || y < 0 || x >= w || x < 0) {
            cout << "Grid is too small\n";
            return 0;
        }
        grid[y][x] = true;
    }

    int r = 0;
    for (size_t j = 0; j < h; j++) {
        for (size_t i = 0; i < w; i++) {
            if (grid[j][i])
            {
                r++;
            }
        }
    }
    return r;
}

int part2(string input)
{
    const int h = 1000;
    const int w = 1000;
    bool grid[h][w];
    for (size_t j = 0; j < h; j++) {
        for (size_t i = 0; i < w; i++) {
            grid[j][i] = false;
        }
    }
    int x = w/2, y = h/2;
    int x2 = w/2, y2 = h/2;
    grid[y][x] = true;
    int turn = 0;
    for (char c : input)
    {
        if (turn == 0)
        {
            if (c == '>') {
                x++;
            }
            else if (c == '<') {
                x--;
            }
            else if (c == '^') {
                y--;
            }
            else if (c == 'v') {
                y++;
            }
            if (y >= h || y < 0 || x >= w || x < 0) {
                cout << "Grid is too small\n";
                return 0;
            }
            grid[y][x] = true;
            turn++;
        }
        else {
            if (c == '>') {
                x2++;
            }
            else if (c == '<') {
                x2--;
            }
            else if (c == '^') {
                y2--;
            }
            else if (c == 'v') {
                y2++;
            }
            if (y2 >= h || y2 < 0 || x2 >= w || x2 < 0) {
                cout << "Grid is too small\n";
                return 0;
            }
            grid[y2][x2] = true;
            turn--;
        }
    }

    int r = 0;
    for (size_t j = 0; j < h; j++) {
        for (size_t i = 0; i < w; i++) {
            if (grid[j][i])
            {
                r++;
            }
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

    cout << "RESULTS" << endl;
    while (getline(ifs, s))
    {
        cout << "Part 1 " << part1(s) << endl;
        cout << "Part 2 " << part2(s) << endl;
    }
    ifs.close();
    
    return 1;
}
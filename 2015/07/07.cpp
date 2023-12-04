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

unsigned short getIndex(map<string, short>& indexes, vector<unsigned short>& var, string v, vector<bool>& setted)
{
    auto k = indexes.find(v);
    if (k != indexes.end())
    {
        return indexes[v];
    }
    else
    {
        indexes[v] = var.size();
        var.push_back(0);
        setted.push_back(false);
        return var.size() - 1;
    }
}
int part1(vector<string> input)
{
    int r = 0;
    map<string, short> indexes = {  };
    
    vector<unsigned short> var;    
    vector<string> splitted;

    unsigned short ind;
    bool done[input.size()];

    vector<bool> setted;
    for (size_t i = 0; i < input.size(); i++)
    {
        done[i] = false;
    }
    bool didAll = true;
    for (size_t indexInput = 0; indexInput < input.size(); indexInput++)
    {
        if (indexInput == 0)
        {
            didAll = true;
        }
        
        string s = input[indexInput];
        splitted = split(s, " ");
        if (!done[indexInput])
        {
            if (splitted.size() == 3) // Number -> Var
            {
                if (isdigit(splitted[0][0]))
                {
                    bool go = true;
                    ind = getIndex(indexes, var, splitted[2], setted);
                    var[ind] = std::stoi(splitted[0]);
                    setted[ind] = true;
                    done[indexInput] = true;
                }
                else
                {
                    ind = getIndex(indexes, var, splitted[2], setted);
                    unsigned short ind2 = getIndex(indexes, var, splitted[0], setted);
                    if (!setted[ind2])
                    {
                        didAll = false;
                    }
                    else
                    {
                        var[ind] = var[ind2];
                        setted[ind] = true;
                    }
                }
            }
            else if (splitted.size() == 5) //shift
            {
                if (splitted[1].compare("AND") == 0)
                {
                    ind = getIndex(indexes, var, splitted[4], setted);
                    unsigned short ind2, ind3;
                    bool isDigit2, isDigit3;

                    if (isdigit(splitted[0][0]))
                    {
                        ind2 = std::stoi(splitted[0]);
                        isDigit2 = true;
                    }
                    else
                    {
                        isDigit2 = false;
                        ind2 = getIndex(indexes, var, splitted[0], setted);
                    }

                    if (isdigit(splitted[2][0]))
                    {
                        ind3 = std::stoi(splitted[2]);
                        isDigit3 = true;
                    }
                    else
                    {
                        isDigit3 = false;
                        ind3 = getIndex(indexes, var, splitted[2], setted);
                    }

                    setted[ind] = false;
                    if (isDigit2 && isDigit3)
                    {
                        var[ind] = ind2 & ind3;
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else if (isDigit2 && setted[ind3])
                    {
                        var[ind] = (ind2 & var[ind3]);
                        setted[ind] = true;
                        done[indexInput] = true;

                    }
                    else if (isDigit3 && setted[ind2])
                    {
                        var[ind] = (var[ind2] & ind3);
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else if (setted[ind2] && setted[ind3])
                    {

                        var[ind] = (var[ind2] & var[ind3]);
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else
                    {
                        didAll = false;
                    }
                }
                else if (splitted[1].compare("OR") == 0)
                {
                    ind = getIndex(indexes, var, splitted[4], setted);
                    unsigned short ind2, ind3;
                    bool isDigit2, isDigit3;

                    if (isdigit(splitted[0][0]))
                    {
                        ind2 = std::stoi(splitted[0]);
                        isDigit2 = true;
                    }
                    else
                    {
                        isDigit2 = false;
                        ind2 = getIndex(indexes, var, splitted[0], setted);
                    }

                    if (isdigit(splitted[2][0]))
                    {
                        ind3 = std::stoi(splitted[2]);
                        isDigit3 = true;
                    }
                    else
                    {
                        isDigit3 = false;
                        ind3 = getIndex(indexes, var, splitted[2], setted);
                    }

                    setted[ind] = false;
                    if (isDigit2 && isDigit3)
                    {

                        var[ind] = ind2 | ind3;
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else if (isDigit2 && setted[ind3])
                    {

                        var[ind] = (ind2 | var[ind3]);
                        setted[ind] = true;
                        done[indexInput] = true;

                    }
                    else if (isDigit3 && setted[ind2])
                    {

                        var[ind] = (var[ind2] | ind3);
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else if (setted[ind2] && setted[ind3])
                    {

                        var[ind] = (var[ind2] | var[ind3]);
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else
                    {
                        didAll = false;
                    }
                }
                else if (splitted[1][0] == 'L')
                {
                    unsigned short ind2, ind3;
                    ind = getIndex(indexes, var, splitted[4], setted);
                    bool isDigit2, isDigit3;

                    if (isdigit(splitted[0][0]))
                    {
                        ind2 = std::stoi(splitted[0]);
                        isDigit2 = true;
                    }
                    else
                    {
                        ind2 = getIndex(indexes, var, splitted[0], setted);
                        isDigit2 = false;
                    }

                    if (isdigit(splitted[2][0]))
                    {
                        isDigit3 = true;
                        ind3 = std::stoi(splitted[2]);
                    }
                    else
                    {
                        isDigit3 = false;
                        ind3 = getIndex(indexes, var, splitted[2], setted);
                    }


                    if (isDigit2 && isDigit3)
                    {
                        var[ind] = (ind2) << ind3;
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else if (isDigit2 && setted[ind3])
                    {
                        var[ind] = (ind2) << var[ind3];
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else if (isDigit3 && setted[ind2])
                    {
                        var[ind] = var[ind2] << ind3;
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else if (setted[ind3] && setted[ind2])
                    {
                        var[ind] = var[ind2] << var[ind3];
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else
                    {
                        didAll = false;
                    }
                }
                else
                {
                    unsigned short ind2, ind3;
                    ind = getIndex(indexes, var, splitted[4], setted);
                    bool isDigit2, isDigit3;

                    if (isdigit(splitted[0][0]))
                    {
                        ind2 = std::stoi(splitted[0]);
                        isDigit2 = true;
                    }
                    else
                    {
                        ind2 = getIndex(indexes, var, splitted[0], setted);
                        isDigit2 = false;
                    }

                    if (isdigit(splitted[2][0]))
                    {
                        isDigit3 = true;
                        ind3 = std::stoi(splitted[2]);
                    }
                    else
                    {
                        isDigit3 = false;
                        ind3 = getIndex(indexes, var, splitted[2], setted);
                    }

                    if (isDigit2 && isDigit3)
                    {
                        var[ind] = (ind2) >> ind3;
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else if (isDigit2 && setted[ind3])
                    {
                        var[ind] = (ind2) >> var[ind3];
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else if (isDigit3 && setted[ind2])
                    {
                        var[ind] = var[ind2] >> ind3;
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else if (setted[ind3] && setted[ind2])
                    {
                        var[ind] = var[ind2] >> var[ind3];
                        setted[ind] = true;
                        done[indexInput] = true;
                    }
                    else
                    {
                        didAll = false;
                    }

                }
            }
            else if (splitted.size() == 4) //not
            {
                ind = getIndex(indexes, var, splitted[3], setted);
                unsigned short ind2 = getIndex(indexes, var, splitted[1], setted);

                if (setted[ind2])
                {
                    var[ind] = ~(var[ind2]);
                    setted[ind] = true;
                }
                else
                {
                    didAll = false;
                }
            }
            else
            {
                cout << "THROW ERROR " << endl;
                return 0;
            }
        }

        if (indexInput == input.size() - 1)
        {
            if (!didAll)
            {
                //restart
                indexInput = -1;
            }
        }
    }
        
    /*for (map<string, short>::iterator it = indexes.begin(); it != indexes.end(); it++)
    {
        cout << "[" << it->first << "] " << var[indexes[it->first]] << endl;
    }*/
    
    return var[indexes["a"]];
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
        if (s.size() > 0)
        {
            if (s[s.size() - 1] == '\r')
                s = s.substr(0, s.size() - 1);
            input.push_back(s);
        }
    }
    ifs.close();

    unsigned short part_1 = part1(input);
    string z = std::to_string(part_1) + " -> b";

    vector<string> input2;
    bool added = false;
    for (string ss : input)
    {
        if (!added && ss.find("-> b") != std::string::npos)
        {
            input2.push_back(z);
                added = true;
        }
        else
        {
            input2.push_back(ss);
        }
    }
    
    unsigned short part_2 = part1(input2);

    cout << "Part 1 " << part_1 << endl;
    cout << "Part 2 " << part_2 << endl;
    
    
    return 1;
}
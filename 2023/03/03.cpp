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

bool isPartNumber(vector<string>& input, int j, int i, int lengthNumber, bool onlyGear = false)
{
    size_t a, b;

    //is part number?
    //cout << "\ttest above" << endl;
    if (j - 1 >= 0)//above
    {
        a = i - lengthNumber - 1 >= 0 ? i - lengthNumber - 1 : 0;
        b = i + 1 < input[j - 1].size() ? lengthNumber + 2 : lengthNumber + 1;
        //cout << i << " " << "\t" << " : " << a << " " << b << endl;
        string s = input[j - 1].substr(a, b);

        //cout << std::flush;
        //cout << i << " " <<  "\t[" << s << "] "<<s.size()<<" : " << a << " " << b << endl;
        for (char c : s)
        {
            if (!isdigit(c) && c != '.' && c != '\r')
            {
                //cout << "\t\t\tABOVE"<<c<<"\n";
                return true;
            }
        }

    }
    //cout << "\ttest below" << endl;
    if (j + 1 < input.size()) //below
    {
        a = i - lengthNumber - 1 >= 0 ? i - lengthNumber - 1 : 0;
        b = i + 1 < input[j + 1].size() ? lengthNumber + 2 : lengthNumber + 1;
        //cout << i << " " << "\t" <<  " : " << a << " " << b << endl;
        string s = input[j + 1].substr(a, b);
        //cout << i << " " << "\t" << s << " : " << a << " " << b << endl;
        for (char c : s)
        {
            if (!isdigit(c) && c != '.' && c != '\r')
            {
                //cout << "\t\t\tBELOW\n";
                return true;
            }
        }
    }

    if (i - lengthNumber - 1 >= 0)//left
    {
        if (!isdigit(input[j][i - lengthNumber - 1]) && input[j][i - lengthNumber - 1] != '.')
        {
            //cout << "\t\t\tLEFT\n";
            return true;
        }
    }

    if (i < input[j].size() && !isdigit(input[j][i]) && input[j][i] != '.' && input[j][i] != '\r') //right
    {
        //cout << "\t\t\tRIGHT" << i << " " << input[j].size() << " :[" <<input[j]<<"]\n";
        return true;
    }



    /*if ([i - lengthNumber >= 0))//left
    {
        //above
        if(s[i - lengthNumber] != '.'))
        partNumbers.push_back(r);
    }
    else if((s[i] != '.'))
    {


    }
    */
    return false;
}

bool findGearsNumber(vector<string>& input, int j, int i, int lengthNumber, map<tuple<int,int>,int> &numbers, int r)
{
    size_t a, b;

    //is part number?
    //cout << "\ttest above" << endl;
    if (j - 1 >= 0)//above
    {
        a = i - lengthNumber - 1 >= 0 ? i - lengthNumber - 1 : 0;
        b = i + 1 < input[j - 1].size() ? lengthNumber + 2 : lengthNumber + 1;
        //cout << i << " " << "\t" << " : " << a << " " << b << endl;
        string s = input[j - 1].substr(a, b);

        //cout << std::flush;
        //cout << i << " " <<  "\t[" << s << "] "<<s.size()<<" : " << a << " " << b << endl;
        for (int k = 0; k < s.size(); k++)
        {
            if (s[k] == '*')
            {
                tuple<int, int> t = {i-k,j-1};
                auto it = numbers.find(t);
                if (it == numbers.end())
                    numbers[t] = 1;
                else
                    numbers[t] = 2;
                //cout << "\t\t\tABOVE"<<c<<"\n";
            }
        }

    }
    //cout << "\ttest below" << endl;
    if (j + 1 < input.size()) //below
    {
        a = i - lengthNumber - 1 >= 0 ? i - lengthNumber - 1 : 0;
        b = i + 1 < input[j + 1].size() ? lengthNumber + 2 : lengthNumber + 1;
        //cout << i << " " << "\t" <<  " : " << a << " " << b << endl;
        string s = input[j + 1].substr(a, b);
        //cout << i << " " << "\t" << s << " : " << a << " " << b << endl;
        for (int k = 0; k < s.size(); k++)
        {
            if (s[k] == '*')
            {
                //cout << "\t\t\tBELOW\n";
                tuple<int, int> t = { i - k,j - 1 };
                auto it = numbers.find(t);
                if (it == numbers.end())
                    numbers[t] = 1;
                else
                    numbers[t] = 2;
            }
        }
    }

    if (i - lengthNumber - 1 >= 0)//left
    {
        if (input[j][i - lengthNumber - 1] == '*')
        {
            tuple<int, int> t = { i - lengthNumber - 1,j - 1 };
            auto it = numbers.find(t);
            if (it == numbers.end())
                numbers[t] = 1;
            else
                numbers[t] = 2;
        }
    }

    if (input[j][i] == '*') //right
    {
        tuple<int, int> t = { i,j - 1 };
        auto it = numbers.find(t);
        if (it == numbers.end())
            numbers[t] = 1;
        else
            numbers[t] = 2;
    }


    return false;
}

int part1(vector<string> input)
{
    int r = 0;
    int lengthNumber = 0;
    vector<int> partNumbers;
    for (size_t j = 0; j < input.size(); j++)
    {
        string s = input[j];
        //cout << "line: " << s << endl;
        for (size_t i = 0; i < s.size(); i++)
        {
            if (!isdigit(s[i]))
            {
                if (r != 0)
                {
                    //cout << "r " << r << endl;
                    //is part number?
                    if (isPartNumber(input, j, i, lengthNumber))
                    {
                        cout << "found "<<r<<" " << endl;
                        partNumbers.push_back(r);
                    }

                    r = 0;
                    lengthNumber = 0;
                }
            } 
            else
            {
                r = (r * 10) + (int(s[i]) - 48);
                lengthNumber++;
            }
        }
        if (r != 0)
        {
            if (isPartNumber(input, j, s.size(), lengthNumber))
            {
                cout << ":found " << r << " " << endl;
                partNumbers.push_back(r);
            }
            r = 0;
            lengthNumber = 0;
        }
    }

    r = 0;
    for (int i : partNumbers)
    {
        r += i;
    }
    
    return r;
}

int getNumber(vector<string>& input, int x, int y)
{
    int b = x;
    while (b - 1 >= 0)
    {
        if (isdigit(input[y][b - 1]))
        {
            b--;
        }
        else {
            break;
        }
    }
    while (x + 1 < input.size())
    {
        if (isdigit(input[y][x + 1]))
        {
            x++;
        }
        else {
            break;
        }
    }
    int r = 0;
    for (b; b <= x; b++)
    {
        r = r * 10 + (int(input[y][b]) - 48);
    }
    return r;
}

int isGear(vector<string>& input, int i, int j)
{
    int count = 0;
    vector<tuple<size_t,size_t>> indexes;
    if (j - 1 >= 0) //above
    {
        if (i - 1 >= 0 && isdigit(input[j - 1][i - 1])) //left
        {
            count++;
            if (count > 2)
            {
                return 0;
            }
            indexes.push_back({ i - 1,j - 1 });
            if (!isdigit(input[j - 1][i]) && i + 1 < input[j - 1].size() && isdigit(input[j - 1][i + 1])) //NXN
            {
                count++;
                if (count > 2)
                {
                    return 0;
                }
                indexes.push_back({ i + 1,j - 1 });
            }
        }
        else //is in corner or has no digite top left, check above and right
        {
            if (isdigit(input[j - 1][i]) ) //above
            {
                count++;
                if (count > 2)
                {
                    return 0;
                }
                indexes.push_back({ i,j - 1 });
            }
            else if (i + 1 < input[j - 1].size() && isdigit(input[j - 1][i + 1])) //to the right above
            {
                count++;
                if (count > 2)
                {
                    return 0;
                }
                indexes.push_back({ i + 1,j - 1 });
            }
        }
    }

    if (j + 1 < input.size())//below
    {
        if (i - 1 >= 0 && isdigit(input[j + 1][i - 1])) //left
        {
            count++;
            indexes.push_back({ i - 1,j + 1 });
            if (!isdigit(input[j + 1][i]) && i + 1 < input[j + 1].size() && isdigit(input[j + 1][i + 1])) //NXN
            {
                count++;
                indexes.push_back({ i + 1,j + 1 });
            }
        }
        else //is in corner or has no digite below left, check below and right
        {
            if (isdigit(input[j + 1][i])) //below
            {
                count++;
                if (count > 2)
                {
                    return 0;
                }
                indexes.push_back({ i,j + 1 });
            }
            else if (i + 1 < input[j + 1].size() && isdigit(input[j + 1][i + 1])) //to the right below
            {
                count++;
                if (count > 2)
                {
                    return 0;
                }
                indexes.push_back({ i + 1,j + 1 });
            }
        }
    }

    if (i - 1 >= 0 && isdigit(input[j][i - 1])) //left
    {
        count++;
        if (count > 2)
        {
            return 0;
        }
        indexes.push_back({ i - 1,j});        
    }

    if (i + 1 < input[j].size() && isdigit(input[j][i + 1])) //to the right below
    {
        count++;
        if (count > 2)
        {
            return 0;
        }
        indexes.push_back({ i + 1,j });
    }

    if (count == 2)
    {
        vector<int> values;
        for (tuple<int, int> index : indexes)
        {
            values.push_back(getNumber(input, get<0>(index), get<1>(index)));
        }
        cout << values[0] << " " << values[1] << " " << (values[0] * values[1]) << endl;
        return values[0] * values[1];
    }
    else {
        return 0;
    }
}



int part2(vector<string> input)
{
    int r = 0;
    int lengthNumber = 0;
    for (size_t j = 0; j < input.size(); j++)
    {
        string &s = input[j];
        for (size_t i = 0; i < s.size(); i++)
        {
            if (s[i] == '*')//gear
            {
                //how many close numbers?
                r+=isGear(input, i, j);
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
        
    while (getline(ifs, s))
    {
        input.push_back(s);
    }

    //cout << "Part 1 " << part1(input) << endl;
    cout << "Part 2 " << part2(input) << endl;
    ifs.close();
    
    return 1;
}
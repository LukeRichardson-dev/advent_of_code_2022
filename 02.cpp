#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>

using namespace std;

void p1() {
    string line;
    ifstream file ("02_1.txt");

    if (!file.is_open()) return;

    int score = 0;
    while ( getline (file, line) )
    {   
        int other = line[0] - 64;
        int you = line[2] - 87;
        int diff = (you - other + 3) % 3;

        if (diff == 0) {
            score += 3;
        } else if (diff == 1) {
            score += 6;
        }
        score += you;
    }

    cout << score << endl;

    file.close();
}



void p2() { //    O  D  Y
    int memotable[3][3] {
        { 2, 0, 1 },
        { 0, 1, 2 },
        { 1, 2, 0 },
    };

    string line;
    ifstream file ("02_1.txt");

    if (!file.is_open()) return;

    int score = 0;
    while ( getline (file, line) )
    {   
        int other = line[0] - 65;
        int diff  = line[2] - 88;
        int you = memotable[diff][other];

        cout << other << ' ' << diff << ' ' << you << endl;

        if (diff == 1) {
            score += 3;
        } else if (diff == 2) {
            score += 6;
        }
        score += you + 1;
    }

    cout << score << endl;

    file.close();
}

int main() {
    p2();

    return 0;
}

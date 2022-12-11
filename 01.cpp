#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>

using namespace std;

void p1() {
    string line;
    ifstream file ("01_1.txt");

    if (!file.is_open()) return;

    int max = 0;
    int acc = 0;
    while ( getline (file, line) )
    {
        if (line.length() == 0) {
            if (acc > max) max = acc;
            acc = 0;
            continue;
        }
        int tnum = stoi(line);
        acc += tnum;
    }

    cout << "\n" << max << endl;
    file.close();
}

void p2() {
    string line;
    ifstream file ("01_1.txt");

    if (!file.is_open()) return;
    int max[3] { 0, 0, 0 };
    int acc { 0 };

    while ( getline (file, line) ) {
        if (line.length() == 0) {
            int index = -1;
            for (int i = 0; i < 3; i++) {
                if (max[i] >= acc) continue;
                index = i;
                break;
            }
            cout << index << endl;
            if (index != -1) {
                for (int i = 1; i >= index; i--) {
                    max[i+1] = max[i];

                    if (i == index) {
                        max[i] = acc;
                        break;
                    }
                }
            }
            acc = 0;
            continue;
        }
        int tnum = stoi(line);
        acc += tnum;
    }

    cout << max[0] + max[1] + max[2] << endl;
    cout << max[0] << endl;
    cout << max[1] << endl;
    cout << max[2] << endl;

    file.close();
}

int main() {
    p2();

    return 0;
}

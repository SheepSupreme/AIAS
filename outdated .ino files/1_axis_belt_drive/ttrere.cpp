#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
    ifstream inputFile("text.txt");

    if (!inputFile.is_open()) {
        cout << "Failed to open the file." << endl;
        return 1; // Exit the program with an error code
    }

    string line;
    while (getline(inputFile, line)) {
        // Process each line here, 'line' contains the current line of text
        cout << line << endl;
    }

    inputFile.close(); // Close the file when done

    return 0;
}
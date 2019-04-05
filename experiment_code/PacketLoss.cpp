#include<iostream>
#include<fstream>
#include<string>
#include<cstdlib>
#include<iomanip>
#include<set>

using namespace std;

void evaluatePacketLoss(string fileName);
void makeFile(string fileName);

int main() {

    string fileName = "results.txt";
    //makeFile("test.txt");
    evaluatePacketLoss(fileName);


    return 0;
}

void evaluatePacketLoss(string fileName) {
    ifstream input(fileName);
    int packets = 1024;
    int packetsReceived = 0;
    set<int> packetCollection;
    for(int i = 0; i < packets; i++) {
        packetCollection.emplace(i);
    }

    for(int i = 0; i < packets; i++) {
        string line;
        getline(input, line);
        try {
            if(packetCollection.find(stoi(line)) != packetCollection.end()) {
                packetsReceived++;
            }
        } catch(std::invalid_argument) {
            cout << "Lost packet at line " << i << endl;
        }
    }

    cout << "Packet loss is " << setprecision(2) <<  ((packets - packetsReceived) * 100.0) / packets << "%" << endl; 

    input.close();
}

void makeFile(string fileName) {
    ofstream output(fileName);

    for(int i = 0; i < 1024; i++) {
        output << to_string(i) << "\n";
    }

    output.close();
}
#include <iostream>
#include <fstream>
#include <vector>

struct Point {
    int x;
    int y;
};

struct Tile {
    int id;
    int cost;
    int available;
};

int main() {
    std::ifstream inputFile("00-trailer.txt"); // Assuming input file name is "input.txt"
    if (!inputFile) {
        std::cerr << "Failed to open the input file." << std::endl;
        return 1;
    }

    int width, height, goldenPoints, silverPoints, tileTypes;
    inputFile >> width >> height >> goldenPoints >> silverPoints >> tileTypes;
    
    std::vector<Point> goldenPointCoords(goldenPoints);
    std::vector<Point> silverPointCoords(silverPoints);
    std::vector<Tile> tiles(tileTypes);
    
    // Read golden points
    for (int i = 0; i < goldenPoints; ++i) {
        inputFile >> goldenPointCoords[i].x >> goldenPointCoords[i].y;
    }
    
    // Read silver points
    for (int i = 0; i < silverPoints; ++i) {
        inputFile >> silverPointCoords[i].x >> silverPointCoords[i].y;
    }
    
    // Read tiles
    for (int i = 0; i < tileTypes; ++i) {
        inputFile >> tiles[i].id >> tiles[i].cost >> tiles[i].available;
    }

    // Close the input file
    inputFile.close();
    
    // Continue with the rest of your program logic here
    
    return 0;
}

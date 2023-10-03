#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

// character class
class Character {
public:
    string name;
    int health;
    int attack;
    
    Character(string n, int h, int a) : name(n), health(h), attack(a) {}
};

// Monster class
class Monster {
public:
    string name;
    int health;
    int attack;
    
    Monster(string n, int h, int a) : name(n), health(h), attack(a) {}
};

// Function to simulate a battle
bool battle(Character& player, Monster& enemy) {
    while (player.health > 0 && enemy.health > 0) {
        // Player attacks first
        int playerDamage = rand() % player.attack + 1;
        enemy.health -= playerDamage;
        cout << "You hit " << enemy.name << " for " << playerDamage << " damage." << endl;
        
        // Check if the enemy is defeated
        if (enemy.health <= 0) {
            cout << "You defeated " << enemy.name << "!" << endl;
            return true;
        }
        
        // Enemy attacks
        int enemyDamage = rand() % enemy.attack + 1;
        player.health -= enemyDamage;
        cout << enemy.name << " hits you for " << enemyDamage << " damage." << endl;
        
        // Check if the player is defeated
        if (player.health <= 0) {
            cout << "You were defeated by " << enemy.name << ". Game Over!" << endl;
            return false;
        }
    }
    
    return true;
}

int main() {
    srand(static_cast<unsigned>(time(nullptr))); // Seed the random number generator
    
    cout << "Welcome to the Text-based RPG!" << endl;
    cout << "Create your character:" << endl;
    
    string playerName;
    cout << "Enter your character's name: ";
    cin >> playerName;
    
    Character player(playerName, 100, 20);
    
    cout << "Welcome, " << player.name << "! Let's begin your adventure." << endl;
    
    // Main game loop
    while (true) {
        cout << "You are in a room. What do you want to do?" << endl;
        cout << "1. Explore" << endl;
        cout << "2. Quit" << endl;
        
        int choice;
        cin >> choice;
        
        if (choice == 1) {
            // Generate a random monster
            Monster enemy("Monster", rand() % 50 + 50, rand() % 10 + 10);
            cout << "You encounter a " << enemy.name << " with " << enemy.health << " health." << endl;
            
  
            if (battle(player, enemy)) {
                cout << "You continue your adventure." << endl;
            } else {
                break; 
            }
        } else if (choice == 2) {
            cout << "Thanks for playing!" << endl;
            break;
        } else {
            cout << "Invalid choice. Please choose 1 or 2." << endl;
        }
    }
    
    return 0;
}

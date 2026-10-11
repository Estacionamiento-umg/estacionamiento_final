#include <iostream>
#include <cmath>
#include <string>
using namespace std;

double calcular(string tipo, int minutos) {
    double base = 0;
    double extra = 0;
    int horasIncluidas = 2;

    if (tipo == "carro") {
        base = 20;
        extra = 5;
    } else if (tipo == "moto") {
        base = 10;
        extra = 3;
    } else if (tipo == "camion") {
        base = 35;
        extra = 10;
    } else {
        base = 15;
        extra = 4;
    }

    double horas = minutos / 60.0;

    if (horas <= horasIncluidas) {
        return base;
    }

    int horasExtra = ceil(horas - horasIncluidas);
    return base + (horasExtra * extra);
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cout << "Uso: motor_tarifas TIPO MINUTOS";
        return 1;
    }

    string tipo = argv[1];
    int minutos = stoi(argv[2]);

    cout << calcular(tipo, minutos);
    return 0;
}

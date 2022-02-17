#include<iostream>
#include<stdlib.h>
#include<string>
using namespace std;


class ClienteFisico{
    //Atributos
    public:
        double numero_cuenta;
        double numero_cliente;

        float retiro;
        float abono;
        float capital;

        
    //Metodoss
    public:
        ClienteFisico(double,double,float);
        float abonar();
        float retirar();
};


class ClienteMoral : public ClienteFisico{
};



ClienteFisico::ClienteFisico(double _numero_cuenta,double _numero_cliente,float _capital){
    numero_cuenta = _numero_cuenta;
    numero_cliente = _numero_cliente;
    capital = _capital;
}

float ClienteFisico::abonar(){
    cout<<"Ingrese la cantidad a abonar a su cuenta: ";
    cin>>abono;
    capital = abono + capital;
    cout<<capital<<endl;
}
float ClienteFisico::retirar(){
    cout<<"Ingrese la cantidad a retirar de su cuenta: ";
    cin>>retiro;
    capital = capital - retiro;
    cout<<capital<<endl;
}

int main(){
 
    ClienteFisico cliente1 = ClienteFisico(1234,23423,100);
    cout<<"Bienvenido"<<endl;
    cliente1.abonar();
    cliente1.retirar();





    return 0;
}
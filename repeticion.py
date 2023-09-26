#include <iostream>
#include <vector>


using namespace std;

int i,j,cajita,arreglo[9], arreglo2[9];
int contador=1;
vector<int> numerosFiltrados, numerosCantidades;


void menu()
{
    for(i=0;i<9;i++)
    {
        cout<<"Ingrese tu "<<i+1<<" numero: ";
        cin>>arreglo[i];
    }
      for(i=0;i<9;i++)
    {
        for(j=i+1;j<9;j++)
        {
            if(arreglo[i]>arreglo[j])
            {
              cajita=arreglo[i];
              arreglo[i]=arreglo[j];
              arreglo[j]=cajita;
            }


        }
    }
    cout<<"Numero menor: "<<arreglo[0]<<"\n";
    cout<<"Numero medio: "<<arreglo[4]<<"\n";
    cout<<"Numero mayor: "<<arreglo[8]<<"\n";

     for (int i = 0; i < 9; i++)

        if(arreglo[i] != arreglo[i+1]){

            numerosFiltrados.push_back(arreglo[i]);
            numerosCantidades.push_back(contador);
            contador = 1;
        }

        else{
            contador++;
        }


        int mayorCantidades = numerosCantidades[0];
        int posMayor = 0;

    for (int i = 1; i < numerosCantidades.size(); i++)
    {

        if (numerosCantidades[i] > mayorCantidades){

            mayorCantidades = numerosCantidades[i];
            posMayor = i;
        }
    };

    cout << "El numero que más se repite es el " << numerosFiltrados[posMayor];

}




int main()
{
menu();
}
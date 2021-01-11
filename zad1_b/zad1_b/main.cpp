#include <bits/stdc++.h>
#include <iostream>
using namespace std;

const int N = 7;

int main()
{
    int matrix[][N] ={  {3, 1, 0, 0, 0, 0, 0} ,
                        {1, 4, 1, 0, 0, 0, 0} ,
                        {0, 1, 4, 1, 0, 0, 0} ,
                        {0, 0, 1, 4, 1, 0, 0} ,
                        {0, 0, 0, 1, 4, 1, 0} ,
                        {0, 0, 0, 0, 1, 4, 1} ,
                        {0, 0, 0, 0, 0, 1, 3} };
    int u[N] = {1,
                0,
                0,
                0,
                0,
                0,
                1};

    int v[N] = {1, 0, 0, 0, 0, 0, 1};  // v^t


    int b[N] = {1, 2, 3, 4, 5, 6, 7};

    double y[N];
    double z[N];
    double q[N];


    //***********************************
    // FAKTORYACJA CHOLESKY'EGO
    double lower[N][N];
    memset(lower, 0, sizeof(lower));

    for (int i = 0; i < N; i++) {

        if(i == 0) { // liczenie pierwszego elementu diagonali
            lower[0][0] = sqrt(matrix[0][0]);
            continue;
        }

        for (int j = i-1; j <= i; j++) {

            if (j == i) // liczenie diagonali
                lower[j][j] = sqrt(matrix[j][j] - pow(lower[j][j-1], 2));

             else // liczenie elementow o 1 nizej diagonali
                lower[i][j] = matrix[i][j] / lower[j][j];            
        }
    }

    //Wypisanie sfaktoryzowanej macierzy C, nie wypisujemy C^t
    cout << "Macierz C: " << endl;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < i+1; j++)
            printf("%f ", lower[i][j]);
        printf("\n");
    }

    cout << endl << endl;

    //  A = C(C^t)z = b
    //  (C^t)*z = y
    //  Cy = b


    //******************************************
    //OBLICZANIE Az = b

    // rozwiazywanie rowania Cy = b metoda forward substitution
    double sum = 0;
    y[0] = b[0]/lower[0][0];

    for(int i = 1; i < N; ++i) {

        sum = lower[i][i-1] * y[i-1];
        y[i] = (b[i]-sum) / lower[i][i];
    }

    //  rozwiazywanie rownania (C^t)z = y metoda backward substitution
    sum = 0;
    z[N-1] = y[N-1]/lower[N-1][N-1];

    for(int i = N-2; i >= 0; --i) {
        sum = lower[i+1][i] * z[i+1];
        z[i] = (y[i]-sum) / lower[i][i];
    }

    // Wypisanie rozwiazan [z] ukladu rownnan Az = b
    for(int i = 0; i < N; ++i)
        cout << "z" << i+1 <<": " << z[i] << endl;
    cout << endl;



    //**********************************************
    //OBLICZANIE Aq = u


    //  A = C(C^t)q = u
    //  (C^t)*q = y
    //  Cy = u
    // rozwiazywanie ukladu rownan liniowych Cy = u metoda forward substitution
     sum = 0;
     y[0] = u[0]/lower[0][0];

     for(int i = 1; i < N; ++i) {

         sum = lower[i][i-1] * y[i-1];
         y[i] = (u[i]-sum) / lower[i][i];
     }

     //  rozwiazywanie ukladu rownan liniowych (C^t)q = y metoda backward substitution
     sum = 0;
     q[N-1] = y[N-1]/lower[N-1][N-1];

     for(int i = N-2; i >= 0; --i) {
         sum = lower[i+1][i] * q[i+1];
         q[i] = (y[i]-sum) / lower[i][i];
     }

    // Wypisanie rozwiazan [q] ukladu rownnan Aq = u
     for(int i = 0; i < N; ++i)
         cout << "q" << i+1 <<": " << q[i] << endl;
     cout << endl;


     //*************************************************
     // Obliczanie ostatecznego rozwiazania zgodnie z ponizszym wzorem
     // w = z - q[ (v^t)z / (1 + (v^t)q) ]

     //***
     // (v^t)z  - licznik
     double vtz = 0;

     for(int i = 0; i < N; ++i)
         vtz += v[i] * z[i];


     //***
     // 1 + (v^t)q - mianownik
     double vtq = 0;

     for(int i = 0; i < N; ++i)
         vtq += v[i] * q[i];
     ++vtq;


     //***
     // ulamek * q
     for(int i = 0; i < N; ++i) {
         q[i] *= vtz;
         q[i] /= vtq;
     }


     //***
     //obliczanie w
     double w[N];

     for(int i = 0; i < N; ++i)
         w[i] = z[i] - q[i];


     // Wypisanie rozwiazan [w]
     for(int i = 0; i < N; ++i)
         cout << "w" << i+1 <<": " << w[i] << endl;
     cout << endl;

     return 0;
}


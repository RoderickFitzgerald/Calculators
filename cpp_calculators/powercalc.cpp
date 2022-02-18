#include <iostream>


int power (int base , int exponent ) {
    if (exponent == 0)
    {
        return 1;
    }
    else 
    {
        return base * power(base, exponent - 1);
    }        
}

int main ()
{
    std::cout << power(4, 4);   
    return 0;
}
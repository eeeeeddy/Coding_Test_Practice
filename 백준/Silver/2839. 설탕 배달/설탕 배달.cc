#include <iostream>

using namespace std;

int n;

int main()
{
	cin >> n;
	int a = 0; //3
	int b = 0; //5
	while (n % 5 != 0 && n >= 0)
	{
		n -= 3;
		a++;
	}
	if (n < 0)
	{
		cout << -1 << endl;
	}
	else
	{
		b = n / 5;
		cout << a + b << endl;
	}
}
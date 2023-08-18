#include <iostream>

using namespace std;

int fibo(int n);

int main() {
	cin.tie(NULL); //cin의 처리속도 증가
	
	int n;
	cin >> n;
	cout << fibo(n) << endl;
}

int fibo(int n) {
	int x;
	if (n == 0) return 0;
	else if (n == 1) return 1;
	else {
		x = fibo(n - 1) + fibo(n - 2);
		return x;
	}
}


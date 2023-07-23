#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

inline int ind(int x, int y, int z, int n) {
    return x * n * n + y * n + z;
}

double get_result(double p, int n, int x, double* f) {
    memset(f, 0, sizeof(double) * (n + 1) * (n + 1) * (n + 1));
    for(int j = 0; j <= x; ++j) for(int k = 0; k <= x; ++k)f[ind(0, j, k, n+1)] = 1;
    for(int i = 1; i <= n; ++i) {
        for(int j = 0; j <= x; ++j) {
            for(int k = 0; k <= x; ++k) {
                f[ind(i, j, k, n+1)] = (1 - p) * f[ind(i - 1, 0, j + 1, n+1)] + p * f[ind(i - 1, j + 1, k + 1, n+1)];
            }
        }
    }
    return f[ind(n, 0, 0, n+1)];
}

int main(int argc, char* argv[]) {
    int n = atoi(argv[1]);
    double p = atof(argv[2]);
    double* f = new double[(n + 1) * (n + 1) * (n + 1)];
    double* r = new double[n + 1];
    
    for(int i = 0; i <= n; ++i) r[i] = get_result(p, n, i, f);

    double e = 0;
    for(int i = 1; i <= n; ++i) e = e + i * (r[i] - r[i - 1]);
    printf("ans = %.6lf\n", e);
    delete[] r;
    delete[] f;
    return 0;
}
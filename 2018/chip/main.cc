#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <sys/time.h>

void f(const int m, const int n, const int k, const double *A, const double *B, double *C) {
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      for (int l = 0; l < k; ++l) {
        C[n * i + j] += A[k * i + l] * B[n * l + j];
      }
    }
  }
}

void init(const int m, const int n, const int k, double *A, double *B, double *C) {
  for (int i = 0; i < m; ++i) {
    for (int l = 0; l < k; ++l) {
      A[k * i + l] = i + l;
    }
  }
  for (int l = 0; l < k; ++l) {
    for (int j = 0; j < n; ++j) {
      B[n * l + j] = 2 * l - j;
    }
  }
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      C[n * i + j] = 0.0;
    }
  }
}

void print(const int m, const int n, const double *C) {
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      printf("%f ", C[n * i + j]);
    }
    printf("\n");
  }
}

double get_max_error(const int m, const int n, const int k, const double *A, const double *B, double *C) {
  double max_err = 0.0;
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      for (int l = 0; l < k; ++l) {
        C[n * i + j] -= A[k * i + l] * B[n * l + j];
      }
      max_err = fmax(fabs(C[n * i + j]), max_err);
    }
  }
  return max_err;
}

double get_wall_time() {
    struct timeval time;

    gettimeofday(&time, NULL);
    return (double)time.tv_sec + (double)time.tv_usec * .000001;
}

int main() {
  double *A, *B, *C;
  int m, n, k;
  const int num_runs = 5;

  m = n = k = 1024;
  A = (double*)malloc(sizeof(double) * m * k);
  B = (double*)malloc(sizeof(double) * k * n);
  C = (double*)malloc(sizeof(double) * m * n);
  double accum_time = 0.0;
  for (int i = 0; i < num_runs; ++i) {
    init(m, n, k, A, B, C);
    double start = get_wall_time();
    f(m, n, k, A, B, C);
    double end = get_wall_time();
    printf("run %d time: %f sec\n", i, end - start);
    accum_time += end - start;
  }
  printf("average time: %f sec\n", accum_time / num_runs);
  printf("max error: %.16e\n", get_max_error(m, n, k, A, B, C));
}

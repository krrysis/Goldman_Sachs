"""
11_Main Function Return

int f(int* a, int b) {

    b = b - 1;

    if (b == 0) return 1;

    *a = *a + 1; // '*a' accesses the value pointed to by pointer 'a'

    return f(a, b) * (*a);

}

int main() {

    int a = 3;

    int b = 3;

    return f(&a, b);

}
Pick one of the choices

    20

    25

    30

    120

    none of the above
"""
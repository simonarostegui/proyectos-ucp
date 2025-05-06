#include <stdio.h>
#include <math.h>

int main() {
    int problem_type;
printf("Enter the problem type:\n1. 56/5x = 5\n2.(25-x)/2 = x/5\n3. 2x^2 + 3x + 4 = 0\n4. y = ax + b\n");
    scanf("%i", &problem_type);

    float num_a, num_b, num_c, x, discriminant, solution1, solution2;
     float a1, b1, a2, b2;
        float x_intersect, y_intersect;
    switch (problem_type)
    {
    case 1:

        printf("Enter values of a, b, and c (e.g., 56/5x = 5):\n");
        scanf(" %f", &num_a);
        printf("/");
        scanf(" %f", &num_b);
        printf("x = ");
        scanf(" %f", &num_c);
        printf("\n");

        if(num_b != 0 && num_c != 0) {
            x = num_a / (num_b * num_c);
            printf("Solution: x = %.2f (rounded down: %d)\n", x, (int)x);
        } else {
            printf("Invalid input for algebraic equation\n");
        }
        break;
    case 2: 
        fflush(stdin);
        printf("Enter values of a, b, and c (e.g., (25-x)/2 = x/5):\n");
        scanf("(%f-x)/%f = x/%f", &num_a, &num_b, &num_c);

        if(num_b != 0 && num_c != 0) {
            x = (num_a * num_c) / (num_b * num_c);
            printf("Solution: x = %.2f (rounded down: %d)\n", x, (int)x);
        } else {
            printf("Invalid input for algebraic equation\n");
        }
        break;
    case 3:
        printf("Enter values of a, b, and c (e.g., 2x^2 + 3x + 4 = 0): ");
        scanf("%fx^2 + %fx + %f", &num_a, &num_b, &num_c);

        discriminant = num_b*num_b - 4*num_a*num_c;
        if(discriminant >= 0) {
            solution1 = (-num_b + sqrt(discriminant)) / (2*num_a);
            solution2 = (-num_b - sqrt(discriminant)) / (2*num_a);

            printf("Solutions: x1 = %.2f (rounded down: %d), x2 = %.2f (rounded down: %d)\n", solution1, (int)solution1, solution2, (int)solution2);
        } else {
            printf("No real solutions\n");
        }
        break;
    case 4:
        printf("Enter the lines in the form y = ax + b (e.g., y = 2x + 3):\n");
        scanf("y = %fx + %f y = %fx + %f", &a1, &b1, &a2, &b2);

        if(a1 - a2 != 0) {
            x_intersect = (b2 - b1) / (a1 - a2);
            y_intersect = a1 * x_intersect + b1;

            printf("Intersection at (%.2f, %.2f) (rounded down: (%d, %d))\n", x_intersect, y_intersect, (int)x_intersect, (int)y_intersect);
        } else {
            printf("Lines are parallel\n");
        }
        break;
    default:
        printf("Invalid problem type\n");
        break;
    }
}
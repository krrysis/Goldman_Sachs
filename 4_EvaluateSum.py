"""
Evaluate Sum

Consider the following pseudocode where x is an integer variable initialized to a non negative integer value.

// x is a non negative integer
int sum
x <- x/2 // integer division; truncates fractions
for (sum <- 1; x > 0; x <- x/2 )
    sum <- sum + 1
end for

 Which of the following will calculate the same value of sum as the fragment above?
Pick one of the choices

    int sum <- 0

    x <- x/2

    while (x >= 0)

        sum <- sum + 1

        x <- x/2

    end while

    _________________________________________________________

    int sum <- 1

    x <- x/2

    while (x >= 0)

        sum <- sum + 1

        x <- x/2

    end while

    _________________________________________________________

    int sum <- 0

    do {

        sum <- sum + 1

        x <- x/2

    } while (x>0)

    _________________________________________________________

    int sum <- 1

    do {

        sum <- sum + 1

        x <- x/2

    } while (x>0)

    _________________________________________________________

    None of the above
    Clear selection
"""

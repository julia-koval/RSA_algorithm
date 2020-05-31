# RSA_algorithm
RSA (an abbreviation for the names Rivest, Shamir, and Adleman) is a public-key cryptographic algorithm based on the computational complexity of the large integer factorization problem.

Purpose: to create a pair of public and private keys.

Actions:

• Choose two primes p and q;

• Calculate n - the product of our p and q;

• Calculate the Euler function: f (n) = (p-1) × (q-1);

• Choose a number e that meets the following criteria: it must be prime, it must be less than f(n), it must be coprime with f(n).
Now the pair of numbers {e, n} is your public key;

• Calculate the number d inverse to e modulo f(n).
The pair {d, n} is the secret key.

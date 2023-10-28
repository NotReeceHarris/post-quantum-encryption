# Post-Quantum Cryptography with Lattices

> Post-quantum cryptography based on lattice structures. This repository is a playground where i explore and experiment with lattices. My primary focus is on researching and developing lattice algorithms driven by personal interest and curiosity.

## Lattice
In the context of post-quantum encryption, a lattice is a mathematical structure used for cryptographic purposes. It involves complex geometric shapes and mathematical equations. Lattice-based cryptography relies on the hardness of certain lattice problems to create encryption schemes that are believed to be secure against attacks by quantum computers. This makes lattice-based encryption a promising candidate for ensuring data security in a post-quantum world.

[![](/assets/lattice.png)](https://ocw.mit.edu/courses/18-409-topics-in-theoretical-computer-science-an-algorithmists-toolkit-fall-2009/a5351bd811ac52366dec759f2c6b2fac_MIT18_409F09_scribe18.pdf) \
<sub>This is an example of a "good basis" and "bad basis" within a lattice structure.</sub>

### How lattices are used in encryption

Bob wants to send a message to Alice. In this encryption process, Alice creates two sets of basis vectors: a "good basis" and a "bad basis." Both of these bases need to define the same lattice structure. The "good basis" consists of vectors that are nearly perpendicular, while the "bad basis" comprises vectors that are nearly parallel.

The reason for having these two bases is that one serves as a private key, while the other is a public key. The "bad basis" is designed to make it harder to solve the ["shortest vector problem,"](https://en.wikipedia.org/wiki/Lattice_problem#Shortest_vector_problem_(SVP)) a key challenge in lattice-based cryptography. In contrast, the "good basis" allows for a more efficient solution to this problem. The idea is that even quantum computers would struggle to solve this problem effectively. Therefore, encoding with the public key (the "bad basis") becomes extremely challenging without access to the private key (the "good basis").

Here's how the process works: Once Bob has Alice's public key (the "bad basis"), he can locate a point on the lattice that represents his message using various methods. He knows the path to this point within the lattice, so he shifts it slightly and sends this new point to Alice. She can then use her private key (the "good basis") to run the "shortest vector problem" and recover the original point representing Bob's message. This approach results in post-quantum encryption, which is highly secure against quantum computing attacks.

### Lattice Dimensions

Lattices can exhibit multiple dimensions, which is what contributes to their complexity. The examples above illustrate a basic 2D lattice (x, y). However, it's essential to understand that a lattice can extend into an arbitrary number of dimensions. This means it can involve not only a flat plane like (x, y) but can also encompass (x, y, z), (x, y, z, w), and beyond, These additional dimensions add layers of complexity and versatility to the lattice concept.

# Compile

```sh 

mkdir build && cd build 
cmake ../
make

```

# Run

```sh 
./bin/receiver
```

Then open another terminator and execute 

```sh 
./bin/sender
```

Then the following will be shown 

```
What do you want to do? Server
Choose from :
	1. Send a plaintext
```

Input `1` and press enter, then

```
What do you want to send?
```

Input a line you want to test, then you can see the text on the receiver side.


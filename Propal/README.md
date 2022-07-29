[delete this and put your project build and use instructions here]


# index

Beautiful assembly references the way this language uses metaphorical images to make the programmer understand the assembly code.

For this assembly we will be using an analogy for a warehouse.
In this warehouse there is an forklift driving around that can perform actions.

all data is contained inside packages that the forklift can manipulate.

0. wait for a tick (NOP)
1. recieve packages from outside.
2. destroy packages
3. store packages
4. picking packages
5. labeling packages
6. moving the forklift

Inside this warehouse there is also a scanner that can read information inside the container and on its label.
Make basic comparisons.

7. checking packages

# the Instructions

## (0) Wait for a tick
the NOP
could be handy for a future when there are multiple forklifst working together.

syntax:
**wait**

effect:
The forklift does absolutely nothing

## (1) recieve packages from outside
Some packages come from outside the warehouse the forklift is working in.
All incomming packages are expected to be 8-bits in length
There will be a flag on the import register that is read to make sure there is a value

syntax:
**import**

assert:
forks are empty
the import register flag is set

effect:
an 8-bit value is loaded on the forklift.

## (2) destroy packages
package on the forklift is send to the waste

syntax:
**waste**

assert:
forks are not empty
otherwise there is nothing to remove on the forks

effect:
forks become empty
A label reference is removed to avoid reading unexpected values from the storage.

## (3) store packages
package is moved to the location the forklift is at.

syntax:
**store** (*int* or *labelname*)?

assert:
forks are not empty
if an integer or label is given I expect the forks to be empty

effect:
forklift is empty
storage location contains package


## (4) picking packages
package is moved from the store location to the forklift

syntax:
**pick**

assert:
forks are empty

effect:
forklift contains package from storage location
storage location becomes empty

## (5) labeling packages
on the forklift there is a label maker that can generate a label to put on the package currently on the forks.
The label will be destroyed the moment the package is *"wasted"*.
When the program asks to move to the label, the forklift moves to the storage location linked to the label.


syntax:
**label** *name*

assert:
the name is not a reseserved keyword.

effect:
there is a location link from the label to the storage location of the package.

## (6) Moving the forklift
move the forklift to a different location in the warehouse
If there is a label for a package in storage then the location in the storage.
integer of a storage location.

syntax:
**move** (*int* or *labelname*)

assert:
if type is int. The forklift moves to that storage location
if type is labelname. The forklift moves to the storage location linked to that label name.

effect:
forklift moves to storage location optionally referenced by label name.

## (7) checking packages
The scanner scans packages.
Tell the scanner what value types are given

syntax:
**scan** *op* (*valuetype*  int* or *labelname*) (*valuetype*  *int* or *labelname*)?

op:
0. not
1. and
2. or
3. lss
4. gtr
5. eq
6. jmpif

valuetype:
0. int
1. fork
2. label

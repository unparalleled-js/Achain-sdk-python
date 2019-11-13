# Achain-sdk-python

# achainpy library

This library is still a work in progress but currently has the ability to perform all `cleos get` functions without compiling the code.

The library now supports signing transactions/key creation for both python 2.7 and 3.x. This is the first iteration and is very rough. The key creation has not been tested fully and should be used at your own risk.

The commands currently implemented.

```
Subcommands:
  get
    info                        Get current blockchain information
    block                       Retrieve a full block from the blockchain
    account                     Retrieve an account from the blockchain
    code                        Retrieve the code and ABI for an account
    abi                         Retrieve the ABI for an account
    table                       Retrieve the contents of a database table
    currency                    Retrieve information related to standard currencies
    accounts                    Retrieve accounts associated with a public key
    servants                    Retrieve accounts which are servants of a given account
    transaction                 Retrieve a transaction from the blockchain
    actions                     Retrieve all actions with specific account name referenced in authorization or receiver
  push
    action                      Push a transaction with a single action
  set
    abi                         Create or update the abi on an account
    code                        Create or update the code on an account
    contract                    Create or update the contract on an account
  system
    newaccount                  Create an account, buy ram, stake for bandwidth for the account
    listproducers               List producers
```

## Installation

### Linux

```
# create virtual environment
mkdir -p ~/envs/achainpy
virtualenv ~/envs/achainpy
# activate the environment
source ~/envs/achainpy/bin/activate
# clone code
git clone https://github.com/Achain-Dev/Achain-sdk-python.git
# install the library
cd Achain-sdk-python
[sudo] python setup.py install libachainpy

```
### Windows

1. Install python
   You can use either Python 2.7 or 3.7 however we suggest python 3.7 as we have tested that version more thoroughly.
   https://www.howtogeek.com/197947/how-to-install-python-on-windows/
   [Python 2.7](https://www.python.org/downloads/release/python-2715/)
   [Python 3.7](https://www.python.org/downloads/release/python-370/)

2. Install git
   https://www.atlassian.com/git/tutorials/install-git

3. Install achainpy

```
# clone code
git clone https://github.com/Achain-Dev/Achain-sdk-python.git
# install the library
cd Achain-sdk-python
python setup.py install

```
## Command line Tool Examples

```
# Get chain information
pycli --url http://127.0.0.1:8888 get info

# get information about a block
pycli --url http://127.0.0.1:8888 get block 100

# Retrieve an account from the blockchain
pycli --url http://127.0.0.1:8888 get account --account act

# Retrieve the code and ABI for an account
pycli --url http://127.0.0.1:8888 get code --account act

# Retrieve the ABI for an account
pycli --url http://127.0.0.1:8888 get abi --account act

```

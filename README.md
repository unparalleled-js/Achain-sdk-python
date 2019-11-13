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
# download code
git clone https://github.com/Achain-Dev/Achain-sdk-python.git
# install the library
cd Achain-sdk-python
[sudo] python setup.py install libachainpy

```


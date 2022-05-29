# spl-airdrop
Python script to automate sending wl tokens to community members.


This script assumes you have [**python3**](https://https://www.python.org/downloads/) installed as well as both the [**solana cli**](https://docs.solana.com/cli/install-solana-cli-tools) & [**spl-token**](https://spl.solana.com/token).


Replace TOKEN_ADDRESS with your spl token address in [**airdrop.py**](https://github.com/triiq/spl-airdrop/blob/main/airdrop.py).

Replace TOKEN_AMOUNT with how many tokens to be sent to each address in [**airdrop.py**](https://github.com/triiq/spl-airdrop/blob/main/airdrop.py).

Replace WALLET_ADDRESS with the addresses to be sent tokens in [**airdrop.txt**](https://github.com/triiq/spl-airdrop/blob/main/airdrop.txt).

Ensure you have the correct wallet & network set up with **solana config get**.

Airdrop your vip list spl token with **python3 airdrop.py**.

If this was useful, come say hey on twitter [**@triiq**](https://twitter.com/triiq_) :)

### How I Use It
I use a combination of a custom rpc node and multiple instances of this script to send hundresds of tokens quickly.

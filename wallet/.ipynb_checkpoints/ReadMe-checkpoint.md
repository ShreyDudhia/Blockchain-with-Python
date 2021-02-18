# Blockchain Wallet using Python

## What is an HD wallet? 
An HD Wallet, or Hierarchical Deterministic wallet is a digital wallet that generates public and private addresses in a hierarchical tree-like structure so the user doesn't have to generate one themselves. Though, HD wallets were introduced by the Bitcoin community it supports other cryptocurrencies as well.

## HD-Derive-wallet
An hd-derive-wallet is a command line tool that derives bip32 wallet addresses and private keys for Bitcoin and other altcoins. hd-derive-wallet is not limited to BIP32, BIP39, and BIP44, but it also supports non-standard derivation paths for the most popular wallets out there today.

The following is also mentioned in the wallet.py file and is used to derive the wallet and store cryptocurrencies.

command = f'./derive -g --mnemonic="{mnemonic}" --coin="{coin}" --numderive="{num}" --cols=index,path,address,privkey,pubkey,pubkeyhash,xprv,xpub --format=json'

## Executing transactions
By using the folowing code, a transaction was initiated. 

def send_tx(coin, account, to, amount):
    if coin == "eth":
        raw_tx = create_tx(coin, account, to, amount)
        signed = account.signTransaction(raw_tx)
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    if coin == BTCTEST:
        raw_tx = create_tx(coin, account, to, amount)
        signed = account.sign_transaction(raw_tx)

        return NetworkAPI.broadcast_tx_testnet(signed)
reciept = send_tx("eth", ETH_key, '0x16603EF5D7A2dc6479c1ecCC295A2aD6A3E8fCe3', 1)
print(reciept)
print(w3.eth.get_balance(account.address))


![Markdown.png](attachment:Markdown.png)
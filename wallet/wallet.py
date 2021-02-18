import subprocess
import json
from web3 import Web3, middleware, Account
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3.middleware import geth_poa_middleware
from constants import *
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

def derive_wallets(Coin):
    command = f'./derive -g --mnemonic="moon lamp awful list destroy winter repeat illness bronze danger where melt" --cols=path,address,privkey,pubkey --format=json --coin={Coin} --numderive=3'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)
    return keys
#account = Account.from_key("0x08fef16140389a137d92b24932c361162209ff2006d085c3c28144e3060030f4")
#ETH_key = priv_key_to_account("0x08fef16140389a137d92b24932c361162209ff2006d085c3c28144e3060030f4", ETH)



Coins = {"ETH":derive_wallets("eth"), "BTC":derive_wallets("BTC")}
#print(Coins["ETH"][0]['privkey'])
print(Coins)

def priv_key_to_account(priv_key, coin):
    if coin  == "eth":
        return Account.privateKeyToAccount(priv_key)
    #if coin == BTCTEST:
        #return PrivateKeyTestnet(priv_key)
ETH_key = priv_key_to_account("548ac9028731238b2ea865f691f1c00e1c135a526845aafe54eb39d69552857c", "eth")

def create_tx(coin, account, to, amount):
    if coin == "eth":
        #  tx = txPrep.buildTransaction({'chainId': self.chainId,
        #                               'gas': self.inchGas,
        #                               '3gasPrice': gasPrice,
                                      #'nonce': nonce})
        #w3.eth.estimateGas(transaction={'to':contractAddress,
            #from':address,
            #value':int(msgValue),
            #data':tx["data"]})
        value = w3.toWei(amount, "ether") # convert 1.2 ETH to 120000000000 wei
        gasEstimate = w3.eth.estimateGas({ "to": to, "from": account.address, "amount": value })
        return {
            "to": to,
            "from": account.address,
            "value": value,
            "gas": gasEstimate,
            "gasPrice": 3000000, #w3.eth.generateGasPrice()
            "nonce": w3.eth.getTransactionCount(account.address),
            "chainId": 5777,#w3.net.chainId()
        }
        
    #if coin == BTCTEST:
      #  return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])


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
        
    
    

from brownie import ZeiToken, accounts, config


def deploy_zei_token():
    account = accounts.add(config["wallets"]["from_key"])
    ZeiToken.deploy(5000000000, {"from": account})


def main():
    deploy_zei_token()

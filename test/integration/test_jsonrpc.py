import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from argod import ArgoDaemon
from argo_config import ArgoConfig


def test_argod():
    config_text = ArgoConfig.slurp_config_file(config.argo_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'000005ece8d1964dc550f050f35c45398a4b9dda3158040e0519b9c230b91ed6'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'000002731816bccf90ab744347dc894cf484e3826b19f967b8d5f028c204a4f0'

    creds = ArgoConfig.get_rpc_creds(config_text, network)
    argod = ArgoDaemon(**creds)
    assert argod.rpc_command is not None

    assert hasattr(argod, 'rpc_connection')

    # Argo testnet block 0 hash == 000002731816bccf90ab744347dc894cf484e3826b19f967b8d5f028c204a4f0
    # test commands without arguments
    info = argod.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert argod.rpc_command('getblockhash', 0) == genesis_hash

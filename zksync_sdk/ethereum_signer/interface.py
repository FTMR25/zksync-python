from abc import ABC, abstractmethod

from zksync_sdk.types import EncodedTx, TxEthSignature

__all__ = ['EthereumSignerInterface', 'TxEthValidatorInterface']


class EthereumSignerInterface(ABC):

    @abstractmethod
    def sign_tx(self, tx: EncodedTx) -> TxEthSignature:
        raise NotImplementedError

    @abstractmethod
    def sign(self, message: bytes) -> TxEthSignature:
        raise NotImplementedError

    @abstractmethod
    def address(self) -> str:
        raise NotImplementedError


class TxEthValidatorInterface(ABC):
    def __init__(self, signer_address: str):
        self.signer_address = signer_address

    @abstractmethod
    def is_valid_signature(self, tx: EncodedTx) -> bool:
        raise NotImplementedError

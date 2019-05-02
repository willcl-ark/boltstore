from lnd_client import LND_CLIENT
from utilities import *


class Invoice:

    def __init__(self, r_hash_bytes, payment_request, r_index):
        self.r_hash_bytes = r_hash_bytes
        self.payment_request = payment_request
        self.r_index = r_index
        self.decoded_pay_req = LND_CLIENT.rpc.decode_pay_req(pay_req=self.payment_request)
        self.is_paid = False

    def __str__(self):
        return f"{self.decoded_pay_req}Is paid: {self.is_paid}"

    def __repr__(self):
        return f"Invoice({self.r_hash_bytes}, {self.payment_request}, {self.r_index})"

    def pay(self, preimage_base64):
        preimage_bytes = base64_to_bytes(preimage_base64)
        hash_bytes = sha256_to_bytes(preimage_bytes)
        hash_hex = bytes_to_hex(hash_bytes)
        if hash_hex == self.decoded_pay_req.payment_hash:
            self.is_paid = True
            print('\nInvoice paid successfully, releasing item.\n\n')
        else:
            print("Preimage not valid. Check encoding is base64")



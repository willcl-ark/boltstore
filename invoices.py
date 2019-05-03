from lnd_client import LND_CLIENT
from utilities import *


class Invoice:

    def __init__(self, r_hash_hex, payment_request, add_index, is_paid=False):
        self.r_hash_hex = r_hash_hex
        self.payment_request = payment_request
        self.add_index = add_index
        self.decoded_pay_req = LND_CLIENT.rpc.decode_pay_req(pay_req=self.payment_request)
        self.is_paid = is_paid

    def __str__(self):
        return f"{self.decoded_pay_req}Is paid: {self.is_paid}"

    def __repr__(self):
        return f"Invoice({self.r_hash_hex}, {self.payment_request}," \
            f"{self.add_index}, {self.is_paid})"

    def pay(self, preimage_base64):
        preimage_bytes = base64_to_bytes(preimage_base64)
        preimage_hash_hex = sha256_of_bytes_to_hex(preimage_bytes)
        # hash_hex = bytes_to_hex(hash_bytes)
        if preimage_hash_hex == self.decoded_pay_req.payment_hash:
            self.is_paid = True
            print('\nInvoice paid successfully, releasing item.\n\n')
        else:
            print("Preimage not valid. Check encoding is base64")



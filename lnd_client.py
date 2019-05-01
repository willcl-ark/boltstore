import lnd_grpc


class LndClient():

    def __init__(self):
        self.config = {}
        self.read_config()
        self.rpc = lnd_grpc.Client(lnd_dir=self.config['lnd_dir'],
                                   network=self.config['network'],
                                   grpc_host=self.config['grpc_host'],
                                   grpc_port=self.config['grpc_port'],
                                   macaroon_path=self.config['macaroon_path'])

    def read_config(self):
        with open("boltstore.conf", "r") as conf:
            data = conf.readlines()
            for line in data:
                if line.startswith("#"):
                    pass
                else:
                    key, value = line.split("=")
                    key = key.strip()
                    value = value.strip()
                    self.config[key] = value


LND = LndClient()
import lnd_grpc


class Lnd:

    config_params = ["lnd_dir", "network", "grpc_host", "grpc_port", "macaroon_path"]

    def __init__(self, user):
        self.config = {}
        self.read_config(user)
        self.rpc = lnd_grpc.Client(lnd_dir=self.config['lnd_dir'],
                                   network=self.config['network'],
                                   grpc_host=self.config['grpc_host'],
                                   grpc_port=self.config['grpc_port'],
                                   macaroon_path=self.config['macaroon_path'])

    def read_config(self, user):
        with open(f"boltstore_{user}.conf", "r") as conf:
            data = conf.readlines()
            for line in data:
                if line.startswith("#"):
                    pass
                else:
                    key, value = line.split("=")
                    key = key.strip()
                    value = value.strip()
                    self.config[key] = value
            if not all(k in self.config for k in Lnd.config_params):
                print(f"boltstore.conf missing LND Client parameters. \n Please ensure"
                      f"that at least the following parameters are specified: \n"
                      f"{Lnd.config_params}")


LND_CLIENT = Lnd('client')
LND_SERVER = Lnd('server')

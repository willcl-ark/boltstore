# Boltstore

Currently lightning payments between buyer and seller on a webstore require the buyer pay the store and the store will in turn pay the seller in a second payment. With the lightning invoice system it is possible to have the buyer make a direct payment to the seller for digital items, with the buyer providing only proof of payment to the webstore to unlock the content.

## Model

Sellers must all run their own copy of LND and additionally lightweight Boltstore daemon which has access to only the invoice.macaroon, allowing it to generate new invoices for payment.

The store will be able to the request new invoices from sellers as buyers request them. As there is no blockchain the store can monitor for transactions the store will note the invoice r_hash as it forwards the invoice to the buyer. Once the buyer pays the invoice, they input the invoice r_preimage into the store as proof-of-payment which the store can verify hashes to the invoice r_hash then releasing the purchased content.

### Sellers

Sellers should modify boltstore_server.conf to point to their LND directory and invoice.macaroon. They can then run app-server.py like:

`python app-server.py host port`

### Webstore

The webstore will modify boltstore_client.conf to point to its LND directory and specify the readonly.macaroon, used to decode payment requests and check sellers have provided invoice of correct value. Currently the store can send invoice requests to the seller using the following syntax:

`python app-client.py host port 'invoice' value`

### Localhost testing

Terminal 1:
`python app-server 127.0.0.1 65222`

Terminal 2:
`python app-server 127.0.0.1 65222 invoice 10000`

## Todo

1) Daemonise the app-server
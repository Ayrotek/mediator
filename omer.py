chmod a+x setup.py
./setup.py run build
aca-py start --inbound-transport http 0.0.0.0 8000 --genesis-url http://test.bcovrin.vonx.io/genesis --inbound-transport ws 0.0.0.0 8001 --outbound-transport ws --outbound-transport http --endpoint http://localhost:8000

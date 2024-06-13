""" from pymodbus.client import ModbusSerialClient

client = ModbusTcpClient('MyDevice.lan')   # Create client object
client.connect()                           # connect to device, reconnect automatically
client.write_coil(1, True, slave=1)        # set information in device
result = client.read_coils(2, 3, slave=1)  # get information from device
print(result.bits[0])                      # use information
client.close()        """

#!/usr/bin/env python3
"""Pymodbus synchronous client example.

An example of a single threaded synchronous client.

usage: simple_sync_client.py

All options must be adapted in the code
The corresponding server must be started before e.g. as:
    python3 server_sync.py
"""

# --------------------------------------------------------------------------- #
# import the various client implementations
# --------------------------------------------------------------------------- #
import pymodbus.client as ModbusClient
import pymodbus

""" from pymodbus import (
    ExceptionResponse,
    ModbusRtuFramer,
    ModbusException,
    pymodbus_apply_logging_config,
) """


def run_sync_simple_client():
    """Run sync client."""
    # activate debugging
    #pymodbus_apply_logging_config("DEBUG")
    print('go')

    pymodbus.client = ModbusClient.ModbusSerialClient(
        port = "COM4",
        # timeout=10,
        # retries=3,
        # retry_on_empty=False,
        # strict=True,
        baudrate=19200,
        bytesize=8,
        parity="N",
        stopbits=1,
        timeout=2,
        retries=1,
        retry_on_empty=True
        # handle_local_echo=False,
    )
    print("connect to server")
    pymodbus.client.connect()

    print("get and verify data")
 #   while True:
    try:
        rr = pymodbus.client.read_holding_registers(0, 1, slave=1)
        print(rr.registers)
    except pymodbus.ModbusException as exc:
        print(f"Received ModbusException({exc}) from library")
        pymodbus.client.close()
        return
    if rr.isError():
        print(f"Received Modbus library error({rr})")
        pymodbus.client.close()
        return
    if isinstance(rr, pymodbus.ExceptionResponse):
        print(f"Received Modbus library exception ({rr})")
        # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
        pymodbus.client.close()

    print("close connection")
    pymodbus.client.close()

if __name__ == "__main__":

    run_sync_simple_client()
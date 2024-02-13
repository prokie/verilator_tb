# test_my_design.py (simple)

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def my_first_test(dut):
    """Try accessing the design."""

    await Timer(1, units="step")  # Wait for 1 time unit
    # dut._log.info("Hello world!")
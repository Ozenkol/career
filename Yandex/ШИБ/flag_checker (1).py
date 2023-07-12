import ctypes
import struct
import sys

# pip install unicorn
from unicorn import *
from unicorn.x86_const import *
from unicorn.arm_const import *
from unicorn.mips_const import *

LONG_LEN = 8
ULONG_CHAR = "L" if ctypes.sizeof(ctypes.c_ulong) == 8 else "Q"

STACK_ADDR = 0x1000
MEMSIZE = 0x2000

FLAG = b"1\x08\xca=\xb2?\xc5\x01\x1e6\xd6\xbc\x8f\xbe]\xbf\x1c\xb8D\x9f\x0e\x88]\x0b\x9a\x8d\xe9\x9c3\xbd\xdd\x08"
FLAG_ADDR = MEMSIZE - len(FLAG)


def transform(seq, n):
    return seq[n:] + seq[:n]


def with_magic(func):
    def wrapper(*args, **kwargs):
        if len(args) == 0:
            return func(*args, **kwargs)

        n = get_magic_value(id(args[0]))
        new_args = (transform(args[0], n), *args[1:])

        return func(*new_args, **kwargs)
    return wrapper


def get_magic_value(object_id):
    return struct.unpack(ULONG_CHAR, ctypes.string_at(object_id, LONG_LEN))[0]


@with_magic
def encrypt(user_flag):
    code = b"\x89\xc8\xb3\x04\xf6\xf3\x31\xc9\x88\xc1\x89\xf7\xad\xc1\xc0\x03\x35\x84\xce\x5b\x3f\xab\xe2\xf4"

    try:
        mu = Uc(UC_ARCH_X86, UC_MODE_32)

        mu.mem_map(0, MEMSIZE)
        mu.mem_write(0, code)
        mu.mem_write(FLAG_ADDR, bytes(user_flag))

        mu.reg_write(UC_X86_REG_ESP, STACK_ADDR)
        mu.reg_write(UC_X86_REG_ESI, FLAG_ADDR)
        mu.reg_write(UC_X86_REG_ECX, len(FLAG))

        mu.emu_start(0, len(code))

        user_flag = mu.mem_read(FLAG_ADDR, len(FLAG))

    except UcError as e:
        print("ERROR: %s" % e)

    return user_flag


def main(argv):
    print("Hello there! Welcome to flag checker v1.0!")
    if len(argv) < 2:
        print("Usage: <flag>")
        return

    user_flag = [ord(x) for x in argv[1]]

    if len(user_flag) != len(FLAG):
        print("Wrong flag length!")
        return

    a = []

    for i in range(0, 5):
        for _ in range(0, i):
            a.append(user_flag)
        user_flag = encrypt(user_flag)

    if user_flag == FLAG:
        print("Correct :)")
    else:
        print("Wrong :(")

    return


if __name__ == "__main__":
    main(sys.argv)

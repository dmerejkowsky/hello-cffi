from _hello import lib, ffi

c_answer = lib.answer()
print(c_answer)
c_greet = lib.greet()
print(ffi.string(c_greet))

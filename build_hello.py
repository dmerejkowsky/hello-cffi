from cffi import FFI
ffibuilder = FFI()

ffibuilder.set_source(
    "_hello",
    """
    #include <hello.h>

    """,
    extra_objects=["build-meson/libhello.a"],
    include_dirs=["."],
)

ffibuilder.cdef("""
int answer(void);
char* greet(void);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

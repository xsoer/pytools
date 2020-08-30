import numpy as np

"""
Numpy type	                    C type	                Description
np.bool	                        bool	                Boolean (True or False) stored as a byte
np.byte	                        signed char	            Platform-defined
np.ubyte	                    unsigned char	        Platform-defined
np.short	                    short	                Platform-defined
np.ushort	                    unsigned short	        Platform-defined
np.intc	                        int	                    Platform-defined
np.uintc	                    unsigned int	        Platform-defined
np.int_	                        long	                Platform-defined
np.uint	                        unsigned long	        Platform-defined
np.longlong	                    long long	            Platform-defined
np.ulonglong	                unsigned long long	    Platform-defined
np.half / np.float16	         	                    Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
np.single	                    float	                Platform-defined single precision float: typically sign bit, 8 bits exponent, 23 bits mantissa
np.double	                    double	                Platform-defined double precision float: typically sign bit, 11 bits exponent, 52 bits mantissa.
np.longdouble	                long double	            Platform-defined extended-precision float
np.csingle	                    float complex	        Complex number, represented by two single-precision floats (real and imaginary components)
np.cdouble	                    double complex	        Complex number, represented by two double-precision floats (real and imaginary components).
np.clongdouble	                long double complex	    Complex number, represented by two extended-precision floats (real and imaginary components).


np.int8	                        int8_t	                Byte (-128 to 127)
np.int16	                    int16_t	                Integer (-32768 to 32767)
np.int32	                    int32_t	                Integer (-2147483648 to 2147483647)
np.int64	                    int64_t	                Integer (-9223372036854775808 to 9223372036854775807)
np.uint8	                    uint8_t	                Unsigned integer (0 to 255)
np.uint16	                    uint16_t	            Unsigned integer (0 to 65535)
np.uint32	                    uint32_t	            Unsigned integer (0 to 4294967295)
np.uint64	                    uint64_t	            Unsigned integer (0 to 18446744073709551615)
np.intp	                        intptr_t	            Integer used for indexing, typically the same as ssize_t
np.uintp	                    uintptr_t	            Integer large enough to hold a pointer
np.float32	                    float
np.float64 / np.float_	        double	                Note that this matches the precision of the builtin python float.
np.complex64	                float complex	        Complex number, represented by two 32-bit floats (real and imaginary components)
np.complex128 / np.complex_	    double complex	        Note that this matches the precision of the builtin python complex.
"""